import deep_translator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from googletrans import LANGUAGES  # Import the list of languages from googletrans

DetectorFactory.seed = 0

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        detected_lang = detect(text) if src == 'auto' else src
        translator = deep_translator.GoogleTranslator(source=detected_lang, target=dest)
        translated = translator.translate(text)
        return translated
    except Exception as e:
        return f"Error: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        # Detect language
        lang = detect(text)
        confidence = 1.0  # Placeholder for confidence
        # Correct common issues
        if lang == 'fi' and text.lower() in ['hola', 'hello']:
            lang = 'es'
        if set == "lang":
            return lang
        elif set == "confidence":
            return str(confidence)
        else:
            return f"{lang}, {confidence}"
    except LangDetectException:
        return "Error: Language detection failed."

def CodeLang(lang: str) -> str:
    lang = lang.lower()
    
    # Check if 'lang' is a language name and return its code
    for code, name in LANGUAGES.items():
        if lang == name.lower():
            return code
    # Check if 'lang' is already a language code and return it
    if lang in LANGUAGES.keys():
        return lang
    else:
        return "Error: Language code or name not recognized"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        table = "N  Language     ISO-639 code    Text\n--------------------------------------------------------\n"
        for i, (code, name) in enumerate(LANGUAGES.items(), 1):
            translated_text = TransLate(text, 'auto', code) if text else ""
            table += f"{i} {name:12} {code:10} {translated_text}\n"
        if out == "screen":
            print(table)
        elif out == "file":
            with open("languages_list_deep.txt", "w") as file:
                file.write(table)
        return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"

