import sys
import time
from typing import Optional

sys.setrecursionlimit(300000)

class FastScanner:
    tokens = None

    @classmethod
    def init(cls) -> None:
        cls.tokens = iter(sys.stdin.read().split())

    @classmethod
    def next_string(cls) -> Optional[str]:
        try:
            return next(cls.tokens)
        except StopIteration:
            return None

    @classmethod
    def next_int(cls) -> Optional[int]:
        token = cls.next_string()
        return int(token) if token is not None else None

    @classmethod
    def next_double(cls) -> Optional[float]:
        token = cls.next_string()
        return float(token) if token is not None else None

class moscowdream:
    DEBUG = False
    _start_runtime = 0.0

    @classmethod
    def init(cls) -> None:
        FastScanner.init()
        if cls.DEBUG:
            cls._start_runtime = time.perf_counter()

    @classmethod
    def close(cls) -> None:
        if cls.DEBUG:
            total_runtime = time.perf_counter() - cls._start_runtime
            print(f"[Algorithmic Runtime] {total_runtime:.6f} seconds", file=sys.stderr)

    @classmethod
    def d_print(cls, *args, sep=" ") -> None:
        if cls.DEBUG:
            print(f"[DEBUG] {sep.join(map(str, args))}", file=sys.stderr)
    
    @classmethod  
    def isValidProblem(cls, value: int) -> bool:
        min = 0
        max = 10
        return min <= value <= max

    @classmethod    
    def isValidNumberOfProblem(cls, value: int) -> bool:
        min = 0
        max = 20
        return min <= value <= max
    
    @classmethod
    def hasAtLeastOneProblem(cls, val: int) -> bool:
        return val >= 1

    @classmethod
    def solve(cls) -> None:
        # First loading
        next_string = FastScanner.next_string
        next_int = FastScanner.next_int
        write = sys.stdout.write
        d_print = cls.d_print

        # Take the input of problemset info
        inputA = next_int()
        inputB = next_int()
        inputC = next_int()
        inputN = next_int()
        extraInput = next_string()

        # Wrong input
        if None in (inputA, inputB, inputC, inputN) or extraInput is not None:
            d_print("Wrong input")
            return

        # Invalid input
        if any(not cls.isValidProblem(n) for n in [inputA, inputB, inputC]) or not cls.isValidNumberOfProblem(inputN):
            d_print("Invalid input")
            return

        # Find problemset info
        d_print("Parsed info -> a: ", inputA, " b: ", inputB, " c: ", inputC, " n: ", inputN)
        if any(not cls.hasAtLeastOneProblem(n) for n in [inputA, inputB, inputC]):
            d_print("Each item does not has at least 1 problem")
            write("NO\n")
            return

        if inputN >= 3 and (inputA + inputB + inputC) >= inputN:
            d_print("Valid problemset")
            write("YES\n")
        else:
            write("NO\n")

if __name__ == "__main__":
    moscowdream.init()
    moscowdream.solve()
    moscowdream.close()