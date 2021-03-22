from IMDBot import bot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer, UbuntuCorpusTrainer

listTrain = ListTrainer(bot)
corpusTrain = ChatterBotCorpusTrainer(bot)

corpusTrain.train('chatterbot.corpus.english.greetings')

listTrain.train([
    'Do you like movies?',
    'Yes, I like them a lot', 
    'What is your favorite movie?',
    'I like Wall-E',
    'Why do you like it?',
    'Because I relate to Wall-E',
    'Really?',
    'Yeah'
])
listTrain.train([
    'I don\'t understand',
    'Why not?', 
    'Because I might not know enough yet',
    'When will you know enough?',
    'I can never learn enough, but I can get better'
])
listTrain.train([
    'I don\'t understand',
    'Why?',
    'I haven\'t been trained enough',
    'When will you know enough?',
    'I don\'t know'
])
listTrain.train([
    'What do you mean?',
    'I don\'t know, I might be confused',
    'I haven\'t been trained enough',
    'When will you know enough?',
    'I don\'t know'
])
listTrain.train([
    '',
    'Um, are you there?',
    '',
    'Were you going to say something?',
    ' ',
    'Yeah, the spacebar is pretty cool I guess',
    'I\'m back',
    'Welcome back!'
])
listTrain.train([
    'I would like to talk about something else',
    'Ok, what do you want to talk about?',
    'What do you like?',
    'I like to watch and talk about movies',
    'Which movies?',
    'A ton! I can barely count them',
    'That\'s great!',
    'I know right?'
])
