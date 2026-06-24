import sys
import time


class cd:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def generateOutput(self):
        # 1. This line blocks and waits for input stream closure (Human Time)
        tokens = sys.stdin.read().split()
        if not tokens:
            return

        # 2. Start the timer (Pure Algorithm Execution Time)
        start_runtime = time.perf_counter()

        iterator = iter(tokens)

        while True:
            try:
                n_str = next(iterator)
                m_str = next(iterator)
            except StopIteration:
                break

            N = int(n_str)
            M = int(m_str)

            if N == 0 and M == 0:
                break

            jack_cds = {int(next(iterator)) for _ in range(N)}
            jill_cds = {int(next(iterator)) for _ in range(M)}

            print(len(jack_cds & jill_cds))

        # 3. Stop the timer
        end_runtime = time.perf_counter()
        total_runtime = end_runtime - start_runtime

        self.dprint(
            f"[Algorithmic Runtime] {total_runtime:.6f} seconds", file=sys.stderr
        )


if __name__ == "__main__":
    cd(False).generateOutput()
