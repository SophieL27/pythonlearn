import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,200))
        self.panel = wx.Panel(self) # 创建一个面板，用于放置其他控件
        flexgrid = wx.FlexGridSizer(2, 2, 10, 10)

        self.statictext1 = wx.StaticText(self.panel, label="Name:")
        self.statictext2 = wx.StaticText(self.panel, label="Age:")
        self.textctrl1 = wx.TextCtrl(self.panel)
        self.textctrl2 = wx.TextCtrl(self.panel)

        flexgrid.Add(self.statictext1, 0, wx.ALIGN_RIGHT)
        flexgrid.Add(self.textctrl1, 0, wx.EXPAND)
        flexgrid.Add(self.statictext2, 0, wx.ALIGN_RIGHT)
        flexgrid.Add(self.textctrl2, 0, wx.EXPAND)

        flexgrid.AddGrowableCol(1)
        self.panel.SetSizer(flexgrid)

app = wx.App(False)
frame = MyFrame(None, 'FlexGridSizer Example')
frame.Show(True)
app.MainLoop()