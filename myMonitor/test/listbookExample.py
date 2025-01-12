import wx

class ListbookExample(wx.Frame):
    def __init__(self, parent, title):
        super(ListbookExample, self).__init__(parent, title=title, size=(800, 600))

        self.listbook=wx.Listbook(self,style=wx.LB_DEFAULT)

        self.page1 = wx.Panel(self.listbook)
        wx.StaticText(self.page1, label="这是页面1", pos=(10, 10))
        button1 = wx.Button(self.page1, label="按钮1", pos=(10, 50))
        button1.Bind(wx.EVT_BUTTON, self.on_button1)


        self.page2=wx.Panel(self.listbook)
        wx.StaticText(self.page2,label="这是页面2", pos=(10, 10))
        button2=wx.Button(self.page2, label="按钮2", pos=(10, 50))
        button2.Bind(wx.EVT_BUTTON, self.on_button2)


        # 添加页面到listbook
        self.listbook.AddPage(self.page1, "页面 1")
        self.listbook.AddPage(self.page2, "页面 2")

        # 设置listbook的大小为窗口的大小
        self.listbook.SetSize(self.GetClientSize())

        # 绑定页面变化事件
        self.listbook.Bind(wx.EVT_LISTBOOK_PAGE_CHANGED, self.on_page_changed)

    def on_button1(self, event):
        wx.MessageBox("按钮1被点击","信息")
    def on_button2(self, event):
        wx.MessageBox("按钮2被点击","信息")
    def on_page_changed(self, event):
        selection = self.listbook.GetSelection()
        wx.MessageBox(f"当前选中的页面是: {selection+1}", "页面更换")

app=wx.App(False)
# 创建窗口
frame=ListbookExample(None, title="Listbook Example")
# 显示窗口
frame.Show()
# 进入主循环
app.MainLoop()
