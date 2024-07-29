import re

text = ('Access advanced vision models via APIs to automate vision tasks, streamline analysis, '
        'and unlock actionable insights. Or build custom apps with no-code model training '
        'and low cost in a managed environment.'
        'Computer vision is a field of 1artificial intelligence (AI) that enables computers '
        'and systems to interpret and analyze visual data and derive meaningful information '
        'from digital images, videos, and other 7visual inputs. Some of its typical real-world '
        'applications include: object detection, visual content (images, documents, videos) '
        'processing, 11understanding and analysis, 9product search, image classification and search,'
        ' and content moderation. Google\'s Vertex AI offers access to Gemini, a family')

# ===========  Method FINDALL  ==========================
# Из библиотеки regular expression
# https://www.w3schools.com/python/python_regex.asp

# Найти все значения из какого-то текста со всеми паттернами

pattern = 'Google\'s'

x = re.findall(pattern, text, flags=re.IGNORECASE)
print(x)

# если over right то возвращает пустой массив - []
pattern = 'Googl\'s'

x = re.findall(pattern, text, flags=re.IGNORECASE)
print(x)

pattern = 'ML'

x = re.findall(pattern, text, flags=re.IGNORECASE)
print(x)

# r - означает только для чтения
# \d - находим все (любые) цифры из текста
pattern = r'\d'
# or
# pattern = r'[0-9]'
# ^(Caret))- за исключением всех цифр
# pattern = r'[^0-9]'

x = re.findall(pattern, text, flags=re.IGNORECASE)
print(x)

pattern = r'G..{3,5}\'s'
pattern = r'G..{3,5}\'s'

x = re.findall(pattern, text, flags=re.IGNORECASE)
print(x)

#  . - любой символ
#  * - от 0 и более, н-р: r'G..*\s'
#  + - от 1 и более
#  ? - либо есть либо нет - 0 or 1, н-р: r'G..{4}\d?\'s'

# Нижний регистр
def lowercase_count(syring):
        pattern = r'[а-я]'
        x = re.findall(pattern, string)
        return len(x)


# ===========  Method SEARCH  ==========================
# Что ищем? Где ищем? Как?
x = re.search(pattern, text, flags=re.IGNORECASE)
print(x)
print(x.start())
print(x.string)
print(x.group())
print(x.span())

# ===========  Method SPLIT  ==========================

pattern = r'\d'
x = re.split(pattern, text, flags=re.IGNORECASE, maxsplit=1)
print(x)
print(len(x))

# ===========  Method SUB  ==========================
# заменили google на news
x = re.sub(pattern, 'NEWS', text, flags=re.I)
print(x1)
pattern1 = 'NEWS'
x = re.split(pattern1, x1, flags=re.IGNORECASE)
print(x)