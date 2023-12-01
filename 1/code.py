def read_data():
    data = open("1/data.txt").read()
    data = data.split("\n")
    return data
MAPS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

content = read_data()
total = []
for line in content:
    number = []
    num_as_char = ''
    for char in line:
        try:
            n = int(char)
            number.append(n)
            num_as_char = ''
        except:
            num_as_char += char
            for key in MAPS.keys():
                if key in num_as_char:
                    n = MAPS[key]
                    number.append(n)
                    num_as_char = char
            continue
    single_number = int(f"{number[0]}{number[-1]}")
    total.append(single_number)
print(sum(total))
