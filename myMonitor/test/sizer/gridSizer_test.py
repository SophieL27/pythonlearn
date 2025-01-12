import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,200))
        self.panel = wx.Panel(self) # 创建一个面板，用于放置其他控件
        grid = wx.GridSizer(2, 2, 10, 10)

        self.statictext1 = wx.StaticText(self.panel, label="Name:")
        self.statictext2 = wx.StaticText(self.panel, label="Age:")
        self.textctrl1 = wx.TextCtrl(self.panel)
        self.textctrl2 = wx.TextCtrl(self.panel)
        grid.Add(self.statictext1, 0, wx.ALIGN_RIGHT)
        grid.Add(self.textctrl1, 0, wx.EXPAND)
        grid.Add(self.statictext2, 0, wx.ALIGN_RIGHT)
        grid.Add(self.textctrl2, 0, wx.EXPAND)

        self.panel.SetSizer(grid)

app = wx.App(False)
frame = MyFrame(None, 'GridSizer Example')
frame.Show(True)
app.MainLoop()