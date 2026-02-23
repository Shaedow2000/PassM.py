import string, random

def gen_passwd( lenght: int, use_only: str ) -> str:
    chars: list[ str ] = []

    if use_only == 'Letters only':
        chars = [ *string.ascii_letters ]
    elif use_only == 'Digits only':
        chars = [ *string.digits ]
    elif use_only == 'Punctuation only':
        chars = [ *string.punctuation ]
    else:
        chars = [ *string.ascii_letters, *string.digits, *string.punctuation ]

    passwd: str = ''
    index: int = random.randint( 0, len( chars ) - 1 )

    for i in range( lenght ):
        passwd += str( chars[ index ] )

        index = random.randint( 0, len( chars ) - 1 )

    return passwd
