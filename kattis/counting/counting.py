import sys

def main():
    input_data = sys.stdin.readline().split()
    
    if input_data:
        input = int(input_data[0])
        
        for i in range(1, 13):
            print(input * i)
        
if __name__ == "__main__":
    main()