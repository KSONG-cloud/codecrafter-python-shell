import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush
        # Wait for user input
        command=input()
        if command=="exit 0":
            return
        
        if command[:4]=="echo":
            print(command[5:])
        else:
            sys.stdout.write(f"{command}: command not found\n")


    


if __name__ == "__main__":
    main()
