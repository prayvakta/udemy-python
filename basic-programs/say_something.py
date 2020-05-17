statement = ''
question_words = ('who', 'what', 'where', 'why', 'when', 'how')
sentence = []

def is_question(text):
    for word in question_words:
        if text.find(word) > -1:
            text += '?'
            return text
    text += '.'
    return text
            

while statement != '\\end':
    statement = input('Say something:')
    if statement != '\\end':
        statement = is_question(statement.lower())
        sentence.append(statement.capitalize())

print(' '.join(sentence))