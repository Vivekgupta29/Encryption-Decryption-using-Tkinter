from tkinter import *
import base64

window = Tk()
window.geometry("1100x2000")
window.title("Tkinter with Secret Messaging")
window.state("zoomed")

f1 = Frame(window,height=100, width=800, relief=SUNKEN)
f1.pack(side=TOP)
# relief types=== FLAT RAISED SUNKEN GROOVE RIDGE

f2 = Frame(window, width=800, relief=GROOVE)
f2.pack(side=LEFT)

f3 = Frame(window, width=800, relief=GROOVE)
f3.pack(side=RIGHT)

f4 = Frame(window, width=1600, relief=GROOVE)
f4.pack(side=BOTTOM,pady=10)

label1 = Label(f1, font=('ARIAL', 40, 'bold'),
                text="Tkinter with Secret Messaging",
                fg="BLUE", bd=10, anchor='w')

label1.grid(row=0, column=0)


# Initializing variables
Msg1 = StringVar()
key1 = StringVar()
Result1 = StringVar()


#ENCODE
labelenc = Label(f2, font=('arial', 30, 'bold'),
               fg="Red",text="Encode", anchor="w")
labelenc.grid(row=0, columnspan=2)   

# Message label
lblMsg = Label(f2, font=('arial', 16, 'bold'),
               text="MESSAGE", bd=16, anchor="w")
lblMsg.grid(row=2, column=0)

# Message Entry box
txtMsg = Entry(f2, font=('arial', 16, 'bold'),
               textvariable=Msg1, bd=6,
               bg="white", justify='left')
txtMsg.grid(row=2, column=1)

# Key label
lblkey = Label(f2, font=('arial', 16, 'bold'),
               text="KEY (Only Integer)", bd=16, anchor="w")
lblkey.grid(row=3, column=0)

# Key Entry
txtkey = Entry(f2, font=('arial', 16, 'bold'),
               textvariable=key1, bd=6,
               bg="white", justify='left')
txtkey.grid(row=3, column=1)

# Result Label
lblResult = Label(f2, font=('arial', 16, 'bold'),
                  text="The Result-", bd=16, anchor="w")
lblResult.grid(row=5, column=0)

# Result Entry
txtResult = Entry(f2, font=('arial', 16, 'bold'),
                  textvariable=Result1,bd=8,
                  bg="white", justify='left')
txtResult.grid(row=5, column=1)



# Initializing variables
Msg2 = StringVar()
key2 = StringVar()
Result2 = StringVar()


#DECODE
labelenc = Label(f3, font=('arial', 30, 'bold'),
               fg="Red",text="Decode", anchor="w")
labelenc.grid(row=0, columnspan=2)   

# Message label
lblMsg = Label(f3, font=('arial', 16, 'bold'),
               text="MESSAGE", bd=16, anchor="w")
lblMsg.grid(row=2, column=0)

# Message Entry box
txtMsg = Entry(f3, font=('arial', 16, 'bold'),
               textvariable=Msg2, bd=6,
               bg="white", justify='left')
txtMsg.grid(row=2, column=1)

# Key label
lblkey = Label(f3, font=('arial', 16, 'bold'),
               text="KEY (Only Integer)", bd=16, anchor="w")
lblkey.grid(row=3, column=0)


# Key Entry
txtkey = Entry(f3, font=('arial', 16, 'bold'),
               textvariable=key2, bd=6,
               bg="white", justify='left')
txtkey.grid(row=3, column=1)


# Result Label
lblResult = Label(f3, font=('arial', 16, 'bold'),
                  text="The Result-", bd=16, anchor="w")
lblResult.grid(row=5, column=0)

# Result Entry
txtResult = Entry(f3, font=('arial', 16, 'bold'),
                  textvariable=Result2,bd=8,
                  bg="white", justify='left')
txtResult.grid(row=5, column=1)

# Vigenère cipher

def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)

def Results1():

    msg = Msg1.get()
    k = key1.get()

    Result1.set(encode(k, msg))
    

def Results2():

    msg = Msg2.get()
    k = key2.get()

    Result2.set(decode(k, msg))


def exit1():
    window.destroy()

def reset():
    Msg1.set("")
    key1.set("")
    Result1.set("")
    Msg2.set("")
    key2.set("")
    Result2.set("")

# Show message button
btnenc = Button(f2, padx=8, pady=6, bd=8, fg="black",
                  font=('arial', 16, 'bold'), width=15,
                  text="ENCODE", bg="cyan",
                  command=Results1).grid(row=6, columnspan=2)

btndec = Button(f3, padx=8, pady=6, bd=8, fg="black",
                  font=('arial', 16, 'bold'), width=15,
                  text="DECODE", bg="cyan",
                  command=Results2).grid(row=7, columnspan=2)

# Reset button
btnReset = Button(f4, padx=8, pady=6, bd=8,
                  fg="black", font=('arial', 16, 'bold'),
                  width=15, text="Reset", bg="light green",
                  command=reset).grid(row=0, columnspan=1)

# Exit button
btnExit = Button(f4, padx=8, pady=6, bd=8,
                 fg="black", font=('arial', 16, 'bold'),
                 width=10, text="Exit", bg="tomato",
                 command=exit1).grid(row=0, column=2)


window.mainloop()