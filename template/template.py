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


class template:
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
    def solve(cls) -> None:
        # ---------------------------------------------------------------------
        # CHOOSE YOUR ARCHITECTURAL INPUT PATTERN BASED ON THE PROBLEM:
        # ---------------------------------------------------------------------
        
        # PATTERN 1: Single Line / Known Constraints (e.g., Faktor, Planina)
        # n_str = next_string()
        # if n_str is not None:
        #     n = int(n_str)
        #     d_print("Input:", n)
        #     write(f"{n}\n")
            
        # PATTERN 2: Unbounded Streaming Rows until true End-of-File (e.g., CD Problem)
        # while True:
        #     element_str = next_string()
        #     if element_str is None:
        #         break
        #     element = int(element_str)
        #     d_print("Input:", element)
        #     write(f"{element}\n")
            
        # PATTERN 3: Explicit Test Case Variable Header Loop
        # t_str = next_string()
        # if t_str is not None:
        #     test_cases = int(t_str)
        #     for t in range(test_cases):
        #         # Execute individual trace logic...

        next_string = FastScanner.next_string
        next_int = FastScanner.next_int
        write = sys.stdout.write
        d_print = cls.d_print

        # Start solving problem from here
        # n_str = next_string()
        # if n_str is not None:
        #     n = int(n_str)
        #     d_print("Input:", n)
        #     write(f"{n}\n")


if __name__ == "__main__":
    template.init()
    template.solve()
    template.close()