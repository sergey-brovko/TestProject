def find_sub_qty(string, sub):
    count = 0
    for x in range(len(string) - len(sub) +1):
        if string[x:x + len(sub)] == sub:
            count += 1
    return count

def minion_game(string):
    string = string.strip()
    Vowels = 'AEIOU'
    stuart = set()
    kevin = set()
    for i in range(len(string)):
        for j in range(len(string)-i):
            sub_string = string[j:j+i+1]
            if string[j] not in Vowels:
                stuart.add(sub_string)
            else:
                kevin.add(sub_string)
    score_stuart = sum([ find_sub_qty(string, sub) for sub in stuart])
    score_kevin = sum([ find_sub_qty(string, sub) for sub in kevin])
    if score_stuart > score_kevin:
        print (f"Stuart {score_stuart}")
    if score_stuart < score_kevin:
        print (f"Kevin {score_kevin}")
    if score_stuart == score_kevin:
        print ('Draw')
minion_game('BANANA')