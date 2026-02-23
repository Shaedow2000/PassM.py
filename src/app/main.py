#!/usr/bin/env python3

from methods import clear, quit

def main() -> None:
    clear()

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
