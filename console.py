#!/usr/bin/python3
"""
Command interpreter module
"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """

    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it to the JSON file, and prints the id
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        objs = []

        if len(args) == 0:
            objs = list(storage.all().values())
        elif args[0] in storage.classes:
            objs = [v for k, v in storage.all().items()
                    if k.split('.')[0] == args[0]]
        else:
            print("** class doesn't exist **")
            return

        print([str(obj) for obj in objs])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')

        # Update the attribute value
        setattr(obj, attr_name, attr_value)
        obj.save()

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        sys.exit(0)

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        sys.exit(0)

    def emptyline(self):
        """
        Called when an empty line is entered in the prompt
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
