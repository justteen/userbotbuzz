from pyrogram import Client, idle

app = Client("tgvc")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT MULAI')
idle()
app.stop()
print('\n>>> USERBOT BERHENTI')
