from modules.base.handler import command, Handler

class TestHandler(Handler):
    @command("test", "Run test command")
    async def test_cmd(self, update, context):
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text="Test command executed"
        )
        return