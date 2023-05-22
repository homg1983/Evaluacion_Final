import speech_recognition as SR
import pyttsx4
import pywhatkit
import datetime
import cv2
import wikipedia
import webbrowser

# Tener un nombre a través del cual se llama y recibe las órdenes.
name = 'alexa'

# Reconocer comandos por voz y convertirlos a texto para su posterior procesamiento.
listener = SR.Recognizer()
engine = pyttsx4.init()

def hablar (texto):
    engine.say(texto)
    engine.runAndWait()

# Convertir texto a voz.
def listen():
    try:
        with SR.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-ES")
            rec  = rec.lower()
            if name in rec:
                rec = rec.replace(name, ' ')
                hablar(rec)
    except:
          pass
    return rec

# Reproducir un video Youtube.
def run():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace(' ', ' ')
        hablar ('Con gusto. Reproduciendo...')
        pywhatkit.playonyt(music)

#   Responder cuándo se le pregunte por la hora actual.
    elif  'hora' in rec:
        hora = rec.replace(' ', ' ')
        hora = datetime.datetime.now().strftime('%H:%M')
        hablar("La hora actual es. "+ hora)
        
# Buscar cualquier información en Wikipedia.
    elif 'wikipedia' in rec:
        orden = rec.replace('wikipedia', ' ')
        wikipedia.set_lang("es")
        info = wikipedia.summary(orden, 2)
        hablar(info)
        
# Abrir la página de Google.
    elif 'google' in rec:
        hablar('Con gusto. Abriendo google')
        webbrowser.open('https://www.google.com/?hl=es')
        
# Tomar una foto.
    elif 'foto' in rec:
        hablar("Con mucho gusto")
        cap = cv2.VideoCapture(0)
        hablar("Estoy preparando la camara")
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)
        hablar("Abriendo camara")
        hablar("Tomando foto")
        hablar("Por favor. Sonrrie")
        ret, frame = cap.read()
        hablar("Tu foto esta lista")
        cv2.imwrite('C:/Users/coman/Desktop/Prueba/foto.jpg', frame)
        hablar("Linda foto. Por favor revisala")

run()