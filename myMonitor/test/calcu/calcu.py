import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title,size=(300,400))
        self.panel = wx.Panel(self) # 创建一个面板，用于放置其他控件
        self.ini_u1()
        self.current_value=""
        self.previous_value=""
        self.operation=None

    def ini_u1(self):
        self.text_ctrl=wx.TextCtrl(self.panel, style=wx.TE_RIGHT)
        self.text_ctrl.Disable()#禁用编辑，仅用于显示

        buttons=[
            ('7',7),('8',8),('9',9),('/','/'),
            ('4',4),('5',5),('6',6),('*','*'),
            ('1',1),('2',2),('3',3),('-','-'),
            ('0',0),('C','C'),('=','='),('+','+')

        ]
        grid_sizer=wx.GridSizer(4,4,10,10)

        for label,id in buttons:
            button=wx.Button(self.panel,label=label)
            button.Bind(wx.EVT_BUTTON,self.on_button_click)
            grid_sizer.Add(button,0,wx.ALL,10)
        main_sizer=wx.BoxSizer(wx.VERTICAL)#创建一个垂直方向的布局管理器
        main_sizer.Add(self.text_ctrl,0,wx.ALL|wx.EXPAND,10)
        main_sizer.Add(grid_sizer, 1,wx.ALL|wx.EXPAND, 10)

        self.panel.SetSizer(main_sizer)
        self.Center()#居中窗口

    def on_button_click(self, event):
        button_label = event.GetEventObject().GetLabel()
        if button_label.isdigit():
            self.append_text(button_label)
        elif button_label in '+-*/':
            self.set_operation(button_label)
        elif button_label == '=':
            self.calculate()
        elif button_label == 'C':
            self.clear_text()

    def calculate(self):
        try:
            if self.operation == '+':
                result = float(self.previous_value) + float(self.current_value)
            elif self.operation == '-':
                result = float(self.previous_value) - float(self.current_value)
            elif self.operation == '*':
                result = float(self.previous_value) * float(self.current_value)
            elif self.operation == '/':
                if float(self.current_value) == 0:
                    self.text_ctrl.SetValue("Error")
                    return
                result = float(self.previous_value) / float(self.current_value)
            self.text_ctrl.SetValue(str(result))
            self.operation = None  # 重置操作符
        except ValueError:
            self.text_ctrl.SetValue("Error")
            self.operation = None  # 重置操作符

    def append_text(self, text):
        self.current_value = self.current_value + text
        self.text_ctrl.SetValue(self.current_value)

    def set_operation(self, operation):
        if self.current_value != "":
            self.previous_value = self.current_value
            self.current_value = ""
            self.operation = operation
            self.text_ctrl.SetValue(f"{self.previous_value} {self.operation} ")
        else:
            self.text_ctrl.SetValue("")



    def clear_text(self):
        self.text_ctrl.SetValue("")
        self.current_value = ""
        self.previous_value = ""
        self.operation = None
app = wx.App(False)
frame = MyFrame(None, 'Calculator')
frame.Show(True)
app.MainLoop()