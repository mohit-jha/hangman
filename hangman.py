import random
def play_again():
    again=input("do yo want to play again yes/no >>>)").lower()
    if again =="y" or "yes":
        play_game()
    else:
        print("thanks for plays")
        pass
def is_word_guessed():
    names=['mohit','himanshu','sushant','abhishek','rohit','santosh','taarik','shakti','kaushal'] 
    return random.choice(names)


def play_game():
    name=is_word_guessed()
    a='abcdefghijklmnopqrstuvwxyz'
    user_c=[]
    user_w=[]
    tryies=2
    guessed=0
    # print(list(name))
    print("the_word_contain",len(name),"letter")
    print(len(name)*"*")
    
    # status=''
    while guessed==False and tryies>0:
        user=input("enter a word or letter>>  ")
        print("no. of tryies is left",tryies)
        if list(name)==user_c:
                print('your gussing is right answer is>>>>)',name)
                break
        if len(user)==1:
            if user not in a:
                print("u r not entering a word or letter")
            
            elif user in user_c:
                print("u r already enter this")
            elif user in name:
                print("well try") 
                user_c.append(user)               
            elif user not in name:
                print("sorry that letter is not part of word")
                user_c.append(user)
                print('this is not in gussing letter>>')
                tryies-=1
        elif len(user)==len(name):
            if user==name:
                print("u r right your gussing is right",name)
                break
            elif user!=name:
                print("wrong")
                tryies-=1
        else:
            print("your len of choose were not same as we gave")
       
        status = ''
        if guessed==0:
            for i in name:
                if i in user_c:
                    status=status+i
                else:
                    status+='-'
            print(status)

        if status==name:
            print("well done(")
            guessed=1
        elif tryies==0:
            print("you are not having tryies")
    play_again()
play_game()
