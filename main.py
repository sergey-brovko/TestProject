import re
def find_sub_qty(string, sub):
    count = 0
    for x in range(len(string) - len(sub) +1):
        if string[x:x + len(sub)] == sub:
            count += 1
    return count

def minion_game(string):
    string = string.strip()
    Vowels = 'AEIOU'
    stuart = {}
    kevin = {}
    for i in range(1,len(string)+1):
        for j in range(len(string)):
            sub_string = string[j:j+i]
            if (sub_string not in stuart) and (string[j] not in Vowels):
                stuart[sub_string] = find_sub_qty(string, sub_string)
            elif (sub_string not in kevin) and (string[j] in Vowels):
                kevin[sub_string] = find_sub_qty(string, sub_string)
    score_stuart = sum(stuart.values())
    score_kevin = sum(kevin.values())
    if score_stuart > score_kevin:
        print (f"Stuart {score_stuart}")
    if score_stuart < score_kevin:
        print (f"Kevin {score_kevin}")
    if score_stuart == score_kevin:
        print ('Draw')
# patern = re.compile('ANA')
# print(patern.search('BANANA').span()[0])
# print(patern.search('BANANA', 2))
# print (find_sub_qty('BANANA', 'ANA'))
minion_game('BANANA')