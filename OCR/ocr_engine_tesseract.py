
import os
import subprocess
from lios.ocr.ocr_engine_base import OcrEngineBase

TESSDATA_POSSIBLE_PATHS = [
	"/usr/share/tesseract-ocr/tessdata",
	"/usr/share/tesseract/tessdata",
	"/usr/share/tessdata",
	"/usr/local/share/tesseract-ocr/tessdata",
	"/usr/local/share/tesseract/tessdata",
	"/usr/local/share/tessdata" ]

TESSDATA_EXTENSION = ".traineddata"

class OcrEngineTesseract(OcrEngineBase):
	name = "Tesseract"
	
	def __init__(self,language=None):
		self.set_language(language)

	def is_available():
		if ("/bin/tesseract" in subprocess.getoutput("whereis tesseract")):
			return True
		else:
			return False

	def is_training_executables_available():
		for executable_name in ["combine_tessdata","unicharset_extractor","shapeclustering","mftraining","cntraining","text2image"]:
			if not ("/bin/"+executable_name in subprocess.getoutput("whereis {0}".format(executable_name))):
				return False
		return True

	def ocr_image_to_text(self,file_name):
		os.system("convert {} -background white -flatten +matte /tmp/{}_for_ocr.png".format(file_name,file_name.split("/")[-1]))

		os.system("tesseract /tmp/{0}_for_ocr.png /tmp/{0}_output -l {1}".format(file_name.split("/")[-1],self.language))
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
		os.system("pkill tesseract")
		
	
	def get_available_languages_in_dirpath(dirpath):
		langs = []
		if os.access(dirpath, os.R_OK):
			for filename in os.listdir(dirpath):
				if filename.lower().endswith(TESSDATA_EXTENSION):
					lang = filename[:(-1 * len(TESSDATA_EXTENSION))]
					langs.append(lang)
		return langs

	def get_available_languages():
		langs = []
		for dirpath in TESSDATA_POSSIBLE_PATHS[::-1]:
			if (os.path.isfile(dirpath+"/configs/box.train")):
				for item in OcrEngineTesseract.get_available_languages_in_dirpath(dirpath):
					langs.append(item)
				return sorted(langs)
		return langs

	def get_all_available_dirs():
		result = []
		for root, dirs, files in os.walk("/"):
			if "tessdata" in dirs:
				dir = os.path.join(root, "tessdata")
				if (os.path.isfile(dir+"/configs/box.train")):
					result.append(dir)

		# Sorting according to possible list
		# [::-1] is used to reverse
		for path in TESSDATA_POSSIBLE_PATHS[::-1]:
			if (path in result):
				result.insert(0, result.pop(result.index(path)))
		return result

	def get_available_dirs():
		dir_list = [];
		for path in TESSDATA_POSSIBLE_PATHS:
			if (os.path.exists(path)):
				if (os.path.isfile(path+"/configs/box.train")):
					dir_list.append(path);
		return dir_list;
