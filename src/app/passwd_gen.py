import string, random

chars: list[ str ] = [ *string.ascii_letters, *string.digits, *string.punctuation ]

def gen_passwd( lenght: int, use_only: str ) -> str:
    global chars

    if use_only == 'letters':
        chars = [ *string.ascii_letters ]
    elif use_only == 'digits':
        chars = [ *string.digits ]
    elif use_only == 'punctuation':
        chars = [ *string.punctuation ]
    else:
        chars = chars

    passwd: str = ''
    index: int = random.randint( 0, len( chars ) - 1 )

    for i in range( lenght ):
        passwd += str( chars[ index ] )

        index = random.randint( 0, len( chars ) - 1 )

    return passwd
