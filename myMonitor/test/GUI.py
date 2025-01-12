import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,200))
        self.panel = wx.Panel(self) # 创建一个面板，用于放置其他控件
        self.button=wx.Button(self.panel, label="Click Me")
        self.Bind(wx.EVT_BUTTON, self.on_button_click, self.button)
        self.Show(True)
    def on_button_click(self, event):
        wx.MessageBox('Hello wxPython',
                    'Message',wx.OK|wx.ICON_INFORMATION)
app=wx.App(False)
frame=MyFrame(None, 'Hello wxPython')

app.MainLoop()