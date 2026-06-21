import sys


class statistics:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def isValidDataCounter(self, inputDataCounter: int) -> bool:
        min = 1
        max = 30
        return min <= inputDataCounter <= max

    def isValidDataSample(self, inputDataSample: int) -> bool:
        min = -1000000
        max = 1000000
        return min <= inputDataSample <= max

    def generateOutput(self):
        # Take input from user
        self.dprint("-------------------------------------")
        testCaseNumber = 0

        while not testCaseNumber >= 10:
            testCaseNumber += 1
            self.dprint(f"Input the test case {testCaseNumber}.")
            inputTestCase = sys.stdin.readline()

            # Check the validity of test case
            if not inputTestCase:
                self.dprint("Invalid input.")
                break

            # Check the input length
            dataInput = inputTestCase.strip().split()
            dataInputLength = len(dataInput)
            self.dprint(f"Data input length is: {dataInputLength}")
            if dataInputLength <= 1:
                self.dprint("Invalid input length.")
                break

            # Check the validity of data counter
            dataCounter = int(dataInput[0].strip())
            self.dprint(f"Data counter is: {dataCounter}")
            if not self.isValidDataCounter(dataCounter):
                self.dprint("Invalid data counter.")
                break

            # Check the length of data sample
            self.dprint(f"Length of data sample is: {dataInputLength-1}")
            if dataCounter != (dataInputLength - 1):
                self.dprint("Invalid lenght of data sample.")
                break

            # Build the data sample
            dataSample = []
            for i in range(dataCounter):
                valDataSample = int(dataInput[i + 1].strip())
                self.dprint(f"{i+1} Data sample value is: {valDataSample}")

                # Check the valid data sample
                if not self.isValidDataSample(valDataSample):
                    self.dprint(f"{i+1} data sample is invalid.")
                    break

                dataSample.append(valDataSample)

            # Check valid final data sample
            self.dprint(f"Final data sample is: {dataSample}")
            if len(dataSample) != dataCounter:
                self.dprint(f"Final data sample is invalid.")

            # Find min, max and range
            statMinimum = min(dataSample)
            statMaximum = max(dataSample)
            statRange = statMaximum - statMinimum
            print(f"Case {testCaseNumber}: {statMinimum} {statMaximum} {statRange}")

        self.dprint("-------------------------------------")


if __name__ == "__main__":
    statistics(False).generateOutput()
