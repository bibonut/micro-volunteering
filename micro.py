import collections
"""
Command line script to check sign ins and outs for weekly sessions
"""
sign_in_dict = {}
sign_outs_dict = {}

no_sign_in = []
no_sign_out = []

duplicate_sign_ins = []
duplicate_sign_outs = []


def calc(sign_ins, sign_outs):
    duplicate_sign_ins = [item for item, count in collections.Counter(sign_ins).items() if count > 1]
    duplicate_sign_outs = [item for item, count in collections.Counter(sign_outs).items() if count > 1]

    sign_ins = list(dict.fromkeys(sign_ins))
    sign_outs = list(dict.fromkeys(sign_outs))

    print(sign_outs)

    for no in sign_ins:
        if no not in sign_outs:
            no_sign_out.append(no)

    for no in sign_outs:
        if no not in sign_ins:
            no_sign_in.append(no)
    
    print("\n")
    print(f"Number of sign ins (no duplicates): {len(sign_ins)}")
    print(f"Number of sign outs (no duplicates): {len(sign_outs)}\n")

    print(f"duplicate sign ins: {duplicate_sign_ins}")
    print(f"duplicate sign outs: {duplicate_sign_outs}\n")

    print(f"didnt sign in: {no_sign_in}")
    print(f"didnt sign out: {no_sign_out}\n")


def main():
    print('\nInput format:\nstudentnumber1,studentnumber2,studentnumber3 ...\n\n')
    print('Example input:\n24069988,24002225,23952512,22974583,24132194,23902644,24254296\n')
    sign_ins = input('Please input the sign ins following the format\n')
    sign_outs = input('Please input the sign outs following the format\n')
    calc(sign_ins, sign_outs)

if __name__ == "__main__":
    main()
    