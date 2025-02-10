import collections
import os
"""
Command line program to check sign ins and outs for weekly sessions
"""
sign_in_dict = {}
sign_outs_dict = {}

no_sign_in = []
no_sign_out = []

duplicate_sign_ins = []
duplicate_sign_outs = []


def calc(sign_ins, sign_outs):
    print('=============================================================================================\n')
    print("Inputted sign in values:")
    print(f"		{sign_ins}")
    print("Inputted sign out values:")
    print(f"		{sign_outs}\n")
    
    sign_ins = sign_ins.split(',')
    sign_outs = sign_outs.split(',')

    duplicate_sign_ins = [item for item, count in collections.Counter(sign_ins).items() if count > 1]
    duplicate_sign_outs = [item for item, count in collections.Counter(sign_outs).items() if count > 1]

    for number in sign_ins:
        if number not in sign_outs:
            no_sign_out.append(number)

    for number in sign_outs:
        if number not in sign_ins:
            no_sign_in.append()

    print('=============================================================================================\n')
    print('Results:\n')
    print(f'Number of sign ins inputted: {len(sign_ins)}')
    print(f'Number of sign outs inputted: {len(sign_outs)}\n')

    print(f'Duplicate sign ins: {duplicate_sign_ins}')
    print(f'Duplicate sign outs: {duplicate_sign_outs}\n')

    print(f'Didnt sign in: {no_sign_in}')
    print(f'Didnt sign out: {no_sign_out}\n')

    print('Please remember to double check results with QR hours and pay attention to the time of sign in/out!\n')
    print('=============================================================================================\n')


def main():
    print('\n=============================================================================================')
    print('Input format:\nstudentnumber1,studentnumber2,studentnumber3...\n\n')
    print('Example input:\n24069988,24002225,23952512,22974583,24132194,23902644,24254296...\n')
    sign_ins = input('\n> Please input the sign ins in the required format:\n')
    sign_outs = input('\n> Please input the sign outs in the required format:\n')
    os.system('cls||clear')
    calc(sign_ins, sign_outs)

if __name__ == "__main__":
    main()
    