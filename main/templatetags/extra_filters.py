from django import template

register = template.Library()

@register.filter(name='truncate_words')
def truncate_words(value, word_count):
    words = value.split()
    if len(words) > word_count:
        return ' '.join(words[:word_count]) + '...'
    return value
