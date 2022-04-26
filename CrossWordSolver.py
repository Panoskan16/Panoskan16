
from wordsplitter import words_list
english_letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# multiple lists will be used in order to filter the words
words_true_letter=[]
words_first_letter=[]
words_second_letter=[]
words_third_letter=[]
words_fourth_letter=[]
words_fifth_letter=[]
words_sixth_letter=[]
words_seventh_letter=[]
words_eighth_letter=[]
words_ninth_letter=[]
words_tenth_letter=[]
words_eleventh_letter=[]
words_twelfth_letter=[]
words_thirteenth_letter=[]
words_fourteenth_letter=[]
words_fifteenth_letter=[]
words_sixteenth_letter=[]
words_seventeenth_letter=[]
words_eighteenth_letter=[]
words_nineteenth_letter=[]
words_twentieth_letter=[]

def Crossword_solver(list_already_in,list_next_in,already_have_word_length=True, word_length=1):
    #Check if this variable has been changed so to skip word length in next times as its already given by the user 
    if already_have_word_length==False:
        word_length=input('How many letters does your word you search for have? ')
        while word_length.isnumeric()==False:
            print('Please, add a valid number of letters for this word')
            word_length=input('How many letters does your word you search for have? ')
        for item in words_list:
            if len(item)==int(word_length):
                words_true_letter.append(item)
    
    # Check if the user has decided that has no other clues so to show him only the possible words not these steps again 
    answer_in_or_out_word=input("1.You know this letter is in this word or 2.You know this letter isn't in this word? Please answer for 1 or 2 only For example: 1 ")
    while answer_in_or_out_word not in ['1','2']:
        print("Please add a valid number between 1 or 2  ")
        answer_in_or_out_word=input("1.You know this letter is in this word or 2.You know this letter isn't in this word?  ")
    if answer_in_or_out_word=="1":
        letter=input("Add the letter you know the word have, for example: a   ")
        while letter.isnumeric():
            print("Please add a valid letter")
            letter=input("Add the letter you know the word have, for example: a   ")
        letter=letter.lower()
        # Check that the letter given is valid
        while letter not in english_letters :
            print("Please add only one letter,if you want to add more than 1 letters you will do it later  " )
            letter=input("Add the letter you know the word have, for example: a  ")
        # Ask the user whether we he will use letter's position or not
        answer_place=input("Do you know this letter place ? Write y for yes or n for no  ")
        while answer_place.isnumeric():
            print("Please add a valid answer")
            answer_place=input("Do you know this letter place ? Write y for yes or n for no  ")
        answer_place=answer_place.lower()
            
        # Find all the words that has the letter given in the position given
        if answer_place in ['y','yes']:
            letter_place=input("Now add only the number of the letter's place in word, for example: 1   ")
            while letter_place.isnumeric()==False:
                print("Please add a valid number for letter's place")
                letter_place=input("Add only the number of the letter's place in word, for example: 1   ")
            letter_place=int(letter_place)-1
            word_length=len(list_already_in[1])
            while int(letter_place)> int(word_length) :
                print("Please add a valid number for letter's place")
                letter_place=input("Add only the number of the letter's place in word, for example: 1   ")
                letter_place=int(letter_place)-1
            for item in list_already_in:
                if item[letter_place]==letter:
                    list_next_in.append(item)
        # Find all the words that has the letter given 
        else:
            answer_not_place=input("Do you know a place where this letter isn't in this word? Write y for yes and n for no  ")
            while answer_not_place.isnumeric():
                print("Please add a valid answer")
                answer_not_place=input("Do you know a place where this letter isn't in this word? Write y for yes and n for no  ")
            answer_not_place=answer_not_place.lower()
            if answer_not_place in ["yes","y"]:
                letter_place=input("Now add only the number of the place this letter isnt in the word  , for example: 1   ")
                letter_place=int(letter_place)-1
                for item in list_already_in:
                        if letter not in item[letter_place] and letter in item:
                            list_next_in.append(item)
                
            else:    
                for item in list_already_in:
                    if letter in item:
                        list_next_in.append(item)
    elif answer_in_or_out_word=="2":
        letter=input("Add the letter you know the word don't have, for example: a   ")
        letter=letter.lower()
        # Check that the letter given is valid
        while letter not in english_letters :
            print("Please add only one letter,if you want to add more than 1 letters you will do it later  " )
            letter=input("Add the letter you know the word don't have, for example: a  ")
    
        # Find all the words that dont have the letter given 
        for item in list_already_in:
            if letter  not in item:
                list_next_in.append(item)

        
        
        
