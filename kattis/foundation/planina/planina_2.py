import sys
import time


class planina:

    debug = False

    @staticmethod
    def dPrint(*args, **kwargs):
        if planina.debug:
            print(*args, **kwargs)

    @staticmethod
    def isValidIterationNumber(value: int) -> bool:
        min = 1
        max = 15
        return min <= value <= max

    @staticmethod
    def generateOutput():
        # Take the line input
        inputIterationNumber = sys.stdin.readline().strip()
        if not input:
            planina.dPrint("Input error")
            return

        # Start the timer
        startRuntime = time.perf_counter()
 
        # Find valid input
        if not inputIterationNumber.isdigit():
            planina.dPrint("Input is not valid")
            return

        # Find iteration number
        iterationNumber = int(inputIterationNumber)
        if not planina.isValidIterationNumber(iterationNumber):
            planina.dPrint("Wrong iteration number")
            return

        # Find the number of points on a single side
        planina.dPrint(f"Totla Iteration Number: {iterationNumber}")
        # Rules: (2^N + 1)^2
        pointsOnSide = ((2 ** iterationNumber) + 1)
        planina.dPrint(f"Points on a single side: {pointsOnSide}")

        # Find the total number of points
        numberOfPoints =(pointsOnSide ** 2)
        planina.dPrint("Number of Points:")
        print(numberOfPoints)

        # Stop the timer here
        endRuntime = time.perf_counter()
        totalRuntime = endRuntime - startRuntime

        planina.dPrint(f"[Algorithmic Runtime] {totalRuntime:.6f} seconds")


if __name__ == "__main__":
    planina.generateOutput()
