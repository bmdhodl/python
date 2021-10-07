words = ['apples', 'bananas', 'tofu', 'cats']

if len(words) == 1:
    print(words[0])
print('{}, and {}'.format(', '.join(words[:-1]), words[-1]))