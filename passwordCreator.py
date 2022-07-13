import string
import random
import os

charactersUsed = 0
password = ""

def savePassword(password):
    with open('password.txt', 'w') as f:
        f.write(password)
    print("Your password has been saved at {}".format(os.path.dirname(os.path.realpath(__file__)) + '\password.txt'))
    exit()

def passwordShowcase(password):
    check = input("Do you want to show your password? (Y/N) ")

    if check == "Y":
        print("Your password is: {}".format(password))
        savePassword(password)
    elif check == "N":
        savePassword(password)
    else:
        print("Unsupported input. Try again.")
        passwordShowcase(password)

def createPassword(password):
    return ''.join(random.sample(password,len(password)))

def createSegment(size, chars):
    return ''.join(random.choice(chars) for _ in range(size))

def segmentManager(chars, type, password, length):
    global charactersUsed
    checker = input ("Does it require {} characters? (Y/N) ".format(type))

    if checker == "Y":
        segmentLength = int(input("How many {} characters do you want (1-{}) ".format(type, length-charactersUsed)))
        charactersUsed += segmentLength
        if charactersUsed > length:
            print("Too many characters requested. Must be less or equal to {}".format(length-charactersUsed))
            segmentManager(chars, type, password, length)
        if length-charactersUsed == 0:
            password += createSegment(segmentLength,chars)
            password = createPassword(password)
            passwordShowcase(password)
        return createSegment(segmentLength,chars)
    elif checker == "N":
        return ""
    else:
        print("Unsupported input. Try again.")
        segmentManager(chars, type, password, length)

def fillPassword(leftovers, password):
    print("You have leftover characters. With what would you like to fill the empty space?")
    print("1. Lower Case Characters")
    print("2. Upper Case Characters")
    print("3. Special Characters")
    print("4. Numbers")
    print("5. Restart")
    check = input()

    if check == "1":
        return createSegment(leftovers,string.ascii_lowercase)
    elif check == "2":
        return createSegment(leftovers,string.ascii_uppercase)
    elif check == "3":
        return createSegment(leftovers,string.punctuation)
    elif check == "4":
        return createSegment(leftovers,string.digits)
    elif check == "5":
        passwordManager(password)
    else:
        print("Unsupported input. Try again.")
        fillPassword(leftovers, password)

def passwordManager(password):
    global charactersUsed
    length = int(input("Write the number of characters in your password: "))

    if length < 1:
        print("Password must have atleast 1 character. Try again.")
        passwordManager(password)
    
    if length > 50:
        print("Password can't have more than 50 characters. Try again.")
        passwordManager(password)

    password += segmentManager(string.ascii_lowercase,"lower case", password, length)
    password += segmentManager(string.ascii_uppercase,"upper case", password, length)
    password += segmentManager(string.punctuation,"special", password, length)
    password += segmentManager(string.digits,"number", password, length)
    password += fillPassword(length-charactersUsed, password)

    return createPassword(password)

password = passwordManager(password)
passwordShowcase(password)