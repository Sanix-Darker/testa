import argparse
import json
import sys
from os import listdir, path

from src.modules import *
from src.testa import Testa
from src.utils import *


# 1- GET PARAMS
# PROCEED WITH TESTS
def main():
    if "testa.json" not in listdir("."):
        print("[x] Any testa configuration file present !")
        exit()
    try:
        if not path.exists("testa.json"):
            print("[x] The configuration file doesn't exist !")
            exit()

        with open("testa.json", "r+") as filee:
            testaconfig = json.loads(filee.read())

            if "module" in testaconfig:
                testaconfig.update(global_testa_config[testaconfig["module"]])

            # We instantiate the Testa Test
            testa_test = Testa(
                scriptStarter=testaconfig["scriptStarter"],
                prefixVariable=testaconfig["prefixVariable"],
                commentStartBy=testaconfig["commentStartBy"],
                launcher=testaconfig["launcher"],
                outputMethod=testaconfig["outputMethod"],
                extension=testaconfig["extensions"][0],
                tryCatch=testaconfig["tryCatch"],
                # For building class test
                function=testaconfig["function"],  # function, etc...
                varDeclaration=testaconfig["varDeclaration"],  # var, let, etc...
                classInstantiationNew=testaconfig[
                    "classInstantiationNew"
                ],  # new, etc...
                AccoladeStart=testaconfig["AccoladeStart"],  # {
                AccoladeEnd=testaconfig["AccoladeEnd"],  # }
                NoneNull=testaconfig["NoneNull"],  # null
                selfOrThis=testaconfig["selfOrThis"],  # this
                # if there is a need of self in the declaration of a function
                self_on_function_params=testaconfig["selfOnFunctionParams"],
                semicolon=testaconfig["semicolon"],
                scriptEnd=testaconfig["scriptEnd"],  # ;
            )

            # We Start the testa_test
            testa_test.start()

            # We can generate a Report of the test we are going to do:
            testa_test.setGenerateReport(True)

            for ppath in testaconfig["path"]:
                testa_test.Function(ppath, testaconfig["extensions"])

            # Most Important, ALWAYS We need to End the test.
            testa_test.end()
            # We Print the Report resume:
            print("[+] Reports saved in './" + testa_test.date_report + "'")
    except Exception:
        print("[+] Testa just Crashed, verify your JSON file !!!")
        get_trace()


if __name__ == "__main__":
    main()
