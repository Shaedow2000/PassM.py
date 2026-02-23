#!/usr/bin/env python3

import os, sys

menu: str = '\tg: generate passwd | c: clear screen | q: quit or [ Ctrl + C ]'

def clear() -> None:
    os.system( 'cls' if os.name == 'nt' else 'clear' )

    print( menu )

    return

def quit() -> None:
    sys.exit( '\n!> Quiting program...' )

def main() -> None:
    print( menu )

    while True:
        command: str = input( '>=> ' ).replace( ' ', '' ).lower()

        if command == 'g':
            pass
        elif command == 'c':
            clear()
        elif command == 'q':
            quit()
        else:
            print( f'!> Command not found: [ { command } ].' )

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        quit()
