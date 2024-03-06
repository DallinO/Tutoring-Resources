def mystery_1(text):
    stack = []

    for letter in text:
        stack.append(letter)
        print(stack)

    result = ""
    while len(stack) > 0:
        result += stack.pop()
        print(result)
    
    return result

text = "Hello"
result = mystery_1(text)
print(result)