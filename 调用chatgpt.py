import openai

import os, sys
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import *
import openai

# Initialize the OpenAI API client
openai.api_key = "org-LtTWDpM5Me8zHzAxdNu93DO3"

# Define your prompt
prompt = "Hello, how are you today?"

# Generate a response from ChatGPT
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
 
# Print the response
print(response["choices"][0]["text"])


class AppUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('My ChatGPT ')
        self.master.geometry('900x500')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('Tftitle.TLabelframe', font=('微软雅黑', 12))
        self.style.configure('Tftitle.TLabelframe.Label', font=('微软雅黑', 12))

        self.ftitle = LabelFrame(self.top, text='', style='Tftitle.TLabelframe')
        self.ftitle.place(relx=0.008, rely=0.017, relwidth=0.982, relheight=0.998)

        self.stext = Text(self.ftitle, font=('黑体', 12), wrap=NONE, )
        self.stext.place(relx=0.017, rely=0.036, relwidth=0.957, relheight=0.412)

        # 垂直滚动条
        self.VScroll1 = Scrollbar(self.stext, orient='vertical')
        self.VScroll1.pack(side=RIGHT, fill=Y)
        self.VScroll1.config(command=self.stext.yview)
        self.stext.config(yscrollcommand=self.VScroll1.set)
        # 水平滚动条
        self.stextxscroll = Scrollbar(self.stext, orient=HORIZONTAL)
        self.stextxscroll.pack(side=BOTTOM, fill=X)
        self.stextxscroll.config(command=self.stext.xview)
        self.stext.config(xscrollcommand=self.stextxscroll.set)

        self.totext = Text(self.ftitle, font=('微软雅黑', 12), wrap=NONE)
        self.totext.place(relx=0.017, rely=0.552, relwidth=0.957, relheight=0.412)

        self.VScroll2 = Scrollbar(self.totext, orient='vertical')
        self.VScroll2.pack(side=RIGHT, fill=Y)
        # 将滚动条与文本框关联
        self.VScroll2.config(command=self.totext.yview)
        self.totext.config(yscrollcommand=self.VScroll2.set)
        # 水平滚动条
        self.totextxscroll = Scrollbar(self.totext, orient=HORIZONTAL)
        self.totextxscroll.pack(side=BOTTOM, fill=X) 
        self.totextxscroll.config(command=self.totext.xview)
        self.totext.config(xscrollcommand=self.totextxscroll.set)
     
        menubar = Menu(self.top, tearoff=False)  # 创建一个菜单
        self.style.configure('Tcleartext.TButton', font=('微软雅黑', 12))
        self.cleartext = Button(self.ftitle, text='清空', command=self.cleartext_Cmd, style='Tcleartext.TButton')
        self.cleartext.place(relx=0.239, rely=0.463, relwidth=0.086, relheight=0.073)

        self.style.configure('Taddyh.TButton', font=('微软雅黑', 12))
        self.addyh = Button(self.ftitle, text='查询', command=self.addyh_Cmd,
                            style='Taddyh.TButton')
        self.addyh.place(relx=0.512, rely=0.463, relwidth=0.2, relheight=0.073)

class App(AppUI):
    def __init__(self, master=None):
        AppUI.__init__(self, master)

    def cleartext_Cmd(self, event=None):
        self.stext.delete(1.0, "end")
        self.totext.delete(1.0, "end")

    def addyh_Cmd(self, event=None):
        cookiestext = self.stext.get(1.0, "end")
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=cookiestext,
            max_tokens=1024,
            n=1,
            temperature=0.5,
        )
        answer = (response["choices"][0]["text"]).split(".")
        for i in answer:
            self.totext.insert(1.0, i)

            self.totext.update()

if __name__ == "__main__":
    top = Tk()
    App(top).mainloop()
