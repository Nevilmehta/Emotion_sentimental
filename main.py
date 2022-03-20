#Cleaning Text Steps
#1) Text file
#2) Lowercase
#3) remove punctuations

import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

txt= open('read.txt', encoding= 'utf-8').read()
lower_case= txt.lower()
cleaned_txt=lower_case.translate(str.maketrans('','',string.punctuation))

#tokenization and stop words
#tokenized_words=cleaned_txt.split()
#convert line into words

tokenized_words= word_tokenize(cleaned_txt,"english")

final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

#NLP emotion algorithm
#1)check if word in the final word is also present in emotion.txt
#   -open emotion file
#   -loop through each line and clear it
#   -extract the word and emotion using split

#2) If word present-> add the emotion to emotion list
#3) finally count each word in emotion list

emotion_list=[]
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line= line.replace("\n",'').replace(",",'').replace("'",'').strip()
        word, emotion=clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w=Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg=score['neg']
    pos=score['pos']
    if neg>pos:
        print('Negative sentiment')
    elif pos>neg:
        print('Positive sentiment')
    else:
        print('Neutral vibe')

sentiment_analyse(cleaned_txt)

fig, ax1= plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph2.png')
plt.show()
