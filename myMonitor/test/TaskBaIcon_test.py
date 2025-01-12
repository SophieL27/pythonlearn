import wx
import wx.adv

TRAY_ICON='../resources/computer.png'
TRAY_TOOLTIP='托盘示例'

class MonitorTaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self):
        super().__init__()
        icon = wx.Icon(TRAY_ICON)
        self.SetIcon(icon, TRAY_TOOLTIP)
        #绑定事件处理函数
        self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, self.OnRightClick)

    def OnRightClick(self, event):
        #创建弹出菜单
        menu=wx.Menu()
        menu.Append(wx.ID_EXIT,"E&xit")
        self.Bind(wx.EVT_MENU,self.OnExit,id=wx.ID_EXIT)
        #弹出菜单
        self.PopupMenu(menu)
        menu.Destroy()

    def OnExit(self, event):
        wx.GetApp().ExitMainLoop()

class MyApp(wx.App):
    def OnInit(self):
        frame=wx.Frame(None,wx.ID_ANY,'TaskBaIcon')
        MonitorTaskBarIcon()
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()