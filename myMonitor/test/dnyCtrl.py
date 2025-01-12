import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title,
                                      size=(400, 300))
        self.panels = []  # 用于存储所有面板的列表

        self.panel = wx.Panel(self)
        self.scrolled_window = wx.ScrolledWindow(self.panel)
        self.scrolled_window.SetScrollRate(5, 5)

        self.scrolled_window_sizer = wx.BoxSizer(wx.VERTICAL)
        self.scrolled_window.SetSizer(self.scrolled_window_sizer)
        self.button = wx.Button(self.panel, label='Add Panel')
        self.button.Bind(wx.EVT_BUTTON, self.on_button)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.scrolled_window, proportion=1, flag=wx.EXPAND)
        self.sizer.Add(self.button, proportion=0, flag=wx.CENTER)
        self.panel.SetSizer(self.sizer)

        self.Show()

    def on_button(self, event):
        new_panel = wx.Panel(self.scrolled_window)
        new_panel.SetBackgroundColour('#ADD8E6')  # Light blue background

        new_text = wx.StaticText(new_panel,
                                 label=f'Panel {len(self.panels) + 1}')
        new_text.SetForegroundColour('RED')  # Red text

        new_sizer = wx.BoxSizer(wx.VERTICAL)
        new_sizer.Add(new_text, proportion=0,
                      flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        new_panel.SetSizer(new_sizer)

        self.panels.append(new_panel)
        self.scrolled_window_sizer.Add(new_panel,
                                       proportion=0, flag=wx.EXPAND)

        self.scrolled_window.Layout()
        self.panel.Layout()

        self.scrolled_window.AdjustScrollbars()
        self.scrolled_window.SetVirtualSize(
            self.scrolled_window.GetBestVirtualSize())

app = wx.App(False)
frame = MyFrame(None, 'wxPython ScrolledWindow Example')
app.MainLoop()