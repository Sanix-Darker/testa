#!/usr/bin/python

#
# -----------------------------------------------------------------------------------------------------
#
#  _____ _____ ____ _____       _    
# |_   _| ____/ ___|_   _|     / \   
#   | | |  _| \___ \ | |_____ / _ \  
#   | | | |___ ___) || |_____/ ___ \ 
#   |_| |_____|____/ |_|    /_/   \_\
#
# Welcome to Testa Python's Class implementation
# A simple Class that's allow you to do UnitTests grammatically whatever the language you are using.
# Testa will be able tout test assertions, functions, classes and a complete application.
# Created by Sanix-darker [ https://github.com/sanix-darker ]
# -----------------------------------------------------------------------------------------------------
#
import json
import time
import argparse
from os import remove, path as pathit
from subprocess import Popen, PIPE, STDOUT

from src import custom_pathlib as customPath
from src.utils import *

Path = customPath.Path


class Testa:

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
        self.scriptStarter = " "  # with what the script start For example in php it's <?php, etc...
        self.prefixVariable = ""  # in php we have '$' for example
        self.function = "def "  # function, etc...
        self.varDeclaration = ""  # var, let, etc...
        self.classInstantiationNew = ""  # new, etc...
        self.AccoladeStart = ":"  # {
        self.AccoladeEnd = ""  # }
        self.NoneNull = "None"  # null
        self.selfOrThis = "self"  # this
        self.self_on_function_params = True  # if there is a need of self in the declaration of a function
        self.semicolon = ""  # ;
        self.TeslAssertClass = ""
        self.listAssertFailed = ""
        self.date_report = ""
        self.scriptEnd = " "  # with what the script start For example in php it's <?php, etc...

    def start(self):
        self.addResume("""
##################################################################
#      _____ _____ ____ _____       _                            #
#     |_   _| ____/ ___|_   _|     / \\                           #
#       | | |  _| \\___ \\ | |_____ / _ \\                          #
#       | | | |___ ___) || |_____/ ___ \\                         #
#       |_| |_____|____/ |_|    /_/   \\_\\ v0.1                   #
#----------------------------------------------------------------#
#-------------------------------------------- By S@n1x d4rk3r ---#
##################################################################
        """)

        self.date_report = "reports_" + time.strftime("%Y-%m-%d_%H:%M:%S")

        # Assert Method tests,let's build our TestClass ere to do tests
        self.TeslAssertClass = "class TestaAssert" + self.AccoladeStart

        # self.TeslAssertClass += "\n    "+self.function+" __init__("+self.selfOnParams(self.selfOrThis,
        # self.self_on_function_params)+")"+self.AccoladeStart self.TeslAssertClass += "\n
        # "+self.selfOrThis+".zero = 0"+self.semicolon + self.AccoladeEnd

        self.TeslAssertClass += "\n    " + self.function + " checkAssert(" + str(
            selfOnParams(self.selfOrThis, self.self_on_function_params, True)) + " " + self.prefixVariable + "assertt)" + self.AccoladeStart
        
        self.TeslAssertClass += "\n        return " + self.prefixVariable + "assertt" + self.semicolon + self.AccoladeEnd

        self.TeslAssertClass += "\n    " + self.function + " isEqual(" + str(
            selfOnParams(self.selfOrThis, self.self_on_function_params, True)) + " " + self.prefixVariable + "a, " + self.prefixVariable + "b)" \
                                + self.AccoladeStart

        self.TeslAssertClass += "\n        return " + self.selfOrThis + ".checkAssert(" \
                                + self.prefixVariable + "a == " + self.prefixVariable + "b)" + self.semicolon \
                                + self.AccoladeEnd

        self.TeslAssertClass += "\n    " + self.function + " isNotEqual(" + str(
            selfOnParams(self.selfOrThis, self.self_on_function_params,
                         True)) + " " + self.prefixVariable + "a, " + self.prefixVariable + "b)" \
                                + self.AccoladeStart

        self.TeslAssertClass += "\n        return " + self.selfOrThis + ".checkAssert(" + self.prefixVariable \
                                + "a != " + self.prefixVariable + "b)" + self.semicolon + self.AccoladeEnd

        self.TeslAssertClass += "\n    " + self.function + " isTrue(" + str(
            selfOnParams(self.selfOrThis, self.self_on_function_params,
                         True)) + " " + self.prefixVariable + "x)" + self.AccoladeStart
        
        self.TeslAssertClass += "\n        return  " + self.selfOrThis + ".checkAssert(" + self.prefixVariable + "x)" \
                                + self.semicolon + self.AccoladeEnd

        self.TeslAssertClass += "\n    " + self.function + " isFalse(" + str(
            selfOnParams(self.selfOrThis, self.self_on_function_params,
                         True)) + " " + self.prefixVariable + "y)" + self.AccoladeStart
        
        self.TeslAssertClass += "\n        return  " + self.selfOrThis + ".checkAssert(" + self.prefixVariable + "y)" \
                                + self.semicolon + self.AccoladeEnd

        self.TeslAssertClass += "\n    " + self.function + " isIsNoneNull(" + str(
            selfOnParams(self.selfOrThis, self.self_on_function_params,
                         True)) + " " + self.prefixVariable + "x)" + self.AccoladeStart
        
        self.TeslAssertClass += "\n        return " + self.selfOrThis + ".checkAssert(" + self.prefixVariable \
                                + "x == " + self.NoneNull + ")" + self.semicolon + self.AccoladeEnd

        self.TeslAssertClass += "\n    " + self.function + " isIsNotNoneNull(" + str(
            selfOnParams(self.selfOrThis, self.self_on_function_params,
                         True)) + " " + self.prefixVariable + "x)" + self.AccoladeStart
        
        self.TeslAssertClass += "\n        return " + self.selfOrThis + ".checkAssert(" + self.prefixVariable \
                                + "x != " + self.NoneNull + ")" + self.semicolon + self.AccoladeEnd

        
        self.TeslAssertClass += "\n    " + self.function + " isSup(" + str(
            selfOnParams(self.selfOrThis, self.self_on_function_params,
                         True)) + " " + self.prefixVariable + "a, " + self.prefixVariable + "b)" \
                                + self.AccoladeStart
        
        self.TeslAssertClass += "\n        return " + self.selfOrThis + ".checkAssert(" + self.prefixVariable \
                                + "a > " + self.prefixVariable + "b)" + self.semicolon + self.AccoladeEnd

        self.TeslAssertClass += "\n    " + self.function + " isSupEqual(" + str(
            selfOnParams(self.selfOrThis, self.self_on_function_params, True)) + " " + self.prefixVariable + "a, "\
                 + self.prefixVariable + "b)" + self.AccoladeStart
        
        self.TeslAssertClass += "\n        return " + self.selfOrThis + ".checkAssert(" + self.prefixVariable \
                                + "a >= " + self.prefixVariable + "b)" + self.semicolon + self.AccoladeEnd

        self.TeslAssertClass += "\n    " + self.function + " isInf(" + str(
            selfOnParams(self.selfOrThis, self.self_on_function_params,
                         True)) + " " + self.prefixVariable + "a, " + self.prefixVariable + "b)" \
                                + self.AccoladeStart
        self.TeslAssertClass += "\n        return " + self.selfOrThis + ".checkAssert(" + self.prefixVariable \
                                + "a < " + self.prefixVariable + "b)" + self.semicolon + self.AccoladeEnd

        self.TeslAssertClass += "\n    " + self.function + " isInfEqual(" + str(
            selfOnParams(self.selfOrThis, self.self_on_function_params,
                         True)) + " " + self.prefixVariable + "a, " + self.prefixVariable + "b)" + self.AccoladeStart

        self.TeslAssertClass += "\n        return " + self.selfOrThis + ".checkAssert(" + self.prefixVariable \
                                + "a <= " + self.prefixVariable + "b)" + self.semicolon + self.AccoladeEnd

        self.TeslAssertClass += self.AccoladeEnd

        # Let instantiate the class
        self.TeslAssertClass += "\n" + self.varDeclaration + "testa = " + self.classInstantiationNew + "TestaAssert()" \
                                + self.semicolon

    def end(self):
        self.addResume("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        self.addResume("%% Testa reports:")
        self.addResume("%%")
        self.addResume("%% " + str(self.countTest) + " tests done! ")
        self.addResume("%%")
        self.addResume("%% " + str(self.countSuccess) + " succeed and " + str(self.countFail) + " failed!")
        self.addResume("%% " + self.listAssertFailed)
        self.addResume(
            "%% " + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" if len(self.listAssertFailed) > 3 else "")
        self.addResume("%% Running time: " + str(self.totalTimer) + " s")
        self.addResume("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        if self.generateReport:
            with open("reports_" + time.strftime("%Y-%m-%d_%H:%M:%S") + ".txt", "w") as ffr:
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
        while True:
            time.sleep(0.0001)
            self.testTimer += 0.0001
            self.totalTimer += 0.0001

            if self.stopTestTimer:
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
    def setResume(self, value):
        self.resume = value

    def getResume(self):
        return self.resume

    # Getter and setter for generateReport
    def setGenerateReport(self, value):
        self.generateReport = value

    def getGenerateReport(self):
        return self.generateReport

    def addResume(self, value):
        self.resume = self.resume + str(value) + "\n"

    def addCountSuccess(self):
        self.countSuccess = self.countSuccess + 1

    def addCountFail(self):
        self.countFail = self.countFail + 1

    def addTestCount(self):
        self.countTest = self.countTest + 1

    def testaPrint(self, msg):
        self.setResume(self.resume + "\n" + "| " + str(msg))
        # print("[+]  >"+str(msg))

    def headTestPresentation(self):
        self.setResume(self.resume + "\n-Test " + str(
            self.countTest + 1) + "----------------------------------------------------------\n|")

    def footTestPresentation(self):
        self.setResume(self.resume + "\n")

    def checkCore(self, assertt, assert_string=None, msg=None):

        self.headTestPresentation()
        self.addTestCount()

        if assert_string is not None:
            self.testaPrint(">> " + str(assert_string))
        self.testaPrint("<< " + str(assertt))

        status = "✗"
        if assertt:
            self.addCountSuccess()
            status = "✓"
        else:
            self.addCountFail()

        if msg is not None:
            self.testaPrint(str(msg))

        self.testaPrint("_______________________________________________________________")
        self.testaPrint("")

        if assertt:
            self.testaPrint("Status: " + status + " Success!")
        else:
            self.testaPrint("Status: " + status + " Failed!")

        self.testaPrint("End on: " + str(self.getTestTimer()) + " s.")

        self.testaPrint("_______________________________________________________________")

        self.footTestPresentation()

    def checkAssert(self, assertt, assert_string=None, msg=None):
        # Timer started!
        self.setTestTimer(0)
        then = time.time()  # Time before the operations start

        self.checkCore(assertt, assert_string, msg)

        now = time.time()  # Time after it finished
        self.setTestTimer(now - then)
        self.setTotalTimer(self.totalTimer + int(self.getTestTimer()))

        return assertt

    def checkAssertFunction(self, assertt, assert_string=None, msg=None):
        self.checkCore(assertt, assert_string, msg)
        return assertt

    # This method test the list of functions contained in a file
    def TestFunctionsInAFile(self, file_path):
        if not pathit.isdir(file_path):
            print("[+] Testa testing on " + file_path)
            self.testaPrint("******************************************************************************")
            self.testaPrint("---------------------------------------------------------------")
            self.testaPrint(" Testa-Test on :" + file_path)
            self.testaPrint("---------------------------------------------------------------")
            # Read the file and parcours line by lines
            case = []
            result = []
            functions = []
            function_to_write = ""
            allready_write = ""
            import_to_write = ""
            doc_ = ""
            with open(file_path, 'r') as filee:
                lines = filee.readlines()

                in_recording_mode = False
                in_recording_mode2 = False
                in_recording_mode3 = False
                in_recording_mode4 = False
                in_recording_mode5 = False

                is_assert = False

                for line in lines:

                    # if we have some import at the head of the file that's method depends on
                    # First we get the testa block
                    if not in_recording_mode5:
                        if "::import_start::" in line:
                            in_recording_mode5 = True
                    elif "::import_end::" in line:
                        in_recording_mode5 = False
                        # import_to_write = ""
                    else:
                        import_to_write += line.replace(self.commentStartBy, "") + "\n"

                    # First we get the testa block
                    if not in_recording_mode:
                        if "::testa_start::" in line:
                            in_recording_mode = True
                    elif "::testa_end::" in line:
                        in_recording_mode = False
                    else:

                        if not in_recording_mode4:
                            if "::doc_start::" in line:
                                in_recording_mode4 = True
                                doc_ = "------------------------------------------\n Documentation on :" + file_path \
                                       + "\n------------------------------------------"
                        elif "::doc_end::" in line:
                            with open("./doc_" + file_path.replace("/", "-").replace(self.extension, "") + ".txt",
                                      "w") as frt:
                                frt.write(doc_)
                            in_recording_mode4 = False
                            doc_ = ""
                        else:
                            doc_ += "\n" + line.replace(self.commentStartBy, "")

                        # Second we get the case block
                        # Here we find the test case
                        if not in_recording_mode2:
                            if "::case_start::" in line:
                                in_recording_mode2 = True
                        elif "::case_end::" in line:
                            in_recording_mode2 = False
                        else:
                            # We need to verify here if it's a simple assert or more
                            case_to_add = line.replace(" ", "").replace(">>", "").replace(self.commentStartBy, "")
                            if ">>" in line:
                                if case_to_add not in case:
                                    # We append on case list
                                    case.append(case_to_add)

                                    if "testa." in line:
                                        is_assert = True
                                        functions_filepath = "testfunction__" + str(self.iteration) + self.extension
                                        if len(line) > 3:
                                            if functions_filepath not in functions and line not in allready_write:
                                                # We append on function list
                                                functions.append(functions_filepath)
                                                allready_write += case_to_add

                                            with open(functions_filepath, "a+") as fileee:
                                                # We replace the output method by putting a comment at the beginning
                                                fileee.write(case_to_add.replace(self.outputMethod,
                                                                                 self.commentStartBy
                                                                                 + self.outputMethod))

                            # if it's not a simple assertion
                            result_to_add = line.replace(" ", "").replace("<<", "").replace(self.commentStartBy, "")
                            if "<<" in line and len(result) < len(case):
                                # if result_to_add not in result:
                                # We append on result list
                                result.append(result_to_add)

                        # Third, the code block
                        if not is_assert:
                            # The function and then
                            if not in_recording_mode3:
                                if "::code_start::" in line:
                                    self.iteration = self.iteration + 1
                                    in_recording_mode3 = True

                                    function_to_write += import_to_write

                            elif "::code_end::" in line:

                                self.iteration = self.iteration + 1
                                in_recording_mode3 = False
                                function_to_write = ""

                            else:
                                # We write this in the file
                                # Remove all commented line
                                functions_filepath = "testfunction__" + str(self.iteration) + self.extension
                                # print(functions_filepath)
                                if "#" not in line and len(line) > 3 and line not in allready_write:
                                    function_to_write += line.replace(self.commentStartBy, "") + "\n"
                                    allready_write += function_to_write

                                    if functions_filepath not in functions:
                                        # We append on function list
                                        functions.append(functions_filepath)
                                    with open(functions_filepath, "a+") as fileee:
                                        # We replace the output method by putting a comment at the beginning
                                        fileee.write(function_to_write.replace(self.outputMethod,
                                                                               self.commentStartBy + self.outputMethod))

                        elif is_assert:
                            self.iteration = self.iteration + 1
                            is_assert = False

            # Parcours now each functions file path
            ii = 0  # iteration for Test case array
            # print("[+] functions: ", functions)
            # print("[+] case: ", case)
            # print("[+] result: ", result)
            for fnc in functions:
                # if it's not a simple assertion
                to_write = self.outputMethod + "(" + case[ii].replace("\n", "") + ")" + self.semicolon + " \n " \
                           + self.commentStartBy + " Should returns: " + \
                           result[ii]

                # We open each function path and add the testa class a the top
                with open(fnc, "r+") as fileee:
                    to_append_at_the_end = fileee.read()
                    with open(fnc, "w") as fileee2:
                        fileee2.write(
                            self.scriptStarter + "\n" + self.TeslAssertClass + "\n\n" + import_to_write + "\n\n"
                            + to_append_at_the_end)  # + self.AccoladeEnd

                with open(fnc, "a+") as fileee:
                    # print("[+] FINAL: ", self.tryCatch.replace("****", to_write) + self.scriptEnd)
                    fileee.write(self.tryCatch.replace("****", to_write) + self.scriptEnd)

                # Let's delete duplicated lines
                delete_duplicate_line(fnc)
                ii = ii + 1

            # Now we will test each function by running each file and get the result
            # if the result is what it's expect We build a Test that win, if not we write it failed
            ii = 0  # iteration for Test case array
            for file_function in functions:

                # Timer started!
                self.setTestTimer(0)
                then = time.time()  # Time before the operations start

                proc = Popen([self.launcher, file_function], stdout=PIPE, stderr=STDOUT)
                output = proc.communicate()[0].decode("utf-8")

                function_ = str(case[ii].replace("\n", "").split("(")[0])
                statement_ = str(case[ii].replace("\n", ""))
                output_ = str(output.replace("\n", ""))
                retult_ = str(result[ii].replace("\n", ""))

                descriptive_message = ""
                descriptive_message += "\n| On: " + function_ + "\n"
                descriptive_message += "| Statement: " + statement_ + "\n"
                descriptive_message += "| output: " + output_ + "\n"

                # if it's not a simple assertion
                descriptive_message += "| Wanted : " + retult_ + ""

                output = output.replace("\n", "")
                wanted = result[ii].replace("\n", "")
                assert_ = (output_.lower() == wanted.lower())
                assert_string = "output == wanted"

                if not assert_:
                    if ii == 0:
                        self.listAssertFailed += "\n%% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n%% Tests " \
                                                 "failing: "
                    self.listAssertFailed += "\n%%    -'" + function_ + "' in " + file_path

                now = time.time()  # Time after it finished
                self.setTestTimer(now - then)
                self.setTotalTimer(self.totalTimer + int(self.getTestTimer()))

                self.checkAssertFunction(assert_, assert_string, descriptive_message)

                if wanted == output:
                    print("[+] | Success!\n-----------------------------------------------------")
                else:
                    print("[+] | Error")

                # We remove the tempory function file
                remove(file_function)
                ii = ii + 1

    def Function(self, file_path, extension_list=None):  # This method test all functions in one application

        path = file_path
        if extension_list is None:
            self.TestFunctionsInAFile(path)
        else:
            if pathit.exists(path):
                if pathit.isfile(path):
                    print("[+] Tests started...!")
                    self.TestFunctionsInAFile(path)
                else:
                    if pathit.isdir(path):
                        # if it start with.
                        if any(ext in path for ext in extension_list):
                            print("[+] > Skipping: ", path)
                        else:
                            print("[+] > ---------")
                            print("[+] > In " + str(path))
                            for path in Path(path).glob('**/*'):
                                if not pathit.isdir(path):
                                    self.TestFunctionsInAFile(str(path))
                    else:
                        print("[+] > This path " + str(path)
                              + " is not valid, please verify it again before relaunch me.")
            else:
                print("[+] > This path " + str(path) + " (file/directory) is not valid.")

        print("[+] Testa testing ended on " + str(path))

# Let's run the Main script
# main()
