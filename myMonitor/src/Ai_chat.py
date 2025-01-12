import wx
from enum import Enum
import requests
from web_request.ai_api import req_post_ai
import json
import web_request

class AiChatWindow(wx.Frame):
    question_list= []
    answer_list=[]
    index=0

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(753, 552), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        # self.m_outPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL|wx.VSCROLL)
        self.m_outPanel = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.VSCROLL)
        self.m_outPanel.SetScrollbars(1, 1, 750, 500)
        self.m_outSize = wx.BoxSizer(wx.VERTICAL)
        self.m_outPanel.SetSizer(self.m_outSize)
        self.m_outPanel.Layout()
        self.m_outSize.Fit(self.m_outPanel)

        bSizer1.Add(self.m_outPanel, 1, wx.EXPAND | wx.ALL, 5)
        self.send_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        send_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.send_panel.SetSizer(send_sizer)
        self.m_sendCtrl = wx.TextCtrl(self.send_panel, wx.ID_ANY, wx.EmptyString,
                                      wx.DefaultPosition, wx.Size(600, -1), 0)

        self.send_btn = wx.Button(self.send_panel, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.DefaultSize, 0)
        self.send_btn.Bind(wx.EVT_BUTTON,self.send_question)

        send_sizer.Add(self.m_sendCtrl, 0, wx.ALL, 5)
        send_sizer.Add(self.send_btn, 0, wx.ALL, 5)
        bSizer1.Add(self.send_panel, 0, wx.ALL, 5)
        # Connect Events

        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        ###########
        username = "admin"
        password = "123456"
        data = {"username": username, "password": password}
        result = requests.post(web_request.web_url + "/login", params=data)
        result = json.loads(result.text)

        if result['code'] == 0:
            web_request.user_token = result['data']['token']
            web_request.user_id = result['data']['userId']
            web_request.username = result['data']['username']

        # print(result)
        ############
    def send_question(self, event):
        question = self.m_sendCtrl.GetValue()
        self.question_list.append(question)
        self.add_message(question,"sender")
        data={"questionList":self.question_list}
        result, result_data = req_post_ai(data)
        print(result_data)

        if result:
            self.answer_list.append(result_data)
            self.add_message(result_data,"receiver")
        else:
            self.add_message("操作失败",  "receiver")

        # new_panel=wx.Panel(self.m_outPanel)
        # new_panel.SetBackgroundColour('#ADD8E6')
        #
        # icon=wx.Bitmap('../resources/cpu.png',wx.BITMAP_TYPE_ANY)
        # new_icon=wx.StaticBitmap(new_panel, wx.ID_ANY, icon)
        #
        # new_sizer = wx.BoxSizer(wx.VERTICAL)
        #
        # new_text=wx.StaticText(new_panel, label=question)
        # new_text.SetForegroundColour('RED')
        # new_sizer.Add(new_icon,proportion=0,flag=wx.ALL|wx.ALIGN_RIGHT,border=5)
        # new_sizer.Add(new_text,proportion=1,flag=wx.ALL|wx.ALIGN_LEFT,border=10)
        #
        # new_panel.SetSizer(new_sizer)
        # self.m_outSize.Add(new_panel, proportion=0, flag=wx.EXPAND)
        # self.m_outPanel.Layout()
        # self.Layout()
        # self.m_outPanel.AdjustScrollbars()
        # self.m_outPanel.SetVirtualSize(self.m_outPanel.GetBestVirtualSize())
        #
        # self.m_sendCtrl.Clear()
    def add_message(self, content, type):
        line_break_count=content.count('\n')
        if line_break_count ==0:
            line_break_count = 1
        temp_panel=wx.Panel(self.m_outPanel,wx.ID_ANY,wx.DefaultPosition,wx.DefaultSize,wx.TAB_TRAVERSAL)

        temp_sizer = wx.BoxSizer(wx.HORIZONTAL)
        temp_panel.SetSizer(temp_sizer)
        image_path=""
        if type == "sender":
            image_path="../resources/cpu.png"
        else:
            image_path="../resources/disk.png"
        image=wx.Image(image_path,wx.BITMAP_TYPE_ANY)
        bitmap=image.ConvertToBitmap()
        static_bitmap=wx.StaticBitmap(temp_panel,wx.ID_ANY,bitmap)

        temp_font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        temp_static_text = wx.StaticText(temp_panel, label=content,style= wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ST_NO_AUTORESIZE|wx.BORDER_THEME)
        temp_static_text.SetFont(temp_font)

        width, height = temp_static_text.GetTextExtent(content)
        print(f"Width: {width}, Height: {height}")
        temp_panel.SetMaxSize((-1, height * line_break_count + 20))
        temp_static_text.SetMaxSize(wx.Size( 650, -1))
        temp_static_text.Wrap(650)

        if type == "sender":
            temp_static_text.SetBackgroundColour(wx.Colour( 125, 123, 0))
            temp_static_text.SetForegroundColour(wx.Colour(255, 0, 0))
            temp_sizer.Add( static_bitmap, 0, wx.ALL, 5)
            temp_sizer.Add(temp_static_text, 0, wx.ALL, 5)
            self.m_outSize.Add(temp_panel, self.index, wx.ALL | wx.ALIGN_LEFT, 5)
        else:
            temp_static_text.SetBackgroundColour(wx.Colour(125, 123, 0))
            temp_static_text.SetForegroundColour(wx.Colour(255, 255, 0))
            temp_sizer.Add(static_bitmap, 0, wx.ALL, 5)
            temp_sizer.Add(temp_static_text, 0, wx.ALL, 5)
            self.m_outSize.Add(temp_panel, self.index, wx.ALL | wx.ALIGN_LEFT, 5)

        self.index += 1

        self.m_outSize.Layout()
        self.m_outSize.Fit(self.m_outPanel)



class myapp(wx.App):
    def OnInit(self):
        myFrame = AiChatWindow(None)
        myFrame.Show()
        return True


if __name__ == '__main__':
    app = myapp()
    app.MainLoop()

