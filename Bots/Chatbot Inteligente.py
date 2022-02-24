"""
chatterbot

"""
from tkinter import *
from  chatterbot import  ChatBot
from chatterbot.trainers import ListTrainer
import nltk
from nltk.corpus import *
Tk()
"""

#nltk.download('punkt')


from spacy.cli import download
download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'
chatbot = ChatBot("robteste", tagger_language=ENGSM)

INICIANDO O CODIGO

chatbot = ChatBot("Robot")

conversa = [
    "Coe",
    "E ai, tranquilo?",
    "Tranquilo",
    "Qual a boa de hoje?",
    "A Hashtag tá ensinando Python e até chatboot",
    "Maneiro né",
    "Irado"

]
trainer = ListTrainer(chatbot)
trainer.train(conversa)

chatbot.get_response("Coe")
while True:
    mensagem = input("Mande Uma mensagem para o chatbot:")
    if mensagem== "parar":
        break
    resposta = chatbot.get_response(mensagem)
    print("resposta")


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('Robot')

trainer = ListTrainer(chatbot)

trainer.train([
    "Coe",
    "E ai, tranquilo?",
    "Tranquilo",
    "Qual a boa de hoje?",
    "A Hashtag tá ensinando Python e até chatboot",
    "Maneiro né",
    "Irado"
])


# Get a response to the input text 'I would like to book a flight.'
while True:
    mensagem = input("Mande Uma mensagem para o chatbot:")
    if mensagem == "parar":
        break
    #response = chatbot.get_response(mensagem)

    resposta = chatbot.get_response(mensagem)
    print(resposta)
"""
janela = Tk()
janela.title("Robot")

janela.mainloop()