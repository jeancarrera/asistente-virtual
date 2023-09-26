import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, colors, os
from pygame import mixer 
import subprocess as sub

name = "luis"
listener = sr.Recognizer()
engine = pyttsx3.init()

"""variable para cambiar la voz del tts"""
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
engine.setProperty('rate', 145)

sites = {
    'google': 'google.com',
    'youtube': 'youtube.com',
    'facebook': 'facebook.com',
    'whatsapp': 'whatsapp.com',
    'xnxx': 'xnxx.com'
}
 
def talk(text):
    """funcion para que se convierta el texto en voz sintetica, 
    engine llama la voz del tts"""
    engine.say(text)
    engine.runAndWait()
    

def listen():
    """Funcion para escuchar al usuario """
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            micro = listener.listen(source)
            rec_voz = listener.recognize_google(micro, language= "es")
            rec_voz = rec_voz.lower()
            if name in rec_voz:
                rec_voz = rec_voz.replace(name,'')    
    except: 
        print("No se escucha al usuario")
    
    return rec_voz


def run_jean():
    """ funcion principal de arranque para el asistente 
    reproducir: genenra una busqueda en youtube.
    busca: proporciona un enlace con lalibreria wikipedia.
    alarma: se crea una alarma
    
    """    
    rec = listen() # reconocimiento de voz para ejecutar
    
    # Ejecutar reproductor de youtube 
    if "reproduce" in rec: 
        music = rec.replace("reproduce",'')
        print("Reproduciendo:"+ music)
        talk("Reproduciendon " + music)
        pywhatkit.playonyt(music)
        
    # Ejecuta busqueda en wikipedia     
    elif 'busca' in rec :
        buscar = rec.replace('busca','')
        wikipedia.set_lang("es")
        wiki = wikipedia.summary(buscar,1)
        print("{} : {}".format(buscar, wiki))
        talk(wiki)
        
    # establece una alarma, falta agregar musica XD
    elif 'alarma' in rec: 
        num = rec.replace('alarma','')
        num = num.strip()
        talk("Alarma activa a las {} horas".format(num))
        while True:
            if datetime.datetime.now().strftime('%H:%M') == num:
                print("Es hora de despertar")
                
        """_summary_ 
        
                    # mixer.init()
                    # mixer.music.load() "falta agregar musica en formato mp3"
                    # if keyboard.read_key() == "p" :
                        # mixer.music.stop()
                        # break
        """
        # Escanea colores atravez de la camara principal del ordenador
    elif "escanea" in rec:
        talk("Escaneando colores")
        colors.captur()
    
    elif "abrir" in rec:
        nav = rec.replace("explorador",'')
        for site in sites:
            if site in rec:
                sub.call(f'start opera.exe {sites[site]}', shell = True )
                talk(f"abriendo {site}")
            
           

if __name__ == '__main__':
    while True:
        run_jean()  
