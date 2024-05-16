from locust import HttpUser, task, between
import random
list_audio = []
with open('./list_audio','r') as f:
    lines = f.readlines()
for line in lines:
    line = line.strip()
    list_audio.append(line)
class MyUser(HttpUser):
    #wait_time = between(1, 3)

    @task
    def submit_audio(self):
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MjM0MjA3NjQ3Mn0.gb5BbO9XlGjHy-_O0DJgPZDwEEmML5A1iMmqn5EL2h4',
        }
        data = {
            'vocab': '',
            'no_speech_threshold': 0.6,
            'num_speakers': -1,
            'diarization': False,
            'offset_end': '',
            'word_timestamps': False,
            'source_lang': 'vi',
            'offset_start': '',
            'internal_vad': False,
            'condition_on_previous_text': True,
            'repetition_penalty': 1.2,
            'log_prob_threshold': -1,
            'timestamps': 's',
            'multi_channel': False,
            'compression_ratio_threshold': 2.4,
        }
        utt = random.choice(list_audio)
        files=open(utt,'rb')
        response = self.client.post('/api/v1/audio', headers=headers, data=data, files={'file': files})
        #print(response)

