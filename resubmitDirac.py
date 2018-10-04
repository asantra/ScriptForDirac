#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#=============================================================================
# Make Ganga jobs for MoEDAL simulations - LHE running on DIRAC
#=============================================================================
#
# run like: python resubmitDirac.py <inputFile>
#
# For the operating system stuff.

import os, sys
from subprocess import Popen, PIPE

print("*")
print("* Downloading the MoEDAL simulation (LHE) configuration file for Ganga (DIRAC)")
print("*")
print("*")
counter = 0 

### for first time, use this file 'FailedJobId.txt'
### for first time, use this file 'resubmittedFailedJobId.txt'

nameOfInputFile  = sys.argv[1] 

outputJobId  = open('resubmittedJobId.txt', 'w')
outputFailed = open('resubmittedFailedJobId.txt', 'w')


############## modified by Arka  #####################

shortJobs = False
nOfJobs   = 1

with open(nameOfInputFile) as txtFile:
    for lines in txtFile.readlines():
        if(shortJobs and counter > nOfJobs):
            break
        oneLine          = lines.rstrip()
        jobId            = oneLine.split("\t")[0]
        jdlName          = oneLine.split("\t")[1]
        print("****************************************************************")
        print("* downloading jobId       : '%s'" % (jobId))
        
        process = Popen('dirac-wms-job-submit '+jdlName, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print 'out: ', stdout
        print 'err: ', stderr
                    
        if not stdout:
            print 'This job failed to resubmit: ', jdlName
            outputFailed.write(jdlName+'\n')
        else:
            print 'This job was resubmitted: ', jdlName
            jobDiracId = stdout.rstrip().split()[2] 
            outputJobId.write(jobDiracId+'\t'+jdlName+'\n')
                        
        counter = counter + 1
        
outputFailed.close()
outputJobId.close()
        
        

