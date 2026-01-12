from .configs import (
    ENV,
    TOKEN,
    ALLOWED_USERS,
)

from .bot import Bot


from modules.test.test import TestHandler

commands = []
handlers = []


test_handler = TestHandler()
cmds, hnds = test_handler.get_handlers()
commands.extend(cmds)
handlers.extend(hnds)

bot = Bot(TOKEN, commands, handlers)
