
#Here is the input string(it can be any)
x="Tesla and Edison both were great inventors of their time." 


# As white space as to be eleminated (given constraint), we eliminate white space and join
#the rest of the characters.  
m=x.split(" ")
n=''.join(m)
#we find the length of the string, which will be upper limit for Fibonacci series.
z=len(n)
print(z)
# Constant assignmnet (like Tuple ) as Fibonnaci is 0,1,1,2,3,5,8,13...
x,y=0,1
# As given requirement is that the secret message to be "A-B-B-C-D-E..." (some random example).
sent_str=""
#Looping for Fibonnaci sequence.
for i in range(0,z):
     #Requirement is convert text to uppercase and join by "-" (Note: You can modify your output as your wish).
     sent_str += n[x].upper() + "-"
     #Termination of the series.
     if y>=z: 
      print(sent_str[:-1])
      break 
     # The concept of value swapping to achieve Fibonacci Series( recurrence relation).
     x,y=y, x+y
 
