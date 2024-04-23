
def find_sub_qty(string, sub):
    index = -1
    indices =0
    while True:
        index = string.find(sub, index + 1)
        if index == -1:
            break
        indices +=1
    return indices

def minion_game(string):
    string = string.strip()
    Vowels = 'AEIOU'
    stuart = {}
    kevin = {}
    for i in range(1,len(string)+1):
        for j in range(len(string)):
            sub_string = string[j:j+i]
            if (string[j] not in Vowels) and (sub_string not in stuart):
                stuart[sub_string] = find_sub_qty(string, sub_string)
            if (string[j] in Vowels) and (sub_string not in kevin):
                kevin[sub_string] = find_sub_qty(string, sub_string)
    if sum(stuart.values()) > sum(kevin.values()):      
        return f"Stuart {sum(stuart.values())}"
    if sum(stuart.values()) < sum(kevin.values()):
        return f"Kevin {sum(kevin.values())}"
    if sum(stuart.values()) == sum(kevin.values()):
        return 'Draw'
    
print(minion_game('BANANA'))