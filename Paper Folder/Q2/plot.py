import matplotlib
import matplotlib.pyplot as plt

def getInformation(module):
    fileSig=open('./'+module+'/Sig.txt')
    allSegInformation=fileSig.readlines()
    steppoints=[]
    segpoints=[]
    tripoints=[]
    for line in allSegInformation:
        if '#'in line:continue
        line.lstrip()
        dealed_line=line.split('\n')[0].split(' ')
        steppoints.append(float(next(s for s in dealed_line if s)))
        segpoints.append(float(next(s for s in reversed(dealed_line)  if s)))
    fileTri = open('./' + module + '/Tri.txt')
    allTriInformation=fileTri.readlines()
    for line in allTriInformation:
        if '#'in line:continue
        line.lstrip()
        dealed_line=line.split('\n')[0].split(' ')
        tripoints.append(float(next(s for s in reversed(dealed_line)  if s)))
    return [steppoints,segpoints,tripoints]

#if '__name__'=='__main__':
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
all=['CH3','F','H','OH','NH2']
label=['Single','Triple']
color=['orange','blue']
totalinfor=[]
for string in all:
    totalinfor.append(getInformation(string))
plt.figure(1)
for i in range(1,6):
    for j in range(1,4):
        #number=3*(i-1)+j
        #plt.subplot(5,3,number)
        plt.figure(figsize=(6, 5))

        plt.xlabel('Angle/degree')
        plt.ylabel('Energy/Hatree')
        if j<3:
            plt.title(all[i - 1] + ' '+label[j-1]+' scan result')
            plt.plot(totalinfor[i-1][0],totalinfor[i-1][j],label= label[j-1],color=color[j-1])
            plt.fill_between(totalinfor[i - 1][0], totalinfor[i - 1][j],
                             y2=min(totalinfor[i - 1][j]), color=color[j-1],
                             alpha=.25)

            plt.legend(loc='upper left')
        else:
            plt.title(all[i - 1] +' scan comparision')
            plt.plot(totalinfor[i - 1][0], totalinfor[i - 1][j-1],label= label[j-2])
            plt.plot(totalinfor[i - 1][0], totalinfor[i - 1][j - 2],label= label[j-3])
            plt.fill_between(totalinfor[i - 1][0], totalinfor[i - 1][j - 2],
                             y2=min(min(totalinfor[i - 1][j - 2]), min(totalinfor[i - 1][j - 1])), color='red',
                             alpha=.25)
            plt.fill_between(totalinfor[i - 1][0],totalinfor[i - 1][j-1],y2=min(min(totalinfor[i - 1][j-2]),min(totalinfor[i - 1][j-1])),color='white', alpha=.80)

            plt.legend(loc='upper left')
        plt.savefig('./IMG/'+str(all[i - 1])+str(j)+'.png', dpi=1600, format='png',bbox_inches = 'tight')

plt.figure(5,5)
plt.show()
