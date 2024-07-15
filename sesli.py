from gtts import gTTS
import os

while True:
    minikinmetini = input("Metni girin (Çıkmak için 'q' tuşuna basın): ")

    if minikinmetini.lower() == 'q':
        break
    minikincevabi = gTTS(text=minikinmetini, lang='tr')


    minikindosyasi = minikinmetini.replace(" ", "_").replace(".", "").replace("!", "") + ".mp3"

    minikincevabi.save(minikindosyasi)

    os.system(minikindosyasi)
