words = ["apple", "banana", "orange", "apple", "apple", "banana"]


def count_words():
    count_dict = {}

    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1

    print(count_dict)


count_words()


