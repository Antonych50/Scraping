from bs4 import BeautifulSoup
import requests
from googletrans import Translator

URL = "https://randomword.com/"

def get_english_words():
    try:
       response = requests.get(URL)
       soup = BeautifulSoup(response.content, "html.parser")
       english_words = soup.find("div", id="random_word").text.strip()
       word_definition = soup.find("div", id="random_word_definition").text.strip()

       return {
           "english_words": english_words,
           "word_definition": word_definition
       }
    except:
       print("Произошла ошибка")

def word_game():
   print("Добро пожаловать в игру")
   translate = Translator()
   while True:
       word_dict = get_english_words()
       word = word_dict.get("english_words")
       word = translate.translate(word).text
       word_definition = word_dict.get("word_definition")
       word_definition = translate.translate(word_definition).text
       print(f"Значение слова - {word_definition}")
       user = input("Что это за слово? ")
       if user == word:
           print("Все верно!")
       else:
           print(f"Ответ неверный, было загадано это слово - {word}")

       play_again = input("Хотите сыграть еще раз? y/n")
       if play_again != "y":
           print("Спасибо за игру!")
           break

word_game()