alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

print(logo)
print("\n")

continue_game = True
while continue_game:
    choice = input("Type 'encode' to encrypt and 'decode' to decrypt\n")

    message = input("Type your message\n")

    shift_number = int(input("type the shift number\n"))

    if choice == 'encode':
        def encode(plain_message, shift_value):
            cipher = ""
            for element in plain_message:
                position = alphabet.index(element)
                new_position = position + shift_value
                new_element = alphabet[new_position]
                cipher += new_element
            print(f"the encoded text is {cipher}")

        encode(plain_message=message, shift_value=shift_number)

    elif choice == 'decode':
        def decode(cipher_text, shift_value):
            plain_text = ""
            for element in cipher_text:
                position = alphabet.index(element)
                new_position = position - shift_value
                new_element = alphabet[new_position]
                plain_text += new_element
            print(f"the decoded message is {plain_text}")
        decode(cipher_text = message, shift_value=shift_number)

    result = input("Type 'yes' if you want to go again else type 'no\n").lower()
    if result == 'yes':
        continue_game
    elif result == 'no':
        print("\nThanks for playing!")
        continue_game = False
