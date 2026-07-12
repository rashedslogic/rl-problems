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

class quadrant:
    DEBUG = False
    _start_runtime = 0.0

    @classmethod
    def init(cls) -> None:
        FastScanner.init()
        if cls.DEBUG:
            cls._start_runtime = time.perf_counter()

    @classmethod
    def close(cls) -> None:
        """Evaluates hardware runtime execution speed."""
        if cls.DEBUG:
            total_runtime = time.perf_counter() - cls._start_runtime
            print(f"[Algorithmic Runtime] {total_runtime:.6f} seconds", file=sys.stderr)

    @classmethod
    def d_print(cls, *args, sep=" ") -> None:
        """Enterprise trace logger. Always routes to stderr safely."""
        if cls.DEBUG:
            print(f"[DEBUG] {sep.join(map(str, args))}", file=sys.stderr)
    
    @classmethod  
    def isValidCoordinate(cls, value: int) -> bool:
        min = -1000
        max = 1000
        return min <= value <= max and value != 0

    @classmethod
    def solve(cls) -> None:
        # First loading
        next_string = FastScanner.next_string
        next_int = FastScanner.next_int
        write = sys.stdout.write
        d_print = cls.d_print

        # Take the coordinate input
        inputX = next_int()
        inputY = next_int()
        extraInput = next_string()
        if inputX is None or inputY is None or extraInput is not None:
            d_print("Wrong input")
            return

        # Is valid input
        d_print("Parsed Coordinates -> X:", inputX, "Y:", inputY)
        if any(not cls.isValidCoordinate(coordinate) for coordinate in [inputX, inputY]):
            d_print("Invalid input")

        # Find quadrant
        if inputX > 0 and inputY > 0:
            write("1\n")
        elif inputX < 0 and inputY > 0:
            write("2\n")
        elif inputX < 0 and inputY < 0:
            write("3\n")
        elif inputX > 0 and inputY < 0:
            write("4\n")
        else:
            d_print("Unknown coordinate")


if __name__ == "__main__":
    quadrant.init()
    quadrant.solve()
    quadrant.close()