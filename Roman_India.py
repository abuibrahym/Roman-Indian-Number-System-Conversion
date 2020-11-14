roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman = input('Enter roman numeral : ').upper()
flag = True
prev = ''
i = 0
for letter in roman:
    if letter not in 'IVXLCDM':
        print(letter + ' is not a valid Roman Numeral')
        flag = False
        break
    prev += letter
    if len(prev) > 1:
        if roman_dict.get(prev[-1]) > roman_dict.get(prev[-2]):
            i += 1
            if i == 2:
                flag = False
                break
        if roman_dict.get(prev[-1]) < roman_dict.get(prev[-2]):
            i -= 1
if len(roman) == 1:
    print('Indian-Arabic Number System {0} = {1}'.format(roman, roman_dict.get(roman[-1])))
else:
    if flag is True:
        a = []
        i = 0
        while i < len(roman)-1:
            if roman_dict.get(roman[i]) >= roman_dict.get(roman[i+1]):
                a.append(roman_dict.get(roman[i]))
            else:
                a.append(roman_dict.get(roman[i+1]) - roman_dict.get(roman[i]))
                i += 1
            i += 1

        if roman_dict.get(roman[-2]) >= roman_dict.get(roman[-1]):
            a.append(roman_dict.get(roman[-1]))

        num = sum(a)
        import roman_numerals_mtd2
        checked = roman_numerals_mtd2.check(str(num))
        temp = ""
        for i in checked:
            temp += i
        if temp == roman:
            print('Indian-Arabic Number System {0} = {1}'.format(roman, num))
        else:
            print('->You entered wrong numeral\n'
                  '->You perhaps tried to enter {0}\n'.format(num),
                  '->The correct way of writing {0} is {1}'.format(num, temp), sep="")
    else:
        print('you entered wrong numeral')
