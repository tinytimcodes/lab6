
def encode(password):
    new_pass = ""
    for char in range(int(password)):

        if char == 7:
            new_pass += "0"
        elif char == 8:
            new_pass += "1"
        elif char == 9:
            new_pass += "2"
        else:
            new_pass += str(int(char) + 3)
    return new_pass

menu = True
while menu == True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3.Quit")
    user_input = input("Please enter an option: ")
    if user_input == '1':
        password = input("Please enter a password to encode: ")
        new_pass = encode(password)
        print("Your password has been encoded and stored!")
    elif user_input == "2":
        print(f"The encoded password is {new_pass}, and the original password is {password}.")
    else:
        menu = False