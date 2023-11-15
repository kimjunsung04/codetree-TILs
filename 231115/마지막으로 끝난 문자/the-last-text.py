word_dict = {}
for _ in range(int(input())):
    word = input()
    if word[-1] not in word_dict:
        word_dict[word[-1]] = []
    word_dict[word[-1]].append(word)
m_word = sorted(word_dict, key=lambda a: len(word_dict[a]))[-1]
print(len(word_dict[m_word]))
for word in word_dict[m_word]:
    print(word)