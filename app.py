import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
import sklearn

nltk.download('punkt')
nltk.download('stopwords')

def text_transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

cv = pickle.load(open('./vectorizer.pkl', 'rb'))
model = pickle.load(open('./EspamModel.pkl', 'rb'))

st.title("Classifier")

input_msg = st.text_input("Enter Message")

if st.button("Check Spam"):
    transForm_text = text_transform(input_msg)
    vect_text = cv.transform([transForm_text])
    result = model.predict(vect_text)[0]
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
