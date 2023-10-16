#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = '(hbnb) '
    classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def default(self, line):
        args = re.match(r'(\w+)\.(\w+)\((.*?)\)', line)
        if args:
            class_name = args.group(1)
            method_name = args.group(2)
            arguments = args.group(3)
            full_command = f"{class_name} {arguments}"

            if method_name == "all":
                self.do_all(full_command)
            elif method_name == "count":
                self.do_count(class_name)
            elif method_name == "show":
                self.do_show(full_command)
            elif method_name == "destroy":
                self.do_destroy(full_command)
            elif method_name == "update":
                self.do_update(full_command)
        else:
            super().default(line)

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on
        the class name and id.
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and
        id (saves the change into the JSON file).
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, args):
        """
        Prints string representations of all instances based or
        not on the class name.
        """
        args = args.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                if len(args) > 0 and args[0] == key.split(".")[0]:
                    print(value)
                elif len(args) == 0:
                    print(value)

    def do_update(self, args):
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                if args[2][0] == '{' and args[-1][-1] == '}':
                    try:
                        dictionary = eval(args[2])
                        if isinstance(dictionary, dict):
                            for k, v in dictionary.items():
                                setattr(storage.all()[key], k, v)
                            storage.all()[key].save()
                    except (SyntaxError, NameError):
                        print("** invalid format **")
                else:
                    setattr(storage.all()[key], args[2], args[3].strip("\""))
                    storage.all()[key].save()

    def do_count(self, arg):
        """
        Counts the number of instances of a class.
        """
        count = 0
        for key in storage.all():
            if arg in key:
                count += 1
        print(count)

    def do_quit(self, args):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
