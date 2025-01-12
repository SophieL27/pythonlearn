import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,200))
        self.panel = wx.Panel(self) # 创建一个面板，用于放置其他控件
        self.textctrl = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
app = wx.App(False)
frame = MyFrame(None, 'TextCtrl Example')
frame.Show(True)
app.MainLoop()