#FizzBuzz is a simple and classic programming game often used to teach basic logic and control flow. The game involves iterating through numbers from 1 up to a specified limit. For each number:

#If the number is divisible by 3, the program outputs "Fizz."
#If the number is divisible by 7, it outputs "Buzz."
#If the number is divisible by both 3 and 7, it outputs "FizzBuzz."
#Otherwise, it simply outputs the number itself in a string format.
#This game is an excellent way to practice using loops, conditionals, and modular arithmetic.
print("Welcome to FizzBuzz!")

def fizzbuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 7 == 0:
        result += "Buzz"
  # Add a small twist to the game:
  # Numbers that contain the digit "3" but aren't divisible by 3 or 7 will output Almost Fizz
    if result == "":
        if "3" in str(number):
            result = "Almost Fizz"
        else:
            result = str(number)
    return result

limit = int(input())

# Play FizzBuzz
#After the function:
  #Get input and cast it to int
  #Call the function fizzbuzz with the input number
  #Print the output of the function
for i in range(1, limit + 1):
    print(fizzbuzz(i))
