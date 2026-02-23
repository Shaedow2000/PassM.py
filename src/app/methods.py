import os, sys

menu: str = '\tg: generate passwd | c: clear screen | q: quit or [ Ctrl + C ]'

def clear() -> None:
    os.system( 'cls' if os.name == 'nt' else 'clear' )

    print( menu )

    return

def quit() -> None:
    sys.exit( '\n!> Quiting program...' )

def is_int( n: str ) -> bool:
    try:
        int( n )

        return True
    except ValueError:
        return False
