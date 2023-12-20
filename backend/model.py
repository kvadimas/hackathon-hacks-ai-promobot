import joblib
import re
import nltk
#from nltk.corpus import stopwords
import spacy
import pandas as pd

nlp = spacy.load('ru_core_news_lg')
model = joblib.load('classifier_pretrained.pkl')

nltk.download('stopwords')

stop_words = nltk.corpus.stopwords.words('russian')
stop_words.extend(['добрый', 'день', 'вечер', 'прошу', 'требую', 'обращаюсь', 'спасибо', 'пожалуйста',
                  'br', 'здравствуйте', 'это', 'год', 'сказать', 'почему', 'человек', 'вопрос', 'мочь',
                  'такой', 'подсказать', 'который', 'какой', 'ещё'])


def prerocess_text_message(msg_text: str) -> str:
    """
    Preprocesses text before classify.

    Parameters
    ----------
    msg_text: str

    Returns
    -------
    str
    A string in lowercase, tokenized, lemmatized and without stopwords.
    """

    # Remove any character that is not a word character or a space character
    text =  re.sub(r'[^\w\s]', ' ', re.sub(r'[^А-яа-я]', ' ', msg_text), flags=re.UNICODE)
    # Tokenize lowcase string
    tokenized_text = nltk.word_tokenize(text.lower())

    # Lemmatize tokens
    doc = nlp(" ".join(tokenized_text))
    lemmas_list = [token.lemma_ for token in doc]

    # Remove stopwords from lemmas
    str_lemmas_wo_stopwords = ' '.join([word for word in lemmas_list if word not in stop_words])
    return str_lemmas_wo_stopwords


def forecast(message: str) -> str:
    msg_processed = prerocess_text_message(message)
    msg = pd.DataFrame({'incident_text': msg_processed}, index=[0])
    """
    Makes multiclass classification for text message.
    """
    return model.predict(msg).reshape(-1)[0]
