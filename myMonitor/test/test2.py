import wx
import wx.aui
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame,self).__init__(parent, title=title,size=(800,600))

        panel = wx.Panel(self)
        # 创建一个AUI Notebook控件
        notebook = wx.aui.AuiNotebook(panel,
                                      style=wx.aui.AUI_NB_TOP |
                                            wx.aui.AUI_NB_TAB_SPLIT |
                                            wx.aui.AUI_NB_TAB_MOVE |
                                            wx.aui.AUI_NB_SCROLL_BUTTONS |
                                            wx.aui.AUI_NB_TAB_EXTERNAL_MOVE)
        self.page1=self.create_page(notebook, "Page 1")
        self.page2=self.create_page(notebook, "Pag e 2")
        self.page3=self.create_page(notebook, "Page 3")

        notebook.AddPage(self.page1, "Page 1")
        notebook.AddPage(self.page2, "Page 2")
        notebook.AddPage(self.page3, "Page 3")

        self.Bind(wx.EVT_CLOSE, self.Onclose)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.EXPAND)
        panel.SetSizer(sizer)
        self.SetSizer(wx.BoxSizer(wx.VERTICAL))
        self.GetSizer().Add(panel, 1, wx.EXPAND)

        self.Center()

    def create_page(self,notebook, label):
        page= wx.Panel(notebook)
        if label == "Page 1":
            button=wx.Button(page,label="显示信息",pos=(10,10))
            button.Bind(wx.EVT_BUTTON,self.on_page1_button)
        elif label == "Page 2":
            static_text=wx.StaticText(page,label="这是页面2",pos=(10,10))
        elif label == "Page 3":
            static_text=wx.StaticText(page,label="",size=(10,10))
            page.static_text=static_text
            button = wx.Button(page, label="更新标签", pos=(100, 10))
            button.Bind(wx.EVT_BUTTON, self.on_page3_button)
        return page


    def on_page1_button(self,event):
        wx.MessageBox("这是来自页面1的信息")
    def on_page3_button(self,event):
        static_text=self.page3.static_text
        static_text.SetLabel("我是页面3")

    def Onclose(self,event):
        self.Destroy()

app=wx.App(False)
frame=MyFrame(None,"AuiNotebook")
frame.Show()
app.MainLoop()
