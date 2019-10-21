

import os
import subprocess 
from lios.ocr.ocr_engine_base import OcrEngineBase

class OcrEngineOcrad(OcrEngineBase):
	name = "Ocrad"
	
	def __init__(self,language=None):
		self.set_language(language)

	def is_available():
		if ("/bin/ocrad" in subprocess.getoutput("whereis ocrad")):
			return True
		else:
			return False
			
	def ocr_image_to_text(self,file_name):
		os.system("convert {} /tmp/{}_for_ocr.pnm".format(file_name,file_name.split("/")[-1]))
		os.system("ocrad /tmp/{0}_for_ocr.pnm -l -c iso-8859-9 -o /tmp/{0}_output.txt".format(file_name.split("/")[-1]))
		os.remove("/tmp/{0}_for_ocr.pnm".format(file_name.split("/")[-1]))
		try:
			with open("/tmp/{0}_output.txt".format(file_name.split("/")[-1]),encoding="iso-8859-9") as file:
				text = file.read().strip()
				os.remove("/tmp/{0}_output.txt".format(file_name.split("/")[-1]))
				return text
		except:
			return ""

	def cancel():
		os.system("pkill convert")
		os.system("pkill ocrad")
		
	
	def get_available_languages():
		langs = ["eng"]
		return langs
