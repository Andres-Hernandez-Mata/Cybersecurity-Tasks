"""
Uso: Spanish
Creado: Andrés Hernández Mata
Version: 1.1.0
Python: 3.9.1
Fecha: 11 Mayo 2020
"""

class Spanish:
    
    upper_letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÄËÏÖÜ"
    letters_and_space = upper_letters + upper_letters.lower() + ' \t\n'

    def load_dictionary():    
        dictionary_file = open("cifrado\spanish.txt", encoding="utf8")    
        spanish_words = {}
        for word in dictionary_file.read().split("\n"):
            word = word.upper()
            spanish_words[word] = None
        dictionary_file.close()
        return spanish_words

    spanish_words = load_dictionary()

    def get_spanish_count(self, message):
        message = message.upper()    
        message = remove_non_letters(message)    
        possible_words = message.split()    
        
        if possible_words == []:
            return 0.0

        matches = 0
        for word in possible_words:        
            if word in spanish_words:
                matches += 1
        return float(matches) / len(possible_words)

    def remove_non_letters(self, message):
        letters_only = []
        for symbol in message:
            if symbol in letters_and_space:
                letters_only.append(symbol)
        return ''.join(letters_only)

    def spanish(self, message, word_percentage=20, letter_percentage=85): 
        words_match = get_spanish_count(message) * 100 >= word_percentage    
        num_letters = len(remove_non_letters(message))
        message_letters_percentage = float(num_letters) / len(message) * 100
        letters_match = message_letters_percentage >= letter_percentage
        return words_match and letters_match
