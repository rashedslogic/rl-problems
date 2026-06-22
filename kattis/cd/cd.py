import sys

class cd:

    def __init__(self, debug: bool = False):
        self.debug = debug

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
    
    def isTerminated(self, inputText: str) -> bool:
        return inputText.strip() == "0 0"

    def generateOutput(self):
        # Take input from user
        self.dprint("-------------------------------------")
        while True:
            self.dprint("Input the test case metadata.")
            inputMetadata = sys.stdin.readline()

            if not inputMetadata:
                self.dprint("Invalid input.")
                break
            
            # Terminate the input if the input is 0 0
            if self.isTerminated(inputMetadata):
                self.dprint("Termination command is found, exiting.")
                break

            # Process two metadata
            self.dprint(f"Raw input: {inputMetadata}")
            metadata = inputMetadata.strip().split()
            numberOfMetadata = len(metadata)
            self.dprint(f"Number of metadata: {numberOfMetadata}")
            if numberOfMetadata != 2:
                self.dprint("Invalid number of metadata.")
                break

            numberOfCdByJack = int(metadata[0].strip())
            numberOfCdByJill = int(metadata[1].strip())
            self.dprint(
                f"Number of CDs owned by Jack: {numberOfCdByJack} and Number of CDs owned by Jill: {numberOfCdByJill}"
            )

            # Check the valid metadata
            if any(not self.isValidMetadata(n) for n in [numberOfCdByJack, numberOfCdByJill]):
                self.dprint("Invalid metadata.")
                break
            
            # Process the input for Jack's CD
            catalogNumberJack = set()
            self.dprint("Input Jack's catalog number.")
            for i in range(numberOfCdByJack):
                self.dprint(f"Input Jack's number {i+1} catalog number of CD")
                inputCatalogNumberOfJack = sys.stdin.readline()

                # Check invalid catalog input.
                if not inputCatalogNumberOfJack:
                    self.dprint("Invalid catalog input.")
                    break
                
                # Find the valid catalog number.
                valCatalogNumberJack = int(inputCatalogNumberOfJack.strip())
                if not self.isValidCatalogNumber(valCatalogNumberJack):
                    self.dprint("Invalid catalog number.")
                    break
                
                # Store catalog number
                self.dprint(f"Jack's catalog number {i+1} is: {valCatalogNumberJack}")
                catalogNumberJack.add(valCatalogNumberJack)
            self.dprint(f"Total catalog numbers of Jack: {catalogNumberJack}")
                
            # Process the input for Jill's CD
            catalogNumberJill = set()
            self.dprint("Input Jill's catalog number.")
            for i in range(numberOfCdByJill):
                self.dprint(f"Input Jill's number {i+1} catalog number of CD")
                inputCatalogNumberOfJill = sys.stdin.readline()

                # Check invalid catalog input.
                if not inputCatalogNumberOfJill:
                    self.dprint("Invalid catalog input.")
                    break
                
                # Find the valid catalog number.
                valCatalogNumberJill = int(inputCatalogNumberOfJill.strip())
                if not self.isValidCatalogNumber(valCatalogNumberJill):
                    self.dprint("Invalid catalog number.")
                    break
                
                # Store catalog number
                self.dprint(f"Jill's catalog number {i+1} is: {valCatalogNumberJill}")
                catalogNumberJill.add(valCatalogNumberJill)
            self.dprint(f"Total catalog numbers of Jill: {catalogNumberJill}")
            
            # Find the number of common CDs
            commonCatalogNumbers = set(catalogNumberJack) & set(catalogNumberJill)
            self.dprint(f"Common catalog numbers: {commonCatalogNumbers}")
            self.dprint("Common catalog numbers count is:")
            print(len(commonCatalogNumbers))

        self.dprint("-------------------------------------")

if __name__ == "__main__":
    cd(False).generateOutput()
