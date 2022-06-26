def revers(row_str):
    word_list = row_str.split(' ')
    word_list[::-1]
    revers_list = word_list[::-1]
    upside_list = [word[::-1] for word in revers_list]
    string = ' '
    return string.join(upside_list)

user_input = input('Enter hebrew to revers:\n')
print(revers(user_input))



