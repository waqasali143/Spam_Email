## Spam_Email<br>
#### [[Email Spam App](https://spam-email-w.streamlit.app/)] <br> 
# <strong> Problem Statment<br>
Email is a powerful tool for communication It is one of the most popular and secure mediums for online transferring and communicating messages or data through the web.But, due to social networks, most of the emails contain unwanted information which is called spam. Identifying such spam emails is one of the important challenges. In this project, we will use the PYTHON text classification technique to identify or classify email spam messages.
On Email Dataset, we will also compare which algorithm is best for text classification.<br>
We will also download the different nltk packages for this project.
# Task:<br>
<strong> Email messages spam or not spam <br><br>
How many messages are Spam or not spam? In this dataset. We check by pie plot<br>
![Screenshot 2024-03-24 131052](https://github.com/waqasali143/Spam_Email/assets/82609521/35170ad6-c856-46cf-a2c4-04d02af8aea5)

<br> 
# Text Preprocessing<br>
and follow will these essential steps.

* Convert the all words lower case.
* Tokenizaton
* Remove the special characters.
* Remove punctuation
* Stemming <br>

# After Training with different Model Results <br><br>
## CountVectorizer Result <br>
![cv](https://github.com/waqasali143/Spam_Email/assets/82609521/91af1fd7-a333-4f75-909c-1cbce4efb833)

<br> <br>
## TfidfVectorizer Results <br> <br>
![tf](https://github.com/waqasali143/Spam_Email/assets/82609521/4e3f9642-1e96-400e-84a7-29a816516ca6)

<br> <br>
## TfidfVectorizer with Max feature Results <br> <br>
![tfm](https://github.com/waqasali143/Spam_Email/assets/82609521/087006b9-10ff-4cb4-b068-559550c7905b)

<br> <br>
### I got the best results with Tfidfvectorizer with Max feature. MultinomialNB model showing the best result
Model

MNB => PrecisionScore = 1.000000 AccScore = 0.973888 f1_Score = 0.872038



