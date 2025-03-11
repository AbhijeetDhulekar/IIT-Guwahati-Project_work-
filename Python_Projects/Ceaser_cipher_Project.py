alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']


def encryption(plain_key,shift_key):
    cipher_text=""
    for char in plain_text:
        position=aplhabet.index(char)
        new_position=(position+shift_key)%26
        cipher_text+=alphabet[new_position]
    print(f"Here's the text after encryption: {cipher_text}")
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        position=alphabet.index(char)
        new_position=(position-shift_key)%26
        plain_text+=alphabet[new_position]
    print(f"Here's the text after decryption: {plain_text}")

wanna_end=False
while not wanna_end:
    your_choice=input("Type 'encrypt' for encryption and type 'decrypt' for descryption:\n")
    text=input("Type your message: \n")
    shift=int(input("Enter the shift key:\n"))

    if your_choice =="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif your_choice=="decrypt":
        decryption(text,shift)
    play_again=input("Type 'yes' to continue or type 'no' to end the game...!\n")
    if play_again=='no':
        wanna_end=True
        print("I hope you enjoyed the game, have a nice day! good bye..")

