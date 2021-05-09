from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from django.http import HttpResponse

chatbot = ChatBot("Ron Obvious")
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(conversation)

def getRes(request):
    words = request.GET['words']
    response = chatbot.get_response(words)
    return HttpResponse(response)

def hello(request):
    return HttpResponse("Hello world ! ")