

from lios.ocr.ocr_engine_base import OcrEngineBase
from lios.ocr.ocr_engine_cuneiform import OcrEngineCuneiform
from lios.ocr.ocr_engine_tesseract import OcrEngineTesseract
from lios.ocr.ocr_engine_ocrad import OcrEngineOcrad
from lios.ocr.ocr_engine_gocr import OcrEngineGocr
from lios.ocr.ocr_engine_abbyy_finereader11 import OcrEngineAbbyyFineReader11
from lios.ocr.ocr_engine_abbyy_finereader9 import OcrEngineAbbyyFineReader9

def get_available_engines():
	list = []
	# Note : The engine classes should be sorted otherwise each time this function
	# will return same engine list in a random order.  
	for engine_name in ["Tesseract","Cuneiform","ABBYY FineReader9","ABBYY FineReader11",
						"Gocr", "Ocrad" ]:
		for item in OcrEngineBase.__subclasses__():
			if (item.name == engine_name and item.is_available()):
				list.append(item)
	
	import operator
	return list


