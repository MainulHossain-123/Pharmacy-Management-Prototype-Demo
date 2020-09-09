from tkinter import *
from tkinter import messagebox
import os
f=open("database_proj",'a+')
root = Tk()
root.title("Simple Pharmacy Managment System")
root.configure(width=1500,height=600,bg='BLACK')
var=-1

label0= Label(root,text="PHARMACY MANAGEMENT SYSTEM ",bg="black",fg="white",font=("Times", 30))
label1=Label(root,text="ENTER ITEM NAME",bg="red",relief="ridge",fg="white",font=("Times", 12),width=25)
entry1=Entry(root , font=("Times", 12))
label2=Label(root, text="ENTER ITEM PRICE",bd="2",relief="ridge",height="1",bg="red",fg="white", font=("Times", 12),width=25)
entry2= Entry(root, font=("Times", 12))
label3=Label(root, text="ENTER ITEM QUANTITY",bd="2",relief="ridge",bg="red",fg="white", font=("Times", 12),width=25)
entry3= Entry(root, font=("Times", 12))
label4=Label(root, text="ENTER ITEM CATEGORY",bd="2",relief="ridge",bg="red",fg="white", font=("Times", 12),width=25)
entry4= Entry(root, font=("Times", 12))
label5=Label(root, text="ENTER ITEM DISCOUNT",bg="red",relief="ridge",fg="white", font=("Times", 12),width=25)
entry5= Entry(root, font=("Times", 12))
button1= Button(root, text="ADD ITEM", bg="white", fg="black", width=20, font=("Times", 12),command=additem)
button2= Button(root, text="DELETE ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=deleteitem)
button3= Button(root, text="VIEW FIRST ITEM" , bg="white", fg="black", width =20, font=("Times", 12),command=firstitem)
button4= Button(root, text="VIEW NEXT ITEM" , bg="white", fg="black", width =20, font=("Times", 12), command=nextitem)
button5= Button(root, text="VIEW PREVIOUS ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=previousitem)
button6= Button(root, text="VIEW LAST ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=lastitem)
button7= Button(root, text="UPDATE ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=updateitem)
button8= Button(root, text="SEARCH ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=searchitem)
button9= Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12),command=clearitem)
