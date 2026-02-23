from tkinter import *
import os

window: Tk = Tk()
home_menu: Frame = Frame( window )
passwd_gen_menu: Frame = Frame( window )
passwd_manager_menu: Frame = Frame( window )

def gui() -> None:
    window.geometry( '950x800' )
    window.title( 'PassM' )

    icon_path: str = os.path.join( os.path.dirname( __file__ ), 'assets', 'padlock.png' )
    icon = PhotoImage( file=icon_path )

    window.iconphoto( True, icon )

    # Main menu

    print( '=> Opened GUI...' )

    window.mainloop()
