import sys

class telja:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def generateOutput(self):
        # Take input from user
        self.dprint("-------------------------------------")
        self.dprint("Input the number.")
        inputNumber = sys.stdin.readline()
        if not inputNumber:
            return

        number = int(inputNumber.strip())
        self.dprint(f"The number is: {number}")

        # Count upto the input number sequentially in different line
        self.dprint("-------------------------------------")
        # Approach 1
        # for i in range(1, number+1):
            # print(i)

        # Approach 2
        for i in range(number):
            print(i + 1)
        self.dprint("-------------------------------------")

if __name__ == "__main__":
    telja(False).generateOutput()
