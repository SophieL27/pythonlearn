# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import platform
import wx
import wx.xrc
import psutil

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"计算机名称：", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		# 获取计算机名称
		computer_name = platform.node()
		self.m_name = wx.StaticText(self, wx.ID_ANY,computer_name, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_name.Wrap(-1)

		bSizer2.Add( self.m_name, 0, wx.ALL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"计算机操作系统：", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

		# 获取计算机操作系统
		self.m_system = platform.system()
		self.m_os = wx.StaticText( self, wx.ID_ANY,self.m_system, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_os.Wrap( -1 )

		bSizer5.Add( self.m_os, 0, wx.ALL, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"域名：", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )

		# 获取计算机域名
		self.m_Uname = platform.uname()[1]
		self.m_dns = wx.StaticText(self, wx.ID_ANY, str(self.m_Uname), wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_dns.Wrap(-1)

		bSizer6.Add( self.m_dns, 0, wx.ALL, 5 )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"系统制造商：", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer7.Add( self.m_staticText7, 0, wx.ALL, 5 )

		#获取系统制造商
		self.m_manufacturer = platform.uname().machine
		self.m_manufa = wx.StaticText( self, wx.ID_ANY, self.m_manufacturer, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_manufa.Wrap( -1 )

		bSizer7.Add( self.m_manufa, 0, wx.ALL, 5 )


		bSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"系统型号：", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer8.Add( self.m_staticText9, 0, wx.ALL, 5 )

		#获取系统型号
		self.m_ostypename = platform.platform()
		self.m_ostype = wx.StaticText( self, wx.ID_ANY, self.m_ostypename, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ostype.Wrap( -1 )

		bSizer8.Add( self.m_ostype, 0, wx.ALL, 5 )


		bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"处理器数：", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer9.Add( self.m_staticText11, 0, wx.ALL, 5 )

		#获取处理器数
		self.m_num = psutil.cpu_count()
		self.m_cpunum = wx.StaticText( self, wx.ID_ANY,str(self.m_num), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cpunum.Wrap( -1 )

		bSizer9.Add( self.m_cpunum, 0, wx.ALL, 5 )


		bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"处理器：", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer10.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_cpu = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cpu.Wrap( -1 )

		bSizer10.Add( self.m_cpu, 0, wx.ALL, 5 )


		bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"内存：", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer11.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.m_memory = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_memory.Wrap( -1 )

		bSizer11.Add( self.m_memory, 0, wx.ALL, 5 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"剩余物理内存：", wx.DefaultPosition, wx.Size( 160,-1 ), 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer12.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_freememory = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_freememory.Wrap( -1 )

		bSizer12.Add( self.m_freememory, 0, wx.ALL, 5 )


		bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer12, 1, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass



app = wx.App(False)
frame = MyFrame1(None)
frame.Show(True)
app.MainLoop()