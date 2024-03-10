#!/usr/bin/python3

"""Entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
import models

classes = {'BaseModel': BaseModel, 'User': User}

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the commandline"""
        return True

    def do_EOF(self, arg):
        """Handles CTRL+D signal"""
        return True

    def emptyline(self):
        """An empty commandline + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new = classes[arg]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            instances = models.storage.all()
            print([str(instance) for instance in instances.values() if instance.__class__.__name__ == arg])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            print("** instance id missing **")

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            instances = models.storage.all()
            count = sum(1 for instance in instances.values() if instance.__class__.__name__ == arg)
            print(count)

    def do_BaseModel(self, arg):
        """Retrieves an instance based on its ID"""
        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
