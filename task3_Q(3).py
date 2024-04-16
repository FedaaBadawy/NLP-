# Question (3)
import nltk
from nltk.corpus import stopwords

def get_stopwords(language):
    nltk.download('stopwords')
    stop_words = set(stopwords.words(language))
    return stop_words

def main():
    languages = ["english", "spanish", "french", "german", "italian"]
    for lang in languages:
        stop_words = get_stopwords(lang)
        print(f"\nStop words in {lang}:")
        print(stop_words)

if __name__ == "__main__":
    main()
