from collections import defaultdict

def group_anagrams(words):
    hashmap = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        hashmap[key].append(word)
    return list(hashmap.values())

words = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(words))