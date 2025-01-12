import wx
import wx.adv
from src.MonitorTaskBarIcon import MonitorTaskBarIcon
from src.login_frame import login_frame

class app(wx.App):
    def OnInit(self):
        frame=wx.Frame(None)
        self.SetTopWindow(frame)
        MonitorTaskBarIcon()
        return True
if __name__ == '__main__':
    app=app(False)
    loginFrame=login_frame(None)
    loginFrame.Show()
    app.MainLoop()