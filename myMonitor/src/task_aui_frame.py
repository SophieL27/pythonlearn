import wx
import wx.aui
from src.ProcessPanel import ProcessPanel
from src.ResourceUtilizationBook import ResourceUtilizationBook
class task_aui_frame(wx.Frame):
    def __init__(self,parent,title):
        super(task_aui_frame,self).__init__(parent,title=title,size=(800,600))

        self.InitUI()
    def InitUI(self):
        self.SetTitle("任务管理")
        panel = wx.Panel(self)
        notebook = wx.aui.AuiNotebook(panel,
                                      style=wx.aui.AUI_NB_TOP |
                                            wx.aui.AUI_NB_TAB_SPLIT |
                                            wx.aui.AUI_NB_TAB_MOVE |
                                            wx.aui.AUI_NB_SCROLL_BUTTONS |
                                            wx.aui.AUI_NB_TAB_EXTERNAL_MOVE)
        pages=[
            (ResourceUtilizationBook(self),"性能"),
            (ProcessPanel(self),"进程"),
            (wx.Panel(notebook),"网络")
        ]

        for page,name in pages:
            notebook.AddPage(page,name)

        sizer=wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook,1,wx.EXPAND)
        panel.SetSizer(sizer)
        self.SetSizer(wx.BoxSizer(wx.VERTICAL))
        self.GetSizer().Add(panel,1,wx.EXPAND)

        self.Center()

class MyApp(wx.App):
    def OnInit(self):
        frame=task_aui_frame(None,"wx.aui.AuiNotebook example")
        frame.Show(True)
        return True

if __name__=='__main__':
    app=MyApp(False)
    app.MainLoop()
