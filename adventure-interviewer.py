def intro():
    print('A wonderful opportunity to save the planet was '
          'offered to me.')
    print('This opportunity involves meat.')
    print('Green Peace is asking me to tackle meat production.')
    print('The scientific research looks at two following areas')
    print('that have shown all kinds of threats to the globe.\n')
    print('The Environment:')
    print('  Worldwide confined animal feedlot operations (CAFO)'
          ' contribute to greenhouse gases.')
    print('  Water supply')
    print('The Human health:')
    print('  Colon cancer')
    print('  Liver cancer')
    print('  Heart fai')
    print('  Kidney stones')
    print('  Arthritis\n')
    print('Plan for action:')
    print('A)Start an awareness campaign for the planet\'s meat production.')
    print('  Social media campaigning')
    print('  Education')
    print('  Radio and TV')
    print('  Talks and interviews\n')
    print('B)Relate myself with farmers aligned with'
          ' holistic natural livestock production')
    print('  Environmental Agencies')
    print('  Boycott CAFOs\n')
    print('You are consolidating new and updated information for your research')
    print('You are going to be dealing with x company')
    print('You can have an interview with x company')
    print('Or investigate x company \n')


def interview():
    print('Manager:     How are you, Im the manager '
          'welcome to x company , what can I do for you ?')
    print('interviewer: Thank you, \n'
          '             I work for Green Peace and')
    print('             I have some questions about x company'
          ' food and water supply ?\n')
    print('             In average how many gallons of water does'
          ' the stock consumes per year ?')
    print('             Is all your stock been feed '
          'with Monsanto products ?')
    print('             In order to deliver your products '
          'how many miles does your\n'
          '             trucks travel in one year ?\n')
    print('Manager:     There is nothing to say, we are in complaint')
    print('             with all the meat regulations, inspections and')
    print('             standards, all the answers to your'
          ' questions are published')
    print('             on our website. Please don\'t waist my time')
    print('interviewer: My question is not about regulations')
    print('             but research shows that surrounding communities')
    print('             are having shortage of water')
    print('             and their agriculture has been affected hello?')
    print('')
    print('Manager:     Abruptly goes back to his office '
          'and does\'t want a talk to you.')
    print('interviewer: You keep asking but no answers.\n')
    keep_questioning()


def investigation():
    print('  You secretly go in disguise\n'
          '  to x company headquarters')
    print('  With your false ID you enter the building\n'
          '  and enter into the manager\'s office .')
    print('  To your surprise you find a mad cow'
          ' wandering by the manager\'s desk\n'
          '  eating paper from the trash.')
    print('  On the wall were pictures of x pics')
    print('  playing  x mutations.\n'
          '  Wow I always wanted to play the x mutations !')
    print('  while you are in shock, you open\n'
          '  the manager\'s computer and copy all'
          ' the files you needed.')
    print('  You exit without incident but after\n'
          '  seeing the x pics playing the\n x mutations'
          ' you got inspired\n'
          '  and start thinking to learn how to play an instrument.\n'
          '  You completed your mission.\n')
    investigating_again()


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print("Sorry, I don't understand.")
    return response


def strategy():
    questions = valid_input('Enter 1 to interview.\n'
                            'Enter 2 to investigate.\n'
                            'What would you like to do?\n'
                            '(Please enter 1 or 2.)\n',
                            '1', '2')
    if '1' in questions:
        interview()
    if '2' in questions:
        investigation()


def keep_questioning():
    questions = valid_input('Would you like to (1)'
                            'keep questioning (2) or not now ?\n', '1', '2')
    if '1' in questions:
        print('You know that the questions were bold and'
              ' as a result no answers were gathered.')
        print('Security from  x company'
              ' escorts you out of the building.\n')
        strategy()
    if '2' in questions:
        print('You know that you need to prepare better and you'
              ' go back to your office.\n')
        strategy()


def investigating_again():
    questions = valid_input('Enter 1 to interview x company.\n'
                            'Enter 2 to investigate x company.\n'
                            'What would you like to do?\n'
                            '(Please enter 1 or 2.)\n', '1', '2')
    if '1' in questions:
        print('You are now back to x company'
              ' and you are ready for justice.')
        print('You are not welcome into x company')
        print('but you walk in with a Class Action Law Suit'
              ' and they want to settle')
        print('You Won Congratulations!')
    if '2' in questions:
        print('You make the mistake of going back to x company')
        print('and they have surveillance video footage on you '
              'from your first investigation, '
              'they put you in jail for trespassing\n'
              'and robbery!\n')
        yes_no()


def yes_no():
    questions = valid_input('Would you like to play again ?(y/n)\n', 'y', 'n')
    if 'n' in questions:
        print('Thank you for Playing\n')
    if 'y' in questions:
        print('Ok Restarting the game')
        intro()
        strategy()


intro()

strategy()
