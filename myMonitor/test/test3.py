import wx
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame,self).__init__(parent, title=title,size=(800,600))
        #在Figure对象上添加一个子图
        self.figure = Figure()

        self.axes=self.figure.add_subplot(111)
        #设置坐标轴标签
        x=np.linspace(0,2*np.pi,100)
        y=np.sin(x)

        self.axes.plot(x,y)

        self.axes.set_xlabel('X axis')
        self.axes.set_ylabel('Y axis')
        #创建一个FigureCanvasWxAgg对象，并与其Figure对象关联
        self.canvas = FigureCanvas(self, -1, self.figure)

        sizer=wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas,1,wx.EXPAND)
        #设置窗口的大小调整器
        self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.OnClose)
    def OnClose(self, event):
        self.Destroy()
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None,'Matplotlib in WxPython')
    frame.Show()
    app.MainLoop()