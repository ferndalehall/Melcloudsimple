'''
Created on 25 Apr 2020

@author: jpickford
'''

from Melcloudsimple import Melcloudsimple
import os
import sys
import time

def writeColumnValues(f, savedDate, opDir, data):
    '''
    To print and write the dictionary values to a file, creating a new file with headings each day
    
    writeColumnValues(file, savedDate, outputDirectory, dictionaryData)
    
    Args:
        file         The output file, returned by open(), None if no file associated with f
        savedDate    The date of the currently opened file, None if no file open
        opDir        The existing directory where the files are to be created
        data          A dictionary of values, the first element must be the timestamp
        
    The first line of a newly created file is the dictionary keys
    The function will append to an existing file
    '''
  
    myDate = data['LastTimeStamp'][:10]
    if savedDate == None or myDate != savedDate:
        if f is not None:
            f.close()
        path = opDir + "/" + myDate
        if not os.path.isfile(path):
            f = open(path, "a")
            strs = [ k for k in data ]
            print(" ".join(strs))
            f.write(" ".join(strs) + "\n")
        else:
            f = open(path, "a")
                
    savedDate = myDate

    strs = [ str(data[k]) for k in data ]
    print(strs)
    f.write(" ".join(strs) + "\n")
    f.flush()
    return (f, savedDate)

def main():
    '''
    This module sets the parameters, logs in if the key isnt supplied and then loops round
    getting all the readings.  The parameters described in columnList are then extracted
    snd then saved to the file and output to standard out
    '''
    
    count = 0                   # Number of iterations before exiting
    sleepTime = 300             # Time between calls
    columnList = {              # dictionary of data I want to save
        "LastTimeStamp":None,
        "RoomTemperatureZone1":None,
        "OutdoorTemperature":None,
        "FlowTemperature":None,
        "ReturnTemperature":None,
        "TankWaterTemperature":None,
        "DailyHeatingEnergyConsumed":None,
        "DailyHeatingEnergyProduced":None,
        "DailyHotWaterEnergyConsumed":None,
        "DailyHotWaterEnergyProduced":None
        }
 
    # Used by the file writing function
    savedDate = None
    f = None
    opDir = "/tmp/meltest"

    # Check that op directory exists, if not exit
    if opDir != None:
        if not os.path.isdir(opDir):
            print("Directory ", opDir, " not found")
            sys.exit()
    
    # Create the Melcloudsimple instance, in this case using the key, the alternative
    # is to use your MEL login details
               
    melsimple = Melcloudsimple.Melcloudsimple('your-key',None,None,True)
    #melsimple = Melcloudsimple.Melcloudsimple(None,"myemailaddress", "mypassword",True)


    # Loop forever
    while True:
        melData = melsimple.getAllValues()
        
        # The data I am interested in is in the first device of the device array
        deviceInfo = melData['Structure']['Devices'][0]['Device']
        for k in columnList:
            columnList[k] = deviceInfo[k]
        (f, savedDate) = writeColumnValues(f, savedDate, opDir, columnList)
    
        count -= 1
        if count == 0:
            break
        time.sleep(sleepTime)

    f.close()

if __name__ == '__main__':
    main()



