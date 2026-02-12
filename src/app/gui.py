from tkinter import *
from tkinter import ttk 
import os, pyperclip

from methods import clear, is_int, new_account, read_json, write_json, write_passkey, first_time, check_passkey
from passwd_gen import gen_passwd

window: Tk = Tk()
passwd_gen_menu: Frame = Frame( window )
passwd_manager_menu: Frame = Frame( window )

login_menu: Frame = Frame( window )
access_menu: Frame = Frame( window )

add_account_menu: Frame = Frame( window )
modify_account_menu: Frame = Frame( window )

def hide_menus() -> None:
    passwd_gen_menu.pack_forget()
    passwd_manager_menu.pack_forget()
    
    login_menu.pack_forget()
    access_menu.pack_forget()

    add_account_menu.pack_forget()
    modify_account_menu.pack_forget()

    return

def first_time_login() -> None:
    error_label: Label = Label( login_menu, text='Passkey should contain 6 or more characters.', font=( 'Impact', 16, 'bold italic underline' ), fg='red' )
    warning_label: Label = Label( login_menu, text='This is the passkey that you will use to login every time to the password manager.\nNOTE: please keep this code with you, or you will be locked out of the password manager!' )
    passkey_entry: Entry = Entry( login_menu, width=30, font=( 'Impact', 14 ) )
    submit: Button = Button( login_menu, text='LogIn', font=( 'Impact', 14 ), command=lambda: ( 
        write_passkey( passkey_entry.get() ) if len( passkey_entry.get() ) >= 6 else error_label.pack( pady=5 ),
        ( hide_menus(), passwd_manager_menu.pack(), print( '-> Logged-in successfully !' ) ) if not first_time() else print( '-> Try again !' )
    ) )

    warning_label.pack()
    passkey_entry.pack( pady=10 )
    submit.pack()

    login_menu.pack()
    print( '-> You are not logged-in !' )

    return

def access() -> None:
    error_label: Label = Label( access_menu, text='Incorrect pass key.', font=( 'Imapct', 16, 'bold italic underline' ), fg='red' )
    entry_label: Label = Label( access_menu, text='Enter pass key:', font=( 'Impact', 14 ) )
    passkey_entry: Entry = Entry( access_menu, width=30, font=( 'Impact', 14 ) )
    submit: Button = Button( access_menu, text='Access', font=( 'Impact', 14 ), command=lambda: (
        ( hide_menus(), passwd_manager_menu.pack(), print( '-> Access granted !' ), passkey_entry.delete( 0, END ) ) if check_passkey( passkey_entry.get() ) else ( error_label.pack(), print( '-> Access denied: Incorrect pass key' ) )
    ) )

    entry_label.pack()
    passkey_entry.pack( pady=10 )
    submit.pack()

    access_menu.pack()

    return

def forget_all( frames: list[ Frame ] ) -> None:
    for i in range( len( frames ) ):
        frames[ i ].pack_forget()

    return

def accounts() -> None:
    frames: list[ Frame ] = []

    data: dict = read_json()

    for i in range( len( data[ 'data' ] ) ):
        frame: Frame = Frame( passwd_manager_menu, relief=RAISED, bd=3 )
        frame.pack( pady=5 )

        Label( frame, text=f'App: { data[ "data" ][ i ][ "app" ] }\nName: { data[ "data" ][ i ][ "name" ] }\nPassword: { data[ "data" ][ i ][ "passwd" ] }', font=( 'Impact', 14 ) ).pack()
        
        buttons_frame: Frame = Frame( frame )
        Button( buttons_frame, text='Remove', font=( 'Impact', 12, 'bold' ), command=lambda index = i: (
            data[ 'data' ].pop( index ),
            write_json( data ),
            forget_all( frames ),
            frames.clear(),
            accounts()
        ) ).pack( side='left' )

        Button( buttons_frame, text='Update', font=( 'Imapct', 12, 'bold' ), command=lambda: () ).pack( side='left' )
        buttons_frame.pack( pady=5 )

        frames.append( frame )

    return

def add_account() -> None:
    app_entry: Entry = Entry( add_account_menu, width=30, font=( 'Impact', 14 ) )
    name_entry: Entry = Entry( add_account_menu, width=30, font=( 'Impact', 14 ) )
    passwd_entry: Entry = Entry( add_account_menu, width=30, font=( 'Impact', 14 ) )

    Label( add_account_menu, text='App name:', font=( 'Impact', 12 ) ).pack()
    app_entry.pack()
    Label( add_account_menu, text='Your name:', font=( 'Impact', 12 ) ).pack()
    name_entry.pack()
    Label( add_account_menu, text='Password:', font=( 'Imapct', 12 ) ).pack()
    passwd_entry.pack()

    Button( add_account_menu, text='Add Account', font=( 'Impact', 14, 'bold' ), command=lambda: (
        new_account( app_entry.get(), name_entry.get(), passwd_entry.get() ),
        print( f'-> Added new { app_entry.get() } account.' )
    ) ).pack()

    add_account_menu.pack()

    return


