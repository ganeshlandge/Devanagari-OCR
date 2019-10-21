

import os
import subprocess 
from lios.ocr.ocr_engine_base import OcrEngineBase

class OcrEngineAbbyyFineReader11(OcrEngineBase):
	name = "ABBYY FineReader11"
	
	def __init__(self,language=None):
		self.set_language(language)

	def is_available():
		if ("/bin/abbyyocr11" in subprocess.getoutput("whereis abbyyocr11")):
			return True
		else:
			return False
			
	def ocr_image_to_text(self,file_name):
		os.system("convert {} /tmp/{}_for_ocr.jpg".format(file_name,file_name.split("/")[-1]))
		os.system("abbyyocr11 -if /tmp/{0}_for_ocr.jpg -rl {1} -f TextUnicodeDefaults -tet UTF8 -of /tmp/{1}_output.txt ".format(file_name.split("/")[-1],self.language))
		print("abbyyocr11 -if /tmp/{0}_for_ocr.jpg -rl {1} -f TextUnicodeDefaults -tet UTF8 -of /tmp/{1}_output.txt ".format(file_name.split("/")[-1],self.language))
		os.remove("/tmp/{0}_for_ocr.jpg".format(file_name.split("/")[-1]))
		try:
			with open("/tmp/{0}_output.txt".format(file_name.split("/")[-1]),encoding="utf-8") as file:
				text = file.read().strip()
				os.remove("/tmp/{0}_output.txt".format(file_name.split("/")[-1]))
				return text
		except:
			return ""
	def cancel():
		os.system("pkill convert")
		os.system("pkill abbyyocr11")
		
	
	def get_available_languages():
		langs = ["Abkhaz","Adyghe","Afrikaans","Agul","Albanian","Altaic",
		"Arabic (Saudi Arabia)","Armenian (Eastern, Western, Grabar)","Avar",
		"Aymara","Azerbaijani (Cyrillic, Latin)","Bashkir","Basque","Belarusian",
		"Bemba","Blackfoot","Breton","Bugotu","Bulgarian","Buryat","Catalan",
		"Cebuano","Chamorro","Chechen","Chinese (Simplified, Traditional)",
		"Chukchee","Chuvash","Corsican","Crimean Tatar","Croatian","Crow",
		"Czech","Dakota","Danish","Dargwa","Dungan","Dutch (Netherlands and Belgium)",
		"English","Eskimo (Cyrillic, Latin)","Estonian","Even","Evenki","Faroese",
		"Fijian","Finnish","French","Frisian","Friulian","Gagauz","Galician","Ganda",
		"German (Luxemburg)","German (new and old spelling)","Greek","Guarani",
		"Hani","Hausa","Hawaiian","Hebrew","Hungarian","Icelandic","Indonesian",
		"Ingush","Irish","Italian","Japanese","Jingpo","Kabardian","Kalmyk",
		"Karachay-balkar","Karakalpak","Kasub","Kawa","Kazakh","Khakass",
		"Khanty","Kikuyu","Kirghiz","Kongo","Korean","Korean (Hangul)",
		"Koryak","Kpelle","Kumyk","Kurdish","Lak","Latin","Latvian","Lezgi",
		"Lithuanian","Luba","Macedonian","Malagasy","Malay","Malinke","Maltese",
		"Mansi","Maori","Mari","Maya","Miao","Minangkabau","Mohawk","Moldavian",
		"Mongol","Mordvin","Nahuatl","Nenets","Nivkh","Nogay",
		"Norwegian (Nynorsk and Bokmal)","Nyanja","Occitan","Ojibway","Ossetian",
		"Papiamento","Polish","Portuguese (Portugal and Brazil)","Provencal",
		"Quechua","Rhaeto-romanic","Romanian","Romany","Rundi","Russian",
		"Russian (old spelling)","Rwanda","Sami (Lappish)","Samoan","Scottish Gaelic",
		"Selkup","Serbian (Cyrillic, Latin)","Shona","Slovak","Slovenian",
		"Somali","Sorbian","Sotho","Spanish","Sunda","Swahili","Swazi","Swedish",
		"Tabasaran","Tagalog","Tahitian","Tajik","Tatar","Thai","Tok Pisin",
		"Tongan","Tswana","Tun","Turkish","Turkmen (Cyrillic, Latin)","Tuvinian",
		"Udmurt","Uighur (Cyrillic, Latin)","Ukrainian","Uzbek (Cyrillic, Latin)",
		"Vietnamese","Welsh","Wolof","Xhosa","Yakut","Yiddish","Zapotec","Zulu"]
		return langs
