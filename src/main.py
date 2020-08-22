import argparse
import json
from src.testa import Testa
from src.utils import *
from src.modules import *

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
                    classInstantiationNew=testaconfig["classInstantiationNew"],  # new, etc...
                    AccoladeStart=testaconfig["AccoladeStart"],  # {
                    AccoladeEnd=testaconfig["AccoladeEnd"],  # }
                    NoneNull=testaconfig["NoneNull"],  # null
                    selfOrThis=testaconfig["selfOrThis"],  # this
                    # if there is a need of self in the declaration of a function
                    self_on_function_params=testaconfig["selfOnFunctionParams"],
                    semicolon=testaconfig["semicolon"],
                    scriptEnd=testaconfig["scriptEnd"]  # ;
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
        else:
            print("[+] Bad parameters input for the path and the config!")
    except Exception:
        print("[+] Testa just Crashed, verify your JSON file !!!")
        get_trace()
