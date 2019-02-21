## To test it out do the following
## python3 pibook_ver2.py /home/pi/Project/res/input_kor.raw

## 임포트문
# voice-record
from __future__ import print_function
import sys
import time
import getopt
import alsaaudio
# pi-camera
from picamera import PiCamera
from time import sleep
# record-sound
import sys
import time
import getopt
import alsaaudio
# google-speech
import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types as st
## google-vision
from google.cloud import vision
from google.cloud.vision import types as vt
## aws-polly
import boto3
from pygame import mixer

## 함수선언
# record voice
def record():
    if __name__ == '__main__':

        card = 'sysdefault:CARD=Device'

        # Inform test usage
        opts, args = getopt.getopt(sys.argv[1:], 'c:')
        for o, a in opts:
            if o == '-c':
                card = a
        if not args:
            usage()

        # Start record
        f = open(args[0], 'wb')
        inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, card)

        # Set attributes: Mono, 16000 Hz, 16 bit little endian samples
        inp.setchannels(1)
        inp.setrate(16000)
        inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        inp.setperiodsize(160)

        # Record voice for 1.25 sec
        loops = 150000
        while loops > 0:
            if (loops == 150000):
                print('ready')
            loops -= 1
            # Read data from device
            l, data = inp.read()
            if l:
                f.write(data)
                time.sleep(.001)
    sst()

def usage():
    sys.stderr.write('usage: recordtest.py [-c <card>] <file>\n')
    sys.exit(2)

# speech to text
def sst():
    inStr = ''

    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    file_name = os.path.join(os.path.dirname(__file__),
                             '',
                             inDir)

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
         content = audio_file.read()
         audio = st.RecognitionAudio(content=content)

    # Set speech-recognition configuration
    config = st.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='ko-KR')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    # Execute OCR if 'read' and 'book' is in user voice
    for result in response.results:
        inStr = '{}'.format(result.alternatives[0].transcript)
        print(inStr)
        if (inStr.count('책')>0 and inStr.count('읽어')>0):
            ocr()

# optical character recognition
def ocr():
    # take a picture
    camera = PiCamera()
    camera.start_preview()
    sleep(7)
    camera.capture(imgDir)
    camera.stop_preview()
    detect_text()

# detect text
def detect_text():
    outStr = ''

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # open image file
    with io.open(imgDir, 'rb') as image_file:
        content = image_file.read()

    # Detect text from image
    image = vt.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Convert string to usable form
    if texts:
        outStr = '{}'.format(texts[0].description)
    outStr = outStr.replace('\n',' ')
    print(outStr)
    tts(outStr)

# text to speech
def tts(text):
    polly = boto3.client('polly')
    spoken_text = polly.synthesize_speech(Text=text,
      	                              OutputFormat='mp3',
               	                      VoiceId='Seoyeon')
    with open(outDir, 'wb') as f:
        f.write(spoken_text['AudioStream'].read())
        f.close()

    # audio play
    mixer.init()
    mixer.music.load(outDir)
    mixer.music.play()
    while mixer.music.get_busy() == True:
        continue

## 전역변수
imgDir = '/home/pi/Project/res/out_kor.jpg'
inDir = '/home/pi/Project/res/input_kor.raw'
outDir = '/home/pi/Project/res/output_kor.mp3'

## 메인코드
record()



