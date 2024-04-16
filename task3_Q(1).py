# Question (1)
import spacy

def tokenize_sentences(text, language):
    # Load the language model
    nlp = spacy.load(language)
    
    # Process the text
    doc = nlp(text)
    
    # Tokenize sentences
    sentences = [sent.text for sent in doc.sents]
    
    return sentences

def main():
    text = input("Enter text: ")
    language = "fr_core_news_sm"  # French language model
    
    # Tokenize sentences
    sentences = tokenize_sentences(text, language)
    
    # Print tokenized sentences
    print("Tokenized sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")

if __name__ == "__main__":
    main()
