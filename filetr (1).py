import os
import json
from translation_package.translator_google import TransLate

def read_config(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def process_file(config):
    try:
        with open(config["file"], "r") as file:
            content = file.read()

        if len(content) > config["max_chars"] or len(content.split()) > config["max_words"] or content.count('.') > config["max_sentences"]:
            content = content[:config["max_chars"]]
        
        translated_text = TransLate(content, "auto", config["target_lang"])

        if config["output"] == "screen":
            print(f"Translated text: {translated_text}")
        elif config["output"] == "file":
            output_file = os.path.splitext(config["file"])[0] + "_" + config["target_lang"] + ".txt"
            with open(output_file, "w") as file:
                file.write(translated_text)
            print("Ok")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    config = read_config("config.json")
    process_file(config)
