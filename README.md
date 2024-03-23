## Spam_Email<br>
#### Email Spam App <br>
# <strong> Problem Statment<br>
Email is a powerful tool for communication It is one of the most popular and secure mediums for online transferring and communicating messages or data through the web.But, due to social networks, most of the emails contain unwanted information which is called spam. Identifying such spam emails is one of the important challenges. In this project, we will use the PYTHON text classification technique to identify or classify email spam messages.
On Email Dataset, we will also compare which algorithm is best for text classification.<br>
We will also download the different nltk packages for this project.
# Task:<br>
<strong> Email messages spam or not spam <br><br>
How many messages are Spam or not spam? In this dataset. We check by pie plot<br>
![Screenshot 2024-03-23 145121](https://github.com/waqasali143/Spam_Email/assets/82609521/1ab04004-1469-4a63-85fa-0e45c808b27e)
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
![cv](https://github.com/waqasali143/Spam_Email/assets/82609521/0773b83a-825f-404c-8454-901aad6d540e)
<br> <br>
## TfidfVectorizer Results <br> <br>
![tf](https://github.com/waqasali143/Spam_Email/assets/82609521/3bbf83db-b3bc-427a-b039-891ab8f6ff6a)
<br> <br>
## TfidfVectorizer with Max feature Results <br> <br>
![mtf](https://github.com/waqasali143/Spam_Email/assets/82609521/a46e8959-06b4-4aa9-b977-d22f6b7fec1c)
<br> <br>
### I got the best results with Tfidfvectorizer. KNeighborsClassifier and MultinomialNB model showing the best result
Model

MNB => PrecisionScore = 1.000000 AccScore = 0.925926 f1_Score = 0.845833

KN => PrecisionScore = 0.980237 AccScore = 0.965966 f1_Score = 0.935849 <br>


