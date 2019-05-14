# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class RoundTracksDialog
###########################################################################

class RoundTracksDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Round Tracks", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 510,300 ), wx.DefaultSize )

		grid_vert = wx.FlexGridSizer( 2, 1, 0, 0 )
		grid_vert.AddGrowableCol( 0 )
		grid_vert.AddGrowableRow( 0 )
		grid_vert.SetFlexibleDirection( wx.BOTH )
		grid_vert.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.netclasslist = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.netclasslist.SetMinSize( wx.Size( 100,100 ) )

		self.net_class = self.netclasslist.AppendTextColumn( u"Net Class", wx.dataview.DATAVIEW_CELL_INERT, 160, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE|wx.dataview.DATAVIEW_COL_SORTABLE )
		self.do_rounding = self.netclasslist.AppendToggleColumn( u"Rounding", wx.dataview.DATAVIEW_CELL_ACTIVATABLE, 80, wx.ALIGN_CENTER, wx.dataview.DATAVIEW_COL_SORTABLE )
		self.scaling = self.netclasslist.AppendTextColumn( u"Scaling %", wx.dataview.DATAVIEW_CELL_EDITABLE, 80, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_SORTABLE )
		self.max_length = self.netclasslist.AppendTextColumn( u"Length %", wx.dataview.DATAVIEW_CELL_EDITABLE, 80, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_SORTABLE )
		self.passes = self.netclasslist.AppendTextColumn( u"Passes #", wx.dataview.DATAVIEW_CELL_EDITABLE, 80, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_SORTABLE )
		grid_vert.Add( self.netclasslist, 1, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		grid_horiz = wx.FlexGridSizer( 0, 4, 0, 0 )
		grid_horiz.AddGrowableCol( 2 )
		grid_horiz.SetFlexibleDirection( wx.BOTH )
		grid_horiz.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.do_create = wx.CheckBox( self, wx.ID_ANY, u"create a new file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.do_create.SetValue(True)
		grid_horiz.Add( self.do_create, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.do_open = wx.CheckBox( self, wx.ID_ANY, u"open the newly created file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.do_open.SetValue(True)
		grid_horiz.Add( self.do_open, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )


		grid_horiz.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.apply = wx.Button( self, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )

		self.apply.SetDefault()
		grid_horiz.Add( self.apply, 0, wx.ALL|wx.EXPAND, 5 )


		grid_vert.Add( grid_horiz, 1, wx.EXPAND, 5 )


		self.SetSizer( grid_vert )
		self.Layout()
		grid_vert.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_close )
		self.netclasslist.Bind( wx.dataview.EVT_DATAVIEW_ITEM_EDITING_DONE, self.on_item_editing, id = wx.ID_ANY )
		self.do_create.Bind( wx.EVT_CHECKBOX, self.on_toggle_create )
		self.apply.Bind( wx.EVT_BUTTON, self.run )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_close( self, event ):
		event.Skip()

	def on_item_editing( self, event ):
		event.Skip()

	def on_toggle_create( self, event ):
		event.Skip()

	def run( self, event ):
		event.Skip()


