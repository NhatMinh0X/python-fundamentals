def for_statement():
    words = ['Mac', 'Linux', 'Windows']  # list
    words_length = 0
    concatenated_string = ''

    for word in words:
        print(word)
        words_length += len(word)
    print(words_length)

    for word in words[:]:  # Loop over a slice copy of the entire list.
        if len(word) > 6:
            words.insert(0, word)

    print(words)

    for word_index in range(len(words)):
        concatenated_string += words[word_index] + ' '

    print(concatenated_string)

    knights_names = []
    knights_properties = []

    knights = {'gallahad': 'the pure', 'robin': 'the brave'}  # dictionary
    for key, value in knights.items():
        knights_names.append(key)
        knights_properties.append(value)

    print(knights_names)
    print(knights_properties)


def range_function():
    assert list(range(5)) == [0,1,2,3,4]
    assert list(range(5, 10)) == [5, 6, 7, 8, 9]
    assert list(range(0, 10, 3)) == [0, 3, 6, 9]
    assert list(range(-10, -100, -30)) == [-10, -40, -70]

for_statement()
