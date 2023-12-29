import tkinter as tk
from tkinter import*
from tkinter.ttk import Combobox
import string, random


root= Tk()
root.title("Random Password Generator")
root.resizable(False,False)
root.geometry("500x400+100+200")
root.configure(bg="#2c5663")


def password_generate():
    length_password= solidboss.get()
    small_letters= string.ascii_lowercase
    capital_letters= string.ascii_uppercase
    digits= string.digits
    special_character= string.punctuation
    all_list=[]
    all_list.extend(list(small_letters))
    all_list.extend(list(capital_letters))
    all_list.extend(list(digits))
    all_list.extend(list(special_character))
    random.shuffle(all_list)
    password.set("".join(all_list[0:length_password]))
    
    


all_no={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10"}
#icon
Image_icon=PhotoImage(file="images/pg-icon.png")
root.iconphoto(False, Image_icon)


#label text

Title= Label(root, text="Random Password Generator",fg="Black", font=("arial",16,"bold"))
Title.pack(anchor="center", pady="20")

length= Label(root, text="Select the Length of Your Password:",fg="white", bg="#2c5663", font=("arial",12))
length.place(x="20",y="80")

solidboss= IntVar()
Selector= Combobox(root, textvariable= solidboss,state="redonly")
Selector['values']=[l for l in all_no. keys()]
Selector.place(x="285",y="82")


#button
generate_button= Button(root,text="Generate Password",bg="#066DB8", fg="white", font= ("arial",12, "bold"), command= password_generate)
generate_button.pack(anchor= "center", pady="50")

result_label= Label(root, text="Generated Password:",fg="white", bg="#2c5663", font=("arial",12))
result_label.place(x="20",y="180")

#generated password
password= StringVar()
password_final= Entry(root,textvariable= password,state="readonly",fg="blue", font=("arial", 12))
password_final.place(x="190",y="180")


