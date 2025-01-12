import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,200))
        self.panel = wx.Panel(self) # 创建一个面板，用于放置其他控件
        self.statictext = wx.StaticText(self.panel, label="Hello World")
app = wx.App(False)
frame = MyFrame(None, 'StaticText Example')
frame.Show(True)
app.MainLoop()