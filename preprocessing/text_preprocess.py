import nltk
nltk.download('punkt')
def basic_tokenize(input):
    if isinstance(input,str):
        return nltk.word_tokenize(input)
    else:
        return ""