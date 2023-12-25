from typing import List

def find_in_different_registers(words: List[str]) -> List[str]:
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
    
    return list(words_to_leave - words_to_remove)


