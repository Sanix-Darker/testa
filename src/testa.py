#!/usr/bin/python

"""
 -----------------------------------------------------------------------------

  _____ _____ ____ _____       _
 |_   _| ____/ ___|_   _|     / \
   | | |  _| \___ \ | |_____ / _ \
   | | | |___ ___) || |_____/ ___ \
   |_| |_____|____/ |_|    /_/   \_\

 Welcome to Testa Python's Class implementation
 A simple Class that's allow you to do UnitTests grammatically whatever the language you are using.
 Testa will be able tout test assertions, functions, classes and a complete application.
 Created by Sanix-darker [ https://github.com/sanix-darker ]
 -----------------------------------------------------------------------------

"""

import time
from os import path as pathit
from os import remove
from subprocess import PIPE, STDOUT, Popen

from src import custom_pathlib as customPath
from src.utils import *

Path = customPath.Path

class TestaAssert:
    def __init__(
        self,
        scriptStarter=" ",
        prefixVariable="",
        commentStartBy="#",
        launcher="python",
        outputMethod="print",
        extension=".py",
        tryCatch="try: \n\t **** \nexcept Exception as es: \n\t print(str(es))",
        function="def ",
        varDeclaration="",
        classInstantiationNew="",
        AccoladeStart=":",
        AccoladeEnd="",
        NoneNull="None",
        selfOrThis="self",
        self_on_function_params=True,
        semicolon="",
        scriptEnd=" ",
    ):

        (
            self.countTest,
            self.countSuccess,
            self.countFail,
            self.totalTimer,
            self.testTimer,
            self.stopTestTimer,
            self.iteration,
        ) = (0, 0, 0, 0, 0, 0, 0)

        self.resume = ""
        self.generateReport = True
        self.commentStartBy = commentStartBy
        self.launcher = launcher
        self.outputMethod = outputMethod
        self.extension = extension
        self.tryCatch = tryCatch

        # For building class test
        # with what the script start For example in php it's <?php, etc...
        self.scriptStarter = scriptStarter
        # in php we have '$' for example
        self.prefixVariable = prefixVariable
        # function, etc...
        self.function = function
        # var, let, etc...
        self.varDeclaration = varDeclaration
        # new, etc...
        self.classInstantiationNew = classInstantiationNew
        # {
        self.AccoladeStart = AccoladeStart
        # }
        self.AccoladeEnd = AccoladeEnd
        # null
        self.NoneNull = NoneNull
        # this
        self.selfOrThis = selfOrThis
        # if there is a need of self in the declaration of a function
        self.self_on_function_params = self_on_function_params
        # ;
        self.semicolon = semicolon
        self.TeslAssertClass = ""
        self.listAssertFailed = ""
        self.date_report = ""
        # with what the script start For example in php it's <?php, etc...
        self.scriptEnd = scriptEnd

    def start(self):
        """ """
        self.addResume("# TESTA reports")

        self.date_report = "reports_" + time.strftime("%Y-%m-%d_%H:%M:%S")

        # Assert Method tests,let's build our TestClass ere to do tests
        self.TeslAssertClass = "class TestaAssert" + self.AccoladeStart

        self.TeslAssertClass += (
            "\n\t" + self.function + " checkAssert("
            + str(selfOnParams(self.selfOrThis, self.self_on_function_params, True))
            + " " + self.prefixVariable + "assertt)" + self.AccoladeStart
        )

        self.TeslAssertClass += (
            "\n\t\treturn " + self.prefixVariable + "assertt"
            + self.semicolon + self.AccoladeEnd
        )

        self.TeslAssertClass += (
            "\n\t" + self.function + " isEqual("
            + str(selfOnParams(self.selfOrThis, self.self_on_function_params, True))
            + " " + self.prefixVariable + "a, " + self.prefixVariable + "b)"
            + self.AccoladeStart
        )

        self.TeslAssertClass += (
            "\n\t\treturn " + self.selfOrThis + ".checkAssert("
            + self.prefixVariable + "a == "
            + self.prefixVariable + "b)"
            + self.semicolon + self.AccoladeEnd
        )

        self.TeslAssertClass += (
            "\n\t" + self.function + " isNotEqual("
            + str(selfOnParams(self.selfOrThis, self.self_on_function_params, True))
            + " " + self.prefixVariable + "a, "
            + self.prefixVariable + "b)" + self.AccoladeStart
        )

        self.TeslAssertClass += (
            "\n\t\treturn " + self.selfOrThis
            + ".checkAssert(" + self.prefixVariable
            + "a != " + self.prefixVariable + "b)" + self.semicolon
            + self.AccoladeEnd
        )

        self.TeslAssertClass += (
            "\n\t" + self.function + " isTrue("
            + str(selfOnParams(self.selfOrThis, self.self_on_function_params, True))
            + " " + self.prefixVariable + "x)" + self.AccoladeStart
        )

        self.TeslAssertClass += (
            "\n\t\treturn  " + self.selfOrThis
            + ".checkAssert("
            + self.prefixVariable + "x)" + self.semicolon
            + self.AccoladeEnd
        )

        self.TeslAssertClass += (
            "\n\t" + self.function + " isFalse("
            + str(selfOnParams(self.selfOrThis, self.self_on_function_params, True))
            + " " + self.prefixVariable + "y)" + self.AccoladeStart
        )

        self.TeslAssertClass += (
            "\n\t\treturn  " + self.selfOrThis
            + ".checkAssert(" + self.prefixVariable + "y)" + self.semicolon
            + self.AccoladeEnd
        )

        self.TeslAssertClass += (
            "\n\t"
            + self.function + " isIsNoneNull("
            + str(selfOnParams(self.selfOrThis, self.self_on_function_params, True))
            + " " + self.prefixVariable + "x)"
            + self.AccoladeStart
        )

        self.TeslAssertClass += (
            "\n\t\treturn " + self.selfOrThis
            + ".checkAssert(" + self.prefixVariable
            + "x == " + self.NoneNull + ")"
            + self.semicolon + self.AccoladeEnd
        )

        self.TeslAssertClass += (
            "\n\t" + self.function
            + " isIsNotNoneNull("
            + str(selfOnParams(self.selfOrThis, self.self_on_function_params, True))
            + " " + self.prefixVariable + "x)" + self.AccoladeStart
        )

        self.TeslAssertClass += (
            "\n\t\treturn " + self.selfOrThis
            + ".checkAssert(" + self.prefixVariable
            + "x != " + self.NoneNull
            + ")" + self.semicolon + self.AccoladeEnd
        )

        self.TeslAssertClass += (
            "\n\t" + self.function + " isSup("
            + str(selfOnParams(self.selfOrThis, self.self_on_function_params, True))
            + " " + self.prefixVariable
            + "a, " + self.prefixVariable + "b)" + self.AccoladeStart
        )

        self.TeslAssertClass += (
            "\n\t\treturn " + self.selfOrThis
            + ".checkAssert(" + self.prefixVariable
            + "a > " + self.prefixVariable
            + "b)" + self.semicolon + self.AccoladeEnd
        )

        self.TeslAssertClass += (
            "\n\t" + self.function + " isSupEqual("
            + str(selfOnParams(self.selfOrThis, self.self_on_function_params, True))
            + " " + self.prefixVariable + "a, " + self.prefixVariable
            + "b)" + self.AccoladeStart
        )

        self.TeslAssertClass += (
            "\n\t\treturn " + self.selfOrThis
            + ".checkAssert(" + self.prefixVariable
            + "a >= " + self.prefixVariable
            + "b)" + self.semicolon + self.AccoladeEnd
        )

        self.TeslAssertClass += (
            "\n\t" + self.function + " isInf("
            + str(selfOnParams(self.selfOrThis, self.self_on_function_params, True))
            + " " + self.prefixVariable
            + "a, " + self.prefixVariable + "b)"
            + self.AccoladeStart
        )
        self.TeslAssertClass += (
            "\n\t\treturn " + self.selfOrThis
            + ".checkAssert(" + self.prefixVariable
            + "a < " + self.prefixVariable
            + "b)" + self.semicolon + self.AccoladeEnd
        )

        self.TeslAssertClass += (
            "\n\t" + self.function
            + " isInfEqual("
            + str(selfOnParams(self.selfOrThis, self.self_on_function_params, True))
            + " " + self.prefixVariable
            + "a, " + self.prefixVariable + "b)"
            + self.AccoladeStart
        )

        self.TeslAssertClass += (
            "\n\t\treturn " + self.selfOrThis + ".checkAssert("
            + self.prefixVariable + "a <= "
            + self.prefixVariable + "b)" + self.semicolon
            + self.AccoladeEnd
        )

        self.TeslAssertClass += self.AccoladeEnd

        # Let instantiate the class
        self.TeslAssertClass += (
            "\n" + self.varDeclaration
            + "testa = " + self.classInstantiationNew
            + "TestaAssert()" + self.semicolon
        )

    def end(self):
        self.addResume("\n- - - - - - - - - - - - - - - - - - - - - - - ")
        self.addResume("| > Results:")
        self.addResume("|")
        self.addResume("| " + str(self.countTest) + " test(s) done ! ")
        self.addResume("|")
        self.addResume(
            "| " + str(self.countSuccess)
            + " succeed and " + str(self.countFail) + " failed!"
        )
        self.addResume("| " + self.listAssertFailed)
        self.addResume(
            "| " + "- - - - - - - - -" if len(self.listAssertFailed) > 3 else ""
        )
        self.addResume("| Running time: " + str(self.totalTimer) + " s")
        self.addResume("\n- - - - - - - - - - - - - - - - - - - - - - - ")

        if self.generateReport:
            with open(
                "reports_" + time.strftime("%Y-%m-%d_%H:%M:%S") + ".md", "w"
            ) as ffr:
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

    def headTestPresentation(self):
        self.addResume("\n##### Test " + str(self.countTest + 1))
        self.addResume("----------------------------------")

    def footTestPresentation(self):
        self.setResume(self.resume + "\n")

    def generateFromStatus(self, msg, assertt, status):
        if msg is not None:
            self.testaPrint(str(msg))
        self.testaPrint("- - - - - - -")
        if assertt:
            self.testaPrint("Status: " + status + " Success!")
        else:
            self.testaPrint("Status: " + status + " Failed!")
        self.testaPrint("End on: " + str(self.getTestTimer()) + " s.")
        self.testaPrint("")

    def setStatusCharacter(self, assertt):
        status = "✗"
        if assertt:
            self.addCountSuccess()
            status = "✓"
        else:
            self.addCountFail()
        return status

    def checkCore(self, assertt, assert_string=None, msg=None):
        self.headTestPresentation()
        self.addTestCount()
        # if assert_string is not None:
        #     self.testaPrint(">> " + str(assert_string))
        # self.testaPrint("<< " + str(assertt))
        status = self.setStatusCharacter(assertt)
        self.generateFromStatus(msg, assertt, status)
        self.footTestPresentation()

    def checkAssert(self, assertt, assert_string=None, msg=None):
        # Timer started!
        self.setTestTimer(0)
        # Time before the operations start
        then = time.time()
        self.checkCore(assertt, assert_string, msg)

        # Time after it finished
        self.setTestTimer(time.time() - then)
        self.setTotalTimer(self.totalTimer + int(self.getTestTimer()))

        return assertt

    def checkAssertFunction(self, assertt, assert_string=None, msg=None):
        self.checkCore(assertt, assert_string, msg)
        return assertt


