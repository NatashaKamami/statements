# languages = ["Python", "Java", "JS", "PHP", "Rust", "C", "C#"]
# for lang in languages:
#     print(lang)

# for i in range(10):
#     print(i)

# grades = {"John": 80, "Jane": 90, "Mary": 85}
# for student, grade in grades.items():
#     print(f"{student}: {grade}")


# names = ["John" "Jane" "Mary"]
# ages = [20, 21, 22]
# for name, age in zip(names, ages):
#     print(f"{name}: {age}")


# #numbers = list(range(100))
# my_range = range(int(input("Enter a range: ")))
# numbers = list(my_range)
# even_numbers = []
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
# print(f"The even numbers between {my_range} are {even_numbers}")
# #print(sum(even_numbers))

# odd_numbers = []
# for number in numbers:
#     if number % 2 != 0:
#         odd_numbers.append(number)
# print(f"The odd numbers between {my_range} are {odd_numbers}")


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = []
odd_numbers = []
total_even = 0
total_odd = 0

for my_number in my_numbers:
    if my_number % 2 == 0:
        even_numbers.append(my_number)
        total_even += my_number
print(f"The even numbers are:{even_numbers} and the sum of the even numbers is: {total_even}")

for my_number in my_numbers:
    if my_number % 2 != 0:
        odd_numbers.append(my_number)
        total_odd += my_number
print(f"The odd numbers are:{even_numbers} and the sum of the odd numbers is: {total_odd}")


for x in range(0, 20, 5): #stat number, end number(which is not included), increaments
    print(x)