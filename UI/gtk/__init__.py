
from lios.ui.ui_base import OcrEngineBase
from lios.ui.ui_gtk import OcrEngineCuneiform

def get_available_ui_engines():
	list = []
	for item in OcrEngineBase.__subclasses__():
		if item.is_available():
			list.append(item)
	return list
