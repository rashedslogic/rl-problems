class hello:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def generateOutput(self):
        # Print Hello World!
        self.dprint("-------------------------------------")
        print("Hello World!")
        self.dprint("-------------------------------------")

if __name__ == "__main__":
    hello(False).generateOutput()