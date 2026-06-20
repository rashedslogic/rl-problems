import sys


class helpaphd:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def generateOutput(self):
        # Take input from user
        self.dprint("-------------------------------------")
        self.dprint("Input the number of test cases.")
        inputNumberOfTestCases = sys.stdin.readline()
        if not inputNumberOfTestCases:
            return

        numberOfTestCases = int(inputNumberOfTestCases.strip())
        self.dprint(f"The number of test cases is: {numberOfTestCases}")
        self.dprint("-------------------------------------")

        # Process each test case
        for i in range(numberOfTestCases):
            # Take input of test case
            self.dprint(f"Input the test case {i+1}.")
            inputTestCase = sys.stdin.readline()
            if not inputTestCase:
                break

            # Print output of test case
            inputTestCase = inputTestCase.strip()
            if inputTestCase == "P=NP":
                print("skipped")
            else:
                inputNumbers = inputTestCase.split("+")
                numberOne = int(inputNumbers[0].strip())
                numberTwo = int(inputNumbers[1].strip())
                self.dprint(f"Number one: {numberOne} and number two: {numberTwo}")
                print(numberOne + numberTwo)

        # self.dprint("-------------------------------------")


if __name__ == "__main__":
    helpaphd(False).generateOutput()
