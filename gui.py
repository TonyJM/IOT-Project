import tkinter as tk
from tkinter import filedialog
from tkinter import font
import threading
import serial
ser = serial.Serial('COM3',9600) 

filename=''
re=1
fString=''
recvString=''
rec=0
trans=0
root=None

class tr(threading.Thread):
    def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

    def run(self):
      #print "Starting " + self.name
      loop_tr()
      #print "Exiting " + self.name



def loop_tr():
    while 1:
        if(trans==1):
            transmit()
        if(re==1):
            recv() 

def transmit():
    global fstring,trans
    #x=input()
    #print("TRANSMIT : "+x)
    ser.write(fString.encode())
    trans=0
    
def recv():
    global root,rec,recvString
    s=""
    while ser.in_waiting:
        r=ser.read().decode()
        s+=r
    if(s!=""):
        recvString+=s
        rec=1
        root.event_generate("<<Foo>>")#Invoke event
    #if(s!=""):
    #    print(s)
    #if s.strip()=='false':
        #break




class ui(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      #print "Starting " + self.name
      loop_ui()
      #print "Exiting " + self.name


       
def loop_ui():
    global rec,root,recvString


    def exit(event):
        root.destroy()

    def UploadAction(event=None):
        global filename,fString
        filename = filedialog.askopenfilename()
        '''
        print('Selected:', filename)
        x='Selected : '+filename
        txt.delete(0.0,tk.END)
        txt.insert(0.0,x)
        '''
        #try:
        with open(filename) as f:
            fString=f.read()
                #print(fString)
        
        #p.config(file=filename)
        #txt.image_create(tk.END,image=p)

    def RunAction(event=None):
        #global r
        global trans
        trans=1

    def BackAction(event=None):
        txt.delete(0.0,tk.END)
        
    '''
    def DownloadAction(event=None):
        filename='rand'
        x=txt.get(1.0,tk.END)
        filename=filedialog.asksaveasfilename(defaultextension=".html", filetypes=(("html file", "*.html"),))
        with open(filename,'w') as f:
            f.write(x)
    '''
    #Generated event
    def doFoo(event):
        global rec
        print("UIFoo")
        print("Rec : ",rec) 
        if(rec==1):
            print("UIPrint")
            print(recvString)
            txt.delete(0.0,tk.END)
            txt.insert(0.0,recvString)
            rec=0

        
    
    root = tk.Tk()
    root.geometry("1920x1080")
    root.config(background="white")
    root.attributes("-fullscreen",True)
    root.bind("<Escape>", exit)
    root.bind("<<Foo>>", doFoo) #bind event

    Hel=font.Font(family='Helvetica', size=12, weight='bold')
    HelTitle=font.Font(family='Helvetica', size=32, weight='bold')

    '''
    txtInp=tk.Text(root)#,command=Input())
    txtInp.config(font=Hel)
    txtInp.place(relx=0.05,rely=0.03)

    txtOut=tk.Text(root)#,command=Output())
    txtOut.config(font=Hel)
    txtOut.config(height=20,width=70)
    txtOut.place(relx=0.25,rely=0.3)
    '''
    btn = tk.Button(root, text='Upload', command=UploadAction)
    btn.config(height=2,width=8,font=Hel,bg="#4dbd6b")
    btn.place(relx=0.35,rely=0.2)

    run = tk.Button(root, text='Send', command=RunAction)
    run.config(height=2,width=8,font=Hel,bg="#4dbd6b")
    run.place(relx=0.45,rely=0.2)

    '''
    dl = tk.Button(root, text='Download', command=DownloadAction)
    dl.config(height=2,width=8,font=Hel,bg="#4dbd6b")
    dl.place(relx=0.55,rely=0.2)
    '''

    back = tk.Button(root, text='Back',command=BackAction)
    back.config(height=2,width=8,font=Hel,bg="#4dbd6b")
    back.place(relx=0.65,rely=0.2)


    lbl=tk.Label(root,text='LiFi')
    lbl.config(height=2,width=20,font=HelTitle,fg="#4dbd6b",bg="white")
    lbl.place(relx=0.3,rely=0.05)
    
    
    txt=tk.Text(root)
    txt.config(font=Hel,bg="white")
    txt.config(height=20,width=70)
    txt.place(relx=0.25,rely=0.3)
    
    '''
    if(rec==1):
        print("UIPrint")
        txt.delete(0.0,tk.END)
        txt.insert(0.0,recvString)
        rec=0

    print("UI")  
    '''

    root.mainloop()








threadUI = ui(1, "ui")
threadUI.start()

threadTR = tr(2, "tr")
threadTR.start()
