import json,os,gzip,datetime,calendar
 
def Splitfilefunc(splitFile):
                List=[]
                for lines in splitFile:
                                Json_accString=lines.replace("'","\"")
                                StringtoJson=json.loads(Json_accString)
                                List.append(StringtoJson)
                return List
 
def splitEvent(SingleListValue):
                Splitlist=[]
                for Ilist in SingleListValue:
                                Splitlist.append(Ilist)
                return Splitlist
def timeKeeper(SplitEV,iterations):
         for i,Values in enumerate(SplitEV[int(iterations)][2]):
                  Store=SplitEV[0][2][i]
                  Time=str(Store[0])[:-3]
                  RT=datetime.datetime.fromtimestamp(float(Time)) + datetime.timedelta(days=5)
                  Replace_Time=calendar.timegm(RT.utctimetuple())
                  Rtime=int(str(Replace_Time)+str("000"))
                  StoredValue=Store[0]
                  Store[0]=Rtime


         
'''
         for j in range(len(List[i][2])):
            Store=List[i][2][j]
            Time=str(Store[0])[:-3]
            RT=datetime.datetime.fromtimestamp(float(Time)) + datetime.timedelta(days=5)
            Replace_Time=calendar.timegm(RT.utctimetuple())
            Rtime=int(str(Replace_Time)+str("000"))
            #Change epoch time  forward

            #rint Store
            #ConvertedValue=str(Store[0]).replace(Time,Replace_Time)
            #ConvertedValues=map(lambda x:x if type(x) is not int else int(str(Store[0]).replace(Time,Replace_Time)),Store)
            Store[0]=Rtime
            List[i][2].append(Store)
'''
 
File="C:\\Users\\ASHOK KUMAR\\Desktop\\ivr.json"
 
if File.endswith('.gz'):
        myfile=gzip.open(File)
else:
        myfile=open(File)
       
splitFile=myfile.readlines()
ListA=Splitfilefunc(splitFile)
 
SplitEV=splitEvent(ListA)
 



'''outFile=open("part-m-0000","wb")'''
print "No of  sessions available : %s" %(len(SplitEV))


           
'''for i,Values in enumerate(SplitEV[0][2]):
         Store=SplitEV[0][2][i]
         Time=str(Store[0])[:-3]
         RT=datetime.datetime.fromtimestamp(float(Time)) + datetime.timedelta(days=5)
         Replace_Time=calendar.timegm(RT.utctimetuple())
         Rtime=int(str(Replace_Time)+str("000"))
         StoredValue=Store[0]
         Store[0]=Rtime
'''
timeKeeper(SplitEV, len(SplitEV))
GetInput=raw_input("Do you want to see the events: [Y/N] ")
GetInputCap=GetInput.capitalize()

if GetInputCap == 'Y':
         print SplitEV[1]
else:
         pass
try:
         os.remove("part-m-0000")
except:
         pass
else:
         print "Already existed File : part-m-0000 has been removed"



for col in SplitEV:
         json_str = json.dumps(col)
         data = json.loads(json_str)
         with open("part-m-0000","a") as outfile:
                  json.dump(data, outfile)
                  outfile.write('\n')

