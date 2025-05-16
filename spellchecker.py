misspelled_words = []
dict_file = "dictionary.txt"
punctuation = '.,!"'

src_file = input("Enter source file: ")
with open(src_file, "r") as src:
    data = src.read()

    # filter words
    for punc in punctuation:
        data = data.replace(punc, " ")
    words = set(data.split())
    with open(dict_file, "r") as dict:
        dict_words = set(dict.read().split())
        for word in words:
            if word.lower() not in dict_words:
                misspelled_words.append(word)
misspelled_words.sort()
for word in misspelled_words:
    print(word)