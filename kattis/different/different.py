import sys


class different:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def generateOutput(self):
        # Take input from user
        self.dprint("-------------------------------------")
        self.dprint("Input the file.")

        while True:
            inputLine = sys.stdin.readline()

            # EOF Check: stop loop if no more input is available
            if not inputLine:
                self.dprint("Reached end of file.")
                break

            # Find two numbers
            inputTwoNumbers = inputLine.strip().split()
            if len(inputTwoNumbers) != 2:
                self.dprint("Input count is not 2.")
                break

            firstNumber = int(inputTwoNumbers[0].strip())
            secondNumber = int(inputTwoNumbers[1].strip())
            self.dprint(
                f"First Number: {firstNumber} and Second Number: {secondNumber}"
            )

            # Calculate the absolute value
            self.dprint("This is absolute value:")
            print(abs(firstNumber - secondNumber))

        self.dprint("-------------------------------------")


if __name__ == "__main__":
    different(False).generateOutput()
