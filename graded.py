def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
     problem5()

# Problem-1
# Create a function with the variable below.
# After you create the variable do the instructions below that.
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# a) Print the 3rd element of the numberList.
# b) Print the size of the array
# c) Delete the second element.
# d) Print the 3rd element.

def problem1():
    arrayForProblems = ["Kenn", "Kevin", "Erin", "Meka"]
    print(arrayForProblems[2])
    print(len(arrayForProblems))
    arrayForProblems.remove("Kevin")
    print(arrayForProblems[2])

# Problem-2
# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', '
# ask them to input another string

def problem2():
    letter = ""
    while(letter != "q"):
        letter = input("Whats your fav letter? ")

# Problem-3
# Create a function that contains a collection of information for the following.
# After you create the collection do the instructions below that.
# Jonathan/John;Michael/Mike;William/Bill;Robert/Rob
# a) Print the collection
# b) Print William's nickname

def problem3():
     nicknames ={
        "Jonathan":"John",
        "Michael": "Mike",
        "William": "Bill",
        "Robert": "Rob"
    }
     print(nicknames)
     print(nicknames["William"])

# Problem-4
# Create an array of 5 numbers. Using a loop,
# print the elements in the array reverse order.
# Do not use a function

def problem4():
    numbers = [3,6, 18, 24, 99]
    for eachEl in range(len(numbers)-1,-1,-1):
        print(numbers[eachEl])

# Problem5():
# Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.

def problem5():
    nummies = [3,6, 18, 24, 99]
    userInput = input("Enter a number.")

for numbers in sequence:
    userInput = input("Enter a number.")
        if(nummies > userInput):
            print("higher")
        if(nummies = userInput):
            print("equal")
        if(nummies < userInput):
            print("lower")



if __name__ == '__main__':
    main()