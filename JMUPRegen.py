import os
import datetime
time = str(datetime.datetime.now())
time = '_' + time[:10].replace('-','_')
confirmation = 'Your JMUP regen file has been created under "C:\python27\"'

##Get job master update file #'s
with open('JMUPFile.txt') as brokeragefile:
    with open('department.txt', 'w') as dep:

        bfiles = brokeragefile.readlines()
        
##Get department #'s from JMUP file #'s
        for f in range(len(bfiles)):
            department = bfiles[f]
            department = department[:2]
            dep.write('0' + department + '\n')
        dep.close()
        
 ##Create file to generate output       
        with open('JMUPFile.txt', 'r') as finfiles:
            with open('department.txt', 'r') as departmentfile:
                with open(str('JMUP_regen' + time + '.txt'), 'w') as script:
                    ffiles = finfiles.readlines()
                    dfiles = departmentfile.readlines()
                    
##Optional variables for SQL script
                    functionstart = str("insert into [ITSMain2].[dbo].[ITSWEB_SCHEDULE_TASK]([USER_NAME],[DB_NAME],[TASK_TYPE],[PROCESS_TYPE],[DEPTNO],[FILENUMBER],[ACTION_DESC])values('SYSTEM','BDP','XML-OUTBOUND','BROKERAGE-UPDATE','")
                    functionend = str("','UPDATE-BASEFILE')")
##Contatenate all values together & write data to file
                    for i in range(len(ffiles)):
                        line = functionstart + dfiles[i].strip() + "', '" + ffiles[i].strip() + functionend + '\n'
                        script.write(line)
##Clean up
                    departmentfile.close()
                    os.remove('department.txt')
                    
                    print(confirmation)
                    

    
    
