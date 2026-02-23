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

# data file path
dir: str = os.path.dirname( __file__ )
file_name: str = 'data.json'
file_path: str = os.path.join( dir, 'assets', file_name )

def read_json() -> dict:
    if not os.path.exists( file_path ):
        with open( file_path, 'w' ) as file:
            json.dump( { 'first-time': True, 'key': '', 'decKey': '', 'data': '' }, file )

    data: dict = {}

    with open( file_path, 'r' ) as file:
        data = json.load( file )

    return data

def write_json( data: dict ) -> None:
    with open( file_path, 'w' ) as file:
        json.dump( data, file )

    return

def write_passkey( key: str ) -> None:
    data: dict = read_json()

    data[ 'key' ] = key
    data[ 'first-time' ] = False

    write_json( data )
    
    return

def first_time() -> bool:
    data: dict = read_json()

    if data[ 'first-time' ]:
        return True
    else:
        return False
