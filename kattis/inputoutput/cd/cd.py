import sys

class cd:

    def __init__(self, debug: bool = False):
        self.debug = debug
        self.tokens = iter(sys.stdin.read().split())

    def nextTokenString(self) -> str:
        try:
            return next(self.tokens)
        except StopIteration:
            return None

    def nextTokenInt(self) -> int:
        token: str = self.nextTokenString()
        return int(token) if token is not None else None

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)
            
    def isValidMetadata(self, metadata: int) -> bool:
        min = 1
        max = 1000000
        return min <= metadata <= max
    
    def isValidCatalogNumber(self, catalogNumber: int) -> bool:
        minimum = 1
        maximum = 1000000000  # 1 Billion 10^9
        return minimum <= catalogNumber <= maximum

    def generateOutput(self):
        # Take input from user
        self.dprint("-------------------------------------")
        self.dprint("Input the test cases.")
        while True:
            numberOfCdByJack = self.nextTokenInt()
            numberOfCdByJill = self.nextTokenInt()

            # Terminate the input if the input is 0 0 or EOF
            if numberOfCdByJack is None or numberOfCdByJill is None or (numberOfCdByJack == 0 and numberOfCdByJill == 0):
                self.dprint("Termination condition or EOF reached.")
                break

            self.dprint(
                f"Number of CDs owned by Jack: {numberOfCdByJack} and Number of CDs owned by Jill: {numberOfCdByJill}"
            )

            # Check the valid metadata
            if any(not self.isValidMetadata(n) for n in [numberOfCdByJack, numberOfCdByJill]):
                self.dprint("Invalid metadata.")
                break
            
            # Process the input for Jack's CD
            catalogNumbersJack = [0] * numberOfCdByJack
            self.dprint("Input Jack's catalog number.")
            for i in range(numberOfCdByJack):
                self.dprint(f"Input Jack's number {i+1} catalog number of CD")
                valCatalogNumberOfJack = self.nextTokenInt()

                # Check invalid catalog input.
                if valCatalogNumberOfJack is None:
                    self.dprint("Invalid input(EOF reached early).")
                    break
                
                # Find the valid catalog number.
                if not self.isValidCatalogNumber(valCatalogNumberOfJack):
                    self.dprint("Invalid catalog number.")
                    break
                
                # Store catalog number
                self.dprint(f"Jack's catalog number {i+1} is: {valCatalogNumberOfJack}")
                catalogNumbersJack[i] = valCatalogNumberOfJack
            self.dprint(f"Total catalog numbers of Jack: {catalogNumbersJack}")

            # Process the input for Jill's CD
            catalogNumbersJill = [0] * numberOfCdByJill
            self.dprint("Input Jill's catalog number.")
            for i in range(numberOfCdByJill):
                self.dprint(f"Input Jill's number {i+1} catalog number of CD")
                valCatalogNumberOfJill = self.nextTokenInt()

                # Check invalid catalog input.
                if valCatalogNumberOfJill is None:
                    self.dprint("Invalid input(EOF reached early).")
                    break
                
                # Find the valid catalog number.
                if not self.isValidCatalogNumber(valCatalogNumberOfJill):
                    self.dprint("Invalid catalog number.")
                    break
                
                # Store catalog number
                self.dprint(f"Jill's catalog number {i+1} is: {valCatalogNumberOfJill}")
                catalogNumbersJill[i] = valCatalogNumberOfJill
            self.dprint(f"Total catalog numbers of Jill: {catalogNumbersJill}")
            
            # Find the number of common CDs using two pointer approache for reducing time limit exceed
            jackPtr = 0
            jillPtr= 0
            commonCount = 0 
            jackCatalogCount = len(catalogNumbersJack)
            jillCatalogCount = len(catalogNumbersJill)

            while jackPtr < jackCatalogCount and jillPtr < jillCatalogCount:
                if catalogNumbersJack[jackPtr] == catalogNumbersJill[jillPtr]:
                    commonCount += 1
                    jackPtr += 1
                    jillPtr += 1
                elif catalogNumbersJack[jackPtr] < catalogNumbersJill[jillPtr]:
                    jackPtr += 1
                else:
                    jillPtr += 1

            self.dprint("Common catalog numbers count is:")
            print(commonCount)

        self.dprint("-------------------------------------")

if __name__ == "__main__":
    cd(False).generateOutput()
