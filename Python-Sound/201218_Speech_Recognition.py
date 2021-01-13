import speech_recognition as sr
from os import path
from pydub import AudioSegment

# fileinnamemp3 = "C:\\Users\\dasep\\Desktop\\SC-Analytics-Podcast-from-White-Paper.mp3"
fileoutname = "C:\\Users\\dasep\\Desktop\\fileout.txt"
fileinnamewav = "C:\\Users\\dasep\\Desktop\\SC-Analytics-Podcast-from-White-Paper.wav"

# files                                                                         
# src = fileinnamemp3
# dst = fileinnamewav

# convert wav to mp3                                                            
# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")

#  initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.AudioFile(fileinnamewav) as source:
    # open the output table
    fileout = open(fileoutname,"w+")
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    fileout.write(text)
    print("file output ready")