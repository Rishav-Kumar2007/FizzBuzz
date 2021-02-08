def fizzbuzz():
    try:
        number=int(input("Enter a number: "))
    except :
        print("Invalid input!")
    if number%3==0 and number%5==0:
        return("FizzBuzz")
    elif number%3==0:
        return("Buzz")
    elif number%5==0:
        return("Fizz")
    else:
        return("None")


print(fizzbuzz())