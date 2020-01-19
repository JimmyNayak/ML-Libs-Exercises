import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# download punkt lib to overcome the resource error
# nltk.download('punkt')
# nltk.download('stopwords')

# sentence = "I Love India. India is the best country to live."
# print(sent_tokenize(sentence))


# sentence = "I Love India. India is the best country to live."
# print(word_tokenize(sentence))


print(stopwords.words('english'))