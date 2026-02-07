from tkinter import *
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

    print( '=> Opened GUI...' )

    window.mainloop()
