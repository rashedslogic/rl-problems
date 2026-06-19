import sys

class template:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def generateOutput(self):
        # # Take input from user
        # self.dprint("-------------------------------------")
        # self.dprint("Input the number.")
        # inputNumber = sys.stdin.readline()
        # if not inputNumber:
        #     return

        # number = int(inputNumber.strip())
        # self.dprint(f"The number is: {number}")

        # Print hello output
        self.dprint("-------------------------------------")
        print("Hello Output!")
        self.dprint("-------------------------------------")

if __name__ == "__main__":
    template(False).generateOutput()
