import sys

VALID_COMMANDS = ["echo", "exit", "type"]

def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush

        # Initialisation
        command, val= ("","")

        # Wait for user input
        command_input = input()

        # If there is a command, break it up into command and value
        if " " in command_input:
            command, val= command_input.split(" ", 1)
        else:
            command = command_input

        # Exit command
        if command=="exit" and val=="0":
            return
        
        
        # echo command: print input
        if command=="echo":
            print(val)

        # type command: check type of input
        elif command=="type":
            if val in VALID_COMMANDS:
                print(f"{val} is a shell builtin")
            else:
                print(f"{val}: not found")
        else:
            sys.stdout.write(f"{command}: command not found\n")


    


if __name__ == "__main__":
    main()
