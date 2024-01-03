def reverse_sentence(sentence):
    words = sentence.split()
    for word in reversed(words):
        print(word[::-1])

input_sentence = input("Please write a sentence: ")
reverse_sentence(input_sentence)
