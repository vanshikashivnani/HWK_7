import requests
r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")
content = r.text
print(content)

def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char.lower() in vowels:
            count = count + 1
    return count

vowel_counts = {}
for count in range(27):
    if count == 0:
        vowel_counts[count] = " "
    else:
        vowel_counts[count] = chr(ord("a") + count - 1)

decoded = ""
for line in content.split("\n"):
    vowel_count = count_vowels(line)
    decoded += vowel_counts[vowel_count]

print(decoded)
