import wx
import wx.aui
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame,self).__init__(parent, title=title,size=(800,600))

        panel = wx.Panel(self)

        notebook=wx.aui.AuiNotebook(panel,
                                    style=wx.aui.AUI_NB_TOP|
                                    wx.aui.AUI_NB_TAB_SPLIT|
                                    wx.aui.AUI_NB_TAB_MOVE |
                                    wx.aui.AUI_NB_SCROLL_BUTTONS|
                                    wx.aui.AUI_NB_TAB_EXTERNAL_MOVE)
        #添加页面到AuiNotebook考试考这个，会添加一个button，点击一下弹出一个message
        page1=wx.Panel(notebook)
        wx.StaticText(page1,label="这是页面 1",pos=(10,10))
        notebook.AddPage(page1,"页面 1")

        page2 = wx.Panel(notebook)
        wx.StaticText(page2, label="这是页面 2", pos=(10, 10))
        notebook.AddPage(page2, "页面 2")

        page3 = wx.Panel(notebook)
        wx.StaticText(page3, label="这是页面 3", pos=(10, 10))
        notebook.AddPage(page3, "页面 3")

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        sizer=wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook,1,wx.EXPAND)
        panel.SetSizer(sizer)
        self.SetSizer(wx.BoxSizer(wx.VERTICAL))#为Frame设置一个sizer
        self.GetSizer().Add(panel,1,wx.EXPAND)#将panel添加到Frame的sizer中

        self.Centre()

    def OnClose(self, event):
        self.Destroy()

app = wx.App(False)
frame = MyFrame(None, 'AuinoteBook 示例')
frame.Show(True)
app.MainLoop()