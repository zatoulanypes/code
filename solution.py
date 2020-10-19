from nltk import word_tokenize

class FileReader:

    def __init__(self, path):
        self.path = path
        
    def __str__(self):
        return self.path

    def __add__(self, file):
        new_file = self.read + file.read
        with open('concat_file.txt', 'w') as f:
            f.write(new_file)
        return FileReader('concat_file.txt')
        
    def read(self):
      try:
        with open(self.path, 'r') as file:
          return file.read()
      except FileNotFoundError:
          return ''

    def count(self):
        self.line_count = len([str for str in self.read()])
        self.word_count = len(word_tokenize(self.read()))
