def razvorot(stroka):
    if len(stroka) == 1:
        return stroka
    return stroka[-1] + razvorot(stroka[:-1])


print(razvorot('asdf'))
