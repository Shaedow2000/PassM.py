#!/usr/bin/env python3

from methods import clear, quit, is_int
from passwd_gen import gen_passwd

def main() -> None:
    clear()

    while True:
        command: str = input( '>=> ' ).replace( ' ', '' ).lower()

        if command == 'g':
            lenght: str = input( '--> Enter lenght of the password: ' )
            print( '- password contains: [ press any key ]> All chars | 1> letters only | 2> digits only | 3> punctuation only.' )
            use_only: str = input( '--> ' )

            if is_int( lenght ):
                print( gen_passwd( int( lenght ), use_only ) )
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
