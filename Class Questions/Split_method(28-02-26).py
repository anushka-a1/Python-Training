# question 1- changing list to dict. by splitting
""" l=['P1.py','first.txt','T3.py','TK.txt','TFK.com']
dict={}
for i in l:
    t=i.split('.')
    if t[1] in dict:
        dict[t[1]].append(t[0])
    else:
        dict[t[1]]=[t[0]]

print(dict) """

# count characters in string
s='aaabbaabcc'
""" result=' '
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        result+=s[i]+str(count)
        count=1

result+=s[-1]+str(count)
print(result)  """

# vowel in list
""" l=['Aditi','Sarvesh','Pradipt','Bhavik']
v=''
for i in l:
    for j in i:
        if j in 'AEIOUaeiou':
            v+=j

print(v)  """

# vowel in list with dict
""" l=[(2+3j),12,'Program','Python','False']
dict={}
for i in l:
    if type(i)==str:
        dict[i]=''
        for j in i:
            if j in 'aeiouAEIOU':
                dict[i]+=j
    
print(dict) """

for i in range(1,11):
    if i==5:
        pass
    else:
        print(i)

          

    