# variable helping count on what list the last results of words have been    
times_function_past=0
# Function takes three arguments 1.on what list latest results of words are,2. on what list new filtered results to go, 3.Whether to ask for letters of word or not if its already given
Crossword_solver(words_true_letter,words_first_letter,already_have_word_length=False,word_length=5)
times_function_past=times_function_past+1
answer=input("Do you have any other letters to add? y for yes or n for no  ")
answer=answer.lower()
#These ifs give the option to use to give from 1 to 10 letters to help computer find the word
if answer in ['y','yes']:
    Crossword_solver(words_first_letter, words_second_letter, word_length=len(words_true_letter[1]))
    times_function_past=times_function_past+1
    answer=input("Do you have any other letters to add? y for yes or n for no  ")
    answer=answer.lower()
    if answer in ['y','yes']:
        Crossword_solver(words_second_letter ,words_third_letter, word_length=len(words_true_letter[1]))
        times_function_past=times_function_past+1
        answer=input("Do you have any other letters to add? y for yes or n for no  ")
        answer=answer.lower()
        if answer in ['y','yes']:
            Crossword_solver(words_third_letter,words_fourth_letter, word_length=len(words_true_letter[1]))
            times_function_past=times_function_past+1
            answer=input("Do you have any other letters to add? y for yes or n for no  ")
            answer=answer.lower()
            if answer in ['y','yes']:
                Crossword_solver(words_fourth_letter,words_fifth_letter, word_length=len(words_true_letter[1]))
                times_function_past=times_function_past+1
                answer=input("Do you have any other letters to add? y for yes or n for no  ")
                answer=answer.lower()
                if answer in ['y','yes']:
                    Crossword_solver(words_fifth_letter,words_sixth_letter, word_length=len(words_true_letter[1]))
                    times_function_past=times_function_past+1
                    answer=input("Do you have any other letters to add? y for yes or n for no  ")
                    answer=answer.lower()
                    if answer in ['y','yes']:
                        Crossword_solver(words_sixth_letter,words_seventh_letter, word_length=len(words_true_letter[1]))
                        times_function_past=times_function_past+1
                        answer=input("Do you have any other letters to add? y for yes or n for no  ")
                        answer=answer.lower()
                        if answer in ['y','yes']:
                            Crossword_solver(words_seventh_letter,words_eighth_letter,word_length=len(words_true_letter[1]))
                            times_function_past=times_function_past+1
                            answer=input("Do you have any other letters to add? y for yes or n for no  ")
                            answer=answer.lower()
                            if answer in ['y','yes']:
                                Crossword_solver(words_eighth_letter,words_ninth_letter, word_length=len(words_true_letter[1]))
                                times_function_past=times_function_past+1
                                answer=input("Do you have any other letters to add? y for yes or n for no  ")
                                answer=answer.lower()
                                if answer in['yes','y']:
                                    Crossword_solver(words_ninth_letter,words_tenth_letter, word_length=len(words_true_letter[1]))
                                    times_function_past=times_function_past+1
                                    answer=input("Do you have any other letters to add? y for yes or n for no  ")
                                    answer=answer.lower()
                                    if answer in ['y','yes']:
                                        Crossword_solver(words_tenth_letter ,words_eleventh_letter, word_length=len(words_true_letter[1]))
                                        times_function_past=times_function_past+1
                                        answer=input("Do you have any other letters to add? y for yes or n for no  ")
                                        answer=answer.lower()
                                        if answer in ['y','yes']:
                                            Crossword_solver(words_eleventh_letter,words_twelfth_letter,word_length=len(words_true_letter[1]))
                                            times_function_past=times_function_past+1
                                            answer=input("Do you have any other letters to add? y for yes or n for no  ")
                                            answer=answer.lower()
                                            if answer in ['y','yes']:
                                                Crossword_solver(words_twelfth_letter,words_thirteenth_letter,word_length=len(words_true_letter[1]))
                                                times_function_past=times_function_past+1
                                                answer=input("Do you have any other letters to add? y for yes or n for no  ")
                                                answer=answer.lower()
                                                if answer in ['y','yes']:
                                                    Crossword_solver(words_thirteenth_letter,words_fourteenth_letter, word_length=len(words_true_letter[1]))
                                                    times_function_past=times_function_past+1
                                                    answer=input("Do you have any other letters to add? y for yes or n for no  ")
                                                    answer=answer.lower()
                                                    if answer in ['y','yes']:
                                                        Crossword_solver(words_fourteenth_letter,words_fifteenth_letter, word_length=len(words_true_letter[1]))
                                                        times_function_past=times_function_past+1
                                                        answer=input("Do you have any other letters to add? y for yes or n for no  ")
                                                        answer=answer.lower()
                                                        if answer in ['y','yes']:
                                                            Crossword_solver(words_fifteenth_letter,words_sixteenth_letter, word_length=len(words_true_letter[1]))
                                                            times_function_past=times_function_past+1
                                                            answer=input("Do you have any other letters to add? y for yes or n for no  ")
                                                            answer=answer.lower()
                                                            if answer in ['y','yes']:
                                                                Crossword_solver(words_sixteenth_letter,words_seventeenth_letter, word_length=len(words_true_letter[1]))
                                                                times_function_past=times_function_past+1
                                                                answer=input("Do you have any other letters to add? y for yes or n for no  ")
                                                                answer=answer.lower()
                                                                if answer in['yes','y']:
                                                                    Crossword_solver(words_seventeenth_letter,words_eighteenth_letter, word_length=len(words_true_letter[1]))
                                                                    times_function_past=times_function_past+1
                                                                    answer=input("Do you have any other letters to add? y for yes or n for no  ")
                                                                    answer=answer.lower()
                                                                    if answer in ['y','yes']:
                                                                        Crossword_solver(words_eighteenth_letter,words_nineteenth_letter, word_length=len(words_true_letter[1]))
                                                                        times_function_past=times_function_past+1
                                                                        answer=input("Do you have any other letters to add? y for yes or n for no  ")
                                                                        answer=answer.lower()
                                                                        if answer in ['y','yes']:
                                                                            Crossword_solver(words_nineteenth_letter,words_twentieth_letter, word_length=len(words_true_letter[1]))
                                                                            times_function_past=times_function_past+1
                                                                            
