import os
import shutil

class WordsLoader:
    def __init__(self):
        self.script_dir = os.path.dirname(os.path.realpath(__file__))
        self.resurse_dir = os.path.join(self.script_dir, 'resurse')


    def load_file(self, file_path):
        if os.path.exists(file_path) and os.path.isfile(file_path):
            shutil.copy(file_path, os.path.join(self.resurse_dir, os.path.basename(file_path)))
        else:
            raise FileNotFoundError(f"File not found at {file_path}")




