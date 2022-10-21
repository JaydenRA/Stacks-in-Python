size = int(input("Size of stack: "))

stack = []
for i in range(size):
    stack.append(None)
    
counter = -1

def main():
    choice = int(input('''
1 - Push
2 - Pop
3 - Show Stack

9 - Exit

Choice: '''))

    if choice == 1:
        element = input("Element: ")
        myPush(element)

    elif choice == 2:
        myPop()

    elif choice == 3:
        showStack()

    elif choice == 9:
        exit()

    else:
        print("That's not an option. Please try again \n")
        main()

def myPush(element):
    global counter
    if counter != (len(stack)-1):
        counter += 1
        stack[counter] = element
    else:
        print("Stack Overflow Error")
    main()

def myPop():
    global counter
    if counter >= 0:
        stack[counter] = None
        counter -= 1
    else:
        print("Stack Underflow Error")
    main()

def showStack():
    print(f"{stack}\n")
    main()

main()
