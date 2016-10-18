from time import sleep

def printTriangularNumbers(n):
    count = 0
    while (count <= n):
        triSum = int(count*(count+1)/2)
        print count , triSum
        count = count + 1

def myFactorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def checkOddEven():
    for x in range(0,21):
        if x % 2 == 0:
            print x , "Is Even!"
        elif x % 3 == 0 or x % 1 == 0:
            print x , "Is Odd!"

def printAsterisksV1(n):
    for x in range(n):
        print "*"
        x += 1

def printAsterisksV2(n):
    count = 0
    while count < n:
        print("*")
        count += 1

def printDiagonally(string):
    x = 0
    while x < len(string):
        print " " * x + string[x]
        x += 1

def printUserMenu():
    menu = """
    1. Test printTriangularNumbers
    2. Test myFactorial
    3. Test checkOddEven
    4. Test printAsterisksV1
    5. Test printAsterisksV2
    6. Test printDiagonally
    7. Exit
    """
    print(menu)

def promptAgain():
    prompt = raw_input("Would you like to continue? Y/N:  ").lower()
    if prompt == 'y':
        return True
    if prompt == 'n':
        print("Exiting Now")
        sleep(0.5)
        return False
    else:
        print("Wrong input: ")
        return promptAgain()

if __name__ == "__main__":
    isRunning = True
    while isRunning:
        printUserMenu()
        choice = input("Please Select an Option 1-7: ")
        print "\n"

        if choice == 1:
            i = int(input("Input how many triangular numbers to display: "))
            printTriangularNumbers(i)
            isRunning = promptAgain()
        if choice == 2:
            i = int(input("Input for myFactorial: "))
            num = myFactorial(i)
            print(num)
            isRunning = promptAgain()
        if choice == 3:
            checkOddEven()
            isRunning = promptAgain()
        if choice == 4:
            i = input("Enter in the number of Asterisks:  ")
            printAsterisksV1(i)
            isRunning = promptAgain()
        if choice == 5:
            i = input("Enter in the number of Asterisks:  ")
            printAsterisksV2(i)
            isRunning = promptAgain()
        if choice == 6:
            print("Enter in a string to print")
            i = raw_input(">> ")
            printDiagonally(i)
            isRunning = promptAgain()
        if choice == 7:
            print("Exiting Now")
            sleep(0.5)
            isRunning = False
