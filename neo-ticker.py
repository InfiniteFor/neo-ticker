# python version: 2.7.14
# made by:        InfiniteFor
# version:        1.01
# dependencies:   pillow, requests

import requests
import json
from Tkinter import *
from PIL import Image, ImageTk

# enter amount of neo you hold
nhold = 300
fullscreen = False

# window configuration
co = 'white'
root = Tk()
root.title("NEO holdings v1.01")
root.iconbitmap(default='neo.ico')
root['bg'] = co
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(4, weight=1)
root.columnconfigure(3, weight=1)

# make it cover the entire screen if true
if fullscreen:
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))

# place current_price widget
w11 = Label(text="NEO price:  ", bg=co, font=("Helvetica", 16))
w11.grid(row=1, column=2, sticky=W)
w12 = Label(bg=co, font=("Helvetica", 16))
w12.grid(row=1, column=3, sticky=W)

# place total_holding widget
w21 = Label(text="Total holdings:  ", bg=co, font=("Helvetica", 16))
w21.grid(row=2, column=2, sticky=W)
w22 = Label(bg=co, font=("Helvetica", 16))
w22.grid(row=2, column=3, sticky=W)

# place 24h_change widget
w31 = Label(text="24h change:  ", bg=co, font=("Helvetica", 16))
w31.grid(row=3, column=2, sticky=W)
w32 = Label(bg=co, font=("Helvetica", 16))
w32.grid(row=3, column=3, sticky=W)

# NEO image widget
image11 = Image.open("neo.ico")
image11 = image11.resize((25, 25), Image.ANTIALIAS)
photo11 = ImageTk.PhotoImage(image11)
wim11 = Label(image=photo11)
wim11.photo = photo11
wim11.grid(row=1, column=1, sticky=W)

# dollar image widget
image21 = Image.open("doll.png")
image21 = image21.resize((25, 25), Image.ANTIALIAS)
photo21 = ImageTk.PhotoImage(image21)
wim21 = Label(image=photo21)
wim21.photo = photo21
wim21.grid(row=2, column=1, sticky=W)

# change image widget
image31 = Image.open("graph.gif")
image31 = image31.resize((25, 25), Image.ANTIALIAS)
photo31 = ImageTk.PhotoImage(image31)
wim31 = Label(image=photo31)
wim31.photo = photo31
wim31.grid(row=3, column=1, sticky=W)


# refresh price function (every 30 sec)
def refresh():
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/neo")
    price_usd = r.json()[0]["price_usd"]
    change_24h = r.json()[0]["percent_change_24h"]

    # calculate total
    total = '$%s' %(float(price_usd) * float(nhold))

    # %change green if positive, red if negative
    if change_24h > 0:
        rg = 'green'
    else:
        rg = 'red'

    # add '%' en '$' sign
    change_24h = '%s%%' %change_24h
    price_usd = '$%s' %round(float(price_usd),2)

    # update widgets
    w12.configure(text=price_usd)
    w22.configure(text=total)
    w32.configure(text=change_24h,fg=rg)
    root.after(30000, refresh)

refresh()
root.mainloop()
