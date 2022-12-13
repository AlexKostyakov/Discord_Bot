import discord
import random
import time
import threading
mems = ["мем1.jpg", "мем2.jpeg", 'мем3.jpeg', 'мем4.jpeg', 'мем5.jpeg', 'мем6.jpeg', 'мем7.jpg', 'мем8.jpeg', 'мем9.jpg', 'мем10.png', 'мем11.jpg','мем13.jpg', 'мем14.jpeg', 'мем15.jpg']
choiser = mems.copy()
TOKEN = "MTA0NTI4NDg3ODY1NDEyODE2OQ.GzUt9S.qD5EORj5W5v-PWUzXUOnJqLWKqSARc6HkQ6pIs"
intents = discord.Intents.all()
Perm = discord.Permissions.all()
Perm.ban_members = True
Perm.kick_members = True
intents.members = True
intents.message_content = True
client = discord.Client(intents= intents, permissions= Perm)
@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("--------")

@client.event
async def on_message(message):
    channel = message.channel
    a = message.content
    b = random.choice(choiser)
    answers = ["Привет", "Здравствуй", "О, какие люди!","Привет, рад видеть", "Наконец-то ты вернулся!"]
    if "/привет" in a.lower() or "/ха" in a.lower()  or "/здра" in a.lower() or "/салам" in a.lower():
        await channel.send(random.choice(answers))
    if message.content.lower().startswith('/забанить'):
        list = message.content.split()
        for member in client.get_all_members():
            if str(member) == str(list[1]):
                await channel.send(f"{member} был забанен {message.author}")
                await member.ban(reason="Забанен, потому что потому", delete_message_days=1)
    elif message.content.lower().startswith('/кикнуть'):
        list = message.content.split()
        for member in client.get_all_members():
            if str(member) == str(list[1]):
                await channel.send(f"{member} был кикнут {message.author}")
                await member.kick()
    if a.lower().startswith("/очистить"):
        await channel.delete_messages(id("HaHa bot#3956"))

    if a.lower().startswith("/мем"):
        await channel.send(file=discord.File(b))
        choiser.pop(b)
    if True:
        time.sleep(3600)
        b = random.choice(choiser)
        await channel.send(file=discord.File(random.choice(mems)))
        choiser.pop(b)
threading.Timer(10000000.0, on_message).start()
client.run(TOKEN)
