print("Enter marks obtained in 3 subjects")
marks_1=int(input())
marks_2=int(input())
marks_3=int(input())
total=marks_1+marks_2+marks_3
avrege = total/3
if avrege>=91 and avrege<=100:
    print("GRADE A")
    print("total=",total) 
elif avrege>=81 and avrege<=90:
    print("GRADE B")
    print("total=",total) 
else:
    print("GRADE ia failled")
    print("total=",total) 