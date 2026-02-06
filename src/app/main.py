#!/usr/bin/env python3

def main() -> None:
    menu: str = '\tg: generate passwd | c: clear screen | q: quit or [ Ctrl + C ]'

    print( menu )
    while True:
        command: str = input( '>=> ' ).replace( ' ', '' ).lower()

if __name__ == '__main__':
    main()
