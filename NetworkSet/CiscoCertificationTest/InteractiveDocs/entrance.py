import importlib

command_module_list = [
    "command_line.expand",
    "command_line.show",
    "command_line.basic"
]

if __name__ == "__main__":
    while True:
        command = raw_input(">>>")
        if command == "stop":
            break
        break_flag = False
        for this_module in command_module_list:
            cli = importlib.import_module(this_module)
            this_cmd = cli.my_cmd
            for cmd_key in this_cmd:
                if cmd_key == command:
                    print "Description: " + this_cmd[cmd_key]
                    break_flag = True
                    break
            if break_flag:
                print "Module stops importing"
                break
        if not break_flag:
            print "Command line not found"
