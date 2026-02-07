from tkinter import *
from tkinter import ttk 
import os

from methods import is_int
from passwd_gen import gen_passwd

window: Tk = Tk()
passwd_gen_menu: Frame = Frame( window )
passwd_manager_menu: Frame = Frame( window )

test = Entry( passwd_manager_menu )
test.pack()

def hide_menus() -> None:
    passwd_gen_menu.pack_forget()
    passwd_manager_menu.pack_forget()

    return

def gui() -> None:
    window.geometry( '950x800' )
    window.title( 'PassM' )

    # window Icon
    icon_path: str = os.path.join( os.path.dirname( __file__ ), 'assets', 'padlock.png' )
    icon = PhotoImage( file=icon_path )

    window.iconphoto( True, icon )

    # buttons side
    buttons_side: Frame = Frame( window )
    buttons_side.pack( fill='y', side='left' )

    # buttons
    passwd_gen_button: Button = Button( buttons_side, text='Password Generation', font=( 'Impact', 16, 'bold' ), width=25, command=lambda: ( hide_menus(), passwd_gen_menu.pack() ) )
    passwd_gen_button.pack()

    passwd_manager_button: Button = Button( buttons_side, text='Password Manager', font=( 'Imapct', 16, 'bold' ), width=25, command=lambda: ( hide_menus(), passwd_manager_menu.pack() ) )
    passwd_manager_button.pack()

    # Password Generation menu
    passwd: StringVar = StringVar( value='' )

    passwd_lenght_error: Label = Label( passwd_gen_menu, text='Lenght should be a number.', font=( 'Impact', 14, 'bold italic underline' ), fg='red' )

    lenght_label: Label = Label( passwd_gen_menu, text='Password Lenght [ default=16 ]:', font=( 'Imapct', 12 ) )
    passwd_lenght: Entry = Entry( passwd_gen_menu, width=30, font=( 'Impact', 14 ) )

    use_label: Label = Label( passwd_gen_menu, text='Use only these chars:', font=( 'Impact', 12 ) )

    use_chars: ttk.Combobox = ttk.Combobox( passwd_gen_menu, values=[ 'All chars', 'Letters only', 'Digits only', 'Punctuation only' ] )
    use_chars.set( 'Select chars' )

    passwd_label: Label = Label( passwd_gen_menu, textvariable=passwd, font=( 'Impact', 20, 'bold' ) )

    generate: Button = Button( passwd_gen_menu, text='Generate password', font=( 'Impact', 14 ), command=lambda: ( passwd.set( value=gen_passwd( int( passwd_lenght.get().replace( ' ', '' ) ) if passwd_lenght.get().replace( ' ', '' ) != '' else 16, use_chars.get() ) ) if is_int( passwd_lenght.get().replace( ' ', '' ) ) or passwd_lenght.get().replace( ' ', '' ) == '' else passwd_lenght_error.pack() ) )
    
    lenght_label.pack()
    passwd_lenght.pack( pady=10 )
    use_label.pack()
    use_chars.pack( pady=10 )
    generate.pack( pady=15 )

    passwd_label.pack( pady=25 )

    # Start gui
    print( '=> Opened GUI...' )

    window.mainloop()
