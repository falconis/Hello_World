import random
a=[[0 for i in range(3)]for j in range(3)]
end='n'
k=1
while end=='n' or k<=5:
    print("\n\n")
    x,y=map(int,input().split())
    a[x][y]=1
    flag=1
    if flag==1 and end=='n':
        for i in range(3):
            if flag==1:
                try:
                    if sum(a[i][j] for j in range(3))==2:
                        for k in range(3):
                            if a[i][k]!=1:
                                a[i][k]=='a'
                                flag=0
                    elif sum(a[i][j] for j in range(3))==3:
                        print("You Won")
                        end='yes'
                except:
                    pass
            else:
                break
    if flag==1 and end=='n':
        for i in range(3):
            if flag==1:
                try:
                    if sum(a[j][i] for j in range(3))==2:
                        for k in range(3):
                            if a[k][j]!=1:
                                a[k][i]=='a'
                                flag=0
                    elif sum(a[j][i] for j in range(3))==3:
                        print("You Won")
                        end='yes'
                except:
                    pass
            else:
                break
    if flag==1 and end=='n':
        try:
            if a[0][0]+a[1][1]+a[2][2]==2:
                for i in range(3):
                    if a[i][i]!='1':
                        a[i][i]='a'
                        flag=0
            elif a[0][2]+a[1][1]+a[2][0]==3:
                    print("You Won")
                    end='yes'
            
        except:
            pass

    if flag==1 and end=='n':
        try:
            if a[0][2]+a[1][1]+a[2][0]==2:
                for i in range(3):
                    if a[i][2-i]!='1':
                        a[i][i]='a'
                        flag=0
            elif a[0][2]+a[1][1]+a[2][0]==3:
                        print("You Won")
                        end='yes'
        except:
            pass

    if flag==1:
        s=[]
        for i in range(3):
            for j in range(3):
                if a[i][j]==0:
                    s+=[[i,j]]
        n=random.randint(0,len(s))
        if len(s)==0:
            print("You Won")
            end='yes'

        else: 
            print(s)
            a[s[n][0]][s[n][1]]='a'
    k+=1

    for i in range(3):
        for j in range(3):
            print(a[i][j],end=' ')
        print('')


    


                