import random
from locust import HttpUser, task,between
import os
list_audio = []
with open('./list_audio','r') as f:
    lines = f.readlines()
for line in lines:
    line = line.strip()
    list_audio.append(line)
class Asruser(HttpUser):
    @task
    def recognize(self):
        utt = random.choice(list_audio)
        files=open(utt,'rb')
        data = {'token': 'xx'}
        self.client.post("/demo/asr", data = data, files={'file': files})
        
