from translation_package.translator_deep import TransLate, LangDetect, CodeLang, LanguageList

def main():
    try:
        # Test TransLate function: Translate "Hello" from auto-detected language to Spanish
        translated_text = TransLate("Hello", "auto", "es")
        print(f"Translated Text: {translated_text}")

        # Test LangDetect function: Detect language of "Hello"
        detected_lang = LangDetect("Hello", "all")
        print(f"Detected Language: {detected_lang}")

        # Test CodeLang function: Get code for "Spanish"
        lang_code = CodeLang("Spanish")
        print(f"Language Code for Spanish: {lang_code}")

        # Test LanguageList function: Display language table and translate "Hello"
        language_list_result = LanguageList("screen", "Hello")
        print(f"Language List Result: {language_list_result}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
