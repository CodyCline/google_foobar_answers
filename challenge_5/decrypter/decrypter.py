import base64

MESSAGE = "YOUR_B64_MESSAGE"

KEY = "USERNAME"

def solution(message, key):
    result = []
    for i, c in enumerate(base64.b64decode(message)):
        result.append(chr(c ^ ord(key[i % len(key)])))
    return ("".join(result))


print(solution(MESSAGE, KEY))
