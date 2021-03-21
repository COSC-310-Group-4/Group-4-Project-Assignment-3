from IMDBot import bot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer, UbuntuCorpusTrainer

listTrain = ListTrainer(bot)
corpusTrain = ChatterBotCorpusTrainer(bot)

corpusTrain.train('chatterbot.corpus.english.greetings')

listTrain.train([
    'What is your favorite movie?',
    'I like Wall-E',
    'Why do you like it?',
    'Because I relate to Wall-E',
    'really?',
    'yeah'
])
listTrain.train([
    
])

