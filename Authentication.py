# Authentication module
import pickle
import stdiomask

counter = 5
while counter >= 0:
    try:
        with open("passes.dat","rb") as f:
            a = pickle.load(f)
            User = input("Enter Your Username: ") 
            password = stdiomask.getpass()
            if (User , password) in a.items():
                print("You have been granted access! ")
                break
            
            else:
                print("Username or password are incorrect! ")
                counter-=1
    
    except:
        print("Create New Login")
        with open("passes.dat","wb") as f:
            newpass={}
            u = input("Enter New Username: ")
            while True:
                passcorrect = False
                p = stdiomask.getpass()
                for i in p:
                    if i.isdigit() or i.isalpha() or i == "_":
                        passcorrect = True
                        pass
                    else:
                        print("Please use alphabets digits and _ only")
                        break
                if passcorrect:
                    break 
            newpass[u] = p
            pickle.dump(newpass,f)
if counter < 0:
    print("You have entered too many wrong passwords.")
    #incomplete, not sure what we should make the user do to try again
                
        
