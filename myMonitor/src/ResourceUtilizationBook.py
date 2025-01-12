import wx
from wx import Panel
from src.PercentPanel import PercentPanel
class ResourceUtilizationBook(wx.Listbook):
    def __init__(self, parent):
        wx.Listbook.__init__(self, parent=parent, id=wx.ID_ANY,pos=wx.DefaultPosition, style=wx.LB_LEFT)

        img_list=wx.ImageList(32,32)
        img_list.Add(wx.Bitmap("../resources/cpu.png", wx.BITMAP_TYPE_PNG))
        img_list.Add(wx.Bitmap("../resources/memory.png", wx.BITMAP_TYPE_PNG))
        img_list.Add(wx.Bitmap("../resources/disk.png", wx.BITMAP_TYPE_PNG))
        self.AssignImageList(img_list)

        pages= [(PercentPanel(self, "cpu", "cpu"),"CPU"),
                (PercentPanel(self, "mem", "mem"),"内存"),
                (Panel(self),"磁盘")]
        img_id=0
        for page,label in pages:
            self.AddPage(page, label, imageId=img_id)
            img_id += 1

        self.Bind(wx.EVT_LISTBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_LISTBOOK_PAGE_CHANGING, self.OnPageChanging)
    def OnPageChanged(self, event):
        old =event.GetOldSelection()
        new = event.GetSelection()
        sel=self.GetSelection()
        print("OnPageChanged, old:%d, new:%d, sel:%d\n"%(old,new,sel))
        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print("OnPageChanging, old:%d, new:%d, sel:%d\n" % (old, new, sel))
        event.Skip()
class ResourceUtilizationFrame(wx.Frame):
    def __init__(self, parent,title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.listbook = ResourceUtilizationBook(self)
        self.Show()
if __name__ == "__main__":
    app = wx.App(False)
    frame = ResourceUtilizationFrame(None,"Resource Utilization")
    app.MainLoop()








