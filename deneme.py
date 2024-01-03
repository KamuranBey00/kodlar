string = "Here is the content and I want to get middle words"
word = "content"
start = string.index(word)
end = start + len(word)
print(string[start:end])