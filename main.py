'''
Program from dead inside and ghouls

Created By --->
--- CoilGames ---
'''

from time import sleep  #  ---> From Delay Code

verification_user = input('You Ghoul SSS+ Rank and Dead Inside? (yes or no)\n\n')
if verification_user.lower() == 'yes':
    default_sum = 993
    start_program = input('1000-7?\n\n Answer: ')  # ---> Checking User Ghoul He
    if start_program == '993':
        while default_sum != 6:
            default_sum = default_sum - 7  # ---> New Sum Value
            answer_sum = default_sum - 7  # ---> Answer Sum
            print(default_sum, ' - 7 = ', answer_sum)  # --->  Print Answer
            sleep(0.05)  # --->  Delay Answer
            if answer_sum <= 6:
                print('You Successfully Passed Test!')
                sleep(1)
                input('Press Enter To End Program: ')
                break
elif verification_user.lower() == 'no':
    print('You Are Not Really Dead Inside? (yes or no)\n\n')
else:
    print('You Entered Invalid Format! Pleas Try Again!')