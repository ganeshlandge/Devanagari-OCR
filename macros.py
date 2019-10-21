

import os
import itertools

def get_list_of_mixed_case_combinations(list_items):
	return list(itertools.chain.from_iterable([[''.join(a) for a in itertools.product(*zip(s.upper(), s.lower()))] for s in list_items]))

home_dir = os.environ['HOME']

tmp_dir = "/tmp/Lios/"

bookmarks_dir = home_dir+"/lios/bookmarks/"

local_text_cleaner_list_file = home_dir+"/lios/text_cleaner_list.text"

default_text_cleaner_list_file = "/usr/share/lios/text_cleaner_list.text"

preferences_file_path = home_dir+"/lios/lios_preferences"

recent_file_path = home_dir+"/lios/lios_recent"

supported_image_formats = get_list_of_mixed_case_combinations(["png","pnm","jpg","jpeg","tif","tiff","bmp","pbm","ppm"])

supported_text_formats = get_list_of_mixed_case_combinations(["txt","text"])

supported_pdf_formats = get_list_of_mixed_case_combinations(["pdf"])

version = "2.0"

logo_file = "/usr/share/lios/lios.png"


readme_file = "/usr/share/lios/readme.text"

default_text_cleaner_list_file = "/usr/share/lios/text_cleaner_list.text"

app_name = "Linux-intelligent-ocr-solution"

source_link = "https://gitlab.com/Nalin-x-Linux/lios-3"

home_page_link = "http://sourceforge.net/projects/lios/"

video_tutorials_link = "https://www.youtube.com/playlist?list=PLn29o8rxtRe1zS1r2-yGm1DNMOZCgdU0i"

major_character_encodings_list = [ 'us_ascii', 'utf-8', 'iso_8859_1','latin1',
 'iso_8859_2', 'iso_8859_7', 'iso_8859_9', 'iso_8859_15', 'eucjp', 'euckr',
 'gb2312_80', 'gb2312_1980', 'windows_1251', 'windows_1252', 'windows_1253',
 'windows_1254', 'windows_1255', 'windows_1256', 'windows_1257', 'windows_1258',
 'shiftjis', 'windows_1256', 'big5_hkscs', 'big5_tw', 'tis620']
