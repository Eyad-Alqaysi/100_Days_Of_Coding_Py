alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    s = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift
            s += alphabet[new_position]
        else:
            s += i
    print(f"Here's the {direction}d result: {s}")
stop =''
while stop != 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode'  to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    stop = input("Type 'yes' if you want to stop the program. Otherwise type 'no'.\n")