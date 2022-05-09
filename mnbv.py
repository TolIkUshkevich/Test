def function(text):
    if text[0] != text[0].upper():
        text = text.replace('-', ' ')
        text = text.replace('_', ' ')
        text = text.title()
        text = text.replace(' ', '')
        text = text.replace(text[0], text[0].lower())
    else:
        text = text.replace('-', ' ')
        text = text.replace('_', ' ')
        text = text.title()
        text = text.replace(' ', '')

    return text
print(function(input()))