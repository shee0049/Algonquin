from time import sleep

def printTriangularNumbers(n):
    count = 0
    while (count <= n):
        triSum = int(count*(count+1)/2)
        print(count , triSum)
        count = count + 1

def myFactorial(n):
    count = 1
    while (count <= n):
        factorial = count * (count - 1)
        print(factorial)
        count += 1

def checkOddEven():
    for x in range(1,21):
        if x % 2 == 0:
            print(x , "Is Even!")
        elif x % 3 == 0:
            print(x , "Is Odd!")

def printAsterisksV1(n):
    for x in range(n+1):
        print("*" * x)
        x += 1

def printAsterisksV2(n):
    count = 0
    while count <= n:
        print("*" * count)
        count += 1
        
def printDiagonally(string):
    x = 0 
    while x < len(string):
        print((" " * x) + string[x])
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
    prompt = raw_input("Would you like to continue? Y\N:  ").lower()
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
        choice = input("Please Select: ")
        print("\n")
    
        if choice == 1:
            n = int(input("Input for Triangular Numbers: "))
            printTriangularNumbers(n)
            isRunning = promptAgain()
        if choice == 2:
            myFactorial(6)
            isRunning = promptAgain()
        if choice == 3:
            checkOddEven()
            isRunning = promptAgain()
        if choice == 4:
            printAsterisksV1(10)
            isRunning = promptAgain()
        if choice == 5:
            printAsterisksV2(10)
            isRunning = promptAgain()
        if choice == 6:
            printDiagonally()
            isRunning = promptAgain()
        
            
    
