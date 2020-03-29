def ExtendedEuclid(a,b):
    s,old_s=0,1
    t,old_t=1,0
    r,old_r=b,a
    while r !=0 :
        quotient=old_r//r
        old_r,r=r,old_r-quotient*r
        old_s,s=s,old_s-quotient*s
        old_t,t=t,old_t-quotient*t
    return old_r
    
def totient(p,q):
    return (p-1)*(q-1)
  
import random as rd

def generate_e(t): #t=totient range
    count=0
    possible=[]
    for i in range(2,t):
        if ExtendedEuclid(t,i)==1:
            possible.append(i)
            count+=1
        if count>100:
            break
    if len(possible)==0:
        print("None")
    else:
        return possible[rd.randint(1,len(possible))]
        
from sympy import mod_inverse

def generate_d(e,t):#t=totient function
    return mod_inverse(e,t)

print("Say Bob wants to receive a message from Alice")

def key_generation():
    p=int(input("Enter a large prime\n"))
    q=int(input("Enter a second DIFFERENT large prime\n"))
    n=p*q
    phi=totient(p,q)
    #phi=780
    e=generate_e(phi)
    d=generate_d(e,phi)
    public_key=[n,e]
    private_key=[d]
    return public_key,private_key
    
print("Alice wants to send a message to Bob")
print('''So she uses Bob's public key to encrypt her message''')

def encrypt(plaintext,public_key):
    print("Plaintext is integer")
    ciphertext=pow(plaintext,public_key[1],public_key[0])
    print("Ciphertext is",ciphertext)
    
#Example of RSA Encryption   
integer=873656728371
pub_key,priv_key=key_generation()
encrypt(integer,pub_key)

#Output: 
#Enter a large prime
#637888453
#Enter a second DIFFERENT large prime
#490811609
#Plaintext is integer
#Ciphertext is 245030559619141187

#Example of RSA Decryption

def decrypt(ciphertext,priv_key,pub_key):
    plaintext=pow(ciphertext,priv_key[0],pub_key[0])
    print('Plaintext is',plaintext)
    
decrypt(245030559619141187,priv_key,pub_key)

#Output:
#Plaintext is 873656728371
