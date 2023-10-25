import os
import re

class Check:
    def __init__(self, languages=None, all=False):
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        self.language_files = self.initialize_language_files()

        if not languages:
            languages = ['ru']

        if all:
            languages = list(self.language_files.keys())

        self.bad_words = self.initialize_bad_words(languages)
        self.patterns = self.compile_patterns()

    def initialize_language_files(self):
        language_files = {}
        resurse_dir = os.path.join(self.script_dir, 'resurse')
        for filename in os.listdir(resurse_dir):
            language_code = os.path.splitext(filename)[0]
            file_path = os.path.join(resurse_dir, filename)
            language_files[language_code] = file_path
        return language_files

    def initialize_bad_words(self, languages):
        bad_words = {}
        for language in languages:
            file_path = self.language_files.get(language)
            if file_path is not None:
                with open(file_path, 'r', encoding='utf-8') as file:
                    bad_words[language] = [line.strip() for line in file]
        return bad_words
    
    def compile_patterns(self):
        patterns = {}
        for language, words in self.bad_words.items():
            patterns[language] = re.compile(r'\b(?:' + '|'.join(re.escape(word) for word in words) + r')\b', re.IGNORECASE)
        return patterns
    
    def filter_profanity(self, text, language='ru'):
        if language not in self.language_files:
            raise ValueError(f'Unsupported language: {language}')
        if language not in self.patterns:
            return False

        if self.patterns[language].search(text):
            return True
        return False