import sys
import platform
import psutil

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"处理器：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_cpu = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_cpu.Wrap( -1 )

		bSizer2.Add( self.m_cpu, 0, wx.ALL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"内存：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer5.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_mem = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_mem.Wrap( -1 )

		bSizer5.Add( self.m_mem, 0, wx.ALL, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"剩余内存：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_freemem = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_freemem.Wrap( -1 )

		bSizer6.Add( self.m_freemem, 0, wx.ALL, 5 )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )
		self.getSystemInfo()

	def __del__( self ):
		pass

	def getSystemInfo(self):
		if (sys.platform == "win32"):
			import wmi
			Wmi = wmi.WMI()
			CS = Wmi.Win32_ComputerSystem()[0]
			CPU = Wmi.Win32_Processor()[0]
			OS = Wmi.Win32_OperatingSystem()[0]


			self.m_cpu.SetLabel(CPU.Name)
			self.m_mem.SetLabel(str(int(CS.TotalPhysicalMemory) // 1024 ** 3) + u"GB")
			self.m_freemem.SetLabel(str(int(OS.FreePhysicalMemory) // 1024) + u"MB")


class myapp(wx.App):
	def OnInit(self):
		myframe = MyFrame1(None)
		myframe.Show(True)
		return True
if __name__ == '__main__':
	app=myapp()
	app.MainLoop()




