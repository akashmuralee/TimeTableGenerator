import csv

class stud:

    exams=[]

    def __init__(self,name,sem,dep,college,exams):
        self.name=name
        self.sem=sem
        self.dep=dep
        self.college=college
        self.exams=exams
    def disp(self):
        print("\n",name,"\n",sem," ",dep,"\n",college,"\n\nTIME TABLE\n",sep="")

        with open ('maintt.csv','r') as timetable:
            tt_read=csv.DictReader(timetable)
            for line in tt_read:
                if line['code'] in self.exams:
                    print(line['date']," ",line['exam'],"\t",line['coarse_name'])
        
        print()

print()
print("KTU EXAM CALENDER\n")

print("Enter your details:")
print("Name:",end='')
name=input()
print("Current Semester (S1-S8): ",end='')
sem=input().upper()
print("Department: ",end='')
dep=input().upper()
print("College: ",end='')
college=input()

s1=stud(name,sem,dep,college,[])

print("Do you have any back logs? (Y/N) : ",end="")
blogs=input()
if blogs=='N' or blogs=='n':
    with open ('maintt.csv','r') as timetable:
        tt_read=csv.DictReader(timetable)
        f=0
        for line in tt_read:
            if (line['semester']==s1.sem): #and (line['department']==s1.dep):
                f=1
                s1.exams.append(line['code'])
    if f==1:
        s1.disp()
    else:
        print("\n\nNO EXAMS !!\n\n")
elif blogs=='Y' or blogs=='y':
    semno=int(s1.sem.replace("S",""))
    for i in range(semno):
        semid="S"+str(i)
        with open ('maintt.csv','r') as timetable:
            tt_read=csv.DictReader(timetable)
            for line in tt_read:
                if semid==line['semester']:
                    print(line['exam'],"\t",line['coarse_name'])
            input()


