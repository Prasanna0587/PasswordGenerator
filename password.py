import random
import string
while(True):
    def generator(length):
        characters = string.ascii_letters+string.digits+string.punctuation
        password =""
        for i in range(length):
            password =password+random.choice(characters)
        return password
    desired_length = int(input("Enter the size of password:"))
    print("password generated = "+generator(desired_length))
    choice=input("do you want to regenerate then enter 'yes' otherwise enter no : ")
    if (choice.lower()=="no"):
        break