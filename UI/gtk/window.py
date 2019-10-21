
from gi.repository import Gtk
from gi.repository import GdkPixbuf
	
class Window(Gtk.Window):
	def __init__(self,title):
		super(Window,self).__init__()
		self.set_title(title)
		
	
	def connect_close_function(self,function):
		self.connect("delete-event",function)
	
	def connect_menubar(self,menubar):
		self.add_accel_group(menubar.get_accel_group())
	
	def connect_configure_event_handler(self,function):
		self.connect("configure-event",function)

	def set_taskbar_icon(self,file_path):
		pixbuf = GdkPixbuf.Pixbuf.new_from_file(file_path)
		self.set_icon(pixbuf)
		

	#add()
	#get_size()
