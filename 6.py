def longest_word(text):
    return max(text.split(), key=len)

text = "а аа ааа аааа ааааа"
print(longest_word(text))