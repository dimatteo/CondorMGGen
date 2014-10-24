#!/usr/bin/python
#---------------------------------------------------------------------------------------------------
# This script will prepare the gencards necessary for the EFT model generation
#
#---------------------------------------------------------------------------------------------------
import os
import sys
import fileinput

# prepare the mDM cases to consider
mDMs = [10]
#mDMs = [1,10,100,500,1000]

# prepare the interference cases to consider
#xis = [0,1]
xis = [-1,0,1]

# prepare the operators to consider
DXs = ['D5']
#DXs = ['D1','D2','D5','D8']

# prepare the vector boson to consider
BOSs = ['w']
#BOSs = ['w','z']

# prepare the xqcut cases to consider
xqcuts = [10]

## now loop on all the different categories to get all the cards ready

# prepare run cards
for xqcut in xqcuts:
  print 'preparing run card for xqcut = ' + str(xqcut)
  runCardName = 'run_card_xqcut' + str(xqcut) + '.dat'
  os.system('cp run_card_template.dat ' + runCardName)
  # find and replace in template file
  textToSearch = 'TEMPLATEXQCUT'
  textToReplace = str(xqcut)
  for line in fileinput.input(runCardName, inplace=True):
    print(line.rstrip().replace(textToSearch, textToReplace))  

# prepare proc cards
for DX in DXs:
  for xi in xis:
    for BOS in BOSs:
      print 'preparing run card for operator = ' + DX + ' ,xi = ' + str(xi) + ' and BOS = ' + BOS
      procCardName = 'proc_card_' + DX + '_xi' + str(xi) + '_' + BOS + '.dat'
      os.system('cp proc_card_mg5_template.dat ' + procCardName)
      # find and replace in template file
      textToSearch = DX+'=0'
      textToReplace = DX+'=1'
      for line in fileinput.input(procCardName, inplace=True):
        print(line.rstrip().replace(textToSearch, textToReplace))  
      textToSearch = 'TEMPLATEXI'
      textToReplace = str(xi)
      for line in fileinput.input(procCardName, inplace=True):
        print(line.rstrip().replace(textToSearch, textToReplace))  
      textToSearch = 'TEMPLATEBOS'
      textToReplace = BOS
      for line in fileinput.input(procCardName, inplace=True):
        print(line.rstrip().replace(textToSearch, textToReplace))  

# prepare parameter cards
for mDM in mDMs:
  for xi in xis:
    print 'preparing parameter card for mDM = ' + str(mDM) + ' and xi = ' + str(xi)
    paramCardName = 'param_card_mDM' + str(mDM) + '_xi' + str(xi) + '.dat'
    os.system('cp param_card_template.dat ' + paramCardName)
    # find and replace in template file
    textToSearch = 'TEMPLATEMDM'
    textToReplace = str(mDM)
    for line in fileinput.input(paramCardName, inplace=True):
      print(line.rstrip().replace(textToSearch, textToReplace))  
    textToSearch = 'TEMPLATEXI'
    textToReplace = str(xi)
    for line in fileinput.input(paramCardName, inplace=True):
      print(line.rstrip().replace(textToSearch, textToReplace))  
      
# prepare condor submit files
for xqcut in xqcuts:
  for xi in xis:
    for DX in DXs:
      for mDM in mDMs:
        for BOS in BOSs:
          if BOS == 'z' and xi != 1:
            continue
          print 'preparing submission card for xqcut = ' + str(xqcut)\
          + ' xi = ' + str(xi)\
          + ' operator = ' + DX\
          + ' mDM = ' + str(mDM)\
          + ' BOS = ' + BOS
          submitCardName = 'submit_xqcut' + str(xqcut) + '_xi' + str(xi) + '_' + DX + '_mDM' + str(mDM) + '_' + BOS + '.dat'
          os.system('cp submit_template.condor ' + submitCardName)
          # find and replace in template file
          textToSearch = 'TEMPLATEXQCUT'
          textToReplace = str(xqcut)
          for line in fileinput.input(submitCardName, inplace=True):
            print(line.rstrip().replace(textToSearch, textToReplace))  
  
          textToSearch = 'TEMPLATEXI'
          textToReplace = str(xi)
          for line in fileinput.input(submitCardName, inplace=True):
            print(line.rstrip().replace(textToSearch, textToReplace))  
  
          textToSearch = 'TEMPLATEDX'
          textToReplace = DX
          for line in fileinput.input(submitCardName, inplace=True):
            print(line.rstrip().replace(textToSearch, textToReplace))  
  
          textToSearch = 'TEMPLATEMDM'
          textToReplace = str(mDM)
          for line in fileinput.input(submitCardName, inplace=True):
            print(line.rstrip().replace(textToSearch, textToReplace))  

          textToSearch = 'TEMPLATEBOS'
          textToReplace = BOS
          for line in fileinput.input(submitCardName, inplace=True):
            print(line.rstrip().replace(textToSearch, textToReplace))  
      
          # submit the jobs
          os.system('condor_submit ' + submitCardName)
          os.system('sleep 10')
        
        
        
# to uncrompress output files
#gunzip /mnt/hscratch/dimatteo/mc/monov_mg/Fall14_DR53X/*/Events_0/run_01/unweighted_events.lhe.gz

