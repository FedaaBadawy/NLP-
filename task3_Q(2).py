# Question (2)
import spacy

def pos_tagging(text, tagset):
    # Load English language model
    nlp = spacy.load("en_core_web_sm")
    
    # Process the text
    doc = nlp(text)
    
    # Perform part-of-speech tagging
    if tagset == "universal":
        tags = [(token.text, token.pos_) for token in doc]
    elif tagset == "penn":
        tags = [(token.text, token.tag_) for token in doc]
    else:
        raise ValueError("Invalid tagset. Please use 'universal' or 'penn'.")
    
    return tags

def main():
    text = input("Enter text: ")
    
    # Perform part-of-speech tagging with Universal POS tagset
    print("\nUniversal POS Tagging:")
    universal_tags = pos_tagging(text, tagset="universal")
    for word, tag in universal_tags:
        print(f"{word}: {tag}")
    
    # Perform part-of-speech tagging with Penn Treebank POS tagset
    print("\nPenn Treebank POS Tagging:")
    penn_tags = pos_tagging(text, tagset="penn")
    for word, tag in penn_tags:
        print(f"{word}: {tag}")

if __name__ == "__main__":
    main()
