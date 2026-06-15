import sys

def main():
    line = sys.stdin.readline()
    token = line.split()

    if len(token) >= 2:
        h = float(token[0])
        b = float(token[1])

        h = max(1, min(h, 1000))
        b = max(1, min(b, 1000))
        area = 0.5 * h * b

        print(f"{area:.9f}")

if __name__ == "__main__":
    main()