#!/usr/bin/python3
import inspect
import io
import sys
import cmd
import shutil

"""
 Cleanup file storage
"""
import os
file_path = "file.json"
if not os.path.exists(file_path):
    try:
        from models.engine.file_storage import FileStorage
        file_path = FileStorage._FileStorage__file_path
    except:
        pass
if os.path.exists(file_path):
    os.remove(file_path)

"""
 Backup console file
"""
if os.path.exists("tmp_console_main.py"):
    shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("_console.py", "tmp_console_main.py")

"""
 Backup models/__init__.py file
"""
if os.path.exists("models/tmp__init__.py"):
    shutil.copy("models/tmp__init__.py", "models/__init__.py")
shutil.copy("models/__init__.py", "models/tmp__init__.py")

"""
 Overwrite models/__init__.py file with switch_to_file_storage.py
"""
if os.path.exists("switch_to_file_storage.py"):
    shutil.copy("switch_to_file_storage.py", "models/__init__.py")


"""
 Updating console to remove "__main__"
"""
with open("tmp_console_main.py", "r") as file_i:
    console_lines = file_i.readlines()
    with open("console.py", "w") as file_o:
        in_main = False
        for line in console_lines:
            if "__main__" in line:
                in_main = True
            elif in_main:
                if "cmdloop" not in line:
                    file_o.write(line.lstrip("    ")) 
            else:
                file_o.write(line)

import _console

"""
 Create console
"""
console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(_console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(stdout=io.StringIO(), stdin=io.StringIO())
my_console.use_rawinput = False

"""
 Exec command
"""
def exec_command(my_console, the_command, last_lines = 1):
    my_console.stdout = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = my_console.stdout
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1*(last_lines+1)):-1])

"""
 Tests
"""
state_name = "California"
result = exec_command(my_console, "create State name=\"{}\"".format(state_name))
if result is None or result == "":
    print("FAIL: No ID retrieved")
with open(file_path, "r") as file:
    s_file = file.read()
    if result not in s_file:
        print("FAIL: New ID not in the JSON file")
print("OK", end="")

shutil.copy("tmp_console_main.py", "_console.py")
shutil.copy("models/tmp__init__.py", "models/__init__.py")
