import sys


class leftbeehind:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def generateOutput(self):
        # Take input from user
        self.dprint("-------------------------------------")
        testCaseNumber = 0
        while not testCaseNumber >= 15:
            testCaseNumber += 1
            self.dprint(f"Input the test case {testCaseNumber}.")

            inputNumberOfJars = sys.stdin.readline()
            if not inputNumberOfJars:
                self.dprint("Invalid input.")
                break

            numberOfJars = inputNumberOfJars.strip().split()
            if len(numberOfJars) != 2:
                self.dprint("Input count is not 2.")
                break

            sweetJars = int(numberOfJars[0].strip())
            sourJars = int(numberOfJars[1].strip())
            self.dprint(f"Sweet Jars: {sweetJars} and Sour Jars: {sourJars}")

            match (sweetJars, sourJars):
                case (0, 0):
                    break
                case (sweet, sour) if sweet + sour == 13:
                    print("Never speak again.")
                case (sweet, sour) if sweet < sour:
                    print("Left beehind.")
                case (sweet, sour) if sweet == sour:
                    print("Undecided.")
                case (sweet, sour) if sweet > sour:
                    print("To the convention.")

        self.dprint("-------------------------------------")


if __name__ == "__main__":
    leftbeehind(False).generateOutput()
