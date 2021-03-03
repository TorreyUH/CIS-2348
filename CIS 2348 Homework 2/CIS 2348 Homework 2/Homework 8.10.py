word_input = input("")
low = 0
high = len(word_input) - 1
result = True
while low < high:
    if word_input[low] == ' ':
        low += 1
    elif word_input[high] == ' ':
        high -= 1
    elif word_input[low] != word_input[high]:
        result = False
        break
    else:
        low += 1
        high -= 1
if result:
    print(word_input + " is a palindrome")
else:
    print(word_input + " is not a palindrome")
