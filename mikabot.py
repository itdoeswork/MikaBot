import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
import json
from discord import Game



Client = discord.Client()
client = commands.Bot(command_prefix = "-")


        
@client.event
async def on_ready():
    print("MikaBot is ready to fight!")
    await client.change_presence(game=Game(name="with Angel<3//-help"))
    
              
@client.event
async def on_message(message):   
    if message.author == client.user:
        return
    if message.content.upper().startswith("-INFO"):
        embed = discord.Embed(title="MikaBot", description="The cutest bot on discord! ^-^", color=0x7f1ae5)
        embed.add_field(name="Owner", value="angel#9928", inline=False)
        await client.send_message(message.channel, embed=embed)
        
    if message.content.upper().startswith("-HELP"):
        embed = discord.Embed(title="Hi I'm MikaBot! ^-^", description="These are my commands:", color=0x7f1ae5)
        embed.add_field(name="-help", value="uh.. you should know what this does.. you just gave the command..", inline=False)
        embed.add_field(name="-info", value="gives you basic info about me!", inline=False)
        embed.add_field(name="-hello", value="Say hi to me!", inline=False)
        embed.add_field(name="-bye", value="Say good bye!", inline=False)
        embed.add_field(name="-night", value="Tell me good night!", inline=False)
        embed.add_field(name="-morning", value="Tell me good morning!", inline=False)
        embed.add_field(name="-hug @user", value="Hug someone! ^-^", inline=False)
        embed.add_field(name="-secret hug @user", value="Hug someone secretly!", inline=False)
        embed.add_field(name="-love @user", value="Declare your love!", inline=False)
        embed.add_field(name="-secret love @user", value="Declare your live in secrecy, I won't tell ^-^", inline=False)
        embed.add_field(name="-fight me", value="Challenge me to a fight", inline=False)
        embed.add_field(name="-duel @user", value="Challenge someone else to a fight", inline=False)
        embed.add_field(name="-dance off @user", value="If figting is not your style, challenge your opponent to a dance battle", inline=False)
        embed.add_field(name="-shame @user", value="Shame someone!", inline=False)
        embed.add_field(name="-say (message)", value="Get me to repeat your words!", inline=False)
        embed.add_field(name="-add quote (message)", value="add a quote to The List of Quotes!", inline=False)
        embed.add_field(name="-quote", value="Pull a random quote from The List of Quotes!", inline=False)
        embed.add_field(name="-ask mika (message)", value="Ask me a question! I'm a psychic you know.", inline=False)
        embed.add_field(name="-what should I draw", value="I'll give you a prompt", inline=False)
        embed.add_field(name="-mika pic", value="Gives you a random mika pic", inline=False)
        embed.add_field(name="-coin", value="Flip a coin!", inline=False)
        embed.add_field(name="-ping", value="Pong?", inline=False)
        embed.add_field(name="-does mika approve?", value="Does she??", inline=False)
        embed.add_field(name="-pointless", value="Press The Pointless Button!", inline=False)
        await client.send_message(message.author, embed=embed)
                                  
                                                 
 
    if message.content.upper().startswith("-MIKA PIC"):
         my_path = r"C:\Users\Melek\Pictures\mika"      
         choice = os.path.join(my_path, random.choice(os.listdir(my_path))) 
         await client.send_message(message.channel, choice)
         
    if message.content.upper().startswith("I KIN MIKA"): 
         await client.send_message(message.author, "don't kin me. you furry.")
         
    if message.content.upper().startswith("ANGEL SUCKS"): 
         await client.send_message(message.author, "angel doesn't suck. you do.")
         
    if message.content.upper().startswith("I AM GAY"): 
         await client.send_message(message.author, "Angel is the gayest")
    
    
         
    if message.content.upper().startswith("-HELLO"):
        msg = " {0.author.mention}".format(message)
        await client.send_message(message.channel, random.choice(["hi, hi, hi",
                                                                     "sup",
                                                                     "Meowello ",
                                                                     "Heyo",
                                                                     "hi",
                                                                     "yo.",
                                                                     "wasssup",
                                                                     "why, hello",
                                                                     "meow??",
                                                                     "did you bring tuna",
                                                                     "hey",
                                                                     "I'd say hi, but I'm busy doing.. uh catstuff? botstuff? what am I?",
                                                                     "Did ya miss me",
                                                                     "meow!",
                                                                     "hello",])+ msg +"  "+"^-^" )
    if message.content.upper().startswith("-BYE"):
        msg = " {0.author.mention}".format(message)
        await client.send_message(message.channel, random.choice(["bye",
                                                                     "goodbye",
                                                                     "I'll miss you",
                                                                     "meow",
                                                                     "meow??",
                                                                     "see ya!",
                                                                     "come back soon!",
                                                                     "take care",
                                                                     "buh-bye friend",
                                                                     "remember to close the god damn door",])+ msg +"  "+"^-^" )
    if message.content.upper().startswith("-MORNING"):
        msg = " {0.author.mention}".format(message)
        await client.send_message(message.channel, random.choice(["good morning",
                                                                     "meow",
                                                                     "too early",
                                                                     "I need another nap",])+ msg +"  "+"^-^" )
    if message.content.upper().startswith("-NIGHT"):
        msg = " {0.author.mention}".format(message)
        await client.send_message(message.channel, random.choice(["good night",
                                                                     "nighty",
                                                                     "sweet dreams",
                                                                     "nighty night",
                                                                     "don't let the shadows get you",
                                                                     "see you in the morning",])+ msg +"  "+"^-^" )      
    if message.content.upper() == "-FIGHT ME":
                await client.send_message(message.channel, random.choice([":fencer:",
                                                                          "come at me bro :fencer:",
                                                                          "can you beat me in a dance competition? :man_dancing:",
                                                                          "you're not a worthy opponent.",
                                                                          "IT'S TIME TO D-D-D-D-D-D-DUEL!:fencer:"
                                                                          "Sasuke? is that you?",
                                                                          "bring it! :fencer:",
                                                                          "While you were busy playing with bots, I studied the blade :fencer:",
                                                                          "silly mortal :fencer:",
                                                                          ":fencer: :fencer: :fencer:",
                                                                          ":fencer: :fencer: :fencer:",
                                                                          ":fencer: :fencer: :fencer:",
                                                                          "I have seen all of naruto. you can't defeat me :fencer:",
                                                                          ":fencer: :fencer: :fencer:",]))
    if message.content.upper().startswith("-PING"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith("-SAY"):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" %(" ".join(args[1:])))
    if message.content.upper() == "-POINTLESS":
        if message.author.id == "343160195075276801":
            await client.send_message(message.channel, "pointless button has been pressed")
        else:
            await client.send_message(message.channel, "thou shall not press the button!")
    if message.content.upper().startswith("-DOES MIKA APPROVE"):
        if "453616927554797578" in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, "you are Mikapproved! ^-^")
        else:
            await client.send_message(message.channel, "you are NOT Mikapproved yet! >.<'")
        
    if message.content.upper().startswith("-ADD QUOTE"):
        if not os.path.isfile("quote_file.pk1"):
            quote_list = []
        else:
            with open("quote_file.pk1", "r") as quote_file:
                quote_list = json.load(quote_file)
        quote_list.append(message.content[10:])
        with open("quote_file.pk1", "w") as quote_file:
                json.dump(quote_list , quote_file)
    if message.content.upper().startswith("-QUOTE"):
        with open("quote_file.pk1", "r") as quote_file:
            quote_list = json.load(quote_file)
        await client.send_message(message.channel, random.choice(quote_list))
    if message.content.upper().startswith("-SHAME"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s> " % (userID)
            rec = " {}".format(user.mention)
            await client.send_message(message.channel, auth + "shames" + rec + ":face_palm:")
        
            
        
    if message.content.upper() == "-CAN I KIN MIKA":
        await client.send_message(message.channel, "beGONE furry :fencer:")
    if message.content.upper().startswith("-HUG"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s> " % (userID)
            rec = " {}".format(user.mention)
            await client.send_message(message.channel, auth + random.choice(["hugs",
                                                                     "embraces",
                                                                     "super hugs",
                                                                     "cuddles",
                                                                     "wants to hold",
                                                                     "wants a hug from",
                                                                     "wishes to be held by",
                                                                     "hugs and hugs and hugs and HUGS",
                                                                     "wishes to hug ",
                                                                     "fucking hugs",]) + rec + ":turtle:")
    
        
    if message.content.upper().startswith("-SECRET HUG"):
        for user in message.mentions:
            msg = "Someone has hugged {}".format(user.mention)
            await client.send_message(message.channel,  msg + ". " + random.choice(["was it you Ashe?",
                                                                     "I wonder who it was.",
                                                                     "hmm",
                                                                     "interesting...",
                                                                     "...",
                                                                     "   ",
                                                                     "   ",
                                                                     "   ",               
                                                                     "Zoinks!",]) + ":ghost:")
    if message.content.upper().startswith("-LOVE"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s> " % (userID)
            rec = " {}".format(user.mention)
            await client.send_message(message.channel, ":heart:" + auth + random.choice(["loves",
                                                                     "adores",
                                                                     "will never fight",
                                                                     "wants to be with",
                                                                     "appreciates",
                                                                     "stands by",
                                                                     "is obsessed with",
                                                                     "is really into",
                                                                     "wishes to stargaze with",
                                                                     "wants to hold",
                                                                     "wants to be loved by",
                                                                     "would never anime betray",]) + rec + ":heart:")
    if message.content.upper().startswith("-SECRET LOVE"):
        for user in message.mentions:
            msg = "Someone secretly loves {}".format(user.mention)
            await client.send_message(message.channel,  msg + ". " + random.choice(["was it you John?",
                                                                     "ooh la la!",
                                                                     "hmm..hmm..",
                                                                     "OOF",
                                                                     "...",
                                                                     "   ",
                                                                     "   ",
                                                                     "   ",
                                                                     "wompety womp!",]) + ":thinking:")
    if message.content.upper().startswith("-FIGHT"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s>" % (userID)
            msg = "wants to fight {}".format(user.mention)
            await client.send_message(message.channel, auth + " " + msg + ":fencer:")

    if message.content.upper().startswith("-DANCE OFF"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s>" % (userID)
            msg = "challenges {}".format(user.mention)
            await client.send_message(message.channel, auth + " " + msg + "  " + "to a dance battle" + "  " + random.choice([":man_dancing:",
                                                                                                                             ":dancer:",
                                                                                                                             ":dancers:",]))
            
    if message.content.upper().startswith("-DUEL"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s>" % (userID)
            msg = "challenges {}".format(user.mention)
            await client.send_message(message.channel, auth + " " + msg + "  "+ "to a d-d-d-d-d-duel" + ":fencer:")
            
    if message.content.upper().startswith("-ASK MIKA"):
            await client.send_message(message.channel, random.choice(["Maybe? idk. Now that I think about it, this thing may be broken. NEXT!:8ball:",
                                                                     "Certainly. :8ball:",
                                                                     "Yes. I'd even bet one of my 9 lives on it. :8ball:",
                                                                     "Not a chance. nope. :8ball:",
                                                                     "The chance of a reality star becoming a president is higher- oh wait :8ball:",
                                                                     "I think it's possible... :8ball:",
                                                                     "no. :8ball:",
                                                                     "Ask again later. I'm tired. Gotta take a cat nap... :8ball:",
                                                                     "womp :8ball:",
                                                                     "Honestly, at this point. I don't even care :8ball:",
                                                                     "Nah :8ball:",
                                                                     "Depends on how many cans of tuna you are willing to spend on the right answer :8ball:",
                                                                     "Yep :8ball:",
                                                                     "Do you want my honest answer, or my nice answer? :8ball:",
                                                                     "Ask yourself! :8ball:",]))
            
    if message.content.upper().startswith("-COIN"):
         await client.send_message(message.channel, random.choice(["Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "Heads",
                                                                     "Tails",
                                                                     "it landed on the side! :O!",]))
    if message.content.upper().startswith("-WHAT SHOULD I DRAW"):
         await client.send_message(message.channel, ":paintbrush: " + random.choice(["A man",
                                                                     "a woman",
                                                                     "a teenager",
                                                                     "a child",
                                                                     "a baby",
                                                                     "a firefighter",
                                                                     "a princess",
                                                                     "a mermaid",
                                                                     "a dragon",
                                                                     "a cheerleader",
                                                                     "a furry",
                                                                     "an emo",
                                                                     "a vampire",
                                                                     "a lion",
                                                                     "a hunter",
                                                                     "a knight",
                                                                     "an alien",
                                                                     "a cowboy",
                                                                     "an anime character",
                                                                     "a cat",
                                                                     "a dog",
                                                                     "a teacher",
                                                                     "a salesperson",
                                                                     "a rockstar",
                                                                     "a rebel",
                                                                     "a ninja",
                                                                     "a samurai",
                                                                     "a body builder",
                                                                     "a doctor",
                                                                     "a monkey",]) + " wearing " + random.choice(["a hat ",
                                                                                                               "a snazzy jacket ",
                                                                                                               "a leather skirt ",
                                                                                                               "a cowboy hat ",
                                                                                                               "a cool cape ",
                                                                                                               "a pair of clown shoes ",
                                                                                                               "chain mail armor ",
                                                                                                               "a little backpack ",
                                                                                                               "a pair of skinny jeans ",
                                                                                                               "a summer dress ",
                                                                                                               "a fursuit ",
                                                                                                               "heavy eyeliner ",
                                                                                                               "an anime-like hairstyle ",
                                                                                                               "a vest ",
                                                                                                               "nothing ",
                                                                                                               "a giant poofy jacket ",]) + "while " + random.choice(["dancing ",
                                                                                                                                                        "fighting robots ",
                                                                                                                                                        "giving a speech ",
                                                                                                                                                        "watching anime ",
                                                                                                                                                        "eating fruits ",
                                                                                                                                                        "a pair of clown shoes ",
                                                                                                                                                        "hunting evil zombies ",
                                                                                                                                                        "chilling with friends ",
                                                                                                                                                        "studying ",
                                                                                                                                                        "baking a cake ",
                                                                                                                                                        "hanging out with puppies ",
                                                                                                                                                        "playing the guitar ",
                                                                                                                                                        "stargazing ",
                                                                                                                                                        "drawing ",
                                                                                                                                                        "playing a game ",
                                                                                                                                                        "having a picnic ",]) + "at " + random.choice(["the cinema",
                                                                                                                                                                                          "the park",
                                                                                                                                                                                          "at a concert",
                                                                                                                                                                                          "the opening of a mountain cave",
                                                                                                                                                                                          "the graveyard",
                                                                                                                                                                                          "home",
                                                                                                                                                                                          "the zoo",
                                                                                                                                                                                          "a furry convention",
                                                                                                                                                                                          "a furry convention",
                                                                                                                                                                                          "a party",
                                                                                                                                                                                          "school",
                                                                                                                                                                                          "a friends' house",
                                                                                                                                                                                          "the beach",
                                                                                                                                                                                          "the mall",
                                                                                                                                                                                          "the department store",
                                                                                                                                                                                          "a playground",]) + " :paintbrush:")
         




    

     
client.run(process.env.BOT_TOKEN):
