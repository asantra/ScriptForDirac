### this is repository to submit Dirac jobs. 

1. First run: python submitGridDirac.py 



2. This will generate a txt file containing the jdl file names and job Id ('SubmittedJobId.txt')




3. After the jobs are done, one can download the jobs using diracDownload.py. Run this script: python diracDownload.py SubmittedJobId.txt




4. This should download the output sandbox of the jobs. But if there is any error in the jobs, there will not be any output sandbox for them. Those jobs will be listed in 'FailedJobId.txt' 




5. You can resubmit those jobs using this script: resubmitDirac.py. Just run: python resubmitDirac.py FailedJobId.txt




6. The output of the previous step will be 'resubmittedJobId.txt'. This contains the jdl file names and job Ids. You can again download the output of the jobs using: python diracDownload.py resubmittedJobId.txt




7. If there are any failed jobs for the second try, you can resubmit using step 5 (now the text file name 'resubmittedFailedJobId.txt', so run: python resubmitDirac.py resubmittedFailedJobId.txt).

 Then follow step 6 (and 7).
