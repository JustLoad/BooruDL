from threading import Thread
from tkinter import *

import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("Danbooru downloader")
root.geometry("500x200")

link = Entry(root)
link.pack()


def download():
    r = requests.get(link.get())

    soup = BeautifulSoup(r.text, 'html.parser')
    res = soup.find_all("img")

    if link.get().startswith("https://danbooru.donmai.us/"):
        label.configure(text="Starting download")
        r2 = requests.get(res[0]["src"])
        open("result.png", "wb").write(r2.content)
        label.configure(text="Download completed")

    elif link.get().startswith("https://yande.re"):
        label.configure(text="Starting download")
        r2 = requests.get(res[1]["src"])
        open("result.png", "wb").write(r2.content)
        label.configure(text="Download completed")

    elif link.get().startswith("https://safebooru.org/"):
        label.configure(text="Starting download")
        r2 = requests.get(res[2]["src"])
        open("result.png", "wb").write(r2.content)
        label.configure(text="Download completed")


downloadb = Button(root, text="Download", command=lambda: Thread(target=download, daemon=True).start())
downloadb.pack()

deleteb = Button(root, text="Delete link", command=lambda: Thread(target=link.delete(0, "end"), daemon=True).start())
deleteb.pack()

label = Label(root)
label.pack()

root.mainloop()
