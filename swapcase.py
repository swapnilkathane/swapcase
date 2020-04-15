def swap_case(s):
    m = ""
    for words in s:
        for i in words:
            if i.islower() == True:
                i = i.upper()
            else:
                i = i.lower()
            res = m + i
            m = res
    #print(m)

    return m


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)