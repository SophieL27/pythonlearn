import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(200, 100))
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)# 绑定定时器事件
        self.timer.Start(1000)# 1000ms = 1s

    def OnTimer(self, event):
        print("定时器事件触发了！")
app=wx.App(False)
frame = MyFrame(None, 'wx.Timer Test')
frame.Show()
app.MainLoop()