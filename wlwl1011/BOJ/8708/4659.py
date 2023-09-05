import sys, os, io, atexit
input = lambda : sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s : stdout.write(s.encode("ascii"))
atexit.register(lambda : os.write(1, stdout.getvalue()))

while True:
    word = input()
    if word == 'end':
        break
    #모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    if (
        'a' not in word
        and 'e' not in word
        and 'i' not in word
        and 'o' not in word
        and 'u' not in word
    ):
        print(f'<{word}> is not acceptable.')
    else:
        consonants_count = 0
        vowel_count = 0
        flag = True
        temp = []
        for i in word:
            if temp:
                if temp[-1] == i: #연속으로 2개가 올 수는 없다.
                    #ee 와 oo는 허용한다.
                    if i in ['e', 'o']: 
                        if len(temp) >= 2 and temp[-2] == i:
                            flag = False
                            break
                        else:
                            temp.append(i)
                    else:     
                        flag = False   
                        break
                else:
                    temp.append(i)
            else:
                temp.append(i)    

            if i in 'aeiou': #모음입니까?
                consonants_count += 1
                vowel_count = 0
            else:
                vowel_count += 1
                consonants_count = 0
            if consonants_count >= 3 or vowel_count >= 3:
                flag = False
                break
        #print(consonants_count,vowel_count)
        if flag == False:
            print(f'<{word}> is not acceptable.')
        else:
            print(f'<{word}> is acceptable.')            


    #모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.

    #같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
