import sys

class dagatal:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def getDaysInMonth(self, month: int) -> int:
        days_map = {
            1: 31,  # January
            2: 28,  # February (as 2019 is not leap year)
            3: 31,  # March
            4: 30,  # April
            5: 31,  # May
            6: 30,  # June
            7: 31,  # July
            8: 31,  # August
            9: 30,  # September
            10: 31,  # October
            11: 30,  # November
            12: 31,  # December
        }
        return days_map.get(month, None)

    def generateOutput(self):
        # Take input the number of month
        self.dprint("-------------------------------------")
        self.dprint("Input the number of month.")
        inputNumberOfMonth = sys.stdin.readline()
        if not inputNumberOfMonth:
            return

        numberOfMonth = int(inputNumberOfMonth.strip())
        self.dprint(f"The number of month is: {numberOfMonth}")

        if not (1 <= numberOfMonth <= 12):
            self.dprint(f"{numberOfMonth} is an invalid input!")
            return

        # Find the number of days in a month
        self.dprint("-------------------------------------")
        print(f"{self.getDaysInMonth(numberOfMonth)}")
        self.dprint("-------------------------------------")


if __name__ == "__main__":
    dagatal(False).generateOutput()
