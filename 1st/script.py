import re

def p1():
    array = []
    with open("all_data.txt") as f:
        data = f.read().split('\n')
        for line in data:
            number = [int(i) for i in line if i.isdigit()]
            combined_number = int(str(number[0])+str(number[-1]))
            array.append(combined_number)

    print(sum(array))

def convert_to_number(text):
  if text.isnumeric():
    return text
  match text:
    case "one":
      return "1"
    case "two":
      return "2"
    case "three":
      return "3"
    case "four":
      return "4"
    case "five":
      return "5"
    case "six":
      return "6"
    case "seven":
      return "7"
    case "eight":
      return "8"
    case "nine":
      return "9"

def p2():
    array = []
    with open("all_data.txt") as f:
        data = f.read().split('\n')
        for line in data:
           text = re.finditer(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', line)
           numbers_in_text = [match.group(1) for match in text]
           first_num = convert_to_number(numbers_in_text[0])
           last_num = convert_to_number(numbers_in_text[-1])
           combined_number = int(first_num + last_num)
           array.append(combined_number)

    print(sum(array))

p2()

