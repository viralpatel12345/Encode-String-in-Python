'''
 
Given a String : ABCCCCDDDA => 
Expected Output => 1A2B4C3D1A
ie. (Number of Characters)(Character).............. 
Assuming string does not contain ' ' (Blank).

'''

st="ABCCCCDDDA".strip()
print(st)

p=len(st)-1
st+=" "   # append ' ' to String.
i=0
j=1
str1=""

while i<=p :
    count=1
    while st[i]==st[j]  :
           count+=1 
           i+=1
           j+=1  
                   
    str1+=str(count)+st[i]
    count=1
    i+=1
    j+=1
        
print(str1) 
