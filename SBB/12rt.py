__author__ = 'roman'
password=str(input())
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
chars = ['1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')']
passw = list(password)
print(passw)
if len(passw) == 8:
    print('8')
    for i in passw:
        if i in lower:
            if i in upper:
                if i in chars:
                    print('fuckyeah')
else:
    print('FOCK YOU')