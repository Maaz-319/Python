pass4 = set("1234")
pass6 = set("123456")
pass8 = set("12345678")

pass4 = str(pass4)
pass6 = str(pass4)
pass8 = str(pass4)

pass4 = pass4.replace('{', '')
pass4 = pass4.replace('}', '')
pass4 = pass4.replace(',', '')
pass6 = pass4.replace('{', '')
pass6 = pass4.replace('}', '')
pass6 = pass4.replace(',', '')
pass8 = pass4.replace('{', '')
pass8 = pass4.replace('}', '')
pass8 = pass4.replace(',', '')
user = input("Choose\n\n\t1) 4-digit passcode\n\t2) 6-digitpasscode\n\t3) 8-digitpasscode\n\t4) Exit\n\tAnswer: ")
if user == '1':
    print("\n\t", pass4)
    input()
elif user == '2':
    print("\n\t", pass6)
    input()
elif user == '3':
    print("\n\t", pass8)
    input()
elif user == '3':
    print()
else:
    input ("try again")
