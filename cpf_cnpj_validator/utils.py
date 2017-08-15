divider = 11


def firstDigit(number, weighs):
    sum = 0

    for i in range(len(weighs)):
        sum += int(number[i]) * weighs[i]

    rest_division = sum % divider

    if rest_division < 2:
        return '0'

    return str(11 - rest_division)


def secondDigit(updated_number, weighs):
    sum = 0

    for i in range(len(weighs)):
        sum += + int(updated_number[i]) * weighs[i]

    rest_division = sum % divider

    if rest_division < 2:
        return '0'

    return str(11 - rest_division)