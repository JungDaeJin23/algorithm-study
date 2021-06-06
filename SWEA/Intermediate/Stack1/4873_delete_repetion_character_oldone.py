# Use stack
def delete_repeated_words(str1):
    stack = [''] * len(str1)
    top = -1

    for alphabet in str1:
        # is empty
        if top == -1:
            # push
            top += 1
            stack[top] = alphabet
        # Don't need to check stack is full. We set stack size as str1 size
        else:
            # pop dont need to pop. just using peek method
            preceding_alphabet = stack[top] # leading?
            top -= 1
            if preceding_alphabet != alphabet:
                # push preceding_alphabet
                top += 1
                stack[top] = preceding_alphabet
                # push alphabet
                top += 1
                stack[top] = alphabet
            # if preceding_alphabet == alphabet: pass
    return top + 1


# input and output
T = int(input())
for tc in range(1, T + 1):
    Str1 = input()
    print("#{0} {1}".format(tc, delete_repeated_words(Str1)))
