from tkinter import *
from tkinter import ttk 
import os

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
    lenght_label: Label = Label( passwd_gen_menu, text='Password Lenght:', font=( 'Imapct', 12 ) )
    passwd_lenght: Entry = Entry( passwd_gen_menu, width=30, font=( 'Impact', 14 ) )

    use_label: Label = Label( passwd_gen_menu, text='Use only these chars:', font=( 'Impact', 12 ) )

    use_chars: ttk.Combobox = ttk.Combobox( passwd_gen_menu, values=[ 'All chars', 'Letters only', 'Digits only', 'Punctuation only' ] )
    use_chars.set( 'Select chars' )
    
    lenght_label.pack()
    passwd_lenght.pack()
    use_label.pack()
    use_chars.pack()

    # Start gui
    print( '=> Opened GUI...' )

    window.mainloop()
