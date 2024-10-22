def is_polindrome(word):
    list1 = []
    for i in range(len(word)):
        if word[i].isalnum():
            list1.append(word[i].lower())
        else:
            list1.append(word[i])
    new = "".join(list1)
    for i in range(len(new) // 2):
        if new[i] != new[len(new) - 1 - i]:
            return "no"
    return "yes"


word = input()
print(is_polindrome(word))