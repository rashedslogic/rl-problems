import sys
import time


class cd:

    def __init__(self, debug: bool = False):
        self.debug = debug

    def dprint(self, *args, **kwargs):
        if self.debug:
            print(*args, **kwargs)

    def generateOutput(self):
        # This line blocks and waits for input stream closure (Human Time)
        tokens = sys.stdin.read().split()
        if not tokens:
            return

        # Start the timer (Pure Algorithm Execution Time)
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

            # jack_cds = {int(next(iterator)) for _ in range(N)}
            # jill_cds = {int(next(iterator)) for _ in range(M)}
            # print(len(jack_cds & jill_cds))

            # Store Jack's CD into a raw primitive array
            jack_cds = [int(next(iterator)) for _ in range(N)]
            self.dprint(f"Jacks CD: {jack_cds}");

            # Perform Two-pointer intersection sweep comparing Jill's CDs
            intersection_count = 0
            jack_idx = 0
            
            for _ in range(M):
                jill_cd = int(next(iterator))

                while jack_idx < N and jack_cds[jack_idx] < jill_cd:
                    jack_idx += 1

                if jack_idx < N and jack_cds[jack_idx] == jill_cd:
                    intersection_count += 1
                    jack_idx += 1

            # Print the final output of common items
            print(intersection_count)

        # Stop the timer
        end_runtime = time.perf_counter()
        total_runtime = end_runtime - start_runtime

        self.dprint(
            f"[Algorithmic Runtime] {total_runtime:.6f} seconds"
        )


if __name__ == "__main__":
    cd(False).generateOutput()
