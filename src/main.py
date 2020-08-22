import argparse
import json
from src.testa import Testa
from src.utils import *

########################################################################################
########################################################################################
# THE MAIN WHERE WE WORK
########################################################################################

# 1- GET PARAMS
# PROCEED WITH TESTS
def main():
    prs = argparse.ArgumentParser()
    prs.add_argument('-c', '--config', help='The Testa configuration file', type=str)
    prs = prs.parse_args()

    config = prs.config

    try:
        if config is not None:
            with open(config, 'r+') as filee:
                testaconfig = json.loads(filee.read())

                # We instantiate the Testa Test
                testa_test = Testa()

                testa_test.scriptStarter = testaconfig["scriptStarter"]
                testa_test.prefixVariable = testaconfig["prefixVariable"]
                testa_test.commentStartBy = testaconfig["commentStartBy"]
                testa_test.launcher = testaconfig["launcher"]
                testa_test.outputMethod = testaconfig["outputMethod"]
                testa_test.extension = testaconfig["extensions"][0]
                testa_test.tryCatch = testaconfig["tryCatch"]
                # For building class test
                testa_test.function = testaconfig["function"]  # function, etc...
                testa_test.varDeclaration = testaconfig["varDeclaration"]  # var, let, etc...
                testa_test.classInstantiationNew = testaconfig["classInstantiationNew"]  # new, etc...
                testa_test.AccoladeStart = testaconfig["AccoladeStart"]  # {
                testa_test.AccoladeEnd = testaconfig["AccoladeEnd"]  # }
                testa_test.NoneNull = testaconfig["NoneNull"]  # null
                testa_test.selfOrThis = testaconfig["selfOrThis"]  # this
                testa_test.self_on_function_params = testaconfig[
                    "selfOnFunctionParams"]  # if there is a need of self in the declaration of a function
                testa_test.semicolon = testaconfig["semicolon"]  # ;
                testa_test.scriptEnd = testaconfig["scriptEnd"]

                # We Start the testa_test
                testa_test.start()

                # We can generate a Report of the test we are going to do:
                testa_test.setGenerateReport(True)

                for ppath in testaconfig["path"]:
                    testa_test.Function(ppath, testaconfig["extensions"])

                # Most Important, ALWAYS We need to End the test.
                testa_test.end()
                # We Print the Report resume:
                # print(testa_test.getResume())
                print("[+] Reports saved in './" + testa_test.date_report + "'")
        else:
            print("[+] Bad parameters input for the path and the config!")

    except Exception:
        print("[+] Testa just Crashed, verify your JSON file !!!")
        get_trace()
