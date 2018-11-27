def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
                 'InterpreterInterface', 'StartServer', 'bob']
    username_input = str(input("Can i have your username: "))

    for i in range(len(usernames)):
        if username_input == usernames[i]:
            print("Acess granted")
            break
        if i == len(usernames)-1:
            print("Acess denied")


main()