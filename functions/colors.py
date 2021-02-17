#!/usr/bin/env python
#
# colors.py : 
#             color related functions
#
# Copyright © Noé Perard-Gayot 2020.                                                                                        #
# Licensed under the MIT License. You may obtain a copy of the License at https://opensource.org/licenses/mit-license.php   #
#


#
#  colors for formating text
#
class color:
    HEADER  = '\033[1;35;68m'
    OKBLUE  = '\033[0;7;34m' 
    OKGREEN = '\033[0;39;32m'
    WARNING = '\033[0;93;14m'
    ERROR   = '\033[6;41;62m'
    LESS    = '\033[2;3;2m'
    ENDC    = '\033[0m'  


    @classmethod
    def print(cls, color, text, end = '\n'):
        '''
        adapt output to a color
        '''
        print( color + text + cls.ENDC, end = end)



def print_format_table(start_fg : int, start_bg: int):
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(start_fg,start_fg+8):
            s1 = ''
            for bg in range(start_bg,start_bg+8):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


# Run setup program
if __name__ == "__main__":
    from sys import argv
    args = argv[1:3]
    print_format_table(int(args[0]), int(args[1]))