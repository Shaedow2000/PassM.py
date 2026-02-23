#!/usr/bin/env python3

import pyperclip

from methods import clear, quit, is_int
from passwd_gen import gen_passwd

def main() -> None:
    clear()

    while True:
        command: str = input( '>=> ' ).replace( ' ', '' ).lower()

        if command == 'g':
            lenght: str = input( '--> Enter lenght of the password [ Enter => 16 ]: ' ).replace( ' ', '' )
            print( '- password contains: [ press any key ]> All chars | 1> letters only | 2> digits only | 3> punctuation only.' )
            use_only: str = input( '--> ' ).replace( ' ', '' )

            if is_int( lenght ) or lenght == '':
                passwd: str = gen_passwd( int( lenght ) if lenght != '' else 16, use_only )
                print( f'!> [  { passwd }  ]' )
                pyperclip.copy( passwd )
                print( '|=> Password copied to clipboard !' )
            else:
                print( f'!> Value { lenght } is not a number.' )
        elif command == 'c':
            clear()
        elif command == 'q':
            quit()
        elif command == '':
            pass
        else:
            print( f'!> Command not found: [ { command } ].' )

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()
