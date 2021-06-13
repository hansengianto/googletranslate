from google_trans_new import google_translator
from os import system

cls = lambda: system('cls')

cls()
print("Simple Language Translator\n")

result_text = """==================================
>> Simple Language Translator <<

Result : {}

To Exit Program, Click CTRL+C
=================================="""


def translate():
	language_destination = str(input("Input Language Destination : "))
	text_to_translate = str(input("Input Text To Translate : "))

	translator = google_translator()
	translate_text = translator.translate(text_to_translate,lang_tgt=language_destination)  
	cls()
	print(result_text.format(translate_text))
while True:
	translate()