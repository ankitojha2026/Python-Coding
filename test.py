sentence='hello  world'
user_input='hello'


# correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(sentence) and c == sentence[i])
# accuracy = (correct_chars / len(sentence)) * 100
# print(accuracy)

x=0
for i in enumerate(user_input):
    print(i)