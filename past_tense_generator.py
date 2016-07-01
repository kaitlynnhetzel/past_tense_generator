#this program generates the past tense of a word

#these verbs are ones with irregular past tenses 
irregular_forms =  {"go": "went","buy": "bought", "break": "broke", "sit": "sat", "come":"came", "eat": "ate", "sleep": "slept", "see": "saw", "pay": "paid", "sing": "sang", "tell": "told", "get": "got", "teach": "taught", "feel": "felt",
"hear": "heard"}

#these verbs are the same in both the present and pass tense 
single_forms =  ["cut", "put", "let", "hurt", "quit", "read", "broadcast", "hit", "cost", "spread"]

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
        vowels = ['a','e','i','o','u','y']
        if to_past[len(to_past) - 2] in vowels:
            to_past = to_past + "ed"
            print (to_past)
        else:
            temp = list(to_past)
            temp[len(to_past)-1] = 'i'
            to_past = "".join(temp)
            to_past = to_past + "ed"
            print (to_past)
    #typical case - just add "ed"       
    else:
        to_past = to_past + "ed"
        print (to_past)
