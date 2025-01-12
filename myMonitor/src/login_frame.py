# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import sys
from web_request.user_api import req_login
###########################################################################
## Class login_frame
###########################################################################

class login_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"用户名：", wx.Point( -1,-1 ), wx.Size( 80,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_username, 0, wx.ALL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer3.Add( self.m_password, 0, wx.ALL, 5 )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_login = wx.Button( self, wx.ID_ANY, u"登录", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_login, 0, wx.ALL, 5 )

		self.m_login.Bind( wx.EVT_LEFT_DOWN, self.onLogin )

		self.m_cancel = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_cancel, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )
		self.m_cancel.Bind( wx.EVT_LEFT_DOWN, self.onCancel )

	def __del__( self ):
		pass
	def onCancel( self, event ):
		event.Skip()
		sys.exit()

	def onLogin( self, event ):
		event.Skip()
		result,token = req_login( self.m_username.GetValue(),self.m_password.GetValue() )
		if result:
			self.Show(False)
		else:
			self.m_staticText2.SetLabel("用户名或密码错误！")
			self.m_staticText2.Show(True)
		print(result)

app = wx.App(False)
frame = login_frame(None)
frame.Show(True)
app.MainLoop()