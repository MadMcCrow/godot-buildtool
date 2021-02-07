#!/usr/bin/env python
#
# main.py :
#               Setup this project according to platform
#				this replaces the improper makefile that used to call scons
#
# Copyright © Noé Perard-Gayot 2020.                                                                                        #
# Licensed under the MIT License. You may obtain a copy of the License at https://opensource.org/licenses/mit-license.php   #
#

#
#	remove unnecesary files
#
def clean():
    pass

#
#	print help info
#	TODO : automate this
#
def _help():
    pass


#
#	will create a shortcut to the editor
#
def shortcut():
    try:
        from os import getcwd
        from functions import platform
        if platform.isLinux():
            from functions.shortcuts import generateDesktopFile
            generateDesktopFile(getcwd() + "/" + _projectName() + ".desktop")
        else:
            raise NotImplementedError
    except:
        raise

#
#	handle command line argument
#
def arg_condition(arg: str, arg_list: list) -> bool:
    return arg in arg_list


#
#	Main setup function
#
def main():
    import sys
    for arg in sys.argv:
        if arg_condition(arg, ["--help", "-h", "h", "help"]):
            _help()
            return

        if arg_condition(arg, ["--build", "-b", "-b", "build"]):
            from functions.build import build
            build()

        if arg_condition(arg, ["--shortcut", "-s", "s", "shortcut"]):
            shortcut()


# Run setup program
if __name__ == "__main__":
    main()
