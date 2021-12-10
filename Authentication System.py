from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib
DATABASE = "userdb.db"

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x250")
        self.master.title("Root Window")

        self.frame = Frame(master)
        self.frame.pack(padx=5, ipady=10, fill="x")

        self.label1 = Label(self.frame, text="My App", bg="hot pink")
        self.label1.pack(pady=5, ipady=10, fill="x")

        self.button_login = Button(self.frame, text="Login", command=self.login_clicked)
        self.button_login.pack(pady=5, ipady=5, fill="x")
        self.button_register = Button(self.frame, text="Register", command=self.register_clicked)
        self.button_register.pack(pady=5, ipady=5, fill="x")

    def login_clicked(self):
        print("Login button clicked")
        self.master.withdraw()
        self.register = Login(self.master)

    def register_clicked(self):
        print("Register button clicked")
        self.master.withdraw()
        self.register = Register(self.master)


class Register:
    def __init__(self,master):
        self.master = master
        self.register = Toplevel (master)
        self.register.geometry("300x300")
        self.register.title("Register")
        self.register.protocol ("WM_DELETE_WINDOW", self.register_close)
        self.frame = Frame(self.register)
        self.frame.pack(padx=5, pady=5, fill="x")
        self.label1 = Label(self.frame, text="Register", bg="hot pink")
        self.label1.pack(pady=10, ipady=10, fill="x")
        self.label_email = Label(self.frame,
        text="Enter email*")
        self.label_email.pack(ipady=5, fill="x")
        self.entry_email = Entry(self.frame)
        self.entry_email.pack(ipady=5, fill="x")
        self.entry_email.focus_set()
        self.label_password= Label(self. frame, text="Enter password*")
        self.label_password.pack(ipady=5, fill="x")
        self.entry_password = Entry(self.frame, show="*")
        self.entry_password.pack(ipady=5, fill="x")
        self.button_register = Button(self.frame, text="Register", command=self.register_clicked)
        self.button_register.pack(pady=15, ipady=5, fill="x")


    def user_exists(self, email):
        # file = open("database.csv", "r")
        # thewholedataset = file.read()
        # thewholedataset = thewholedataset.split("\n")
        # exist = False
        # for line in thewholedataset:
        #     linesplit = line.split(",")
        #     linemail = linesplit[0].split("\n")[0]
        #     if email == linemail:
        #         exist = True
        #         break
        # return exist
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM USER WHERE email = ?", (email,))
        result = cursor.fetchone()
        connection.close()

        print(result)
        if result == None:
            print("1")
            return False
        elif result == "None":
            print("2")
            return False
        else:
            return True

    def register_close(self):
        self.register.destroy()
        self.master.deiconify()

    def register_clicked(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        print (f"email: {email}\password: {password}")
        if not "@" in email:
            messagebox.showerror("Register", "Invalid Email")
        elif self.user_exists(email):
            messagebox.showerror("Register", "User Already Exists")
        elif len(password) < 2:
            messagebox.showerror("Register", "Password too short")
        else:
            #self.write_user(email,password)
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            SECUREHASH = hashlib.sha512( str( password ).encode("utf-8") ).hexdigest()

            user_record = [email, SECUREHASH]
            cursor.execute("INSERT INTO USER (email, password) VALUES (?, ?)", user_record)

            connection.commit()
            connection.close()
            #file = open("database.csv", "a")
            #file.write(email + password + "\r\n")
            #file.write(f"{email},{password}\r\n")
            messagebox.showinfo("Register", "Account Created Succesfully")
            self.register_close()


class Login():
    def __init__(self,master):
        self.master = master
        self.login = Toplevel (master)
        self.login.geometry("300x300")
        self.login.title("Login")
        self.login.protocol ("WM_DELETE_WINDOW", self.login_close)
        self.frame = Frame(self.login)
        self.frame.pack(padx=5, pady=5, fill="x")
        self.label1 = Label(self.frame, text="Login", bg="hot pink")
        self.label1.pack(pady=10, ipady=10, fill="x")
        self.label_email = Label(self.frame,
        text="Enter email*")
        self.label_email.pack(ipady=5, fill="x")
        self.entry_email = Entry(self.frame)
        self.entry_email.pack(ipady=5, fill="x")
        self.entry_email.focus_set()
        self.label_password= Label(self. frame, text="Enter password*")
        self.label_password.pack(ipady=5, fill="x")
        self.entry_password = Entry(self.frame, show="*")
        self.entry_password.pack(ipady=5, fill="x")
        self.button_register = Button(self.frame, text="Login", command=self.login_clicked)
        self.button_register.pack(pady=15, ipady=5, fill="x")

    def user_exists(self, email):
        # file = open("database.csv", "r")
        # thewholedataset = file.read()
        # thewholedataset = thewholedataset.split("\n")
        # exist = False
        # for line in thewholedataset:
        #     linesplit = line.split(",")
        #     linemail = linesplit[0].split("\n")[0]
        #     if email == linemail:
        #         exist = True
        #         break
        # return exist
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM USER WHERE email = ?", (email,))
        result = cursor.fetchone()
        connection.close()

        #print(result)
        if result == None:
            return False
        elif result == "None":
            return False
        else:
            return True

    def login_close(self):
        self.login.destroy()
        self.master.deiconify()
    def login_clicked(self):
        email = self.entry_email.get()
        password = self.entry_password.get()
        #print(email,password)
        file = open("database.csv", "r")
        thewholedataset = file.read()
        #print(thewholedataset)
        thewholedataset = thewholedataset.split("\n")
        #print(thewholedataset)
        loggedin = False
        """
        for line in thewholedataset:
            linesplit = line.split(",")
            linemail = linesplit[0].split("\n")[0]
            #print(email == linemail)
            #print(email)
            #print(linemail)
            if email == linemail:
                linepassw = linesplit[1].split("\n")[0]
                #print(password == linepassw)
                if password == linepassw:
                    loggedin = True
                    user = email
                    break
        """
        if self.user_exists(email):
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            HASHEDPASSWORD = hashlib.sha512( str( password ).encode("utf-8") ).hexdigest()
            cursor.execute("SELECT * FROM USER WHERE email = ?", (email,))
            result = cursor.fetchone()
            connection.close()

            if result[2] == HASHEDPASSWORD:
                print(result[2], HASHEDPASSWORD)
                messagebox.showinfo("Login", "Sign in Successfull")
            else:
                messagebox.showinfo("Login", "Incorrect Password")
            #file = open("database.csv", "a")
            #file.write(email + password + "\r\n")
            #file.write(f"{email},{password}\r\n")
            self.login_close()
        else:
            messagebox.showerror("login","User doesn't exist")
        #if (loggedin == False):
        #    messagebox.showerror("login","Invalid Details")




root = Tk()
app = App(root)
root.mainloop()
