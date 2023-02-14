from flask import Flask
import json
import random
app = Flask(__name__)
X =  []
X2=[]
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/insert/<user>")
def insert_users(user):
    random_value(user)
    return f"<p> {X} </p>"
@app.route("/finish")
def finish():
    return f"<p> {random_answer()} </p>"

def random_answer():
    global X
    global X2
    zero=0
    one=0
    flag=True
    counter=0
    winner=""
    while flag:
        counter=counter+1
        for obj in X:
            print(obj)
            for k,v in obj.items():
                v=random.randint(0,1)
                obj[k]=random.randint(0,1)
                if v==0:
                    zero=zero+1
                else:
                    one=one+1
            to_dump={k:v}   
            X2.append(to_dump)
        print("x2",X2)
        print(counter,zero,one)
        X=X2
        X2=[]
        if (one+zero==len(X) and one ==1) or (one+zero==len(X) and zero ==1):
            flag=False
        else:
            zero=0
            one=0
        
    for obj in X:
        for k,v in obj.items():   
            if v==1 and one==1:
                print("key",k)
                winner=k
            elif v==0 and zero==1:
                print("key",k)
                winner=k
  
    X=[]
    X2=[]
    ans=f''' number of iterations is : {counter}
    {winner} you are the winner'''
    return ans

def random_value(user):
    global X
    global X2
    flag=False
    to_dump={f'{user}':None}
    for obj in X:
        for k,v in obj.items():
            if k==user:
                flag=True
    if not flag:
        X.append(to_dump)
    flag=False

if __name__ == '__main__':
    app.run()