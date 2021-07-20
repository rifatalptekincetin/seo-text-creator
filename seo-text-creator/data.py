import nltk.data

def get_sentences(x='data.txt'):
    tokenizer = nltk.data.load('tokenizers/punkt/turkish.pickle')
    with open(x,'r',encoding="utf-8") as f:
        text=f.read()
        return tokenizer.tokenize(text)
