import wx


class CalculatorFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(CalculatorFrame, self).__init__(*args, **kw)

        # 创建主面板
        panel = wx.Panel(self)

        # 创建文本框用于显示输入和输出
        self.display = wx.TextCtrl(panel, value="", style=wx.TE_RIGHT | wx.TE_READONLY)

        # 定义按钮和它们对应的标签
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        # 创建按钮网格sizer
        grid_sizer = wx.GridSizer(4, 4, 5, 5)
        self.buttons = []
        for label in buttons:
            btn = wx.Button(panel, label=label)
            btn.Bind(wx.EVT_BUTTON, self.OnButtonClick)
            self.buttons.append(btn)
            grid_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

        # 创建主sizer，将文本框和按钮网格垂直排列
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.display, 0, wx.EXPAND | wx.ALL, 10)
        main_sizer.Add(grid_sizer, 1, wx.EXPAND | wx.ALL, 10)
        panel.SetSizer(main_sizer)

    def OnButtonClick(self, event):
        btn = event.GetEventObject()
        label = btn.GetLabel()

        if label == 'C':
            self.display.Clear()
        elif label == '=':
            try:
                # 这里只是简单地将文本框内容作为Python表达式求值
                # 在实际应用中，应该实现更安全的计算逻辑
                result = eval(self.display.GetValue())
                self.display.Clear()
                self.display.WriteText(str(result))
            except Exception as e:
                wx.MessageBox(f"Error: {e}", "Error", wx.ICON_ERROR)
        else:
            self.display.AppendText(label)


class CalculatorApp(wx.App):
    def OnInit(self):
        frame = CalculatorFrame(None, title="简易计算器", size=(350, 300))
        frame.Show(True)
        return True


if __name__ == '__main__':
    app = CalculatorApp()
    app.MainLoop()