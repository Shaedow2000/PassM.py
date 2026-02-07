import string, random

chars: list[ str ] = [ *string.ascii_letters, *string.digits, *string.punctuation ]

def gen_passwd( lenght: int ) -> str:
    passwd: str = ''
    index: int = random.randint( 0, len( chars ) - 1 )

    for i in range( lenght ):
        passwd += str( chars[ index ] )

        index = random.randint( 0, len( chars ) - 1 )

    return passwd
