

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from gi.repository import Pango

class TextView(Gtk.TextView):
	AT_START=0
	AT_CURSOR=1
	AT_END=2
	
	def __init__(self):
		super(TextView, self).__init__()
		self.set_wrap_mode(Gtk.WrapMode.WORD)
		buffer = self.get_buffer()
		self.highlight_tag = buffer.create_tag('Reading')		
	
	def connect_insert(self,function):
		buffer = self.get_buffer()
		buffer.connect("insert-text",lambda x, y,z,a  : function())

	def connect_delete(self,function):
		buffer = self.get_buffer()
		buffer.connect("delete-range",lambda x, y,z  : function())

	def set_text(self,text):
		buffer = self.get_buffer()
		buffer.set_text(text);
	
	def get_text(self):
		buffer = self.get_buffer()
		start,end = buffer.get_bounds()
		text = buffer.get_text(start,end,False)
		return text

	# For Text Cleaner
	def get_text_from_cursor_to_end(self):
		buffer = self.get_buffer()
		end = buffer.get_end_iter()
		mark = buffer.get_insert()
		start = buffer.get_iter_at_mark(mark)
		text = buffer.get_text(start,end,False)
		return text

	def delete_text_from_cursor_to_end(self):
		buffer = self.get_buffer()
		end = buffer.get_end_iter()
		mark = buffer.get_insert()
		start = buffer.get_iter_at_mark(mark)
		buffer.delete(start,end)
	
	def insert_text(self,text,position,place_cursor=False):
		buffer = self.get_buffer()
		if (position == TextView.AT_START):
			iter = buffer.get_start_iter()
			buffer.insert(iter,text)
			
		elif position == TextView.AT_CURSOR:
			buffer.insert_at_cursor(text)
		else:
			iter = buffer.get_end_iter()
			buffer.insert(iter,text)
	
	def set_highlight_font(self,highlight_font):
		self.highlight_tag.set_property('font',highlight_font)

	def set_highlight_color(self,highlight_color):
		self.highlight_tag.set_property('foreground',
			Gdk.color_parse(highlight_color).to_string())

	def set_highlight_background(self,background_highlight_color):
		self.highlight_tag.set_property('background',
			Gdk.color_parse(background_highlight_color).to_string())
	
		
	def set_font(self,font_discription):
		pangoFont = Pango.FontDescription(font_discription)
		self.modify_font(pangoFont)
	
	def set_font_color(self,font_color):
		self.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse(font_color))
		
	def set_background_color(self,background_color):
		self.modify_bg(Gtk.StateFlags.NORMAL, Gdk.color_parse(background_color))
	
	def get_cursor_line_number(self):
		buffer = self.get_buffer()
		insert_mark = buffer.get_insert()
		offset = buffer.get_iter_at_mark(insert_mark)
		return offset.get_line()
	
	def get_line_count(self):
		buffer = self.get_buffer()
		return buffer.get_line_count()

	def move_cursor_to_line(self,line_number):
		buffer = self.get_buffer()
		iter = buffer.get_iter_at_line(line_number)
		buffer.place_cursor(iter)
		self.scroll_to_iter(iter, 0.0,False,0.0,0.0)
	
	def get_modified(self):
		buffer = self.get_buffer()
		return buffer.get_modified()
	
	def set_modified(self,value):
		buffer = self.get_buffer()
		buffer.set_modified(value)
	
	def has_selection(self):
		buffer = self.get_buffer()
		return buffer.get_has_selection()

	def get_selected_text(self):
		buffer = self.get_buffer()
		start,end = buffer.get_selection_bounds()
		return buffer.get_text(start,end,0)
	
	def delete_all_text(self):
		buffer = self.get_buffer()
		start, end = buffer.get_bounds()
		buffer.delete(start, end)
	
	# Placing a bookmark
	def get_mark_at_line(self,line):
		buffer = self.get_buffer()
		iter = buffer.get_iter_at_line(line)
		return buffer.create_mark(None,iter,True)
		
	# Moving to existing bookmark
	def move_cursor_to_mark(self,mark):
		buffer = self.get_buffer()
		iter = buffer.get_iter_at_mark(mark)
		buffer.place_cursor(iter)
		self.scroll_to_iter(iter, 0.0,False,0.0,0.0)
	
	# For saving Bookmark with line number
	def get_line_number_of_mark(self,mark):
		buffer = self.get_buffer()
		iter = buffer.get_iter_at_mark(mark)
		return iter.get_line()
		
	def get_cursor_mark(self):
		buffer = self.get_buffer()
		return buffer.get_insert()
	
	# For autofilling new bookmark name
	def get_current_line_text(self):
		buffer = self.get_buffer()
		mark = buffer.get_insert()
		start_iter = buffer.get_iter_at_mark(mark)
		end_iter = start_iter.copy()
		start_iter.backward_sentence_start()
		end_iter.forward_to_line_end()
		return buffer.get_text(start_iter,end_iter,True)		
	
	# For highlighting bookmark position and go-to-line
	def highlights_cursor_line(self):
		buffer = self.get_buffer()
		self.remove_all_highlights()
		mark = buffer.get_insert()
		start_iter = buffer.get_iter_at_mark(mark)
		end_iter = start_iter.copy()
		end_iter.forward_to_line_end()
		self.scroll_to_iter(start_iter, 0.0,False,0.0,0.0)
		buffer.apply_tag(self.highlight_tag, start_iter, end_iter)
	
	#Find , Find and Replace , Spell check , TextReader
	

	
	def remove_all_highlights(self):
		buffer = self.get_buffer()
		start = buffer.get_start_iter()
		end = buffer.get_end_iter()
		buffer.remove_tag(self.highlight_tag, start, end)
		
		
			
	def replace_last_word(self,replace_word):
		buffer = self.get_buffer()
		buffer.delete(self.start_iter, self.end_iter)
		buffer.insert(self.start_iter," "+replace_word)
		self.start_iter = self.end_iter.copy()

	def get_next_word(self):
		buffer = self.get_buffer()
		insert_mark = buffer.get_insert()
		self.start_iter = buffer.get_iter_at_mark(insert_mark)
		self.end_iter = self.start_iter.copy()
		iter0 = self.start_iter.copy()
		iter0.backward_word_start()
		self.remove_all_highlights()
		self.end_iter.forward_word_end()
		buffer.apply_tag(self.highlight_tag, self.start_iter, self.end_iter)
		buffer.place_cursor(self.end_iter)
		return buffer.get_text(self.start_iter,self.end_iter,0)			

	def get_previous_word(self):
		buffer = self.get_buffer()
		insert_mark = buffer.get_insert()
		self.end_iter = buffer.get_iter_at_mark(insert_mark)
		self.start_iter = self.end_iter.copy()		
		iter0 = self.end_iter.copy()
		iter0.forward_word_end()
		self.remove_all_highlights()		
		self.start_iter.backward_word_start ()
		buffer.apply_tag(self.highlight_tag, self.start_iter, self.end_iter)
		buffer.place_cursor(self.start_iter)
		return buffer.get_text(self.start_iter,self.end_iter,0)

	def get_context_text(self):
		buffer = self.get_buffer()
		insert_mark = buffer.get_insert()
		iter1 = buffer.get_iter_at_mark(insert_mark)
		iter2 = iter1.copy()
		iter1.backward_sentence_start()
		iter2.forward_sentence_end()
		return buffer.get_text(iter1,iter2,0)
	
	def delete_last_word(self):
		buffer = self.get_buffer()
		buffer.delete(self.start_iter,self.end_iter)
	
	def get_next_sentence(self):
		buffer = self.get_buffer()
		insert_mark = buffer.get_insert()
		iter1 = buffer.get_iter_at_mark(insert_mark)
		iter2 = iter1.copy()
		start = buffer.get_start_iter()
		end = buffer.get_end_iter()
		self.remove_all_highlights()
		iter2.forward_sentence_end()
		buffer.apply_tag(self.highlight_tag, iter1, iter2)
		buffer.place_cursor(iter2)
		return buffer.get_text(iter1,iter2,0)
	
	def is_cursor_at_end(self):
		buffer = self.get_buffer()
		insert_mark = buffer.get_insert()
		iter1 = buffer.get_iter_at_mark(insert_mark)
		end = buffer.get_end_iter()
		if(end.equal(iter1)):
			return 1;
		else:
			return 0;

	def is_cursor_at_start(self):
		buffer = self.get_buffer()
		insert_mark = buffer.get_insert()
		iter1 = buffer.get_iter_at_mark(insert_mark)
		start = buffer.get_start_iter()
		if(start.equal(iter1)):
			return 1;
		else:
			return 0;
	
	# For Find/Find and Replace
	
	def move_forward_to_word(self,word):
		buffer = self.get_buffer()
		insert_mark = buffer.get_insert()
		self.start_iter = buffer.get_iter_at_mark(insert_mark)
		result = self.start_iter.forward_search(word, 0, None)
		if (result):
			self.start_iter, self.end_iter = result
			buffer.place_cursor(self.end_iter)
			self.remove_all_highlights()
			buffer.apply_tag(self.highlight_tag, self.start_iter, self.end_iter)
			self.scroll_to_iter(self.start_iter,00,False,False,False)
			return True
		return False

	def move_backward_to_word(self,word):
		buffer = self.get_buffer()
		insert_mark = buffer.get_insert()
		self.start_iter = buffer.get_iter_at_mark(insert_mark)
		self.end_iter = self.start_iter.copy()
		result = self.start_iter.backward_search(word, 0, None)
		if (result):
			self.start_iter, self.end_iter = result
			buffer.place_cursor(self.start_iter)
			self.remove_all_highlights()
			buffer.apply_tag(self.highlight_tag, self.start_iter, self.end_iter)
			self.scroll_to_iter(self.start_iter,00,False,False,False)
			return True
		return False

