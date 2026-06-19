import sys

# Increase the limit to 15,000 digits so it safely handles 10^4 digits
sys.set_int_max_str_digits(15000)

class simpleaddition:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def generateOutput(self):
        # Take input from user
        self.dprint("-------------------------------------")
        self.dprint("Input first number.")
        inputFirstNumber = sys.stdin.readline()
        self.dprint("Input second number.")
        inputSecondNumber = sys.stdin.readline()
        if not inputFirstNumber or not inputSecondNumber:
            return

        firstNumber = int(inputFirstNumber.strip())
        secondNumber = int(inputSecondNumber.strip())
        self.dprint(f"First number is: {firstNumber} and Second number is: {secondNumber}")

        # Add two numbers
        self.dprint("-------------------------------------")
        print(firstNumber + secondNumber)
        self.dprint("-------------------------------------")

if __name__ == "__main__":
    simpleaddition(False).generateOutput()
