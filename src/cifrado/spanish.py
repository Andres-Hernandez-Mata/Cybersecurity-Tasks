"""
Uso: Spanish
Creador: Andrés Hernández Mata
Version: 3.5.0
Python: 3.9.1
Fecha: 11 Mayo 2020
"""

import logging
from datetime import datetime
from termcolor import colored

logging.basicConfig(level=logging.INFO, filename="cybersecurity_tasks.log", format="%(asctime)s %(levelname)s:%(message)s")

# Krod Pxqgr
class Spanish:
    
    def load_dictionary(self):
        try:
            dictionary_file = open("cifrado\diccionario.txt", encoding="utf8")    
            spanish_words = {}
            for word in dictionary_file.read().split("\n"):
                word = word.upper()
                spanish_words[word] = None
            dictionary_file.close()
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"])) 

        return spanish_words    

    def get_spanish_count(self, message):
        try:
            detect_spanish = Spanish()
            spanish_words = detect_spanish.load_dictionary()
            message = message.upper() 
            message = detect_spanish.remove_non_letters(message)    
            possible_words = message.split()    
            
            if possible_words == []:
                return 0.0

            matches = 0        
            for word in possible_words:      
                if word in spanish_words:
                    matches += 1
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))

        return float(matches) / len(possible_words)

    def remove_non_letters(self, message):
        try:
            upper_letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÄËÏÖÜ"
            letters_and_space = upper_letters + upper_letters.lower() + ' \t\n'
            letters_only = []
            for symbol in message:
                if symbol in letters_and_space:
                    letters_only.append(symbol)
            
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))
        
        return ''.join(letters_only)

    def spanish(self, message, word_percentage=20, letter_percentage=85):
        try:
            detect_spanish = Spanish()
            words_match = detect_spanish.get_spanish_count(message) * 100 >= word_percentage    
            num_letters = len(detect_spanish.remove_non_letters(message))
            message_letters_percentage = float(num_letters) / len(message) * 100
            letters_match = message_letters_percentage >= letter_percentage
        
        except Exception as error:
            logging.error(error, exc_info=True)
            print(colored("%s [ERROR] Ha ocurrido un error" % datetime.now(), "red", attrs=["bold"]))
            print(colored(error, "red", attrs=["bold"]))

        return words_match and letters_match
