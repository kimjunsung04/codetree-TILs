word1 = input()
word2 = input()

# Please write your code here.
if sorted(list(word1)) == sorted(list(word2)):
    print("Yes")
else:
    print("No")