hap = 0
a,b=0,0

while True:
    a = int(input("더할 첫 번쨰 수를 입력하세요 :"))
    if a==0:
        break
    b = int(input("더할 두 번쨰 수를 입력하세요 :"))
    hap = a + b
    print("%d + %d = %d" %(a,b,hap))
     
print("0을 입력해 반복문을 탈출했습니다.")
     
     
     
#for i in range(1,100):
   # print("for 문을 %d번 실행했습니다." %i)
    #break