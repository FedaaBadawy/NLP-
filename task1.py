# import nltk
# nltk.download()

from nltk import sent_tokenize , word_tokenize

text = input("Enter a text: ")

print("Choose a number:")
print("1: Print tokenized words")
print("2: Print tokenized sentences")
print("3: Print output using split function")

while True:
    choice = input("Enter your choice: ")

    if choice == '1':
        print(word_tokenize(text))

    elif choice == '2':
        print(sent_tokenize(text))

    elif choice == '3':
        print(text.split())

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
