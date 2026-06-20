import sys


class carrots:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def generateOutput(self):
        # Take input from user
        self.dprint("-------------------------------------")
        self.dprint("Input the contestants and solved problem count")
        inputNumbers = sys.stdin.readline()
        if not inputNumbers:
            return

        numbers = inputNumbers.strip().split()
        if len(numbers) != 2:
            return

        contestants = int(numbers[0])
        solvedProblems = int(numbers[1])
        self.dprint(f"Contestants: {contestants} and Solved Problems: {solvedProblems}")

        # Print number of carrot
        self.dprint("-------------------------------------")
        self.dprint("The number of carrot is:")
        print(solvedProblems)
        self.dprint("-------------------------------------")


if __name__ == "__main__":
    carrots(False).generateOutput()
