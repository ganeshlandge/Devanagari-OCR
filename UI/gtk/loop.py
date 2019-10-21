

from gi.repository import Gtk		
from gi.repository import Gdk		
		
def start_main_loop():
	Gdk.threads_init()
	Gtk.main()
def stop_main_loop(data=None):
	Gtk.main_quit()

def acquire_lock():
	Gdk.threads_enter()

def release_lock():
	Gdk.threads_leave()
	
