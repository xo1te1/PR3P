def letters(text):
    return ' '.join([word.capitalize() for word in text.split()])

text = "доброї ночі"
result = letters(text)
print(result)