import sys
 
class busassignment:
 
    def __init__(self, debug: bool = False):
        self.debug = debug
 
    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)
 
    def findMaximumCapacity(self):
        # Find the number of stopage
        self.dprint("Input number of stopage.")
        inputNumberOfStopage = sys.stdin.readline()
        if not inputNumberOfStopage:
            return
 
        numberOfStopage = int(inputNumberOfStopage.strip())
        self.dprint(f"Number of stopage: {numberOfStopage}")
        self.dprint("-------------------------------------")
 
        # Process all passengers at each stopage
        currentPassenger = 0
        maximumCapacity = 0

        for i in range(numberOfStopage):
            # Find the number of passengers
            self.dprint(f"Input the off/on passengers for stopage {i+1}")
            inputNumberOfPassengers = sys.stdin.readline()
            if not inputNumberOfPassengers:
                break
 
            numberOfPassengers = inputNumberOfPassengers.strip().split()
            if len(numberOfPassengers) != 2:
                break
            getOffPassengers = int(numberOfPassengers[0])
            getOnPassengers = int(numberOfPassengers[1])
            self.dprint(f"Get off passengers: {getOffPassengers} and get on passengers: {getOnPassengers}")
 
            # Calculate net passengers at this stopage
            currentPassenger += (getOnPassengers - getOffPassengers)
            self.dprint(f"Current passengers: {currentPassenger}")
 
            # Calculate maximum capcity of the bus
            maximumCapacity = max(maximumCapacity, currentPassenger)
            self.dprint(f"Maximum capacity at stopage {i+1}: {maximumCapacity}")
            self.dprint("-------------------------------------")

        print(maximumCapacity)
        self.dprint("-------------------------------------")
 
if __name__ == "__main__":
    busassignment(False).findMaximumCapacity()