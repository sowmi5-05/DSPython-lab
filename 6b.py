 
def is_palindrome(s):
    s = ''.join(s.lower().split())
    n = len(s)
    queue = []
    for i in range(n // 2):
        queue.append(s[i])
    if n % 2 == 0:
        start = n // 2
    else:
        start = (n // 2) + 1
    for i in range(start, n):
        if len(queue) == 0 or queue[-1] != s[i]:
            return False
        queue.pop()
    return True
text = input("Enter a word or phrase: ")
if is_palindrome(text):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
