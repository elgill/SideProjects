# Current Plan is to Create a wordle idea generator
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox

#----------------------------------------------------------------------------------------------------#
#   NAME: App_Window
#   DESCRIPTION: Class to encapsulate Application window
#----------------------------------------------------------------------------------------------------#
class App_Window:
    letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

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

class Wordle_Board:
    letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]    
    #----------------------------------------------------------------------------------------------------#
    #   NAME: getWordAnswer
    #   DESCRIPTION: Return a random word from the answer list
    #   PARAMS: self - Wordle_Board object
    #   RETURN: None
    #----------------------------------------------------------------------------------------------------#
    def getWordAnswer(self):
        return "0"

    #----------------------------------------------------------------------------------------------------#
    #   NAME: __init__
    #   DESCRIPTION: Create Object
    #   PARAMS: self - Wordle_Board object
    #   RETURN: None
    #----------------------------------------------------------------------------------------------------#
    def __init__(self):
        self.answer=getWordAnswer()
    


class Wordle_Block:
    #yellow,green,gray,undefined
    #status=""
    #----------------------------------------------------------------------------------------------------#
    #   NAME: toggle_status
    #   DESCRIPTION: Function to toggle between colors
    #   PARAMS: self - Wordle_Block object
    #   RETURN: None
    #----------------------------------------------------------------------------------------------------#
    def toggle_status(self):
        if self.status=="yellow":
            self.status="green"
        elif self.status=="green":
            self.status="gray"
        else:
            self.status="yellow"

    #----------------------------------------------------------------------------------------------------#
    #   NAME: set_letter
    #   DESCRIPTION: Sets letter for object
    #   PARAMS: self - Wordle_Block object
    #           letter - letter to set
    #   RETURN: None
    #----------------------------------------------------------------------------------------------------#   
    def set_letter(self,letter):
        self.letter=letter

    #----------------------------------------------------------------------------------------------------#
    #   NAME: __init__
    #   DESCRIPTION: Create Object
    #   PARAMS: self - Wordle_Block object
    #   RETURN: None
    #----------------------------------------------------------------------------------------------------#
    def __init__(self):
        self.status="gray"

#----------------------------------------------------------------------------------------------------#
#   Entry Point for initialization
#----------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    app = App_Window()
    app.tk.mainloop()