import json
import time
from inputimeout import inputimeout, TimeoutOccurred
def open_data(data):
    f = open(data)
    d = f.read()
    b = json.loads(d)
    return b

def quiz_bot(data):
    r = 0
    t = 1
    savollar_toplami = data['quiz']
    print('Diqqat savol 5 sekundan keyin boshlanadi')
    time.sleep(5)
    for i in savollar_toplami:
        savollar = savollar_toplami[i]
        for n in savollar:
            savol = savollar[n]
            print(f"{t}) {savol['question']}")
            t+=1
            s = 1
            for m in savol['options']:
                print(f"{s}-{m}")
                s+=1
            try:
                javob = inputimeout(prompt='Javobni kiriting:', timeout=10)
                if savol['options'].index(savol['answer'])+1==int(javob):
                    r+=1
                    print("To'g'ri javob") 
                else:
                    print("Noto'g'ri javob")
            except TimeoutOccurred:
                something = 'Vaqt tugadi!'
                print(something)
            
    print(f"{r} ta topdingiz")
data = open_data('quizbaza.json')  
quiz_bot(data)