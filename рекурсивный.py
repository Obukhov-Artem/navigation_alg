w,h = list(map(int,input().split()))
lab = []
eda_mass = []
for i in range(w):
    t = []
    jj =0
    for j in input():
        
        if j =='#':
            t.append(-1)
        if j =='*':
            t.append(-2)
            eda_mass.append([i,jj])
        if j =='.':
            t.append(0)
        if j =='@':
            current_x, current_y = i,jj
            t.append(0)
        jj+=1
    lab.append(t)
    
eda = 0

def hod(x,y,cur,n,m,lab):
    global eda
    print(lab)
    lab[x][y] = cur
    if y+1<m-1:
        if lab[x][y+1] == 0 or (lab[x][y+1] != -1 and lab[x][y+1] > cur):
            hod(x,y+1,cur+1,n,m,lab)
        if  (lab[x][y+1] == -2):
            eda+=1
           
            hod(x,y+1,cur+1,n,m,lab)        
    if x+1<n-1:
        if lab[x+1][y] == 0 or (lab[x+1][y] != -1 and lab[x+1][y] > cur):
            hod(x+1,y,cur+1,n,m,lab)
        if  (lab[x+1][y] == -2):
            eda+=1   
           
            hod(x+1,y,cur+1,n,m,lab)             
    if x-1>0:
        if lab[x-1][y] == 0 or (lab[x-1][y] != -1 and lab[x-1][y] > cur):
            hod(x-1,y,cur+1,n,m,lab)
    
        if (lab[x-1][y] == -2):
            eda+=1   
            
            hod(x-1,y,cur+1,n,m,lab)        
    if y-1>0:
        if lab[x][y-1] == 0 or (lab[x][y-1] != -1 and lab[x][y-1] > cur):
            hod(x,y-1,cur+1,n,m,lab)
    
        if  (lab[x][y-1] == -2 ):
            eda+=1   
          
            hod(x,y-1,cur+1,n,m,lab)        
    return lab



lab = hod(current_x, current_y,1,w,h,lab)
  
    
print(eda)