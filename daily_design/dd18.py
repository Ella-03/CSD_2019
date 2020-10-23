#!/usr/bin/python3
#Ella Adam
#12/12/19

class Login(tk.Frame):
    login_tries = 0
    
    def __init__(self):
        tk.Frame.__init__(self)
        
        #create login frame stuff
        self.lbl_username = tk.Label(self, text = "Username:", font = DEFAULT)
        self.lbl_username.grid(row = 0, column = 0)
               
        self.ent_username = tk.Entry(self, font = DEFAULT, bg = "light blue")
        self.ent_username.grid(row = 0, column = 1)
#        self.background = self.ent_username.cget("bg")
                               
        self.lbl_password = tk.Label(self, text = "Password:", font = DEFAULT)
        self.lbl_password.grid(row = 1, column = 0)
        
        self.ent_password = tk.Entry(self, show="*", font = DEFAULT, bg = "light blue")
        self.ent_password.grid(row = 1, column = 1)
        
        self.lbl_instruction_1 = tk.Label(self, font = DEFAULT,
                                     text = "To login, fill out the")
        self.lbl_instruction_1.grid(row = 2, column = 0, columnspan = 2)
        
        self.lbl_instruction_2 = tk.Label(self, font = DEFAULT,
                                     text = "boxes and click Login.")
        self.lbl_instruction_2.grid(row = 3, column = 0, columnspan = 2)     
        
        self.btn_login = tk.Button(self, text = "LOGIN", bg="light blue",
                              command = self.raise_authenticate, font = DEFAULT)
        self.btn_login.grid(row = 4, column = 0, columnspan = 2)

#Added buttons
        self.btn_add_user = tk.Button(self, text = "Add User", bg = "light blue", font = DEFAULT)
        self.btn_add_user.grid(row = 5, column = 0)
        
        self.btn_update_user = tk.Button(self, text = "Update User", bg = "light blue", font = DEFAULT)
        self.btn_update_user.grid(row = 5, column = 1)