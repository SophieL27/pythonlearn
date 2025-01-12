import wx
import wx.lib.mixins.listctrl as listmix
import threading
from src.component import MyListCtrl
import time
import psutil

def full_process_data(list,panel):
    max_cpu_index=None
    max_mem_index=None
    max_cpu=None
    max_mem=None
    data={}
    no=0
    count=0
    while True:
        for proc in psutil.process_iter(['pid',
                                         'name', 'cpu_percent',
                                         'memory_percent', 'status']):
            count += 1
            index=list.InsertItem(no,proc.info['name'])

            list.SetItem(index,1,str(proc.info['pid']))
            list.SetItem(index,2,proc.info['status'])
            # list.SetItem(index,3,str(proc.info['cpu_percent']))
            # list.SetItem(index,4,str(proc.info['memory_percent']))
            # list.SetItem(index,5,str(proc.username()))
            #data[index]=proc
            if proc.info['cpu_percent'] is None:
                list.SetItem(index,3,"0.00")
                proc.info['cpu_percent']=0.00
            else:
                list.SetItem(index,3,format(proc.info['cpu_percent'],'.2f'))

            if proc.info['memory_percent'] is None:
                list.SetItem(index,4,"0.00")
                proc.info['memory_percent'] = 0.00
            else:
                list.SetItem(index,4, format(proc.info['memory_percent'], '.2f'))

            data[index]=(proc.info['name'],str(proc.info['pid']),proc.info['status'],format(proc.info['cpu_percent'],'.2f'),
                                              format(proc.info['memory_percent'],'.2f'))
            no+=1

            if max_cpu is None:
                max_cpu_index=index
                max_mem_index=index
                max_mem=proc.info['memory_percent']
                max_cpu=proc.info['cpu_percent']
            else:
                if max_cpu > proc.info['cpu_percent']:
                    max_cpu_index = index
                    max_cpu=proc.info['cpu_percent']
                if max_mem < proc.info['memory_percent']:
                    max_mem_index = index
                    max_mem = proc.info['memory_percent']

            panel.itemDataMap=data
            item=list.GetItem(max_cpu_index)
            item.SetTextColour(wx.BLUE)
            list.SetItem(item)
            print(max_mem)
            item=list.GetItem(max_mem_index)
            item.SetTextColour(wx.GREEN)
            list.SetItem(item)
            panel.sort()

            wx.CallAfter(panel.update_list,data,max_cpu_index,max_mem_index)
            time.sleep(1)

class ProcessPanel(wx.Panel,listmix.ColumnSorterMixin):
    def __init__(self,parent):

        wx.Panel.__init__(self,parent=parent,id=wx.ID_ANY)

        self.itemDataMap=None
        self.list=None
        self.create()
        self.load_job=threading.Thread(target=full_process_data,name='process_load',args=(self.list,self))
        self.load_job.start()

    def create(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.list=MyListCtrl(self,wx.ID_ANY,style=wx.LC_REPORT
                             |wx.BORDER_NONE|wx.LC_EDIT_LABELS|wx.LC_SORT_ASCENDING)
        sizer.Add(self.list,1,wx.EXPAND)
        self.set_list_title()

        self.SetSizer(sizer)
        self.SetAutoLayout(True)

    def set_list_title(self):
        self.list.InsertColumn(0,"名字")
        self.list.InsertColumn(1,"PID")
        self.list.InsertColumn(2,"状态")
        self.list.InsertColumn(3,"CPU占用率")
        self.list.InsertColumn(4,"MEM占用率")
        self.list.InsertColumn(5,"用户")

    def GetListCtrl(self):
        return self.list

    def sort(self):
        listmix.ColumnSorterMixin.__init__(self,6)

    def update_list(self,data,max_cpu_index,max_mem_index):
        self.itemDataMap=data
        if max_cpu_index is not None:
            item=self.list.GetItem(max_cpu_index)
            item.SetTextColour(wx.BLUE)
            self.list.SetItem(item)
        if max_mem_index is not None:
            item = self.list.GetItem(max_mem_index)
            item.SetTextColour(wx.GREEN)
            self.list.SetItem(item)
        self.list.Refresh()
class MainFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(800,600))
        self.panel=ProcessPanel(self)
        self.Show()
if __name__=="__main__":
    app=wx.App(False)
    frame=MainFrame(None,"wxPython Matplotlib Example")
    frame.Show()
    app.MainLoop()

