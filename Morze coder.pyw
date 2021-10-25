from tkinter import *
from tkinter import ttk
tk = Tk()
frm = ttk.Frame(tk, padding=100)
tk.title('Морзе')
tk.geometry('400x200')
tk.resizable(width=0, height=0)
text = Text(width=40, height=3, wrap=WORD)
inpText = Text(width=40, height=3, wrap=WORD)
scroll = Scrollbar(command=text.yview)
inpScroll = Scrollbar(command=inpText.yview)
morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',}

fromMorse =  {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
     '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R',
     '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
     '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
     '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
     '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
     '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
     '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
     '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':',
     '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
     '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3','/': ' '
     }

def coder():
   finallySen = []
   sentens  = text.get("1.0","end")
   sentens = sentens.upper()
   sentens.split()
   sentens = list(sentens)
   for i in range(len(sentens)):
      word =morse.get(sentens[i])
      if word== None:
         word = '/'
      finallySen.append(word) 
   finallySen = ' '.join(finallySen)
   inpText.delete("1.0","end")
   inpText.insert(1.0, finallySen)
   print(finallySen)

def decoder(): 
  cod = text.get("1.0","end")
  finallyWord=[]
   #cod= '.... . .-.. .-.. --- / .-- --- .-. .-.. -.. / ..-. ..- -.-. -.- / ... -.-- ... - . -- /'
  cod = cod.split()
  cod = list(cod)
  for g in range(len(cod)):
     
     werb = fromMorse.get(cod[g])

     finallyWord.append(werb)
  finallyWord = ''.join(finallyWord)
  inpText.delete("1.0","end")
  inpText.insert(1.0, finallyWord)
  print(finallyWord) 

def proces():
   stat =text.get("1.0","end")
   for i in range(len(stat)):
      if stat.find('/')!=-1:
         decoder()
      else:
         coder()
   if stat.endswith('/') !=True:
      stat =stat[0:-1]
deCodBtn = Button(tk,text="Translete" ,height=2, width=10,command=proces).place(x=150, y=150)
text.pack()
inpText.pack()
tk.mainloop()