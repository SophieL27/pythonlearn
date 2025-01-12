import wx
import wx.adv


TRAY_ICON='../resources/computer.png'
TRAY_TOOLTIP='托盘示例'
from src.Ai_chat import AiChatWindow
from src.pc_info import pc_info
from src.task_aui_frame import task_aui_frame
class MonitorTaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self):
        super().__init__()
        icon = wx.Icon(TRAY_ICON)
        self.SetIcon(icon, TRAY_TOOLTIP)
        self.ai_chat_frame=None
        self.pc_info=None
        self.task_aui_frame=None

        #绑定事件处理函数
        self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, self.OnRightClick)
    def create_menu_item(self,menu,label,func):
        item=wx.MenuItem(menu,-1,label)
        menu.Bind(wx.EVT_MENU,func,id=item.GetId())
        menu.Append(item)
        return item

    def OnRightClick(self, event):
        #创建弹出菜单
        menu=wx.Menu()
        self.create_menu_item(menu, "我的计算机", self.on_pc_info)
        self.create_menu_item(menu, "任务管理器", self.on_task)
        self.create_menu_item(menu, "AI聊天", self.on_ai_chat)

        menu.AppendSeparator()

        menu.Append(wx.ID_EXIT,"E&xit")
        self.Bind(wx.EVT_MENU,self.OnExit,id=wx.ID_EXIT)

        #弹出菜单
        self.PopupMenu(menu)
        menu.Destroy()

    def OnExit(self, event):
        wx.GetApp().ExitMainLoop()


    def on_task(self, event):
        self.task_frame = task_aui_frame( None,"任务管理")
        self.task_frame.Show(True)

    def on_ai_chat(self, event):
        if self.ai_chat_frame is None:
           self.ai_chat_frame = AiChatWindow(None)
        self.ai_chat_frame.Show(True)

    def on_pc_info(self, event):
        if self.pc_info is None:
           self.pc_info = pc_info(None)
        self.pc_info.Show(True)
class MyApp(wx.App):
    def OnInit(self):
        frame=wx.Frame(None,wx.ID_ANY,'TaskBaIcon')
        MonitorTaskBarIcon()
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
