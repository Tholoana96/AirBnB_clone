#!/usr/bin/python3

"""Entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


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
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        self._handle_instance_command('show', arg)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        self._handle_instance_command('destroy', arg)

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        self._handle_all_command(arg)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        self._handle_instance_command('update', arg)

    def do_count(self, arg):
        """Retrieves the number of instances of a class"""
        self._handle_count_command(arg)

    def _handle_instance_command(self, command, arg):
        """Handles show, destroy, and update commands for instances"""
        args = arg.split()
        if not args:
            print(f"** class name missing **")
        elif args[0] != "BaseModel":
            print(f"** class doesn't exist **")
        elif len(args) < 2 and command != 'all':
            print(f"** instance id missing **")
        elif len(args) < 3 and command == 'update':
            print(f"** attribute name missing **")
        elif len(args) < 4 and command == 'update':
            print(f"** value missing **")
        else:
            if command == 'all':
                self._handle_all_command(arg)
            elif command == 'show':
                self._show_instance(args[0], args[1])
            elif command == 'destroy':
                self._destroy_instance(args[0], args[1])
            elif command == 'update':
                self._update_instance(args[0], args[1], args[2], args[3])

    def _handle_all_command(self, arg):
        """Handles the 'all' command"""
        args = arg.split()
        if not args:
            new_list = [str(obj) for obj in storage.all().values()]
            print(new_list)
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_list = [str(obj) for obj in storage.all().values() if isinstance(obj, BaseModel)]
            print(new_list)

    def _show_instance(self, class_name, instance_id):
        """Handles the 'show' command for instances"""
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def _destroy_instance(self, class_name, instance_id):
        """Handles the 'destroy' command for instances"""
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def _update_instance(self, class_name, instance_id, attribute, value):
        """Handles the 'update' command for instances"""
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
        else:
            cast = None
            if not value.startswith('"'):
                if '.' in value:
                    cast = float
                else:
                    cast = int
            else:
                value = value.replace('"', '')
            attributes = storage.attributes()[class_name]
            if attribute in attributes:
                value = attributes[attribute](value)
            elif cast:
                try:
                    value = cast(value)
                except ValueError:
                    pass
            setattr(storage.all()[key], attribute, value)
            storage.all()[key].save()

    def _handle_count_command(self, arg):
        """Handles the 'count' command"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            matches = [k for k in storage.all() if k.startswith(args[0] + '.')]
            print(len(matches))


if __name__ == '__main__':
    HBNBCommand().cmdloop()

