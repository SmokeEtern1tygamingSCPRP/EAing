word_list = ['apple', 'book', 'laptop', 'cat', 'banana', 'orange', 'PC', 'grape', 'kiwi']

user_input = input('Введите слово: ')

if user_input in word_list:
    print('Слово', user_input)
else:
    print('Слово', user_input, 'отсутствует в списке.')
