def break_words(stuff):
    """把句子里的单词按空格分开 得到的是数组"""
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """排序"""
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """删除列表的index=0那一项 pop会返回被删除的值"""
    """Print the first word after popping it off."""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """删除列表的index=-1那一项 -1也是默认值 pop会返回被删除的值"""
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """调用了最开始的两个function 得到的结果就是把它们都过一遍后的值"""
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """调用第一个和第三第四个function"""
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """调用倒数第三个function"""
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
