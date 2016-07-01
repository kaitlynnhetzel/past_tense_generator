#this program generates the past tense of a word

#these verbs are ones with irregular past tenses 
irregular_forms =  {"go": "went","buy": "bought", "break": "broke", "sit": "sat", "come":"came", "eat": "ate", "sleep": "slept", "see": "saw", "pay": "paid", "sing": "sang", "tell": "told", "get": "got", "teach": "taught", "feel": "felt",
"hear": "heard", "understand": "understood", "is": "was"}

#these verbs are the same in both the present and pass tense 
single_forms =  ["cut", "put", "let", "hurt", "quit", "read", "broadcast", "hit", "cost", "spread"]

#a vowel list, for reference
vowels = ['a','e','i','o','u','y']

#suffixes of root words that will never be repeated
end_hushers = ["x", "lk", "sh", "ch", "ck", "h", "k", "nt", "lp", "wn"]
def needsDoubleConsonant(verb):
    count = 0
    for letter in verb:
        if letter in vowels:
            count = count + 1

    if count > 1:
        return False
    else:
        last_two = verb[len(verb)-2] + verb[len(verb)-1]
        last = verb[len(verb)-1]
        #if the last letter is one that will never be repeated
        if last in end_hushers:
            return False
        #if the suffix of the word will never need a repeated letter
        elif last_two in end_hushers:
            return False
        #if the last two letters of the verb are already a repeated letter
        elif last == verb[len(verb)-2] :
            return False
        return True

#repeat until user is finished
while True:
    to_past = input("What is your verb? (Type EXIT to quit): ")
    #exit case
    if to_past == "EXIT":
        print ("Thanks for using my program. Goodbye!")
        break
    #checking irregular verbs
    elif to_past.lower() in irregular_forms:
        print (irregular_forms[to_past.lower()])
    #checking single-form verbs
    elif to_past.lower() in single_forms:
        print (to_past.lower())
    #checking for a verb ends in 'e' - slightly special case
    elif to_past[len(to_past) -1] == 'e':
        to_past = to_past + "d"
        print(to_past)
    #checking special case if verb ends in a y
    elif to_past[len(to_past) - 1] == 'y':
        
        if to_past[len(to_past) - 2] in vowels:
            to_past = to_past + "ed"
            print (to_past)
        else:
            temp = list(to_past)
            temp[len(to_past)-1] = 'i'
            to_past = "".join(temp)
            to_past = to_past + "ed"
            print (to_past)
    #checking if verb needs a repeated consonant before "ed"
    elif needsDoubleConsonant(to_past):
        to_past = to_past + to_past[len(to_past) -1] + "ed"
        print (to_past)
    #typical case - just add "ed"       
    else:
        to_past = to_past + "ed"
        print (to_past)

