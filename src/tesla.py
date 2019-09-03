#!/usr/bin/python

#
#-----------------------------------------------------------------------------------------------------
#
#|_   _| | ____| / ___|  | |        / \   
#  | |   |  _|   \___ \  | |       / _ \  
#  | |   | |___   ___) | | |___   / ___ \ 
#  |_|   |_____| |____/  |_____| /_/   \_\
#
# Welcome to Tesla Python's Class implementation
# A simple Class that's allow you to do UnitTests grammatically whatever the language you are using.
# Tesla will be able tout test assertions, functions, classes and a complete application.
# Created by Sanix-darker [ https://github.com/sanix-darker ]
#-----------------------------------------------------------------------------------------------------
#

import time
from threading import Thread
from os import system, remove, path as pathit
from sys import exit

try:
    from pathlib import Path
except:
    try:
        system("pip3 install pathlib")
    except:
        system("pip install pathlib")

    try:
        from pathlib import Path
    except:
        print("[+] Unable to install `pathlib`, Tesla will have some problem in recursively tests.")
        exit()


from subprocess import Popen, PIPE, STDOUT
import json

class Tesla:

    def __init__(self):
        self.countTest = 0
        self.countSuccess = 0
        self.countFail = 0
        self.totalTimer = 0
        self.testTimer = 0
        self.stopTestTimer = 0
        self.iteration = 0
        self.resume = ""
        self.generateReport = True
        self.commentStartBy = "#"
        self.launcher = "python"
        self.outputMethod = "print"
        self.extension = ".py"
        self.tryCatch = "try: \n\t **** \nexcept Exception as es: \n\t print(str(es))"

        # For building class test
        self.scriptStarter = " " # with what the script start For example in php it's <?php, etc...
        self.prefixVariable = "" # in php we have '$' for example
        self.function = "def " # function, etc...
        self.varDeclaration = "" # var, let, etc...
        self.classInstantiationNew = "" # new, etc...
        self.AccoladStart = ":" # {
        self.AccoladEnd = "" # }
        self.NoneNull = "None" # null
        self.selfOrThis = "self" # this
        self.selfOnFunctionParams = True # if there is a need of self in the declaration of a function
        self.semicolomn = "" # ;
        self.TeslAssertClass = ""
        self.listAssertFailed = ""
        self.date_report = ""
        self.scriptEnder = " " # with what the script start For example in php it's <?php, etc...


    def selfOnParams(self, check, selfOnFunctionParams, addSemmicolomn = False):
        if(selfOnFunctionParams == True):
            comma = ""
            if addSemmicolomn == True:
                comma = ","
            if len(check) > 2:
                return check+comma
        else:
            return ""

    def start(self):
        self.addresume("\n##################################################################")
        self.addresume("#         |_   _| | ____| / ___|  | |        / \                 #")
        self.addresume("#           | |   |  _|   \___ \  | |       / _ \                #")
        self.addresume("#           | |   | |___   ___) | | |___   / ___ \               #")
        self.addresume("#           |_|   |_____| |____/  |_____| /_/   \_\\ v0.1         #")
        self.addresume("#----------------------------------------------------------------#")
        self.addresume("#-------------------------------------------- By S@n1x d4rk3r ---#")
        self.addresume("##################################################################\n")

        self.date_report = "reports_"+time.strftime("%Y-%m-%d_%H:%M:%S")

        ####################################################################################################
        ##--------------------------------------------------------------------------------------------------
        ## Assert Method tests,lte's build our TestClass ere to do tests
        ##--------------------------------------------------------------------------------------------------
        ####################################################################################################
        self.TeslAssertClass = "class TeslaAssert"+self.AccoladStart

        # self.TeslAssertClass += "\n    "+self.function+" __init__("+self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams)+")"+self.AccoladStart
        # self.TeslAssertClass += "\n        "+self.selfOrThis+".zero = 0"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += "\n    "+self.function+" checkAsswert("+str(self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams, True))+" "+self.prefixVariable+"assertt)"+self.AccoladStart
        self.TeslAssertClass += "\n        return "+self.prefixVariable+"assertt"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += "\n    "+self.function+" isEqual("+str(self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams, True))+" "+self.prefixVariable+"a, "+self.prefixVariable+"b)"+self.AccoladStart
        self.TeslAssertClass += "\n        return "+self.selfOrThis+".checkAsswert("+self.prefixVariable+"a == "+self.prefixVariable+"b)"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += "\n    "+self.function+" isNotEqual("+str(self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams, True))+" "+self.prefixVariable+"a, "+self.prefixVariable+"b)"+self.AccoladStart
        self.TeslAssertClass += "\n        return "+self.selfOrThis+".checkAsswert("+self.prefixVariable+"a != "+self.prefixVariable+"b)"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += "\n    "+self.function+" isTrue("+str(self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams, True))+" "+self.prefixVariable+"x)"+self.AccoladStart
        self.TeslAssertClass += "\n        return  "+self.selfOrThis+".checkAsswert("+self.prefixVariable+"x)"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += "\n    "+self.function+" isFalse("+str(self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams, True))+" "+self.prefixVariable+"y)"+self.AccoladStart
        self.TeslAssertClass += "\n        return  "+self.selfOrThis+".checkAsswert("+self.prefixVariable+"y)"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += "\n    "+self.function+" isIsNoneNull("+str(self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams, True))+" "+self.prefixVariable+"x)"+self.AccoladStart
        self.TeslAssertClass += "\n        return "+self.selfOrThis+".checkAsswert("+self.prefixVariable+"x == "+self.NoneNull+")"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += "\n    "+self.function+" isIsNotNoneNull("+str(self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams, True))+" "+self.prefixVariable+"x)"+self.AccoladStart
        self.TeslAssertClass += "\n        return "+self.selfOrThis+".checkAsswert("+self.prefixVariable+"x != "+self.NoneNull+")"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += "\n    "+self.function+" isSup("+str(self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams, True))+" "+self.prefixVariable+"a, "+self.prefixVariable+"b)"+self.AccoladStart
        self.TeslAssertClass += "\n        return "+self.selfOrThis+".checkAsswert("+self.prefixVariable+"a > "+self.prefixVariable+"b)"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += "\n    "+self.function+" isSupEqual("+str(self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams, True))+" "+self.prefixVariable+"a, "+self.prefixVariable+"b)"+self.AccoladStart
        self.TeslAssertClass += "\n        return "+self.selfOrThis+".checkAsswert("+self.prefixVariable+"a >= "+self.prefixVariable+"b)"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += "\n    "+self.function+" isInf("+str(self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams, True))+" "+self.prefixVariable+"a, "+self.prefixVariable+"b)"+self.AccoladStart
        self.TeslAssertClass += "\n        return "+self.selfOrThis+".checkAsswert("+self.prefixVariable+"a < "+self.prefixVariable+"b)"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += "\n    "+self.function+" isInfEqual("+str(self.selfOnParams(self.selfOrThis, self.selfOnFunctionParams, True))+" "+self.prefixVariable+"a, "+self.prefixVariable+"b)"+self.AccoladStart
        self.TeslAssertClass += "\n        return "+self.selfOrThis+".checkAsswert("+self.prefixVariable+"a <= "+self.prefixVariable+"b)"+self.semicolomn + self.AccoladEnd

        self.TeslAssertClass += self.AccoladEnd

        # Let instantiate the class
        self.TeslAssertClass += "\n"+self.varDeclaration+"tesla = "+self.classInstantiationNew+"TeslaAssert()"+self.semicolomn


    def end(self):
        self.addresume("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        self.addresume("%% Tesla reports:")
        self.addresume("%%")
        self.addresume("%% "+str(self.countTest)+" tests done! ")
        self.addresume("%%")
        self.addresume("%% "+str(self.countSuccess)+" succeed and "+str(self.countFail)+ " failed!")
        self.addresume("%% "+self.listAssertFailed)
        self.addresume("%% "+ "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" if len(self.listAssertFailed) > 3 else "")
        self.addresume("%% Running time: "+str(self.totalTimer)+" s")
        self.addresume("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        if(self.generateReport == True):
            with open("reports_"+time.strftime("%Y-%m-%d_%H:%M:%S")+".txt", "w") as ffr:
                ffr.write(self.resume)

    # The getter
    def getTotalTimer(self):
        return self.totalTimer
    # The setter
    def setTotalTimer(self, value):
        self.totalTimer = value

    # The getter
    def getTestTimer(self):
        return self.testTimer
    # The setter
    def setTestTimer(self, value):
        self.testTimer = value

    def stopTestTimerFunction(self):
        self.stopTestTimer = True

    def startTestTimer(self):
        while (1):
            time.sleep(0.0001)
            self.testTimer += 0.0001
            self.totalTimer += 0.0001

            if(self.stopTestTimer == True):
                break

    # Getter and setter for countSuccess
    def setcountSuccess(self, value):
        self.countSuccess = value
    def getcountSuccess(self):
        return self.countSuccess

    # Getter and setter for countFail
    def setcountFail(self, value):
        self.countFail = value
    def getcountFail(self):
        return self.countFail

    # Getter and setter for resume
    def setresume(self, value):
        self.resume = value
    def getresume(self):
        return self.resume

    # Getter and setter for generateReport
    def setgenerateReport(self, value):
        self.generateReport = value
    def getgenerateReport(self):
        return self.generateReport

    def addresume(self, value):
        self.resume = self.resume + str(value) + "\n"

    def addCountSuccess(self):
        self.countSuccess = self.countSuccess + 1

    def addCountFail(self):
        self.countFail = self.countFail + 1

    def addTestCount(self):
        self.countTest = self.countTest + 1

    def teslaPrint(self, msg):
        self.setresume(self.resume + "\n"+ "| "+str(msg))
        # print(" >"+str(msg))

    def headTestPresentation(self):
        self.setresume(self.resume + "\n-Test "+str(self.countTest+1)+"----------------------------------------------------------\n|")

    def footTestPresentation(self):
        self.setresume(self.resume + "\n")

    def returnStateMentIfMessageIsEmpty(self, msg, statement):
        if msg == None:
            return statement + ":"
        else:
            return msg + ":\n| >> " + statement


    def checkCore(self, assertt, assert_string=None, msg=None):

        self.headTestPresentation()
        self.addTestCount()

        if assert_string != None:
            self.teslaPrint(">> "+str(assert_string))
        self.teslaPrint("<< "+str(assertt))

        status = "✗"
        if assertt == True:
            self.addCountSuccess()
            status = "✓"
        else:
            self.addCountFail()

        if (msg != None):
            self.teslaPrint(str(msg))

        self.teslaPrint("_______________________________________________________________")
        self.teslaPrint("")

        if assertt == True:
            self.teslaPrint("Status: "+ status + " Success!")
        else:
            self.teslaPrint("Status: "+ status + " Failed!")

        self.teslaPrint("End on: "+str(self.getTestTimer()) + " s.")

        self.teslaPrint("_______________________________________________________________")

        self.footTestPresentation()


    def checkAsswert(self, assertt, assert_string=None, msg=None):
        # Timer started!
        self.setTestTimer(0)
        then = time.time() #Time before the operations start

        self.checkCore(assertt, assert_string, msg)

        now = time.time() #Time after it finished
        self.setTestTimer(now-then)
        self.setTotalTimer(self.totalTimer + int(self.getTestTimer()))

        return assertt


    def checkAsswertFunction(self, assertt, assert_string=None, msg=None):
        self.checkCore(assertt, assert_string, msg)
        return assertt


    def deleteDuplicateLine(self, filePath):
        lines_seen = set() # holds lines already seen
        outfile = open(filePath+"_tmp_", "w")
        for line in open(filePath, "r"):
            if line not in lines_seen: # not a duplicate
                outfile.write(line)
                lines_seen.add(line)
        outfile.close()

        with open(filePath+"_tmp_", "r+") as filet:
            with open(filePath, "w") as filet2:
                filet2.write(filet.read())

        # We delete the tempory file
        remove(filePath+"_tmp_")


    def recordOrNot(self, recordMode, line, start_block, end_block):
        if not recordMode:
            if start_block in line:
                recordMode = True
        elif end_block in line:
            recordMode = False
        return recordMode


    # This method test the list of functions contained in a file
    def TestFunctionsInAFile(self, filePath):
        if(not pathit.isdir(filePath)):
            print("Tesla testing on "+filePath)
            self.teslaPrint("**********************************************************************************************************************************")
            self.teslaPrint("---------------------------------------------------------------")
            self.teslaPrint(" Tesla-Test on :"+ filePath)
            self.teslaPrint("---------------------------------------------------------------")
            # Read the file and parcours line by lines
            Case = []
            Result = []
            functions = []
            function_toWrite = ""
            allready_write = ""
            with open(filePath, 'r') as filee:
                lines = filee.readlines()

                inRecordingMode = False
                inRecordingMode2 = False
                inRecordingMode3 = False

                isAssert = False

                for line in lines:

                    # First we get the tesla block
                    if not inRecordingMode:
                        if "::tesla_start::" in line:
                            inRecordingMode = True
                    elif "::tesla_end::" in line:
                        inRecodingMode = False
                    else:
                        # Second we get the case block
                        # Here we find the test Case
                        if not inRecordingMode2:
                            if "::case_start::" in line:
                                inRecordingMode2 = True
                        elif "::case_end::" in line:
                            inRecodingMode2 = False
                        else:

                            # We need to verify here if it's a simple assert or more
                            case_to_add = line.replace(" ", "").replace(">>", "").replace(self.commentStartBy, "")
                            if ">>" in line:
                                if case_to_add not in Case:
                                    # We append on Case list
                                    Case.append(case_to_add)

                                    if "tesla." in line:
                                        isAssert = True
                                        functions_filepath = "testfunction__"+str(self.iteration)+self.extension
                                        if len(line) > 3:
                                            if functions_filepath not in functions and line not in allready_write:
                                                # We append on function list
                                                functions.append(functions_filepath)
                                                allready_write += case_to_add

                                            with open(functions_filepath, "a+") as fileee:
                                                # We replace the output method by putting a comment at the beginning
                                                fileee.write( case_to_add.replace(self.outputMethod, self.commentStartBy+self.outputMethod) )

                            # if it's not a simple assertion
                            result_to_add = line.replace(" ", "").replace("<<", "").replace(self.commentStartBy, "")
                            if "<<" in line and len(Result) < len(Case):
                                #if result_to_add not in Result:
                                # We append on Result list
                                Result.append(result_to_add)

                        # Third, the code block
                        if (isAssert == False):
                            # The function and then
                            if not inRecordingMode3:
                                if "::code_start::" in line:
                                    self.iteration = self.iteration + 1
                                    inRecordingMode3 = True
                                    function_toWrite = ""

                            elif "::code_end::" in line:

                                self.iteration = self.iteration + 1
                                inRecodingMode3 = False
                                function_toWrite = ""

                                # with open("testfunction__"+str(iteration - 1)+".py", "w+") as fileee:
                                #     fileee.write(Case[iteration])
                            else:
                                # We write this in the file
                                # Remove all commented line
                                functions_filepath = "testfunction__"+str(self.iteration)+self.extension
                                # print(functions_filepath)
                                if "#" not in line and len(line) > 3 and line not in allready_write:
                                    function_toWrite += line + "\n"
                                    allready_write += function_toWrite

                                    if functions_filepath not in functions:
                                        # We append on function list
                                        functions.append(functions_filepath)
                                    with open(functions_filepath, "a+") as fileee:
                                        # We replace the output method by putting a comment at the beginning
                                        fileee.write( function_toWrite.replace(self.outputMethod, self.commentStartBy+self.outputMethod) )

                        elif (isAssert == True):
                            self.iteration = self.iteration + 1
                            isAssert = False

            # Parcours now each functions file path
            ii = 0 # iteration for Test Case array
            # print("functions: ", functions)
            # print("Case: ", Case)
            # print("Result: ", Result)
            for fnc in functions:
                # if it's not a simple assertion
                to_write = self.outputMethod+"("+Case[ii]+")"+self.semicolomn+" \n " + self.commentStartBy+" Should returns: "+Result[ii]

                # We open each function path and add the tesla class a the top
                with open(fnc, "r+") as fileee:
                    to_append_at_the_end = fileee.read()
                    with open(fnc, "w") as fileee2:
                        fileee2.write( self.scriptStarter +"\n"+ self.TeslAssertClass + "\n\n" + to_append_at_the_end) #  + self.AccoladEnd

                with open(fnc, "a+") as fileee:
                    fileee.write(self.tryCatch.replace("****", to_write) + self.scriptEnder)

                # Let's delete duplicated lines
                self.deleteDuplicateLine(fnc)
                ii = ii + 1

            # Now we will test each function by running each file and get the result
            # if the result is what it's expect We build a Test that win, if not we write it failed
            ii = 0 # iteration for Test Case array
            for file_function in functions:

                # Timer started!
                self.setTestTimer(0)
                then = time.time() #Time before the operations start

                proc = Popen([self.launcher, file_function], stdout=PIPE, stderr=STDOUT)
                output = proc.communicate()[0].decode("utf-8")

                function_ = str(Case[ii].replace("\n", "").split("(")[0])
                statement_ = str(Case[ii].replace("\n", ""))
                output_ = str(output.replace("\n", ""))
                retult_ = str(Result[ii].replace("\n", ""))

                descriptive_message = ""
                descriptive_message += "\n| On: "+ function_ + "\n"
                descriptive_message += "| Statement: "+ statement_ + "\n"
                descriptive_message += "| output: "+ output_ + "\n"

                # if it's not a simple assertion
                descriptive_message += "| Wanted : "+ retult_ + ""


                output = output.replace("\n", "")
                wanted = Result[ii].replace("\n", "")
                assert_ = (output_.lower() == wanted.lower())
                assert_string = "output == wanted"

                if assert_ == False:
                    if ii == 0:
                        self.listAssertFailed += "\n%% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n%% Tests failing:"
                    self.listAssertFailed += "\n%%    -'"+function_+"' in "+filePath

                now = time.time() #Time after it finished
                self.setTestTimer(now-then)
                self.setTotalTimer(self.totalTimer + int(self.getTestTimer()))

                self.checkAsswertFunction(assert_, assert_string, descriptive_message)

                if wanted == output:
                    print("| Success!\n-----------------------------------------------------")
                else:
                    print("| Error")

                # We remove the tempory function file
                remove(file_function)
                ii = ii + 1

    def Function(self, filePath, extension_list=None): # This method test all functions in one application

        # --------------------------------------------------------------------------------
        # The GRAMMAR --------------------------------------------------------------------

        # ::tesla_start::
        # ::case_start::
        # >> addition(2, 2)
        # << 4
        # ::case_end::
        # ::code_start::
        # --- Your specific function source code here!
        # ::code_end::
        # ::tesla_end::

        # The GRAMMAR --------------------------------------------------------------------
        # --------------------------------------------------------------------------------

        path = filePath
        if extension_list == None:
            self.TestFunctionsInAFile(path)
        else:
            if(pathit.exists(path)):
                if(pathit.isfile(path)):
                    print("> A file given!")
                    self.TestFunctionsInAFile(path)
                else:
                    if(pathit.isdir(path)):
                        # if it start with.
                        if(any(ext in path for ext in extension_list)):
                            print("> Skipping: ", path)
                        else:
                            print("> ---------")
                            print("> In "+str(path))
                            for path in Path(path).glob('**/*'):
                                if (not pathit.isdir(path)):
                                    self.TestFunctionsInAFile(str(path))
                    else:
                        print("> This path " + str(path) + " is not valid, please verify it again before relaunch me.")
            else:
                print("> This path " + str(path) + " (file/directory) is not valid.")

        print("Tesla testing ended on "+str(path))


    def generateDoc(self): # This method will generate automaticcally a small documentation in html format of sure about tests done on a function
        # --------------------------------------------------------------------------------
        # The GRAMMAR --------------------------------------------------------------------

        # ::tesla_start::
        #
        # ::doc_start::
        #  .
        #  Here a small description of the function  that will be generate on the documentation
        #  .
        # ::doc_end::
        #
        # ::case_start::
        # >> addition(2, 2)
        # << 4
        # ::case_end::
        #
        # ::code_start::
        #
        # --- Your specific function source code here!
        #
        # ::code_end::
        #
        # ::tesla_end::

        # The GRAMMAR --------------------------------------------------------------------

        print("[+] Starting generating documentation...")


########################################################################################
########################################################################################
# THE MAIN WHERE WE WORK
########################################################################################

import argparse

# 1- GET PARAMS
# PROCEED WITH TESTS
def main():
    prs = argparse.ArgumentParser()
    prs.add_argument('-c', '--config', help='The Tesla configuration file', type=str)
    prs = prs.parse_args()


    config = prs.config

    try:

        if config != None :

            with open(config, 'r+') as filee:
                teslaconfig = json.loads(filee.read())

                # We instantiate the Tesla Test
                TeslaTest = Tesla()

                TeslaTest.scriptStarter = teslaconfig["scriptStarter"]
                TeslaTest.prefixVariable = teslaconfig["prefixVariable"]
                TeslaTest.commentStartBy = teslaconfig["commentStartBy"]
                TeslaTest.launcher = teslaconfig["launcher"]
                TeslaTest.outputMethod = teslaconfig["outputMethod"]
                TeslaTest.extension = teslaconfig["extensions"][0]
                TeslaTest.tryCatch = teslaconfig["tryCatch"]
                # For building class test
                TeslaTest.function = teslaconfig["function"] # function, etc...
                TeslaTest.varDeclaration = teslaconfig["varDeclaration"] # var, let, etc...
                TeslaTest.classInstantiationNew = teslaconfig["classInstantiationNew"] # new, etc...
                TeslaTest.AccoladStart = teslaconfig["AccoladStart"] # {
                TeslaTest.AccoladEnd = teslaconfig["AccoladEnd"] # }
                TeslaTest.NoneNull = teslaconfig["NoneNull"] # null
                TeslaTest.selfOrThis = teslaconfig["selfOrThis"] # this
                TeslaTest.selfOnFunctionParams = teslaconfig["selfOnFunctionParams"] # if there is a need of self in the declaration of a function
                TeslaTest.semicolomn = teslaconfig["semicolomn"] # ;
                TeslaTest.scriptEnder = teslaconfig["scriptEnder"]

                # We Start the TeslaTest
                TeslaTest.start()

                # We can generate a Report of the test we are going to do:
                TeslaTest.setgenerateReport(True)

                for ppath in teslaconfig["path"]:
                    TeslaTest.Function(ppath, teslaconfig["extensions"])

                # Most Important, ALWAYS We need to End the test.
                TeslaTest.end()
                # We Print the Report resume:
                # print(TeslaTest.getresume())
                print("Reports saved in './"+TeslaTest.date_report+"'")
        else:
            print("Bad parameters input for the path and the config!")

    except Exception as es:
        print("Tesla just Crached !!!")
        print(es)

# Let's run the Main script
main()