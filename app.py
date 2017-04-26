#!/usr/bin/env python
"""
Usage:
    Dojo add_room <room_type> <rooms>...
    Dojo add_person <first_name> <last_name> [staff|fellow] [Y|N]
    Dojo (-i | --interactive)
    Dojo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit

import dojo

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = '*****Random Room Allocation*****' \
        + ' (Enter help for a list of commands.)'
    prompt = 'DOJO>>> '
    file = None

    @docopt_cmd
    def do_add_room(self, arg):
        """Usage: add_room [<room_type>] <room_names>... """
	room_type = arg['<room_type>']
	room_name = arg['<room_names>']
	#dojo.create_room(room_type,room_name)
        print(arg)

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> [staff|fellow] [Y|N]"""
	person_fname = arg['<first_name>']
	person_lname = arg['<last_name>']
	person_position = arg['<staff|fellow>']
	living_space = arg['<Y|N>']
	#dojo.add_person(person_fname,person_lname,person_position,living_space)
        print(arg)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)


