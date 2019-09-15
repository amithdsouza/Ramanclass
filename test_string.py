


def half_strings(s):
    a = s.strip()
    b = a.split()
    c = len(b)
    mid = c / 2
    first = b[:mid]
    second = b[mid:]
    second.reverse()
    print first, second

    f = len(first)
    s = len(second)
    m = min(f, s)
    third = []
    for i in range(m):
        third.append(first[i])
        third.append(second[i])
    third.extend(first[m:])
    third.extend(second[m:])
    print third


TEST_STRINGS = [
                 '',
                 'one',
                 ' two three ',
                 'four five six seven',
                 'eight nine six one three',
               ]


for s in TEST_STRINGS:
    half_strings(s)
