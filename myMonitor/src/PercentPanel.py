import wx
import psutil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import  colorsys

class PercentPanel(wx.Panel):
    def __init__(self, parent,title,data_name):
        wx.Panel.__init__(self, parent)

        self.title=title
        self.data_name=data_name

        self.axes_x= []
        self.figure = plt.Figure()
        self.axes = self.figure.add_subplot()
        self.axes.set_xlim(0,100)
        self.axes.set_ylim(0,100)
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, wx.LEFT|wx.TOP|wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
        self.init_data()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)  # 绑定定时器事件
        self.timer.Start(1000)  # 1000ms = 1s


    def init_data(self):


        self.cpu_count=psutil.cpu_count()
        self.mem_count=1

        self.line={}
        self.time_no=0
        self.axes_x=[]
        self.cpu_percent={}
        self.mem_percent={}

        if self.data_name == 'cpu':
            for i in range(self.cpu_count):
                self.cpu_percent[i]=[]
                color=self.get_color(i)
                (temp,)=self.axes.plot([],[],linewidth=1,color=color)
                self.line[str(i)] = temp
        elif self.data_name == 'mem':
            for i in range(self.mem_count):
                self.cpu_percent[i] = []
                color = self.get_color(i+self.cpu_count)
                (temp,) = self.axes.plot([], [], linewidth=1, color=color)
                self.line[str(i)] = temp




    def get_color(self,i):
        return colorsys.hsv_to_rgb(float(i) / float(self.cpu_count),1.0,1.0)

    def get_cpu_percent(self):
        cpu_id=0
        percent=psutil.cpu_percent(interval=1,percpu=True)
        for item in percent:
            self.cpu_percent[cpu_id].append(item)
            cpu_id += 1

    def get_mem_percent(self):
        percent=psutil.virtual_memory().percent
        if 0 not in self.mem_percent:
            self.mem_percent[0] = []
        self.mem_percent[0].append(percent)

    def on_timer(self,event):
        if self.data_name == 'cpu':
            self.axes_x.append(self.time_no)
            self.time_no+=1
            self.get_cpu_percent()
            j=0
            for item in self.cpu_percent:
                self.line[str(j)].set_data(self.axes_x,self.cpu_percent[item])
                j+=1
        elif self.data_name == 'mem':
            self.axes_x.append(self.time_no)
            self.time_no += 1
            self.get_mem_percent()
            j = 0
            for item in self.mem_percent:
                self.line[str(j)].set_data(self.axes_x, self.mem_percent[item])
                j += 1
        self.canvas.draw()




class MainFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self, parent, title=title,size=(800,600))
        self.panel = PercentPanel(self,title='System Monitor',data_name='cpu')
        self.Show()
if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame(None,"wxPython Matplotlib Demo")
    app.MainLoop()