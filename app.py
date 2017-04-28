#!/usr/bin/env python
"""
Usage:
    Dojo create_room <room_type> <rooms>...
    Dojo add_person <first_name> <last_name> <staff-fellow> <Y-N>
    Dojo (-i | --interactive)
    Dojo (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from termcolor import cprint
from pyfiglet import figlet_format
from dojo import Dojo
import os
dojo = Dojo()


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
    os.system('clear')
    cprint(figlet_format('Dojo\n', font='xsansi'), 'blue', attrs=['bold'])
    intro = ('Welcome To The Dojo \n\nType "help" To View More Commands or "quit" To Exit Applicaton \n\n------------------'
             '\n\nCOMMANDS \n\n------------------ \n\n1 - add_person <person_name> (FELLOW|STAFF) [wants_accommodation] \n2 - create_room <room_type> <room_name>...')

    intro = '   *****Random Room Allocation*****' \
        + '\n   ----------------------------------' \
        + ' \n  Enter help for a list of commands.'
    prompt = 'DOJO>>> '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room [<room_type>] <room_names>... """
        room_type = arg['<room_type>']
        room_names = arg['<room_names>']
        dojo.create_room(room_type, room_names)
        for room in room_names:
            print(room_type + " room " + str(room) + " successfully created!\n")

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> <staff-fellow> [<Y-N>]"""
        first_name = arg['<first_name>']
        last_name = arg['<last_name>']
        name = arg['<first_name>'] + ' ' + arg['<last_name>']
        position = arg['<staff-fellow>']
        accomodation = arg['<Y-N>']
        dojo.add_person(name, position, accomodation)
        print(name + " successfully added")

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
