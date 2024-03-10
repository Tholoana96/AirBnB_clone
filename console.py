#!/usr/bin/python3
"""Command interpreter module"""
import cmd
import sys
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
# Import other classes as needed

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        sys.exit(0)

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print()
        sys.exit(0)

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        cmd, arg, line = self.parseline(line)
        if cmd is None:
            return
        if cmd == "":
            self.emptyline()
            return
        if not self.onecmd_plus_hooks(line):
            print("*** Unknown syntax:", line)

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        elif args not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in storage.all().values() if obj.__class__.__name__ == args])

if __name__ == "__main__":
    HBNBCommand().cmdloop()