class Testa(TestaAssert):
    def executeEachFunction(self, case, result, file_path, functions):
        """
        Now we will test each function by running each file and get the result
        if the result is what it's expect We build a Test that win, if not we write it failed

        """
        ii = 0  # iteration for Test case array
        for file_function in functions:
            # Timer started!
            self.setTestTimer(0)
            then = time.time()  # Time before the operations start

            proc = Popen([self.launcher, file_function], stdout=PIPE, stderr=STDOUT)
            output = proc.communicate()[0].decode("utf-8")

            function_, statement_ = str(case[ii].replace("\n", "").split("(")[0]), str(
                case[ii].replace("\n", "")
            )
            output_, retult_ = str(output.replace("\n", "")), str(
                result[ii].replace("\n", "")
            )

            descriptive_message = (
                "\n| On: `" + function_ + "`\n" + "| Statement: *" + statement_ + "*\n"
            )
            descriptive_message += (
                "| output: **" + output_ + "**\n" + "| Wanted : ***" + retult_ + "***"
            )
            # if it's not a simple assertion

            output, wanted = output.replace("\n", ""), result[ii].replace("\n", "")
            assert_, assert_string = (
                output_.lower() == wanted.lower()
            ), "output == wanted"

            if not assert_:
                if ii == 0:
                    self.listAssertFailed += (
                        "\n%% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n%% Tests "
                        "failing: "
                    )
                self.listAssertFailed += "\n%%    -'" + function_ + "' in " + file_path

            now = time.time()  # Time after it finished
            self.setTestTimer(now - then)
            self.setTotalTimer(self.totalTimer + int(self.getTestTimer()))
            self.checkAssertFunction(assert_, assert_string, descriptive_message)

            print(
                "[+] | Success!\n------------------------------"
            ) if wanted == output else print("[+] | Error")

            # We remove the tempory function file
            remove(file_function)
            ii = ii + 1

    def proceedFunctionsAndBuildOutput(
        self, case, file_path, result, import_to_write, functions
    ):
        """
        Parcours now each functions file path

        """
        ii = 0  # iteration for Test case array
        for fnc in functions:
            # if it's not a simple assertion
            to_write = (
                self.outputMethod
                + "(" + case[ii].replace("\n", "")
                + ")" + self.semicolon
                + " \n " + self.commentStartBy
                + " Should returns: " + result[ii]
            )
            # We open each function path and add the testa class a the top
            with open(fnc, "r+") as fileee:
                to_append_at_the_end = fileee.read()
                with open(fnc, "w") as fileee2:
                    fileee2.write(
                        self.scriptStarter
                        + "\n" + self.TeslAssertClass
                        + "\n\n" + import_to_write
                        + "\n\n" + to_append_at_the_end
                    )  # + self.AccoladeEnd
            with open(fnc, "a+") as fileee:
                # print("[+] FINAL: ", self.tryCatch.replace("****", to_write) + self.scriptEnd)
                fileee.write(self.tryCatch.replace("****", to_write) + self.scriptEnd)
            # Let's delete duplicated lines
            delete_duplicate_line(fnc)
            ii = ii + 1
        self.executeEachFunction(case, result, file_path, functions)

    def writeFunctionsInFile(self, line, function_to_write, allready_write, functions):
        """
        We write this in the file

        """
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
                fileee.write(
                    function_to_write.replace(
                        self.outputMethod, self.commentStartBy + self.outputMethod
                    )
                )
        return function_to_write, allready_write

    def appendImport(self, line, import_to_write, in_recording_mode5):
        """
        If we have some import at the head of the file that's method depends on

        """
        # First we get the testa block
        if not in_recording_mode5:
            if "::import_start::" in line:
                in_recording_mode5 = True
        elif "::import_end::" in line:
            in_recording_mode5 = False
            # import_to_write = ""
        else:
            import_to_write += line.replace(self.commentStartBy, "") + "\n"

        return in_recording_mode5, import_to_write

    def appendDoc(self, line, file_path, in_recording_mode4):
        """ """
        if not in_recording_mode4:
            if "::doc_start::" in line:
                with open(
                    "./doc_"
                    + file_path.replace("/", "-").replace(self.extension, "")
                    + ".md",
                    "a+",
                ) as frt:
                    frt.write(
                        "------------------------------------------\n "
                        + "Documentation on :" + file_path
                        + "\n------------------------------------------"
                    )
                in_recording_mode4 = True
        elif "::doc_end::" in line:
            in_recording_mode4 = False
        else:
            with open(
                "./doc_" + file_path.replace("/", "-").replace(self.extension, "")
                + ".md",
                "a+",
            ) as frt:
                frt.write("\n" + line.replace(self.commentStartBy, ""))

        return in_recording_mode4

    def appendCode(
        self,
        line,
        functions,
        import_to_write,
        function_to_write,
        allready_write,
        in_recording_mode3,
    ):
        """ """
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
            (function_to_write, allready_write) = self.writeFunctionsInFile(
                line, function_to_write, allready_write, functions
            )

        return in_recording_mode3, function_to_write, allready_write

    def writeFunctionInFile(self, line, case, functions, allready_write):
        """ """
        case_to_add = (
            line.replace(" ", "").replace(">>", "").replace(self.commentStartBy, "")
        )
        if ">>" in line:
            if case_to_add not in case:
                # We append on case list
                case.append(case_to_add)
                if "testa." in line:
                    is_assert = True
                    functions_filepath = (
                        "testfunction__" + str(self.iteration) + self.extension
                    )
                    if len(line) > 3:
                        if (
                            functions_filepath not in functions
                            and line not in allready_write
                        ):
                            # We append on function list
                            functions.append(functions_filepath)
                            allready_write += case_to_add
                        with open(functions_filepath, "a+") as fileee:
                            # We replace the output method by putting a comment at the beginning
                            fileee.write(
                                case_to_add.replace(
                                    self.outputMethod,
                                    self.commentStartBy + self.outputMethod,
                                )
                            )
        return functions, allready_write

    def appendCase(
        self, line, case, result, functions, allready_write, in_recording_mode2
    ):
        """ """
        # Second we get the case block
        # Here we find the test case
        if not in_recording_mode2:
            if "::case_start::" in line:
                in_recording_mode2 = True
        elif "::case_end::" in line:
            in_recording_mode2 = False
        else:
            # We need to verify here if it's a simple assert or more
            functions, allready_write = self.writeFunctionInFile(
                line, case, functions, allready_write
            )

            # if it's not a simple assertion
            result_to_add = (
                line.replace(" ", "").replace("<<", "").replace(self.commentStartBy, "")
            )
            if "<<" in line and len(result) < len(case):
                # if result_to_add not in result: We append on result list
                result.append(result_to_add)

        return in_recording_mode2, allready_write, functions, result

    def testaProcess(
        self,
        line,
        case,
        result,
        is_assert,
        functions,
        file_path,
        function_to_write,
        import_to_write,
        allready_write,
        in_recording_mode4,
        in_recording_mode3,
        in_recording_mode2,
    ):
        """ """
        in_recording_mode4 = self.appendDoc(line, file_path, in_recording_mode4)

        # We append case
        (in_recording_mode2, allready_write, functions, result) = self.appendCase(
            line, case, result, functions, allready_write, in_recording_mode2
        )

        # Third, the code block
        if not is_assert:
            (in_recording_mode3, function_to_write, allready_write) = self.appendCode(
                line,
                functions,
                import_to_write,
                function_to_write,
                allready_write,
                in_recording_mode3,
            )
        elif is_assert:
            self.iteration = self.iteration + 1
            is_assert = False

        return (
            result,
            is_assert,
            in_recording_mode4,
            in_recording_mode3,
            in_recording_mode2,
            function_to_write,
            allready_write,
        )

    def appendTesta(
        self,
        line,
        case,
        result,
        functions,
        is_assert,
        file_path,
        import_to_write,
        allready_write,
        function_to_write,
        in_recording_mode,
        in_recording_mode2,
        in_recording_mode3,
        in_recording_mode4,
    ):
        """ """
        # First we get the testa block
        if not in_recording_mode:
            if "::testa_start::" in line:
                in_recording_mode = True
        elif "::testa_end::" in line:
            in_recording_mode = False
        else:
            (
                result,
                is_assert,
                in_recording_mode4,
                in_recording_mode3,
                in_recording_mode2,
                function_to_write,
                allready_write,
            ) = self.testaProcess(
                line,
                case,
                result,
                is_assert,
                functions,
                file_path,
                function_to_write,
                import_to_write,
                allready_write,
                in_recording_mode4,
                in_recording_mode3,
                in_recording_mode2,
            )

        return (
            in_recording_mode4,
            in_recording_mode3,
            in_recording_mode2,
            in_recording_mode,
            function_to_write,
            allready_write,
            is_assert,
        )

    # This method test the list of functions contained in a file
    def TestFunctionsInAFile(self, file_path):
        """ """
        if not pathit.isdir(file_path):
            print("[+] Testa testing on " + file_path)
            self.addResume("\n------------------------------")
            self.addResume("\n#### File : " + file_path)

            # Read the file and parcours line by lines
            (
                case,
                result,
                functions,
                function_to_write,
                allready_write,
                import_to_write,
            ) = ([], [], [], "", "", "")

            with open(file_path, "r") as filee:
                lines = filee.readlines()
                in_recording_mode, in_recording_mode2, in_recording_mode3 = (
                    False,
                    False,
                    False,
                )
                in_recording_mode4, in_recording_mode5, is_assert = False, False, False

                for line in lines:
                    (in_recording_mode5, import_to_write) = self.appendImport(
                        line, import_to_write, in_recording_mode5
                    )

                    (
                        in_recording_mode4,
                        in_recording_mode3,
                        in_recording_mode2,
                        in_recording_mode,
                        function_to_write,
                        allready_write,
                        is_assert,
                    ) = self.appendTesta(
                        line,
                        case,
                        result,
                        functions,
                        is_assert,
                        file_path,
                        import_to_write,
                        allready_write,
                        function_to_write,
                        in_recording_mode,
                        in_recording_mode2,
                        in_recording_mode3,
                        in_recording_mode4,
                    )

            self.proceedFunctionsAndBuildOutput(
                case, file_path, result, import_to_write, functions
            )

    # This method test all functions in one application
    def Function(self, file_path, extension_list=None):
        """ """
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
                            for path in Path(path).glob("**/*"):
                                if not pathit.isdir(path):
                                    self.TestFunctionsInAFile(str(path))
                    else:
                        print(
                            "[+] > This path "
                            + str(path)
                            + " is not valid, verify it again before relaunch me."
                        )
            else:
                print(
                    "[+] > This path " + str(path) + " (file/directory) is not valid."
                )
        print("[+] Testa testing ended on " + str(path))
