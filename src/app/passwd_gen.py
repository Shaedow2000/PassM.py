import string, random

def gen_passwd( lenght: int, use_only: str ) -> str:
    chars: list[ str ] = []

    if use_only == '1':
        chars = [ *string.ascii_letters ]
    elif use_only == '2':
        chars = [ *string.digits ]
    elif use_only == '3':
        chars = [ *string.punctuation ]
    else:
        chars = [ *string.ascii_letters, *string.digits, *string.punctuation ]

    passwd: str = ''
    index: int = random.randint( 0, len( chars ) - 1 )

    for i in range( lenght ):
        passwd += str( chars[ index ] )

        index = random.randint( 0, len( chars ) - 1 )

    return passwd
