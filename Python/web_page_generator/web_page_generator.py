
import tkinter as tk
from tkinter import *
import webbrowser 


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self, master)
        self.master.title("Web Page Generator")



        #button for default HTML page
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=2, padx=(200,0) , pady=(100,10),sticky=N+W)

        #button for Custom HTML page
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(row=2, column=3, padx=(20,10) , pady=(100,10),sticky=N+W)

        #Label widget for Custom entry
        self.label = tk.Label(self.master,text='Enter custom text or click the Default HTML page button')
        self.label.grid(row=0,column=0,padx=(27,0),pady=(40,0),sticky=N+W)

        #Entry widget
        self.entry = tk.Entry()
        self.entry.grid(row=1,column=0,rowspan=1,columnspan=50,padx=(30,40),pady=(0,0),sticky=N+E+W)

        #function for default HTML page
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        #function for custom text HTML page
    def customHTML(self):
        entry = (self.entry.get())
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + entry + "</h1>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        
        
        











if __name__ == "__main__":
    root= tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

    
