def minion_game(string):
    vowels= "AEIOU"
    kevin_words={}
    stuart_words={}
    length = len(string)
    for i in range(length):
       for j in range(i+1,length+1):
         sub_string = string[i:j]
         if string[i] in vowels:
            kevin_words[sub_string] = kevin_words.get(sub_string,0)+1
         else:
            stuart_words[sub_string] = stuart_words.get(sub_string,0)+1
    kevin_score= sum(kevin_words.values())
    stuart_score = sum(stuart_words.values())
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score>kevin_score:
        print(f"Stuart {stuart_score}") 
    else:
        print("Its a draw.")   
        
            
if __name__ == '__main__':
    s = input()
    minion_game(s)