# With the help of the following variable finds out what list have the final results to print it out 
if times_function_past==1:
        print('words_first_letter: ',words_first_letter)
elif times_function_past==2:
    print('words_second_letter: ',words_second_letter)
elif times_function_past==3:
    print('words_third_letter: ',words_third_letter)
elif times_function_past==4:
    print('words_fourth_letter: ',words_fourth_letter)
elif times_function_past==5:
    print('words_fifth_letter: ',words_fifth_letter)
elif times_function_past==6:
    print('words_sixth_letter: ',words_sixth_letter)
elif times_function_past==7:
    print('words_seventh_letter: ',words_seventh_letter)
elif times_function_past==8:
    print('words_eighth_letter: ',words_eighth_letter)
elif times_function_past==9:
    print('words_ninth_letter: ',words_ninth_letter)
elif times_function_past==10:
    print('words_tenth_letter: ',words_tenth_letter)
elif times_function_past==11:
        print('words_eleventh_letter: ',words_eleventh_letter)
elif times_function_past==12:
    print('words_twelfth_letter: ',words_twelfth_letter)
elif times_function_past==13:
    print('words_thirteenth_letter: ',words_thirteenth_letter)
elif times_function_past==14:
    print('words_fourteenth_letter: ',words_fourteenth_letter)
elif times_function_past==15:
    print('words_fifteenth_letter: ',words_fifteenth_letter)
elif times_function_past==16:
    print('words_sixteenth_letter: ',words_sixteenth_letter)
elif times_function_past==17:
    print('words_seventeenth_letter: ',words_seventeenth_letter)
elif times_function_past==18:
    print('words_eighteenth_letter: ',words_eighteenth_letter)
elif times_function_past==19:
    print('words_nineteenth_letter: ',words_nineteenth_letter)
elif times_function_past==20:
    print('words_twentieth_letter: ',words_twentieth_letter)
    
