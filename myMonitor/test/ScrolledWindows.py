import wx
class MyFrame(wx.Frame):
    def __init__(self, parent,title):
        super(MyFrame, self).__init__(parent,title=title, size=(600, 400))
        self.panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        # 创建一个滚动窗口
        scrolled = wx.ScrolledWindow(self.panel,-1,style=wx.VSCROLL)
        scrolled.SetScrollRate(0,10)# 水平方向不滑动，垂直方向滑动10像素

        sizer=wx.BoxSizer(wx.VERTICAL)
        for i in range(30):
            label="Line {}".format(i+1)
            statictext = wx.StaticText(scrolled,label=label)
            sizer.Add(statictext, 0, flag=wx.EXPAND|wx.ALL, border=5)

        scrolled.SetSizer(sizer)
        scrolled.FitInside()

        vbox.Add(scrolled,1,wx.EXPAND|wx.ALL, border=5)
        self.panel.SetSizer(vbox)# 添加到面板上
        self.panel.Layout()# 布局

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None,'测试')
    frame.Show()
    app.MainLoop()