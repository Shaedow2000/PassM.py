import os, sys, json

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

def read_json() -> str:
    dir: str = os.path.dirname( __file__ )
    file_name: str = 'data.json'

    file_path: str = os.path.join( dir, 'assets', file_name )

    if not os.path.exists( file_path ):
        with open( file_path, 'w' ) as file:
            json.dump( { "key": "", "decKey": "", "data": "" }, file )

    data: str = ''

    with open( file_path, 'r' ) as file:
        data = json.load( file )

    return data
