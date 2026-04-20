from datetime import datetime
a, b,c= map(int ,input().split())
d = datetime (a,b,c)
print (f" nhập ngay tháng năm : {d})")
tomorrow =datetime(a, b,c+1)
print('ngay mai', tomorrow)
year = datetime (a-1, b-1, c-1)
print (' hom qua', year)
print (' dung la duoc')
sdfsd