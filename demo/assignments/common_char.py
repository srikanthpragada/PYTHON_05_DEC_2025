def common_char(s1, s2):
    return "".join(set(s1) & set(s2))


print(common_char('abcd', 'defa'))
