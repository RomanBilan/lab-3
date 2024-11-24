from translation_package.translator_google import TransLate, LangDetect, CodeLang, LanguageList

if __name__ == "__main__":
    # Вказуємо джерело мови 'es' для іспанської, щоб уникнути неправильної детекції
    print(TransLate("Hola", "es", "en"))  # Переклад з іспанської на англійську

    # Тестування визначення мови з більшою частиною тексту для кращої точності
    print(LangDetect("Hola, cómo estás?", "all"))  # Краще виявляє іспанську з більшою кількістю тексту

    # Тест функції CodeLang
    print(CodeLang("Spanish"))  # Має повернути 'es'

    # Тест функції LanguageList
    print(LanguageList("screen", "Hola"))
