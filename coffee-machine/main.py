from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cash_reg = 0

def machine_call(drink):
    global cash_reg
    resource_deductor(drink)
    print("Please insert coins")
    qua = int(input("How many quarters? "))
    dim = int(input("How many dimes? "))
    nick = int(input("How many nickels? "))
    pen = int(input("How many pennies? "))
    cash = currency_converter(qua, dim, nick, pen)
    cost = MENU[drink]["cost"]
    change = cash - cost
    change = round(change, 2)
    if change < 0:
        print("Sorry thats not enough cash, money refunded.")
    else:
        cash_reg += MENU[drink]["cost"]
        if change > 0:
            print(f"Your {drink} costs ${cost}, so Here's your change: ${change}")
        else:
            print(f"Your {drink} costs ${cost}")
        print(f"Enjoy your {drink}!!")

def recharge():
    for key in resources:
        if key == "coffee":
            topup = int(input(f"How much grams of {key} you want to add?: "))
        else:
            topup = int(input(f"How much ml of {key} you want to add?: "))
        resources[key] += topup
    print("Machine topped up, enjoy uninterrupted drinks!")

def currency_converter(qua, dim, nick, pen):
    dollar = pen*0.01 + nick*0.05 + dim*0.1 + qua*0.25
    return dollar

def rss_check(drink):
    for key in resources:
        if key in MENU[drink]["ingredients"]:
            if resources[key] < MENU[drink]["ingredients"][key]:
                return False

def resource_deductor(drink):
    for key in resources:
        if key in MENU[drink]["ingredients"]:
            resources[key] -= MENU[drink]["ingredients"][key]

def coffee_vending(drink):
    match drink:
        case "report":
            for key in resources:
                if key == "coffee":
                    print(f"{key}: {resources[key]}g")
                else:
                    print(f"{key}: {resources[key]}ml")
            print(f"Money: ${cash_reg}")
        case "recharge":
            recharge()
        case _:
            machine_call(drink)

machine_online = True

print(logo)

while machine_online:
    drink = input("What do you want? (espresso / latte / cappuccino) *other options include 'report'/'recharge'*: ")
    if drink != "recharge" and drink != "report": 
        check = rss_check(drink)
        if check is False:
            print("Sorry, insufficient ingredients in machine. Please recharge resources.")
            continue
    coffee_vending(drink)
    machine_toggle = input("Do you want to turn off the machine? 'y' or 'n': ")
    if machine_toggle == 'y'.lower():
        machine_online = False
        
#added sufficient resource check