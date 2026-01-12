from telegram import BotCommand
from telegram.ext import CallbackQueryHandler, MessageHandler
from telegram.ext._handlers.commandhandler import CommandHandler


def command(cmd, description, filter=None):
    def decorator(func):
        func.decorator_type = "command"
        func.cmd = cmd
        func.description = description
        func.filter = filter
        return func

    return decorator


def callback(pattern, filter=None):
    def decorator(func):
        func.decorator_type = "callback"
        func.pattern = pattern
        func.filter = filter
        return func

    return decorator


def message(filter):
    def decorator(func):
        func.decorator_type = "message"
        func.filter = filter
        return func

    return decorator


class Handler:
    commands = []
    handlers = []

    def get_handlers(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and hasattr(attr, "decorator_type"):
                if attr.decorator_type == "command":
                    self.commands.append(BotCommand(attr.cmd, attr.description))
                    self.handlers.append(
                        CommandHandler(attr.cmd, attr, filters=attr.filter)
                    )

                elif attr.decorator_type == "callback":
                    self.handlers.append(
                        CallbackQueryHandler(
                            attr, pattern=attr.pattern, filters=attr.filter
                        )
                    )

                elif attr.decorator_type == "message":
                    self.handlers.append(
                        MessageHandler(filters=attr.filter, callback=attr)
                    )

        return self.commands, self.handlers