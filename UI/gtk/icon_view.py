
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
import os


class IconView(Gtk.IconView):
	def __init__(self):
		super(IconView,self).__init__()
		self.set_selection_mode(Gtk.SelectionMode.MULTIPLE)
		self.liststore_images = Gtk.ListStore(GdkPixbuf.Pixbuf, str)
		self.set_pixbuf_column(0)
		self.set_text_column(1)
		self.set_columns(1)
		self.set_model(self.liststore_images)

	#methord is not thread safe
	def add_item(self,filename):
		try:
			pixbuff =  GdkPixbuf.Pixbuf.new_from_file(filename)
		except:
			pass
		else:
			height = pixbuff.get_height()
			width = pixbuff.get_width()
			ratio = (height*50)/width
			buff = pixbuff.scale_simple(50,ratio,GdkPixbuf.InterpType.BILINEAR)
			del pixbuff
			self.liststore_images.append([buff, filename])
			self.queue_draw()
			del buff

	def remove_selected_items(self,remove_file_too=True):
		for item in self.get_selected_items():
			iter = self.liststore_images.get_iter_from_string(item.to_string())
			if(remove_file_too):
				os.remove(self.liststore_images.get_value(iter, 1))
			self.liststore_images.remove(iter)
	
	def select_all_items(self):
		self.select_all()

	def select_item(self,filename):
		model = self.get_model()
		#iter = model.get_iter_first()
		for item in self.get_selected_items():
			iter = self.liststore_images.get_iter_from_string(item.to_string())
			if (filename == self.liststore_images.get_value(iter, 1)):		
				path = model.get_path(iter)
				self.select_path(path)
				break;
				
	
	def reload_preview(self,filename):
		for item in self.liststore_images:
			if (item[1] == filename):
				pixbuff =  GdkPixbuf.Pixbuf.new_from_file(filename)
				height = pixbuff.get_height()
				width = pixbuff.get_width()
				ratio = (height*50)/width
				buff = pixbuff.scale_simple(50,ratio,GdkPixbuf.InterpType.BILINEAR)
				del pixbuff
				item[0] = buff
				del buff
		
	
	def get_selected_item_names(self):
		items = []
		for item in reversed(self.get_selected_items()):
			items.append(self.liststore_images[item[0]][1])
		return items;

	def invert_list(self,*data):
		liststore = Gtk.ListStore(GdkPixbuf.Pixbuf, str)
		for item in reversed(self.liststore_images):
			liststore.append((item[0],item[1]))
		self.liststore_images = liststore
		self.set_model(self.liststore_images)
	
	def connect_on_selected_callback(self,function):
		self.connect("selection-changed",function)
	
	def connect_context_menu_button_callback(self,function):
		def fun(widget,event):
			if ((event.type == Gdk.EventType.BUTTON_RELEASE and event.button == 3) or
				(event.type == Gdk.EventType.KEY_PRESS and event.hardware_keycode == 135)):
				function()
		self.connect("button-release-event",fun)
		self.connect("key-press-event",fun)

