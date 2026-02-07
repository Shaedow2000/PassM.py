from tkinter import *
import os

def gui() -> None:
    window: Tk = Tk()
    window.geometry( '950x800' )
    window.title( 'PassM' )

    icon_path: str = os.path.join( os.path.dirname( __file__ ), 'assets', 'padlock.png' )
    icon = PhotoImage( file=icon_path )

    window.iconphoto( True, icon )

    window.mainloop()

gui()
