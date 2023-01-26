from tkinter import *
from ttkbootstrap import *
from xmlrpc import client
from ttkbootstrap import Style

    #other widgets and layout

class LoginPage(Frame):
    

    
    
    

    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("RubixCube Lots")
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.username_label = Label(self, text="Username:")
        self.username_label.pack()
        
        self.username_entry = Entry(self)
        self.username_entry.pack()
        
        self.password_label = Label(self, text="Password:")
        self.password_label.pack()
        
        self.password_entry = Entry(self, show="*")
        self.password_entry.pack()
        
        self.login_button = Button(self, text="Login", command=self.login)
        self.login_button.pack()
        
    def login(self):
        # Get the username and password from the entry widgets
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Connect to Odoo using XML-RPC
        common = client.ServerProxy('http://your_odoo_host/xmlrpc/2/common')
        uid = common.authenticate(db, username, password, {})
        
        # Check if login was successful
        if uid:
            print("Login successful!")
            # Do something here, such as redirecting to another page
        else:
            print("Invalid username or password.")

root = Tk()
root.geometry("800x600")
## import the dark theme

app = LoginPage(master=root)    

style = Style(theme="superhero")
app.mainloop()



