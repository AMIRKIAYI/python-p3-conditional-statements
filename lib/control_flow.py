# !/usr/bin/env python3
# Check authenticity 🥰🥰🥰🥰🥰
def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
print(admin_login("sudo", "12345"))    
print(admin_login("admin", "12345"))
print(admin_login("ADMIN", "12345"))



#Check the tempereture 😜😜😜😜😜😜
def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
print(hows_the_weather(33))
print(hows_the_weather(99))
print(hows_the_weather(75))
    
# Divisibility of numbers 🫠🫠🫠🫠
def fizzbuzz(number):
    # your code here
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    
    else:
        return number
print(f"this number is {fizzbuzz(15)}")  


# use Operation sighn given to calculate 🤣🤣🤣🤣
def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "/":
        return num1/num2
    elif operation == "*":
        return num1 * num2
    else:
        print("Invalid operation!") == None
       
    
    
print(calculator("/", 5, 5))

        
 
#Using if elif else statement😁😁😁😁😁
dog = "hungry"
if dog == "lazy":
    owner = "chase him away."
elif dog == "sleep":
    owner = "let him sleep."
elif dog == "barking":
    owner = "shut him up."
elif dog == "hungry":
    owner = "feed him."
else:
    owner = "I don't know what to do."
print(owner)

#Using try and except😅😅😅😅😅
def divide(num1, num2):
    try: 
        quotient=num1/num2
        print(quotient)
    except:
        print("An error occured")    

divide(2, 6)

#Using finally 😆😆😆😆😆
def divide2(num3, num4):
    try:
        quotient=num3/num4
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float.")
    finally:
        print("Isn't division fun?")    

divide2(8, 3)


#Using dictionary mapping😂😂😂😂😂😂
dog = "thirsty"
dict_map = {
    "hungry": "preparing food",
    "thirsty": "refiling water bowl",
    "playfull": "playing tag of war",
    "curdly": "snuggling"

}

# Remember that a dictionary's .get() method lets us set a default value!🙂🙂🙂🙂🙂
owner= dict_map.get(dog, "reading newspaper")
print(owner)



# #Iterate through numbers😉😉😉😉😉
# for i in range(10):
#     print("Looping!")
#     print(f"i is: {i}")


# bottle_heights = [0.008, 0.09, 0.006, 0.007, 0.005] #measurement in metres

# cm_heights = [height * 100 for height in bottle_heights] # Why is 0.007 misbehaving????😕😕😕😕😇😇😇

# print(cm_heights)


