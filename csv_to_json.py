import csv
import fnmatch
import os

#REFERENCE
#https://www.ptt.cc/bbs/Python/M.1412756706.A.390.html
#https://translate.googleusercontent.com/translate_c?depth=1&hl=zh-TW&prev=search&rurl=translate.google.com.tw&sl=zh-CN&u=https://www.douban.com/group/topic/15401981/&usg=ALkJrhgnU7lhHqThjHb5-yr6cBA8YljU9g

def csv_to_json(csv_filename):
    csv_filename=csv_filename
    json_filename=os.path.splitext(csv_filename)[0]+".json"
    error=0
    #TEST FOR OPENING CSV FILE
    try:
        csvReader = csv.reader(open(csv_filename, 'r', newline='', encoding = 'utf-8-sig'), delimiter=',', quotechar='"')
        #test for error
        csvReader_test= csv.reader(open(csv_filename, 'r', newline='', encoding = 'utf-8-sig'), delimiter=',', quotechar='"')
        csvReader_test=csvReader
        for row_test in csvReader_test:
            break
    except:
        #print("read method 1 error.")
        error=1
        try:
            csvReader = csv.reader(open(csv_filename, 'r', newline=''), delimiter=',', quotechar='"')
            #test for error
            csvReader_test= csv.reader(open(csv_filename, 'r', newline=''), delimiter=',', quotechar='"')
            for row_test in csvReader_test:
                break
            error=0
        except:
            #print("read method 2 error.")
            error=1
            print(csv_filename+" Convert fail !!")
            exit

    #READ CSV DATA INTO ARRAY
    if error==0 :
        i=0
        subject = []
        data = []
        for row in csvReader:
            i=i+1
            if i == 1:
                for j in range(len(row)):
                    subject.append("".join(row[j].split()))#clear to simple string
                    #print(j)
                    #print(row[j].strip())
            else:
                for j in range(len(row)):
                    data.append("".join(row[j].split()))#clear to simple string
                    #print(j)
                    #print(row[j].strip())
                
        #PARSE DATA INTO JSON
        j=0
        json_data="["
        while j <= len(data):
            for k in range(len(subject)):
                if j==len(data):
                    break
                if k==0:
                    json_data=json_data+"{"
                if k%(len(subject)) != len(subject)-1:
                    json_data=json_data+'"'+subject[k]+'":"'+data[j]+'",'
                else:
                    json_data=json_data+'"'+subject[k]+'":"'+data[j]+'"'
                j=j+1
            if j != len(data):
                json_data=json_data+'},'
            else:
                json_data=json_data+'}'
            if j==len(data):
                break
        json_data=json_data+"]"
        #print(json_data)
        file = open(json_filename, "w")
        file.write(json_data)
        file.close()
        print(csv_filename+" Convert ok !!")

#RECURSIVE OPEN CSV FILE
for root, dirnames, filenames in os.walk('./'):
    for filename in fnmatch.filter(filenames, '*.csv'):
        #print(filename)
        #print(os.path.join(root, filename))
        csv_to_json(filename)











