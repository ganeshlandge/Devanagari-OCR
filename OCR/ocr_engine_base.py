

import abc
import multiprocessing


class OcrEngineBase(metaclass=abc.ABCMeta):
	def __init__(self,language=None):
		self.language = language
	
	@staticmethod
	@abc.abstractmethod
	def get_available_languages():
		return
	
	@abc.abstractmethod
	def ocr_image_to_text(self,image_file_name):
		pass
	
	def cancel():
		pass
		

	def set_language(self,language):
		if language in self.__class__.get_available_languages():
			self.language = language
			return True
		else:
			return False
	
	def ocr_image_to_text_with_multiprocessing(self,image_file_name):
		parent_conn, child_conn = multiprocessing.Pipe()
		
		p = multiprocessing.Process(target=(lambda parent_conn, child_conn,
		image_file_name : child_conn.send(self.ocr_image_to_text(image_file_name))),
		args=(parent_conn, child_conn,image_file_name))
		
		p.start()
		p.join()
		
		return parent_conn.recv();


	@staticmethod
	@abc.abstractmethod
	def is_available():
		return		
