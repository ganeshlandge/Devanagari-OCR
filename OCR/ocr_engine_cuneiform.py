

import os
import re
import subprocess 
from lios.ocr.ocr_engine_base import OcrEngineBase


LANGUAGES_LINE_PREFIX = "Supported languages: "
LANGUAGES_SPLIT_RE = re.compile("[^a-z]")


class OcrEngineCuneiform(OcrEngineBase):
	name = "Cuneiform"
	
	def __init__(self,language=None):
		self.set_language(language)

	def is_available():
		if ("/bin/cuneiform" in subprocess.getoutput("whereis cuneiform")):
			return True
		else:
			return False
			
	def ocr_image_to_text(self,file_name):
		os.system("convert {} /tmp/{}_for_ocr.png".format(file_name,file_name.split("/")[-1]))
		os.system("cuneiform -f text -l {0} -o /tmp/{1}_output.txt /tmp/{1}_for_ocr.png".format(self.language,file_name.split("/")[-1]))
		os.remove("/tmp/{0}_for_ocr.png".format(file_name.split("/")[-1]))
		try:
			with open("/tmp/{0}_output.txt".format(file_name.split("/")[-1]),encoding="utf-8") as file:
				text = file.read().strip()
				os.remove("/tmp/{0}_output.txt".format(file_name.split("/")[-1]))
				return text
		except:
			return ""
	def cancel():
		os.system("pkill convert")
		os.system("pkill cuneiform")
		
	
	def get_available_languages():
		langs = []
		for line in subprocess.getoutput("cuneiform -l").split("\n"):
			if line.startswith(LANGUAGES_LINE_PREFIX):
				line = line[len(LANGUAGES_LINE_PREFIX):]
				for language in LANGUAGES_SPLIT_RE.split(line):
					if language != "":
						langs.append(language)
		return langs
