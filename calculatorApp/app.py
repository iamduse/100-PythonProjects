import art
def calculator_app():
    print(art.logo)

    #Functions
    def add(n1, n2):
        return n1 + n2
    def multiply(n1, n2):
        return n1 * n2
    def subtract(n1, n2):
        return n1 - n2

    def divide(n1, n2):
        return n1 / n2
    #Store the function as dictionary so, I can use as key and value
    calculator = {
        "+": add, # when you don't call a function u don't need to add the ()
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    first_number = float(input("Enter First Number: "))
    want_to_continue = True
    while want_to_continue:
        for symbol in calculator:
            print(symbol)
        symbol = input("choose operator: ")
        second_number = float(input("Enter second Number: "))
        result = calculator[symbol](first_number, second_number)
        print(result)

        restart = input("Do you want to continue with the previous result, please type 'y' for yes 'n' for n: ")
        if restart == "y".lower():
            first_number = result

        else:
            want_to_continue = False
            print("GOOD LUCK")
            #calculator_app()


calculator_app()



