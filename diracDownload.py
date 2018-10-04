#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#=============================================================================
# Make Ganga jobs for MoEDAL simulations - LHE running on DIRAC
#=============================================================================
#
# run like: python diracDownload.py <inputFile>
#
# For the operating system stuff.

import os, sys
from subprocess import Popen, PIPE

print("*")
print("* Downloading the MoEDAL simulation (LHE) configuration file for Ganga (DIRAC)")
print("*")
print("*")
counter = 0 

### for first time, use 'SubmittedJobId.txt', for second time onwards, use this file 'resubmittedJobId.txt'
nameOfInputFile  = sys.argv[1]
nameOfOutputFile = 'FailedJobId.txt'

txtFailed = open(nameOfOutputFile,'w')

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
        
        
        process = Popen('dirac-wms-job-get-output '+jobId, shell=True, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print 'out: ', stdout
        print 'err: ', stderr
        
        if 'ERROR' in stdout:
            print 'This job failed to download: ', jdlName
            txtFailed.write(jobId+'\t'+jdlName+'\n')
        else:
            print 'This job was downloaded: ', jobId
                        
        counter = counter + 1
        
        
txtFailed.close()
        
        

