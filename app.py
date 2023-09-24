#Starting app creation using api like SE,NER AND EMOTION DETECTION 
from tkinter import *
class NLPApp:
    def __init__(self):
        #login ka qui load karna
        self.root=Tk()   #tk class object
        self.root.title('sway')
        self.root.iconbitmap('images/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='gray')
        self.login_gui()
        self.root.mainloop()
    
    def login_gui(self):
        heading=Label(self.root,text='NLP APP',bg='gray',fg='white')
        heading.pack(pady=(10,10))
        heading.configure(font=('verdana',24,'bold'))
        
        #Email
        label1=Label(self.root,text='Enter email')    #label for email 
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50) #used entry class to create a box and self cuz we'll use it somewhere
        self.email_input.pack(pady=(5,10),ipady=4)
        
        #Password
        label2=Label(self.root,text="Enter password")
        label2.pack(pady=(10,10))

        password=Entry(self.root,width=50)
        password.pack(pady=(5,10),ipady=4)
        
        #Login
        login=Button(self.root,text='login',width=30,height=2)    #Button class to create login 
        login.pack(pady=(10,10))

        label3=Label(self.root,text='Not a user ?')
        label3.pack(pady=(10,10),ipady=4)
        
        #Register
        redirect_btn=Button(self.root,text='Register Now',width=30,height=2,command=self.register_gui)
        redirect_btn.pack(pady=(10,10))
        
        
        


nlp=NLPApp()


