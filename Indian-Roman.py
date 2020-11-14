roman_dict = {1: "I", 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
         10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
         100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
         1000: 'M', 2000: 'MM', 3000: 'MMM'}
num = input('Enter number : ')
count = len(num)
exp = []
roman = []
if int(num) < 4000:
    if count == 1:
        print("In roman numerals " + num + " = ", roman_dict.get(int(num)))

    if count == 2:
        exp.append((int(num[0]) * 10))
        roman.append(roman_dict.get(exp[0]))
        if num[1] != "0":
            exp.append(int(num[1]))
            roman.append(roman_dict.get(exp[1]))
        print("In roman numerals " + num + " = ", *roman, sep="")

    if count == 3:
        exp.append((int(num[0]) * 100))
        roman.append(roman_dict.get(exp[0]))

        if num[1] != "0":
            exp.append((int(num[1]) * 10))
            roman.append(roman_dict.get(exp[1]))

        if num[2] != "0":
            exp.append(int(num[2]))
            if len(exp) == 2:
                roman.append(roman_dict.get(exp[1]))
            if len(exp) == 3:
                roman.append(roman_dict.get(exp[2]))

        print("In roman numerals " + num + " = ", *roman, sep="")

    if count == 4:
        exp.append((int(num[0]) * 1000))
        roman.append(roman_dict.get(exp[0]))

        if num[1] != "0":
            exp.append((int(num[1]) * 100))
            roman.append(roman_dict.get(exp[1]))

        if num[2] != "0":
            exp.append((int(num[2]) * 10))
            if len(exp) == 2:
                roman.append(roman_dict.get(exp[1]))
            if len(exp) == 3:
                roman.append(roman_dict.get(exp[2]))

        if num[3] != "0":
            exp.append(int(num[3]))
            if len(exp) == 2:
                roman.append(roman_dict.get(exp[1]))
            if len(exp) == 3:
                roman.append(roman_dict.get(exp[2]))
            if len(exp) == 3:
                roman.append(roman_dict.get(exp[3]))
        print("In roman numerals " + num + " = ", *roman, sep="")
else:
    print("Enter less than 4000")
