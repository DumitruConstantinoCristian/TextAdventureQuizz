runnning=True
while runnning:

    print('Hi welcome to the E-SAFETY quiz!')
    print('Im going to ask you some questions!')
    print('You ll have 3 choices,pick the one that you think is correct,also you ll have 3 lives for every wrong answer im going to substract 1 ')
    print('if you reach 0 lives you ll lose!')
    print('Now imput your name so we can start')
    name=input()

    lives=3

    print('Why is important to create strong passwords online?')
    print('A:To impress friends')
    B=print('B: To make it harder for hackers to guess')
    print('C:To remember them easily')
    answer=input()
    if answer== 'b':
        print(f'GOOD JOB {name} you re right!')
    
    
    
    else:
        print('im sorry you re wrong')
        lives-=1
        print(f'you have {lives} lives left')

    next=input('press any key to continue:')

    print('When chatting online, what information should you never share with strangers?')
    print('A:Your favorite movie')
    B=print('B:Personal information like home address and phone number')
    print('C: Your pets name')
    answer2=input()
    if answer2== 'b':
          print(f'GOOD JOB {name} you re right!')
    else:
        print('im sorry you re wrong')
        lives-=1
        print(f'you have {lives} lives left')

    next2=input('press any key to continue:')
    if lives>0:
        print('What should you do if you receive an unsolicited message from someone you dont know on social media?')
        A=print('A:Reply with your personal information')
        B=print('B:Accept the message and start chatting')
        C=print('C:Decline or ignore and report the profile ')
        answer3=input()
        if answer3=='c':
             print(f'GOOD JOB {name} you re right!')
        else:
            print('im sorry you re wrong')
            lives-=1
            print(f'you have {lives} lives left')

    

    if lives<0:
        
  
    
        print('What is two-factor authentication (2FA) used for?')
        A=print('A:To share your password with someone else')
        B=print('B:To add an extra layer of security to your accounts')
        C=print('C:To simplify account access ')
        answer4=input()
        if answer4=='b':
             print(f'GOOD JOB {name} you re right!')
        else:
            print('im sorry you re wrong')
            lives-=1
            print(f'you have {lives} lives left')

    

    if lives>0:
        print('Why should you be cautious when downloading files from the internet?')
        A=print('A:Files from the internet are always safe')
        B=print('B:Downloaded files can contain malware or viruses')
        C=print('C:To support the internet ')
        answer5=input()
        if answer5=='b':
             print(f'GOOD JOB {name} you re right!')
        else:
            print('im sorry you re wrong')
            lives-=1
            print(f'you have {lives} lives left')

    
    if lives>0:
        print(' What does the acronym URL stand for?')
        A=print('A: Uniform Resource Locator')
        B=print('B:Universal Registration Link')
        C=print('C:United Resource Locator ')
        answer6=input()
        if answer6=='a':
             print(f'GOOD JOB {name} you re right!')
        else:
            print('im sorry you re wrong')
            lives-=1
            print(f'you have {lives} lives left')

    

    if lives>0:
        print(' What is phishing in the context of online security?')
        A=print('A:A way to catch fish online ')
        B=print('B:An email from a close friend')
        C=print('C:A cyberattack to trick individuals into revealing sensitive information')
        answer7=input()
        if answer7=='c':
             print(f'GOOD JOB {name} you re right!')
        else:
            print('im sorry you re wrong')
            lives-=1
            print(f'you have {lives} lives left')
    if lives>0:
        print(f'WELL DONE {name}!You finished the quiz with {lives} lives left')
        option=input('Do you want to try again? y/n: ')
    else:
        print('YOU RAN OUT OF LIVES')
        option=input('Do you want to try again? y/n: ')
        if option.lower() == 'y':
            runnning=True
        elif option.lower() == 'n':
            break







   


    


    
