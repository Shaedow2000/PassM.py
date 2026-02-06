import string, random

chars: list[ str ] = [ *string.ascii_letters, *string.digits, *string.punctuation ]

def gen_passwd() -> str:
    passwd: str = ''
    index: int = random.randint( 0, len( chars ) - 1 )

    for i in range( 12 ):
        passwd += str( chars[ index ] )

        index = random.randint( 0, len( chars ) )

    return passwd
