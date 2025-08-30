import emoji

print(emoji.emojize("python fun emoji :snake: :thumbs_up: :red_heart: ::"))


def printSorry(num):
    for i in range(num):
        print(i, emoji.emojize("Sorry :red_heart:"))

    return True


printSorry(2)
