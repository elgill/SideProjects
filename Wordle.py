# Current Plan is to Create a wordle idea generator
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

#----------------------------------------------------------------------------------------------------#
#   NAME: App_Window
#   DESCRIPTION: Class to encapsulate Application window
#----------------------------------------------------------------------------------------------------#
class App_Window:
    letters=""

    #----------------------------------------------------------------------------------------------------#
    #   NAME: __init__
    #   DESCRIPTION: Launch app window
    #   PARAMS: self - App_Window object
    #   RETURN: None
    #----------------------------------------------------------------------------------------------------#
    def __init__(self):
        self.tk = Tk()
        self.tk.title('Wordle Thing')
        #sets default size and default maximized stateReturn
        self.tk.geometry("800x600")
        try:
            self.tk.state('zoomed')
        except TclError:
            # Fix for linux systems
            m = self.tk.maxsize()
            self.tk.geometry('{}x{}+0+0'.format(*m))
        self.tk.configure(background='gray')
        self.state = False
        # Key Bindings
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    #----------------------------------------------------------------------------------------------------#
    #   NAME: toggle_fullscreen
    #   DESCRIPTION: Trigger to toggle fullscreen
    #   PARAMS: self - App_Window object
    #           event
    #   RETURN: "break"
    #----------------------------------------------------------------------------------------------------#
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    #----------------------------------------------------------------------------------------------------#
    #   NAME: end_fullscreen
    #   DESCRIPTION: Trigger to exit fullscreen
    #   PARAMS: self - App_Window object
    #           event
    #   RETURN: "break"
    #----------------------------------------------------------------------------------------------------#
    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
    
    #----------------------------------------------------------------------------------------------------#
    #   NAME: handleError
    #   DESCRIPTION: Function to display error to user
    #   PARAMS: self - App_Window object
    #           e - Error string to display
    #   RETURN: None
    #----------------------------------------------------------------------------------------------------#
    def handleError(self,e):
        messagebox.showerror('Python Error', e)

#----------------------------------------------------------------------------------------------------#
#   Entry Point for initialization
#----------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    app = App_Window()
    app.tk.mainloop()