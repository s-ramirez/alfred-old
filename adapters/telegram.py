from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class TelegramAdapter:
    def __init__(self, token, classifier):
        self.classifier = classifier
        self.updater = Updater(token)

        self.dispatcher = self.updater.dispatcher
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(MessageHandler(Filters.text, self.respond))

        self.dispatcher.add_error_handler(self.error)

    def start(self, bot, update):
        update.message.reply_text("Hello, master.")

    def respond(self, bot, update):
        response = self.classifier.classify(update.message.text)
        update.message.reply_text(response)

    def error(self, bot, update, error):
        print('Update "%s" caused error "%s"' % (update, error))

    def start_listening(self):
        self.updater.start_polling()
        # self.updater.idle()
