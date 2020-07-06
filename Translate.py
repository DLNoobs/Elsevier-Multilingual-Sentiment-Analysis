import os
from google.cloud import translate_v2 as translate
translate_client = translate.Client()

def translate_text(text, translate_client):    
    result = translate_client.translate(text,source_language = 'en', target_language='hi')
    #print(u'Text: {}'.format(result['input']))
    #print(u'Translation: {}'.format(result['translatedText']))
    return result['translatedText']

f = open(os.getcwd()+"/Dataset.txt", "r")
g = open(os.getcwd()+"/Translated_Dataset.txt","w+")
i = 0
number_of_sentence = 3001   #Modify Number of Sentence
while(i < number_of_sentence):
    sent = f.readline().split('\t')
    trans = translate_text(sent[0], translate_client)
    g.write(trans.encode('utf8')+'  '+sent[1].encode('utf8'))
    i += 1
    print(i)
f.close()
g.close()