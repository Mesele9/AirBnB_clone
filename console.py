#!/usr/bin/env python3
''' Contains console '''

import cmd
import shlex
import models
import datetime
from import_classes import *
import sys

#sys.path.append("/home/vagrant/AirBnB_clone/models")


class HBNBCommand(cmd.Cmd):
        ''' Console / command interpreter '''

        def do_quit(self, args):
                '''Quit command to exit the program '''
                return True

        def do_EOF(self, args):
                '''Quit command to exit the program '''
                return True

        def do_create(self, args):
                '''Creates a new instance '''
                try:
                        args = shlex.split(args)
                        if len(args) == 0:
                                raise SyntaxError
                        obj = eval('{}()'.format(args[0]))
                        print(obj.id)
                except SyntaxError:
                        print("** class name missing **")
                except NameError:
                        print("** class doesn't exist **")

        def do_show(self, args):
                '''Prints an instance '''
                try:
                        args = shlex.split(args)
                        if len(args) == 0:
                                raise SyntaxError
                        elif args[0] not in my_classes:
                                raise NameError

                        if len(args) == 1:
                                raise IndexError
                        obj_dict = models.storage.all()
                        key = args[0] + '.' + args[1]
                        if key in obj_dict.keys():
                                print(obj_dict[key])
                        else:
                                raise KeyError
                except SyntaxError:
                        print("** class name missing **")
                except NameError:
                        print("** class doesn't exist **")
                except IndexError:
                        print("** instance id missing **")
                except KeyError:
                        print("** no instance found **")

        def do_destroy(self, args):
                '''Destroy an instance '''
                try:
                        args = shlex.split(args)
                        if len(args) == 0:
                                raise SyntaxError

                        if args[0] not in my_classes:
                                raise NameError

                        if len(args) == 1:
                                raise IndexError

                        obj_dict = models.storage.all()
                        key = args[0] + '.' + args[1]
                        if key in obj_dict.keys():
                                models.storage.delete(key)
                        else:
                                raise KeyError
                except SyntaxError:
                        print("** class name missing **")
                except NameError:
                        print("** class doesn't exist **")
                except IndexError:
                        print("** instance id missing **")
                except KeyError:
                        print("** no instance found **")

        def do_all(self, args):
                '''Prints all instances of a class or all classes '''
                try:
                        args = shlex.split(args)
                        instance_list = []
                        for instance in args:
                                if instance not in my_classes:
                                        raise NameError

                        if len(args) > 0:
                                for instance in models.storage.all().values():
                                        if instance.__class__.__name__ in args:
                                                instance_list.append(instance)
                        else:
                                for instance in models.storage.all().values():
                                        instance_list.append(instance)

                        print(instance_list)
                except NameError:
                        print('** class doesn\'t exist **')

        def do_update(self, args):
                ''' Updates an instance '''
                try:
                        args = shlex.split(args)

                        if len(args) == 0:
                                raise SyntaxError

                        if args[0] not in my_classes:
                                raise NameError

                        if len(args) == 1:
                                raise IndexError

                        key = args[0] + '.' + args[1]
                        if key not in models.storage.all().keys():
                                raise KeyError

                        if len(args) == 2:
                                raise AttributeError

                        for i in range(2, len(args), 2):
                                if i + 1 >= len(args):
                                        raise ValueError
                                models.storage.update(key, args[i], args[i + 1])
                except SyntaxError:
                        print("** class name missing **")
                except NameError:
                        print("** class doesn't exist **")
                except IndexError:
                        print("** instance id missing **")
                except KeyError:
                        print("** no instance found **")
                except AttributeError:
                        print("** attribute name missing **")
                except ValueError:
                        print("** value missing **")

        def do_count(self, args):
                ''' Counts instances of a class '''
                try:
                        args = shlex.split(args)
                        num = 0
                        if args[0] not in my_classes:
                                raise NameError
                        for instance in models.storage.all().values():
                                if type(instance).__name__ == args[0]:
                                        num += 1
                        print(num)
                except NameError:
                        print('** class doesn\'t exist **')

        def emptyline(self):
                ''' Does not repeat prev command on empty line '''
                pass

        def precmd(self, line):
                ''' parses line if line has . syntax '''
                if line.endswith(')'):
                        line = list(line.partition('.'))
                        parameters = (line[2].partition)('(')[2]
                        parameters = parameters.rstrip(')')
                        line[2] = line[2].partition('(')[0]

                        split_params = shlex.split(parameters)

                        if (len(split_params) >= 2 and
                           split_params[1].startswith('{')):
                                parameters = parameters.partition('{')
                                obj_id = shlex.split(parameters[0])[0]
                                obj_id = obj_id[:-1]
                                parameters = parameters[1] + parameters[2]

                                parameters = eval(parameters)
                                if type(parameters) is not dict:
                                        print('** no sets **')
                                        return

                                new_str = ''
                                for (key, value) in parameters.items():
                                        pair = repr(key) + ' ' + repr(value)
                                        new_str = ' '.join([new_str, pair])
                                parameters = obj_id + ' ' + new_str
                        else:
                                for i in range(len(split_params) - 1):
                                        split_params[i] = split_params[i][:-1]

                                parameters = ' '.join(
                                             [repr(x) for x in split_params])

                        return ' '.join([line[2], line[0], parameters])

                return line


if __name__ == '__main__':
        hbnb_console = HBNBCommand()
        hbnb_console.prompt = '(hbnb) '
        hbnb_console.cmdloop()
