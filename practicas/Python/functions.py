def say_hello():
    return "Hello"

print(say_hello())

def say_hello_user(name):
    print("Hello " + name)

name = "David"

say_hello_user(name)

def user_age(current_year, birth_year):
    age = current_year - birth_year
    return age

print(user_age(2021, 1998))

def sum_two_numbers(x, y):
    sum = x + y
    return sum

print("Addition = ",sum_two_numbers(5,7))

def full_name(first_name, last_name):
    name = first_name + last_name
    return name

print(full_name("David", "Aznar"))
