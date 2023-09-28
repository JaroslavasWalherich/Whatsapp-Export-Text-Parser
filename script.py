import re
import pandas as pd
import nltk
from nltk.corpus import stopwords

class TextCleaner:
    def __init__(self, text):
        self.text = text

    def remove_patterns(self, regex_patterns):
        for pattern in regex_patterns:
            self.text = re.sub(pattern, "", self.text)

    def remove_sentences(self, sentences_to_delete):
        for sentence in sentences_to_delete:
            self.text = self.text.replace(sentence, "")

    def remove_blank_lines(self):
        self.text = "\n".join(line for line in self.text.splitlines() if line.strip())

    def to_lower(self):
        self.text = self.text.lower()

    def remove_emojis(self):
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"
            u"\U0001F300-\U0001F5FF"
            u"\U0001F680-\U0001F6FF"
            u"\U0001F700-\U0001F77F"
            u"\U0001F780-\U0001F7FF"
            u"\U0001F800-\U0001F8FF"
            u"\U0001F900-\U0001F9FF"
            u"\U0001FA00-\U0001FA6F"
            u"\U0001FA70-\U0001FAFF"
            u"\U0001F004-\U0001F0CF"
            u"\U0001F170-\U0001F251"
            "]+", flags=re.UNICODE)
        
        # Remove emojis
        self.text = emoji_pattern.sub(r'', self.text)

        # Remove empty lines
        self.text = '\n'.join(line for line in self.text.splitlines() if line.strip())

    def remove_arabic_stopwords(self):
        arabic_stopwords = set(stopwords.words("arabic"))
        lines = self.text.splitlines()
        cleaned_lines = []

        for line in lines:
            words = line.split()
            cleaned_words = [word for word in words if word not in arabic_stopwords]
            cleaned_lines.append(" ".join(cleaned_words))

        self.text = "\n".join(cleaned_lines)

def read_patterns_and_sentences(patterns_file, sentences_file):
    try:
        with open(patterns_file, "r", encoding="utf-8") as patterns_file:
            regex_patterns = [line.strip() for line in patterns_file.readlines()]

        with open(sentences_file, "r", encoding="utf-8") as sentences_file:
            sentences_to_delete = [line.strip() for line in sentences_file.readlines()]

        return regex_patterns, sentences_to_delete
    except FileNotFoundError:
        print("Error: Patterns or sentences file not found.")
        return [], []

def main():
    input_file = "input.txt"
    output_csv_file = "output.csv"
    patterns_file = "patterns.txt"
    sentences_file = "sentences.txt"

    regex_patterns, sentences_to_delete = read_patterns_and_sentences(patterns_file, sentences_file)

    try:
        with open(input_file, "r", encoding="utf-8") as input_file:
            text = input_file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    if text:
        text_cleaner = TextCleaner(text)
        text_cleaner.remove_patterns(regex_patterns)
        text_cleaner.remove_sentences(sentences_to_delete)
        text_cleaner.remove_blank_lines()
        text_cleaner.to_lower()
        text_cleaner.remove_emojis()
        text_cleaner.remove_arabic_stopwords() 

        # Save the cleaned text to a file
        with open(output_csv_file, "w", encoding="utf-8") as output_file:
            output_file.write(text_cleaner.text)

if __name__ == "__main__":
    main()
