import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    cipher_text = ''
    newShift = 0
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            charIndex = alphabet.index(char)
            newShift = (charIndex + shift) % 26
            cipher_text += alphabet[newShift]
        else:
            cipher_text += char

    print(f"Your {direction}d secret phrase is {cipher_text}")

def caller():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    while direction != "encode" and direction != "decode":
        direction = input("Please pick the given choices: Type 'encode' to encrypt or type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)

choice = "yes"

while choice == "yes":
    caller()
    choice = input("Do you want to go again? Type 'yes' or 'no': ").lower()

print("Goodbye!")
