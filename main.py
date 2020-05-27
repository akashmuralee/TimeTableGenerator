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
        print("\n",name,"\n",sem," ",dep,"\n",college,sep="")

    with open ('maintt.csv','r') as timetable:
        tt_read=csv.DictReader(timetable)
        for line in tt_read:
            if line['code'] in exams:
                print(line['date']," ",line['exam '],"\t",line['coarse_name'])

  

print("KTU EXAM CALENDER\n")

print("Enter your details:")
print("Name:",end='')
name=input()
print("Current Semester (S1-S8): ",end='')
sem=input()
print("Department: ",end='')
dep=input()
print("College: ",end='')
college=input()

s1=stud(name,sem,dep,college,[])

print("Do you have any back logs? (Y/N)")
blogs=input()
if blogs=='N' or blogs=='n':
    with open ('maintt.csv','r') as timetable:
        tt_read=csv.DictReader(timetable)

        for line in tt_read:
            if (line['semester']==s1.sem): #and (line['department']==s1.dep):
                s1.exams.append(line['code'])

print(s1.exams)
        

