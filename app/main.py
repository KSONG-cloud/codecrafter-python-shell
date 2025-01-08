import sys
import os

VALID_COMMANDS = ["echo", "exit", "pwd", "type"]


# gets a continuous string of files and splits them into individual files, 
# can handle whitespace in between quotes 
def file_splitter(files):
    NOTSTART = -1
    start = NOTSTART
    files_list = []
    for i in range(len(files)):
        # if we haven't started recording
        if start==NOTSTART and files[i]=="'":
            start = i
            continue
        
        # we have started recording and reached the end
        if start!=NOTSTART and files[i]=="'":
            end = i
            files_list.append(files[start: end+1 ])
            start=NOTSTART
            continue
        
    return files_list

# replace big whitespaces with one space 
def remove_big_whitespace(text):
    text_list = text.split()
    return " ".join(text_list)


def main():
    # Uncomment this block to pass the first stage


    PATH = os.environ.get("PATH")
    HOME = os.environ.get("HOME")

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
            if val.startswith("'") and val.endswith("'"):
                print(val[1:-1])
            else:
                # replace big whitespaces with one space if there is not single quotes
                print(remove_big_whitespace(val))

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


        # print current working directory
        elif command=="pwd":
            print(os.getcwd())


        # change directory
        elif command=="cd":
            # Default Home Case
            if val=="~":
                os.chdir(HOME)
            else:
                try:    
                    os.chdir(val)
                except FileNotFoundError:
                    print(f"cd: {val}: No such file or directory")

        # cat
        elif command=="cat":
            files = files_splitter(val)
            text_list = []
            for file in files:
                text = open(file, 'r').read()
                text_list.append(text)
                text.close()



        # Check for executables in PATH first

        # Execute commands: Use os.system() [os.system() method 
        # executes the command (a string) in a subshell. This method 
        # is implemented by calling the Standard C function system() 
        # and has the same limitations. If the command generates any 
        # output, it is sent to the interpreter’s standard output stream. 
        elif os.path.isfile(command):
            os.system(f"{command} {val}")
            continue
        else:
            command_found = False
            for path in paths:
                if os.path.isfile(f"{path}/{command}"):
                    os.system(f"{path}/{command} {val}")
                    command_found = True
                    continue
            # If we find the executable. continue, 
            # else say it's not found
            if command_found:
                continue
            else:
                sys.stdout.write(f"{command}: command not found\n")
            


    


if __name__ == "__main__":
    main()
