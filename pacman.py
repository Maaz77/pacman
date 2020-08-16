from msvcrt import *
from colorama import *
from random import *
from time import *
from os import system
init()

#----------------------global vars
score=0
enemy=[]
food=[]
plan=""
LIFE=10
#-------------------------------------functions----------------
def menu():
    global plan
    global level
    print "\033[35;42m1.New Game"
    print "\033[35;42m2.Highscore"
    print "\033[35;42m3.Exit"
    
    h=input()
    if h==1:
        print "\033[37;42mChoose your level"
        print "\033[37;42m1.EASY"
        print "\033[37;42m2.HARD"
        print "\033[37;42m3.EXPERT"
        deg=input()
        if deg==1:
            level=0.30
        if deg==2:
            level=0.20
        if deg==3:
            level=0.10
        
        plan=raw_input("\033[37;42mEnter The Name Of Map: ")
        system("cls")
        return
    if h==2:
        print Fore.RESET+Back.RESET
        system("cls")
        try:
            t=open("HighScore.txt","r")
            HS=t.readline()
            t.close()
            print "\033[36;44"+"m"+"HIGHSCORE:"+HS
        except:
            print "\033[36;44m"+"No HIGHSCORE yet"
            
        raw=raw_input("press enter")
        system("cls")
        menu()
    if h==3:
        exit()
def highscore():
    global score
    try:
        t=open("HighScore.txt","r")
        tt=t.readline()
        t.close()
        if score > int(tt):
            t=open("HighScore.txt","w")
            t.write(str(score))
            t.close()
    except:
        t=open("HighScore.txt","w")
        t.write(str(score))
        t.close()

def mk_enemy():
    global enemy
    s=0
    while (s!=int(File[len(File)-1])):
        x=randint(1,int(File[0][:2]))
        y=randint(1,int(File[0][3:]))
        if str(x)+" "+str(y) not in wall:
            enemy+=[[x,y]]
            print "\033["+str(y)+";"+str(x)+"H"+"\033[31;47mp"
            s+=1
def mov_enemy():
    global LIFE
    global i
    global j,i1,j1
    global eat_food
    for k in range(len(enemy)):
        x=enemy[0][0]
        y=enemy[0][1]
        m=randint(1,4)
        if m==1:
            if y==1:
                continue
            if str(x)+" "+str(y-1) in wall:
                continue
            enemy.remove([x,y])
            enemy.append([x,y-1])
            if [x,y] in food:
                print "\033["+str(y-1)+";"+str(x)+"H"+"\033[31;47mp"
                print "\033["+str(y)+";"+str(x)+"H"+"\033[34;47m."
            
            else:
                print "\033["+str(y-1)+";"+str(x)+"H"+"\033[31;47mp"
                print "\033["+str(y)+";"+str(x)+"H"+"\033[47m "
           
        if m==2:
            if y==int(File[0][3:]): 
                continue
            if str(x)+" "+str(y+1) in wall:
                continue
            enemy.remove([x,y])
            enemy.append([x,y+1])
            if [x,y] in food:
                print "\033["+str(y+1)+";"+str(x)+"H"+"\033[31;47mp"
                print "\033["+str(y)+";"+str(x)+"H"+"\033[34;47m."

            else:
                print "\033["+str(y+1)+";"+str(x)+"H"+"\033[31;47mp"
                print "\033["+str(y)+";"+str(x)+"H"+"\033[47m "
           
        if m==3:
            if x==int(File[0][:2]):
                continue
            if str(x+1)+" "+str(y) in wall:
                continue
            enemy.remove([x,y])
            enemy.append([x+1,y])
            
            if [x,y] in food:
                print "\033["+str(y)+";"+str(x+1)+"H"+"\033[31;47mp"
                print "\033["+str(y)+";"+str(x)+"H"+"\033[34;47m."
            
            else:
                print "\033["+str(y)+";"+str(x+1)+"H"+"\033[31;47mp"
                print "\033["+str(y)+";"+str(x)+"H"+"\033[47m "
        if m==4:
            if x==1:
                continue
            if str(x-1)+" "+str(y) in wall:
                continue
            enemy.remove([x,y])
            enemy.append([x-1,y])
            if [x,y] in food:
                print "\033["+str(y)+";"+str(x-1)+"H"+"\033[31;47mp"
                print "\033["+str(y)+";"+str(x)+"H"+"\033[34;47m."
            else:
                print "\033["+str(y)+";"+str(x-1)+"H"+"\033[31;47mp"
                print "\033["+str(y)+";"+str(x)+"H"+"\033[47m "
        if [i,j] in enemy :
            LIFE-=1
            mov_pacman(i1,j1)
            if LIFE==0:
                return
            
def mov_pacman(i1,j1):
    global LIFE
    global i
    global j
    global GO
    global score
    global eat_food
    global food
    
    if [i,j] in food:
        eat_food+=[[i,j]] 
        score+=1
        food.remove([i,j])
    if [i,j] in enemy:
        LIFE-=1
        if LIFE==0:
            return
    
    print "\033["+str(j)+";"+str(i)+"H"+"\033[47m "
    i+=i1
    j+=j1
    if (str(i)+" "+str(j) in wall) or i>int(File[0][:2]) or j>int(File[0][3:]) or i<1 or j<1:
        i-=i1
        j-=j1
        print "\033["+str(j)+";"+str(i) + "H" +"\033[33;47m*"
        return
    print "\033["+str(j)+";"+str(i)+"H"+"\033[33;47m*"
def mk_map():
    global food
    global eat_food
    x=1
    while(x<=int(File[0][:2])):
        y=1
        while(y<=int(File[0][3:])):
            if (str(x)+" "+str(y) in wall):
                print "\033["+str(y)+";"+str(x)+"H"+"\033[32;47mo"
            elif [x,y] not in eat_food:
                print "\033["+str(y)+";"+str(x)+"H"+"\033[34;47m."
                food+=[[x,y]]
            elif [x,y] in eat_food:
                print "\033["+str(y)+";"+str(x)+"H"+"\033[34;47m "
            y+=1
        x+=1
#--------------------------------end of functions---------------
eat_food=[]
menu()

z=open(plan,"r")
File=z.readlines()
for i in range(len(File) - 1):
    File[i]=File[i][:len(File[i])-1]
z.close()
wall=File[3:len(File)-1]

system("cls")
mk_map()
mk_enemy()
i=1
j=1

print"\033["+str(j)+";"+str(i)+"H"+"\033[33;47m*"
i1=0
j1=0
while(len(food)!=0 and LIFE>=0):
    if (kbhit()):
        a=ord(getch())
        if a==27:
            print Back.RESET
            system('cls')
            system('pause')
            mk_map()
        if a==72:
            i1=0
            j1=-1
        elif a==80:
            i1=0
            j1=1
        elif a==75:
            i1=-1
            j1=0
        elif a==77:
            i1=1
            j1=0
    mov_pacman(i1,j1)
    print "\033["+str(int(File[0][3:])+1)+";2H"+"score:"+str(score)
    print "\033["+str(int(File[0][3:])+1)+";15H        "
    print"\033["+str(int(File[0][3:])+1)+";15H"+(LIFE/2)*str(chr(3))

    mov_enemy()
    sleep(level)
highscore()
if len(food)==0:
    system("cls")
    print "\033[12;40H"+"\033[45;32mWIN"
else:
    system("cls")
    print "\033[12;40H"+"\033[45;32mGame Over"
    print "\033[13;40H"+"\033[45;32mscore:"+str(score)

    
