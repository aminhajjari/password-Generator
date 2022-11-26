import random
import string
import os
import datetime

settings = {
    'lower' : True,
    'upper' : True,
    'symbols' : True,
    'number' : True ,
    'space' : False ,
    'length' : 8

}


PASSWORD_MIN_LENGTH = 4
PASSWORD_MAX_LENGTH = 30

def clear_screen():
    os.system('cls')


def welcome_message():
    print('Hello.welcome to Password Generator.')
    print('enjoy the app')
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%d-%m %H:%M:%S"))
    print('-'*25)


def get_user_length_of_password(option, default,
                     pw_min_length=PASSWORD_MIN_LENGTH, pw_max_length=PASSWORD_MAX_LENGTH):

    while True:
        user_input = input('Enter length of password. '
                            f'Default is {default},(Enter : Defualt): ')
        
        if user_input == '':
            return default
        
        if user_input.isdigit() :
            user_password_length = int(user_input)
            if  4<= user_password_length <= 30:
                return int(user_input)
            else:
                print('invalid input. length of password should be'
                        f' between {pw_min_length} and {pw_max_length}')
        else:

            print('Invalid input,you should input a number.')
        print('Try again please')




def get_yes_or_no_from_user(option, default):

    while True:
        user_input = input(f'inculd {option}?  defualt is {default} ,' 
                            '(yes= y, no= n, enter : defualt): ')

        if user_input == '':
            return default

        if user_input in ['y','n']:
            return user_input == 'y'
  
        print('Invalid input! please input again')




def input_settings(settings):

    for option , default in settings.items():
        if option != 'length':
            user_choice = get_yes_or_no_from_user(option, default)
            settings[option] = user_choice
        else:
            user_length = get_user_length_of_password(option, default)
            settings[option] = user_length

 

def ask_setting_change(settings):
    while True:
        user_choose = input('Do you want change settings? (y:yes, n:no, Enter:yes): ')
        if user_choose in ['y', 'n', '']:
            if user_choose in ['y', '']:
                print('-'*5, 'Change Setting','-'*5, sep='')
                input_settings(settings)
            break
        else:
            print('invalid input.(choose from yes:y, no:n, Enter:yes)')
            print('please try again.')




def password_generator_random_char(choices):
    choice = random.choice(choices)

    if choice == 'upper':
        return random.choice(string.ascii_uppercase)
    if choice == 'lower':
        return random.choice(string.ascii_lowercase)
    if choice == 'symbols':
        return random.choice(string.punctuation)
    if choice == 'number':
        return random.choice(string.digits)
    if choice == 'space':
        return ' '





def paaword_generator(settings):
    final_pass = ''
    
    password_length = settings['length']
    
    choices = list(filter(lambda x: settings[x],['lower','upper','symbols','space','number']))
    
        
    

    for i in range(password_length):
        final_pass += password_generator_random_char(choices)

    return final_pass


def ask_user_regenerator():
    while True:
        user_answer = input('Regenerator? (yes:y, no:n, Enter:yes): ')
        
        if user_answer in ['y', 'n','']:
            if user_answer == 'n':
                return False
            return True
        else:
            print('invalid input.(choose from yes:y, no:n, Enter:yes)')
            print('please try again.')
            
            
        


            
def password_generator_loop(settings):
    while True:
        print('-'*20)
        print(f'Generator password is: {paaword_generator(settings)}')

        if ask_user_regenerator() == False:
            break
        
               



      
        
def run():

    clear_screen()
    welcome_message()
    ask_setting_change(settings)
    password_generator_loop(settings)
    print('Thanks for choose us.')
    

run()

    