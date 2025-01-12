import wx
from src.component import MyListCtrl
class MyFrame(wx.Frame):
    def __init__(self, *args,**kw):
        super(MyFrame, self).__init__(*args, **kw)
        panel = wx.Panel(self)

        self.listCtrl = MyListCtrl(panel,wx.ID_ANY, style=wx.LC_REPORT
                                                |wx.BORDER_NONE
                                                |wx.LC_EDIT_LABELS
                                                |wx.LC_SORT_ASCENDING)
        self.listCtrl.InsertColumn(0, "Column 1")
        self.listCtrl.InsertColumn(1, "Column 2")
        self.listCtrl.InsertColumn(2, "Column 3")

        for i in range(10):
            index=self.listCtrl.InsertItem(i, "Item %d" % i)
            self.listCtrl.SetItem(index, 1, "Description %d" % i)
            self.listCtrl.SetItem(index, 2, "Description %d" % i)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.listCtrl,1,wx.EXPAND|wx.ALL,5)
        panel.SetSizer(sizer)
        self.Show()
        
if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
