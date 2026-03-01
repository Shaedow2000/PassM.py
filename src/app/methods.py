import os, sys, json, bcrypt, random, string, base64, hashlib
from cryptography.fernet import Fernet
from tkinter import END, Entry

menu: str = '\tg: generate passwd | c: clear screen | q: quit or [ Ctrl + C ]'

# def clear() -> None:
#     os.system( 'cls' if os.name == 'nt' else 'clear' )
#
#     print( menu )
#
#     return
#
# def quit() -> None:
#     sys.exit( '\n!> Quiting program...' )

class DecString:
    def __init__( self, str_key: str ) -> None:
        self.str_key = str_key 

    def encrypt( self ) -> None:
        decString: str = ''.join( random.choices( string.ascii_letters + string.digits + string.punctuation, k=22 ) )

        key = base64.urlsafe_b64encode( hashlib.sha256( self.str_key.encode() ).digest() )

        fernet: Fernet = Fernet( key )
        encDecString: bytes = fernet.encrypt( decString.encode() )

        data: dict = read_json()
        data[ 'decKey' ] = encDecString.decode()

        write_json( data )

        return

    def decrypt( self ) -> str:
        data: dict = read_json()

        key = base64.urlsafe_b64encode( hashlib.sha256( self.str_key.encode() ).digest() )

        fernet: Fernet = Fernet( key )

        encDecString: bytes = data[ 'decKey' ].encode()

        DecString: bytes = fernet.decrypt( encDecString )

        return DecString.decode() 

class DecData:
    def __init__( self, key: bytes ) -> None:
        self.fernet: Fernet = Fernet( key )

    def encrypt( data: list | dict | str ) -> None:
        return

    def decrypt( data: str ) -> None:
        return

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
            json.dump( { 'first-time': True, 'key': '', 'decKey': '', 'data': [] }, file )

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

    hashed_key: bytes = bcrypt.hashpw( key.encode(), bcrypt.gensalt() )

    data[ 'key' ] = hashed_key.decode()
    data[ 'first-time' ] = False

    write_json( data )
    
    return

def first_time() -> bool:
    data: dict = read_json()

    if data[ 'first-time' ]:
        return True
    else:
        return False

def check_passkey( key: str ) -> bool:
    data: dict = read_json()
    stored_key: bytes = data[ 'key' ].encode()

    return bcrypt.checkpw( key.encode(), stored_key )

def duplicate_account( new_acc: dict, data: dict ) -> bool:
    for i in range( len( data ) ):
        account: dict = data[ i ]
    
        if new_acc[ 'app' ].lower() == account[ 'app' ].lower() and new_acc[ 'name' ] == account[ 'name' ]:
            print( '-> Duplicate account: This account alread exists in your data base.' )
            return True

    return False

def new_account( app: str, name: str, passwd: str ) -> None:
    data: dict = read_json()

    new_acc: dict = {
        'app': app.capitalize(),
        'name': name,
        'passwd': passwd
    }

    if not duplicate_account( new_acc, data[ 'data' ] ):
        data[ 'data' ].append( new_acc )
        write_json( data )

        print( f'-> Added new { new_acc[ "app" ] } account.' )

    return

def empty_entries( *entries: Entry ) -> None:
    for i in range( len( entries ) ):
        entries[ i ].delete( 0, END )

    return

def is_entry_empty( *entry: Entry ) -> bool:
    for i in range( len( entry ) ):
        if entry[ i ].get().replace( ' ', '' ) == '':
            return True

    return False
