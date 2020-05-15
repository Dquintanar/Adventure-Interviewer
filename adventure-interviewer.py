import random
import time


def print_pause(story):
    print(story)
    time.sleep(2)


bad_companies = ['"Tyson Foods"',
                 '"Cargill and Smithfield"',
                 '"JBS USA Holdings Inc"',
                 '"Omaha Steaks"',
                 '"Taco Loco"', ]

pictures = ['the Queen mutating to a mosquito',
            'Oprah on a Koala body',
            'Trump\'s hair in a pig',
            'chickens with human faces',
            'pigs with wings', ]

instruments = ['trombone',
               'trumpet',
               'viola',
               'electric base',
               'drums',
               'two tubas at the same time', ]
companies = random.choice(bad_companies)
pics = random.choice(pictures)
instrument = random.choice(instruments)


def intro():
    print_pause('A wonderful opportunity to save the planet was '
                'offered to me.')
    print_pause('This opportunity involves meat.')
    print_pause('Green Peace is asking me to tackle meat production.')
    print_pause('The scientific research looks at two following areas')
    print_pause('that have shown all kinds of threats to the globe.\n')
    print_pause('The Environment:')
    print_pause('  Worldwide confined animal feedlot operations (CAFO)'
                ' contribute to greenhouse gases.')
    print_pause('  Water supply')
    print_pause('The Human health:')
    print_pause('  Colon cancer')
    print_pause('  Liver cancer')
    print_pause('  Heart fai')
    print_pause('  Kidney stones')
    print_pause('  Arthritis\n')
    print_pause('Plan for action:')
    print_pause('A)Start an awareness campaign for the planet\'s meat production.')
    print_pause('  Social media campaigning')
    print_pause('  Education')
    print_pause('  Radio and TV')
    print_pause('  Talks and interviews\n')
    print_pause('B)Relate myself with farmers aligned with'
                ' holistic natural livestock production')
    print_pause('  Environmental Agencies')
    print_pause('  Boycott CAFOs\n')
    print_pause('You are consolidating new and updated information for your research')
    print_pause('You are going to be dealing with ' + companies)
    print_pause('You can have an interview with ' + companies)
    print_pause('Or investigate ' + companies + '\n')


def interview():
    print_pause('Manager:     How are you, Im the manager '
                'welcome to' + companies + ' , what can I do for you ?')
    print_pause('interviewer: Thank you, \n'
                '             I work for Green Peace and')
    print_pause('             I have some questions about ' + companies +
                ' food and water supply ?\n')
    print_pause('             In average how many gallons of water does'
                ' the stock consumes per year ?')
    print_pause('             Is all your stock been feed '
                'with Monsanto products ?')
    print_pause('             In order to deliver your products '
                'how many miles does your\n'
                '             trucks travel in one year ?\n')
    print_pause('Manager:     There is nothing to say, we are in complaint')
    print_pause('             with all the meat regulations, inspections and')
    print_pause('             standards, all the answers to your'
                ' questions are published')
    print_pause('             on our website. Please don\'t waist my time')
    print_pause('interviewer: My question is not about regulations')
    print_pause('             but research shows that surrounding communities')
    print_pause('             are having shortage of water')
    print_pause('             and their agriculture has been affected hello?')
    print('')
    print_pause('Manager:     Abruptly goes back to his office '
                'and does\'t want a talk to you.')
    print_pause('interviewer: You keep asking but no answers.\n')
    keep_questioning()


def investigation():
    print_pause('  You secretly go in disguise\n'
                '  to ' + companies + ' headquarters')
    print_pause('  With your false ID you enter the building\n'
                '  and enter into the manager\'s office.')
    print_pause('  To your surprise you find a mad cow'
                ' wandering by the manager\'s desk\n'
                '  eating paper from the trash.')
    print_pause('  On the wall were pictures of ' + pics)
    print_pause('  playing ' + instrument + '.\n'
                '  Wow I always wanted to play the ' + instrument + '!')
    print_pause('  while you are in shock, you open\n'
                '  the manager\'s computer and copy all'
                ' the files you needed.')
    print_pause('  You exit without incident but after\n'
                '  seeing ' + pics + ' playing the\n ' + instrument +
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
            print_pause("Sorry, I don't understand.")
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
        print_pause('You know that the questions were bold and'
                    ' as a result no answers were gathered.')
        print_pause('Security from ' + companies +
                    ' escorts you out of the building.\n')
        strategy()
    if '2' in questions:
        print_pause('You know that you need to prepare better and you'
                    ' go back to your office.\n')
        strategy()


def investigating_again():
    questions = valid_input('Enter 1 to interview ' + companies + '.\n'
                            'Enter 2 to investigate ' + companies + '.\n'
                            'What would you like to do?\n'
                            '(Please enter 1 or 2.)\n', '1', '2')
    if '1' in questions:
        print_pause('You are now back to ' + companies +
                    ' and you are ready for justice.')
        print_pause('You are not welcome into ' + companies)
        print_pause('but you walk in with a Class Action Law Suit'
                    ' and they want to settle')
        print_pause('You Won Congratulations!')
    if '2' in questions:
        print_pause('You make the mistake of going back to ' + companies)
        print_pause('and they have surveillance video footage on you '
                    'from your first investigation, '
                    'they put you in jail for trespassing\n'
                    'and robbery!\n')
        you_loose()
        yes_no()


def yes_no():
    questions = valid_input('Would you like to play again ?(y/n)\n', 'y', 'n')
    if 'n' in questions:
        print_pause('Thank you for Playing\n')
    if 'y' in questions:
        print_pause('Ok Restarting the game')
        intro()
        strategy()


def you_loose():
    print_pause('You loose')


def adventure_game():
    intro()
    strategy()



adventure_game()
