import wx
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

class MyFrame(wx.Frame):
    def __init__(self, parent,id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.figure = Figure()
        self.axes=self.figure.add_subplot(111)
        self.axes.plot([1,2,3],[4,5,6])
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.TOP|wx.LEFT|wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

        self.Center()
class MyApp(wx.App):
    def OnInit(self):
        frame=MyFrame(None,wx.ID_ANY,"Matplotlib in WXPython")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__=='__main__':
    app=MyApp(0)
    app.MainLoop()
