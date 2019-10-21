

from gi.repository import Gtk
from gi.repository import GdkPixbuf


class AboutDialog(Gtk.AboutDialog):

	def __init__(self,title,buttons):
		super(AboutDialog,self).__init__(title,None,True,buttons)
	
	def set_logo_from_file(self,filename):
		pixbuff =  GdkPixbuf.Pixbuf.new_from_file(filename)
		self.set_logo(pixbuff)
			
		
	#show_all()
	#run()
