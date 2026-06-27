import sys
import time


class faktor:

    debug = False

    @staticmethod
    def dPrint(*args, **kwargs):
        if faktor.debug:
            print(*args, **kwargs)

    @staticmethod
    def isValidJournalInfo(metadata: int) -> bool:
        min = 1
        max = 100
        return min <= metadata <= max

    @staticmethod
    def generateOutput():
        # Take the line input
        inputJournalInfo = sys.stdin.readline().strip()
        if not input:
            faktor.dPrint("Input error")
            return

        # Start the timer
        startRuntime = time.perf_counter()

        # Find journal info
        journalInfo = inputJournalInfo.split()
        if len(journalInfo) != 2:
            faktor.dPrint("Wrong journal info")
            return

        numberOfArticle = int(journalInfo[0].strip())
        impactFactor = int(journalInfo[1].strip())
        faktor.dPrint(
            f"Number of Article: {numberOfArticle} and impact factor {impactFactor}"
        )

        if any(
            not faktor.isValidJournalInfo(i) for i in [numberOfArticle, impactFactor]
        ):
            faktor.dPrint("Invalid journal info")

        bribedScientist = numberOfArticle * (impactFactor - 1) + 1
        print(bribedScientist)

        # Stop the timer here
        endRuntime = time.perf_counter()
        totalRuntime = endRuntime - startRuntime

        faktor.dPrint(f"[Algorithmic Runtime] {totalRuntime:.6f} seconds")


if __name__ == "__main__":
    faktor.generateOutput()
