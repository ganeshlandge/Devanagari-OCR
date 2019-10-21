

from gi.repository import Gtk


class FileChooserDialog(Gtk.FileChooserDialog):
	OPEN = Gtk.FileChooserAction.OPEN
	SAVE = Gtk.FileChooserAction.SAVE
	OPEN_FOLDER = Gtk.FileChooserAction.SELECT_FOLDER
	ACCEPT = Gtk.ResponseType.OK
	
	def __init__(self,title,action,filters=None,dir=None):
		if(action == Gtk.FileChooserAction.OPEN or
			action == Gtk.FileChooserAction.SELECT_FOLDER):
			super(FileChooserDialog,self).__init__(title,None,action,buttons=(Gtk.STOCK_OPEN,Gtk.ResponseType.OK))
		else:
			super(FileChooserDialog,self).__init__(title,None,action,buttons=(Gtk.STOCK_SAVE,Gtk.ResponseType.OK))
		
		if (action != Gtk.FileChooserAction.SELECT_FOLDER):
			filter = Gtk.FileFilter()
			for item in filters:
				filter.add_pattern("*."+item)
			self.add_filter(filter)

		if (dir):
			self.set_current_folder(dir)

	#def run() distroy() get_filename()	set_current_folder()
