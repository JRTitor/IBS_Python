from typing import List

def find_in_different_registers(words: List[str]) -> List[str]:
    """
    This function takes a list of words and returns a list of words that appear only once in the list.

    Parameters:
    words (List[str]): A list of words

    Returns:
    List[str]: A list of words that appear only once in the input list

    """
    d = dict()

    for word in words:
        d[word] = d.get(word, 0) + 1

    words_to_remove = set()
    words_to_leave = set()

    for k, v in d.items():
        if v > 1:
            words_to_remove.add(k.lower())
        else:
            words_to_leave.add(k.lower())
# мажно было бы сделать с двумя словарями, но я спешил сделать так, чтобы работало, поэтому использовал разность множетсв, и получилось не эффективно
    return list(words_to_leave - words_to_remove) 


