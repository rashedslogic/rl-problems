import sys
import time


class cd:

    debug = False

    @staticmethod
    def dprint(*args, **kwargs):
        if cd.debug:
            print(*args, **kwargs)

    @staticmethod
    def generateOutput():
        # This line blocks and waits for input stream closure (Human Time)
        tokens = sys.stdin.read().split()
        if not tokens:
            return

        # Start the timer
        startRuntime = time.perf_counter()

        iterator = iter(tokens)

        while True:
            try:
                nStr = next(iterator)
                mStr = next(iterator)
            except StopIteration:
                break

            mN = int(nStr)
            mM = int(mStr)

            # Break if termination line(0 0)
            if mN == 0 and mM == 0:
                break

            # Store Jack's CD into a raw primitive array
            jackCDs = [int(next(iterator)) for _ in range(mN)]
            cd.dprint(f"Jacks CD: {jackCDs}")

            # Perform Two-pointer intersection sweep comparing Jill's CDs
            intersectionCount = 0
            jackCDsIndex = 0

            for _ in range(mM):
                jill_cd = int(next(iterator))

                while jackCDsIndex < mN and jackCDs[jackCDsIndex] < jill_cd:
                    jackCDsIndex += 1

                # Store the intersection information
                if jackCDsIndex < mN and jackCDs[jackCDsIndex] == jill_cd:
                    intersectionCount += 1
                    jackCDsIndex += 1

            # Print the final output of common items
            print(intersectionCount)

        # Stop the timer here
        endRuntime = time.perf_counter()
        totalRuntime = endRuntime - startRuntime

        cd.dprint(f"[Algorithmic Runtime] {totalRuntime:.6f} seconds")


if __name__ == "__main__":
    cd.generateOutput()
