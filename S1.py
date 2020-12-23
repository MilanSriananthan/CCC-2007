def answer(seq):
    if int(seq[0]) < 1989:
        return  "Yes"
    if int(seq[0]) > 1989:
        return "No"
    if int(seq[1]) > 2:
        return "No"
    if int(seq[1]) == 1:
        return "Yes"
    if int(seq[2]) < 28:
        return "Yes"
    return "No"
cases = int(input())
for i in range(cases):
    date = input()
    date = date.split(" ")
    print(answer(date))