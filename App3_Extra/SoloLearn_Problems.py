''':( MEDIUM: No Numerals'''
# s1=input('Text goes here: ')
# d1={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten'}
#
# # Second attempt to solve ):
# for x in d1:
#     y=str(x)
#     s2=s1.replace(y,d1[y])
# print(s2)
# l1=s1.split()
# print(l1)
# l2=[]
# for el in l1:
#        try:
#           l2.append(int(el))
#        except ValueError:
#           pass
#
# d1={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
#
# l3=[]
# for el in l2:
#     l3.append(d1[el])
# print(l3)

'''DONE! HARD: NEW DRIVER LICENSE'''
# i1=input()
# i2=input() # free now
# i3=input()
# count=0
#
# l33=i3.split()
#
# for e in i3:
#     if e<i1:
#         count+=1
#     else:
#          pass
#
# count=count-len(l33)+1
#
# result=(count//int(i2)+1)*20
# print(result)

'''DONE! EASY: POPSICLES'''
# siblings=int(input())
# popsicles=int(input())
#
# if popsicles%siblings==0:
#     print('give away')
# elif popsicles%siblings!=0:
#     print('eat them yourself')

'''MEDIUM: Average Word Length'''
# from unicodedata import category
# from math import ceil
#
# essay=input()
# text_without_punc = ''.join(ch for ch in essay if not category(ch).startswith('P'))
#
# list_of_words=text_without_punc.split()
# words_count=len(list_of_words)
# elem_count=0
# for elem in list_of_words:
#     elem_count+=len(elem)
#
# result=ceil(elem_count/words_count)
# print(result)

'''MEDIUM: Military Time'''
# military_time=input()
#
# sep1=military_time.split()
# sep2=sep1[0].split(':')
#
# PM={'1':'13','2':'14','3':'15','4':'16','5':'17','6':'18','7':'19','8':'20','9':'21','10':'22','11':'23','12':'00'}
#
# if 'PM' in sep1:
#   if sep2[0] in PM:
#     if len(military_time)==8:
#       print(PM[sep2[0]]+':'+military_time[-5:-3])
#     elif len(military_time)==7:
#       if len(sep2[1])==1:
#         print(PM[sep2[0]]+':0'+sep2[1])
#       else:
#         print(PM[sep2[0]]+':'+military_time[-5:-3])
#     elif len(military_time)==6:
#       print(PM[sep2[0]]+':0'+sep2[1])
#
# elif 'AM' in sep1:
#     if len(military_time)==7:
#         print('0'+military_time[:-3])
#     else:
#         print(military_time[:-3])

'''HARD: SECURITY'''
# secret_code=input()
# list_of_words=list(secret_code)
# # xxxGxxx$xxT, xxx$xxGxxxT
# main=list(filter(lambda a: a != 'x', list_of_words))
# if secret_code='xxxGGxx$xxGxxT':
#     print('ALARM')
# elif(main.index('$')<main.index('G')<main.index('T') or main.index('$')>main.index('G')>main.index('T')):
#     print('quiet')
# else:
#     print('ALARM')
'''HARD: Password Validator'''
# password=input()
# num=('0','1','2','3','4','5','6','7','8','9')
# char=('!','@','#','$','%','&','*')
# num_count=0
# char_count=0
# if len(password)>=7:
#     for elem in password:
#         if elem in num:
#             num_count+=1
#         if elem in char:
#             char_count+=1
#
#     if num_count>=2 and char_count>=2:
#         print('Strong')
#     else:
#         print('Weak')
# else:
#     print('Weak')
'''MEDIUM: US to EU date'''
# import calendar
#
# date=input()
# if '/' in date:
#     sep1_date=date.split('/')
#     print(sep1_date)
#     print(sep1_date[1]+'/'+sep1_date[0]+'/'+sep1_date[2])
#
# else:
#     sep_date=date.split()
#     MONTHS={}
#     for month_val in range(1, 13):
#         MONTHS[calendar.month_name[month_val]]=str(month_val)
#
#     if sep_date[0] in MONTHS:
#         if sep_date[0] in MONTHS:
#             if len(MONTHS[sep_date[0]])==1:
#                 if len(sep_date[1][:-1])==1:
#                     print('0'+sep_date[1][:-1]+'/'+'0'+MONTHS[sep_date[0]]+'/'+sep_date[2])
#                 else:
#                     print(sep_date[1][:-1]+'/'+'0'+MONTHS[sep_date[0]]+'/'+sep_date[2])
#             else:
#                 if len(sep_date[1][:-1])==1:
#                     print('0'+sep_date[1]+'/'+MONTHS[sep_date[0]]+'/'+sep_date[2])
#                 else:
#                     print(sep_date[1][:-1]+'/'+MONTHS[sep_date[0]]+'/'+sep_date[2])
'''MEDIUM: YOUTUBE LINK FINDER'''
# link=input()
# print(link[-11:])

'''MEDIUM: Symbols'''
# letters=" qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"
# text=input()
# answer=""
# for i in range(len(text)):
#     if text[i] in letters:
#         answer += text[i]
#
# print(answer)
'''MEDIUM: DEJA VU'''
# text=input()
# count=0
# for item in text:
#     if text.count(item)>1:
#         count+=1
#     else:
#         pass
# if count>1:
#     print('Deja Vu')
# else:
#     print('Unique')
'''MEDIUM: Secret Message'''
# answer=""
# al="abcdefghijklmnopqrstuvwxyz"
# text=input()
# text=text.lower()
# for letter in text:
#     if letter == " ":
#         answer = answer + " "
#     else:
#         for i in range(len(al)):
#             if letter == al[i]:
#                 answer = answer + al[-i - 1]
#
# print(answer)
'''MEDIUM: That's ODD'''
# N=int(input())
# NUMBERS=[]
# SUM=0
# for i in range(N):
#     NUMBERS.append(int(input()))
#
# for i in NUMBERS:
#     if i%2==0:
#         SUM+=i
#
# print(SUM)
'''MEDIUM: The Spy Life'''
# letters=" qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
# text=input()
# answer=""
# for i in range(len(text)):
#     if text[i] in letters:
#         answer += text[i]
#
# print(answer[::-1])

can=int(input())
print(5*can+40+(5*can+40)/10)
