from django import template


register = template.Library()

censored_words = [
    'штраф',
    'экспонат',
    'клуб',
    'сексуального',
    'возвращение',
    'список'
]

@register.filter()
def censor(value):
    for word in value.split():
        if word.lower() in censored_words:
            value = value.replace(word[1:], "*" * (len(word)-1))
    return value