import sys
import os

VALID_COMMANDS = ["echo", "exit", "type"]

def main():
    # Uncomment this block to pass the first stage


    PATH = os.environ.get("PATH")

    # print(PATH)

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush

        # Initialisation
        command, val= ("","")

        # Wait for user input
        command_input = input()

        # separating the paths from PATH
        paths = PATH.split(":")

        # print(command_input)
        # If there is a command, break it up into command and value
        # Here instead of splitting, we can instead use .startswith()
        # E.g. if command_input.startswith("echo"):
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
            
            command_path = None
            
            for path in paths:
                if os.path.isfile(f"{path}/{val}"):
                    command_path = f"{path}/{val}"

            if val in VALID_COMMANDS:
                print(f"{val} is a shell builtin")
            elif command_path:
                print(f"{val} is {command_path}")
            else:
                print(f"{val}: not found")

        # Check for executables in PATH first

        # Execute commands: Use os.system() [os.system() method 
        # executes the command (a string) in a subshell. This method 
        # is implemented by calling the Standard C function system() 
        # and has the same limitations. If the command generates any 
        # output, it is sent to the interpreter’s standard output stream. 
        elif os.path.isfile(command):
            os.system(command)
        else:
            for path in paths:
                if os.path.isfile(f"{path}/{command}"):
                    os.system(f"{path}/{command} {val}")
                    continue
                      
            sys.stdout.write(f"{command}: command not found\n")
            continue


    


if __name__ == "__main__":
    main()
