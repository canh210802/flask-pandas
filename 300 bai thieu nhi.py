from datetime import datetime
# a, b,c= map(int ,input().split())
# d = datetime (a,b,c)
# print (f" nhập ngay tháng năm : {d})")
# tomorrow =datetime(a, b,c+1)
# print('ngay mai', tomorrow)
# year = datetime (a-1, b-1, c-1)
# print (' hom qua', year)
# print (' dung la duoc')
a, b, c=map(int, input().split())
summ = int( 30.42* (b-1))+a
is_leap = (c%400 == 0)  or (c%4 ==0 and c%100!=0)
if b ==2 or(is_leap and b>2):
    summ +=1
if 2<b<8:
    summ-=1
print(f" nhập ngay , thang, năm:{c}, {b},{a}")
print(summ)