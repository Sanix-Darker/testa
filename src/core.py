import tesla as Tesla
import argparse
import json
########################################################################################
# THE MAIN WHERE WE WORK

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