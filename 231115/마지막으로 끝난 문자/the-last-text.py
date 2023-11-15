word_dict = {}
for _ in range(int(input())):
    word = input()
    if word[-1] not in word_dict:
        word_dict[word[-1]] = []
    word_dict[word[-1]].append(word)
m_word = input()
if m_word not in word_dict:
    print(0)
print(len(word_dict[m_word]))
for word in word_dict[m_word]:
    print(word)