def gui() -> None:
    window.geometry( '950x800' )
    window.title( 'PassM' )

    # window Icon
    icon_path: str = os.path.join( os.path.dirname( __file__ ), 'assets', 'padlock.png' )
    icon = PhotoImage( file=icon_path )

    window.iconphoto( True, icon )

    # logo
    logo_label: Label = Label( window, text='PassM', font=( 'Impact', 22, 'bold italic underline' ), fg='white', bg='darkblue', relief='flat', bd=20 )
    logo_label.pack( fill='x' )

    # buttons side
    buttons_side: Frame = Frame( window )
    buttons_side.pack( fill='y', side='left' )

    # buttons
    passwd_gen_button: Button = Button( buttons_side, text='Password Generation', font=( 'Impact', 16, 'bold' ), width=25, command=lambda: ( hide_menus(), passwd_gen_menu.pack() ) )
    passwd_gen_button.pack( pady=5 )

    passwd_manager_button: Button = Button( buttons_side, text='Password Manager', font=( 'Imapct', 16, 'bold' ), width=25, command=lambda: ( hide_menus(), first_time_login() if first_time() else access() ) )
    passwd_manager_button.pack( pady=5 )

    # Password Generation menu
    passwd: StringVar = StringVar( value='' )

    passwd_lenght_error: Label = Label( passwd_gen_menu, text='Lenght should be a number.', font=( 'Impact', 14, 'bold italic underline' ), fg='red' )

    lenght_label: Label = Label( passwd_gen_menu, text='Password Lenght [ default=16 ]:', font=( 'Imapct', 12 ) )
    passwd_lenght: Entry = Entry( passwd_gen_menu, width=30, font=( 'Impact', 14 ) )

    use_label: Label = Label( passwd_gen_menu, text='Use only these chars:', font=( 'Impact', 12 ) )

    use_chars: ttk.Combobox = ttk.Combobox( passwd_gen_menu, values=[ 'All chars', 'Letters only', 'Digits only', 'Punctuation only' ] )
    use_chars.set( 'Select chars' )

    passwd_label: Label = Label( passwd_gen_menu, textvariable=passwd, font=( 'Impact', 20, 'bold' ) )
    copy: Button = Button( passwd_gen_menu, text='Copy', font=( 'Impact', 14 ), command=lambda: ( pyperclip.copy( passwd.get() ) ) )

    generate: Button = Button( passwd_gen_menu, text='Generate password', font=( 'Impact', 14 ), command=lambda: ( passwd.set( value=gen_passwd( int( passwd_lenght.get().replace( ' ', '' ) ) if passwd_lenght.get().replace( ' ', '' ) != '' else 16, use_chars.get() ) ) if is_int( passwd_lenght.get().replace( ' ', '' ) ) or passwd_lenght.get().replace( ' ', '' ) == '' else passwd_lenght_error.pack() ) )

    lenght_label.pack()
    passwd_lenght.pack( pady=10 )
    use_label.pack()
    use_chars.pack( pady=10 )
    generate.pack( pady=15 )

    passwd_label.pack( pady=25 )
    copy.pack()

    # Password manager menu
    top_frame: Frame = Frame( passwd_manager_menu )

    Button( top_frame, text='Quit', font=( 'Impact', 12, 'bold' ), command=lambda: ( hide_menus(), access_menu.pack() ) ).pack( side='left', padx=5 )
    Label( top_frame, text='Password Manager:', font=( 'Imapct', 16, 'bold underline' ) ).pack( side='left', padx=5 )
    Button( top_frame, text='Add', font=( 'Impact', 12, 'bold' ), command=lambda: ( hide_menus(), add_account() ) ).pack( side='left', padx=5 )

    top_frame.pack( pady=10 )

    data: dict = read_json()

    if len( data[ 'data' ] ) == 0:
        Label( passwd_manager_menu, text='No Data Found D:', font=( 'Impact', 15, 'bold italic' ) ).pack()
    else:
        accounts()
    
    # Start gui
    print( '=> Opened GUI...' )

    window.mainloop()
