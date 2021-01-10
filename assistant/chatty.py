import threading
import speech_recognition as sr
from utils.utils import Utils
from intents.greeting import Greeting

class chatty(threading.Thread):
    def __init__(self,logger,config):
        self.logger = logger
        self.config = config
        self.speech = sr.Recognizer()
        self.utils = Utils(self.logger)
        threading.Thread.__init__(self)

    def read_voice_cmd(self):
        voice_input = ''
        try:
            with sr.Microphone() as source:
                 audio = self.speech.listen(source=sorce, timeout=5, phrase_time_limit=5)
            voice_input = self.speech.recognize_google(audio)
            self.logger.info('Input : {}' .format(voice_input))

        except sr.UnknownValueError:
            pass

        except sr.RequestError:
            print('Network error.')

        except sr.WaitTimeoutError:
            pass

        except TimeoutError:
             pass

        return voice_input.lower()

    def run(self):
         while True:
             voice_note = self.read_voice_cmd()
             for key in self.config:
                    utterances = Utils.match_pattern(voice_note,self.config[key]['utterances'])
                    if utterances:
                       response = Utils.choose_random(self.config[key]['response'])
                       break

             if key == 'intent_greeting':
                 Greeting(self.logger,response).speak()
                 break

             else:
                 Utils.playsound('intent not found')

