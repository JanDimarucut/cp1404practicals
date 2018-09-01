
unique_words = {}
user_input = input("Text: ")
while user_input != "":

    words = user_input.split()

    for word in words:
        text = unique_words.get(word, 0)
        unique_words[word] = text + 1

    words = list(unique_words.keys())
    words.sort()

    max_length = max(len(word) for word in words)
    for word in words:
        print("{:{}} : {}".format(word, max_length, unique_words[word]))
    user_input = input("text: ")
print("Farewell")