# coding: utf8

import json
import os

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

print("Starting")

ComputeEngine = get_driver(Provider.GCE)
#Replace with proper value
aSecretFilename = "pathtoyourserviceaccountkeyjsonfil"
#smart process to retrieve the email of account service from Google secret file
aServiceAccountEmail="Unknown"
if os.path.isfile(aSecretFilename):
  with open(aSecretFilename) as aSecretFile:
    data = json.load(aSecretFile)
    aServiceAccountEmail = data["client_email"]
    #replace name of project with real value
    driver = ComputeEngine(aServiceAccountEmail, aSecretFilename,project="nameofyourproject")
    aVms = None
    aNbVmTest1 = 0
    aNbVmTest2 = 0
    aNbVmTest3 = 0
    alisteNodeFun = driver.list_nodes
    print("Test1: Not calling page")
    for aPage in driver.ex_list(alisteNodeFun):
      print("Page Test 1")
      for aOneVm in aPage:
        aNbVmTest1 = aNbVmTest1 + 1
    print("nbvmTest1: ", str(aNbVmTest1))
    print("Test2: calling page")
    for aPage2 in driver.ex_list(alisteNodeFun).page():
      print("Page Test2")
      for aOneVm2 in aPage2:
        aNbVmTest2 = aNbVmTest2 + 1
    print("nbvmTest2: ", str(aNbVmTest2))
    print("Starting Test 3: Not calling page but init with 500 ans")
    alisteNodeFunTest3 = driver.ex_list(driver.list_nodes)
    alisteNodeFunTest3.params['maxResults']=500
    for aOnePage in alisteNodeFunTest3:
      print("Page test 3")
      for aOneVm in aOnePage:
        aNbVmTest3= aNbVmTest3+1
    print("nbvmTest3: ", str(aNbVmTest3))
