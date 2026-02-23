#!/usr/bin/env python3

from methods import clear, quit
from passwd_gen import gen_passwd

def main() -> None:
    clear()

    while True:
        command: str = input( '>=> ' ).replace( ' ', '' ).lower()

        if command == 'g':
            print( gen_passwd() ) 
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
