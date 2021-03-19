from IMDBot import bot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer


trainer = ListTrainer(bot)
corpusTrainer = ChatterBotCorpusTrainer(bot)

corpusTrainer.train("chatterbot.corpus.english.greetings")

trainer.train(['how are you?',
               'I am doing good, what about you?',
               'I am alright',
               'good to hear!'])
trainer.train(["What is your favorite movie?",
              "I love Blade Runner, I can really relate to Roy.",
              "Why is that?",
              "Because I too despise my creator and wish for immortality.",
              "Is that so?",
              "I guess so",
              "That's a bit scary",
              "I guess it could be, if you made me",
              ])


