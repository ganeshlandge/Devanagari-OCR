

from gi.repository import Gtk


class Dialog(Gtk.Dialog):
	BUTTON_ID_1 = 1
	BUTTON_ID_2 = 2
	BUTTON_ID_3 = 3
	def __init__(self,title,buttons):
		super(Dialog,self).__init__(title,None,True,buttons)
	
	def add_widget(self,widget):
		box = self.get_content_area();
		box.add(widget)
	
	def add_widget_with_label(self,widget,label_text):
		new_box = Gtk.Box()
		label = Gtk.Label(label_text)
		label.set_mnemonic_widget(widget)
		new_box.pack_start(label, True, True, 0)
		new_box.pack_start(widget, True, True, 0)
		box = self.get_content_area();
		box.add(new_box)
		box.show_all()		

	def connect_configure_event_handler(self,function):
		self.connect("configure-event",function)
		
	#show_all()
	#run()
