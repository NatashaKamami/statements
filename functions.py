# def function_name(parameters): 
#     return value


def greeting(name):
    print(f"Hi, {name}")   

greeting("Jane")


#A function that calculates the sum of numbers
def sum_of_numbers(num1, num2): 
    return num1 + num2

result = sum_of_numbers(3, 4)
result2 = sum_of_numbers(100, 200)
print(result)
print(result2)


#A function that finds the largest/maximum number 
def find_max_number(a, b, c, d):  
    return max(a, b, c, d)

max_number = find_max_number(2, 5, 8, -10)
print(max_number)


#A function that finds the smallest/minimum number
def find_min_number(a, b, c, d): 
    return min(a, b, c, d)

min_number = find_min_number(2, 5, 8, -10)
print(min_number)


#A function that calculates the area of a circle
import math
#print(math.pi)

def area_of_circle(radius): 
    return math.pi * radius **2

area = area_of_circle(14)
print(area)


#A function that checks password strength
import string
def check_pass_strength(password):
    special_characters = string.punctuation #enables us to include special characters(punctuation)
    if len(password) < 8:
        return "Weak"
    elif not any(char.isdigit() for char in password): #if none of the characters is a number
        return "Moderate"
    elif not any(char.isupper() for char in password): #if none of the characters is uppercase
        return "Moderate"
    elif not any(char in special_characters for char in password): #if none of the characters is a special character
        return "Moderate"
    else:
        return "Strong"
       
#pass_strength = check_pass_strength("Ez2djjeeiotrojfje@")
pass_strength = check_pass_strength(input("Enter your password :"))
print(f"Password strength: {pass_strength}")


#A function that creates/generates a random password
import secrets, string
def generate_random_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    # print(characters)
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

random_password = generate_random_password()
print(random_password)


#A function that calculates compoud interest
def compound_interest(principal, rate, time):
    
    total_amount = principal * (1 + rate/100) ** time
    interest = total_amount - principal
    return interest

interest = compound_interest(int(input("Enter Principal: ")), int(input("Enter the rate: ")), int(input("Enter the time: ")))
print(f"Compound interest: {interest}")
