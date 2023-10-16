#!/usr/bin/python3

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand is a command interpreter for the AirBnB clone project.
    It inherits from the cmd.Cmd class of the cmd module in Python.
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

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
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
        id (save the change into the JSON file).
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
        Prints all string representation of all instances based or
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
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
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
                setattr(storage.all()[key], args[2], args[3].strip("\""))
                storage.all()[key].save()

    def default(self, line):
        args = line.split(".")
        if len(args) > 1:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.do_count(args[0])
            elif re.match(r"show\(\"(.*)\"\)", args[1]):
                id = re.match(r"show\(\"(.*)\"\)", args[1]).group(1)
                self.do_show(args[0] + " " + id)
            elif re.match(r"destroy\(\"(.*)\"\)", args[1]):
                id = re.match(r"destroy\(\"(.*)\"\)", args[1]).group(1)
                self.do_destroy(args[0] + " " + id)
            elif re.match(r"update\(\"(.*)\", (.*)\)", args[1]):
                match = re.match(r"update\(\"(.*)\", (.*)\)", args[1])
                id = match.group(1)
                dictionary = match.group(2)
                self.do_update(args[0] + " " + id + " " + dictionary)

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        count = 0
        for key in storage.all():
            if arg in key:
                count += 1
        print(count)

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
