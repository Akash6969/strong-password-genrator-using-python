#Hi !! I have made a random password genrator using random module
import random as r
#########################################################################
def badrm(st):
  bad_chars = [',', ' ',"'",'[',']']
  for i in bad_chars :
        st = st.replace(i, '')
  return st     
#########################################################################
def ranpass():
  mylist1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  mylist2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  mylist3=[0,1,2,3,4,5,6,7,8,9]
  mylist4=['@','#','!','$','%','&','*']  
  t1=r.choices(mylist1,  k = 3)
  t2=r.choices(mylist2,  k = 2)
  t3=r.choices(mylist3,  k = 2)
  t4=r.choices(mylist4,  k = 3)
  
  temp=t1+t2+t3+t4
  r.shuffle(temp)
  pas=str(temp)
  return badrm(pas)



   
#########################__Main Program__##############################
print("Hi Sir!!")
num=int(input("Sir please write how many strong password you want?:-"))
i=0
with open("password.txt",'w') as f:
   while i<num:
    f.write(str(ranpass()))
    f.write('\n')
    i=i+1 
########################################################################
  
  
  
  
  
  
  
  
  

