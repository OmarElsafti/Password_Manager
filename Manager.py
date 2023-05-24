# -*- coding: utf-8 -*-
"""
Author: @OmarElsafti

Password Manager
"""

q = input("a for new input, q to exit: ")
while True:
    if q == 'q':
        break
    elif q == 'a':
        import random
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
        site = input("Enter Website Name: ")
        uname = input("Enter User Name: ")
        length = int(input("Enter Password Length: "))
        password = ""

        for i in range(0, length + 1):
            letter = letters[round(random.random() * len(letters)) - 1]
            password += letter
            
        with open("passwords.txt", 'a') as file:
            file.write("Website: " + site + "\n")
            file.write("User Name: " + uname + "\n")
            file.write("Password: " + password + "\n")
            file.write("\n\n\n")
        q = input("a for new input, q to exit: ")
    else:
        q = input("a for new input, q to exit: ")