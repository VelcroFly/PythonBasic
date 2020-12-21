import string


def int_func(text):
    try:
        word_list = text.split()
    except AttributeError:
        return None

    for pos, word in enumerate(word_list):
        for letter in word:
            if letter not in string.ascii_letters:
                break
            word_list[pos] = word.title()
    return ' '.join(word_list)


if __name__ == '__main__':
    print(int_func(123))
    print(int_func('апва word 123'))
