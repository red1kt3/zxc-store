s = "[]}"
characters = {
    '(': ')',
    '[': ']',
    '{': '}'
}
stack = []
for i in s:
    if i in characters:
        stack.append(i)



print(stack)