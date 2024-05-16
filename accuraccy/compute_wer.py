from jiwer import wer
import re 
import inflect 
import string
p = inflect.engine()

def number_to_text(number):
    return p.number_to_words(number)

def norm_text(s):
    s = re.sub(r'\d+', lambda x: number_to_text(int(x.group())), s)
    s = s.translate(str.maketrans('', '', string.punctuation))
    
    return s.lower()

with open('./text_ref','r') as f:
    lines = f.readlines()
d_ref = {}
for line in lines:
    line = line.strip()
    utt = line.split()[0]
    text = ' '.join(line.split()[1:])
    d_ref[utt] = text
    
with open('./text_v1','r') as f:
    lines = f.readlines()
d_su = {}
d_old_su = {}

for line in lines:
    line = line.strip()
    utt = line.split()[0]
    text = ' '.join(line.split()[1:])
    d_su[utt]  = norm_text(text)
    d_old_su[utt] = text

with open('./text_v2','r') as f:
    lines = f.readlines()
d_tuan = {}
d_old_tuan = {}
for line in lines:
    line = line.strip()
    utt = line.split()[0]
    text = ' '.join(line.split()[1:])
    d_tuan[utt]  = norm_text(text)
    d_old_tuan[utt] = text



for k in d_tuan:
    if k in d_su and k in d_ref:
        acc2 = 100 - round(100*wer(d_ref[k],d_tuan[k]),2)
        acc1 = 100 - round(100*wer(d_ref[k],d_su[k]),2)
        print("{}|{}|{}|{}|{}|{}".format("http://103.141.140.202/audio_test/wav/"+k+".wav",d_ref[k],d_old_su[k], acc1, d_old_tuan[k],acc2))

refs = []
hyp_tuan = []
hyp_su = []
for k in d_tuan:
    if k in d_su and k in d_ref:
        refs.append(d_ref[k])
        hyp_tuan.append(d_tuan[k])
        hyp_su.append(d_su[k])
acc2 = 100*(1 - wer(refs, hyp_tuan))
acc1 = 100*(1 - wer(refs, hyp_su))

print("Overall Accuracy | v1 : {} | v2 : {}".format(acc1,acc2))