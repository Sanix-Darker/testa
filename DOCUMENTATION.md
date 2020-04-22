# TEST-A DOCUMENTATION

Some few things to know before using testa.

## How to config it

- First : In your code, make sure to enclose the instructions you want to test with the testa grammar, for example:
    - In Python:
    ```python

        # For a Simple assertion:

        # ::import_start::
        # --- Your imports here, if your methods need them ---
        # ::import_end::

        # ::testa_start::
        # ::case_start::
        # >> testa.isEqual(2, 2)
        # << true
        # ::case_end::
        # ::testa_end::

        #
        # ::doc_start::
        #  .
        #  Here a small description of the function  that will be generate on the documentation
        #  .
        # ::doc_end::
        #

        # With methods :

        # ::testa_start::
        # ::case_start::
        # >> addition(2, 2)
        # << 4
        # ::case_end::
        # ::code_start::
        def addition(a, b):
            return a+b
        # ::code_end::
        # ::testa_end::

    ```

    - In Javascript: 
    ```javascript

        // ::import_start::
        // --- Your imports here ---
        // ::import_end::

        // For a Simple assertion:

        // ::testa_start::
        // ::case_start::
        // >> testa.isEqual(2, 2)
        // << true
        // ::case_end::
        // ::testa_end::


        // For more instructions:

        // ::testa_start::
        // ::case_start::
        // >> addition(2, 2)
        // << 4
        // ::case_end::

        //
        // ::doc_start::
        //  .
        //  Here a small description of the function  that will be generate on the documentation
        //  .
        // ::doc_end::
        //

        // ::code_start::
        // --- Your specific list of instruction / functions source code here!
        function addition(a, b){
            return a+b
        }
        // ::code_end::
        // ::testa_end::
    ```

    - In php :
    ```php
        <?php
            // ::testa_start::
            // ::case_start::
            // >> square(9)
            // << 3.0
            // ::case_end::
            // ::code_start::
            function square($a){
                return sqrt($a);
            }
            // ::code_end::
            // ::testa_end::
    ```

    - In Ruby :
    ```ruby
        # ::testa_start::
        # ::case_start::
        # >> square(9)
        # << 3.0
        # ::case_end::
        # ::code_start::
        def square(a)
            return a/2
        # ::code_end::
        # ::testa_end::
    ```
- Second : You need to config a `testa_json_file` or just to use what is allready config for each anguage as default.
    - An example of testa config file for `Javascript`:
    ```json
    {
        "path": ["./javascript/square.js", "./javascript/my_javascript_app/"],
        "extensions": [".js"],
        "launcher": "node",
        "outputMethod": "console.log",
        "commentStartBy": "//",
        "tryCatch": "try{ \n\t **** \n}catch(err){ \n\t console.log(es);}",
        "function": " ",
        "varDeclaration": "var ",
        "classInstantiationNew": "new ",
        "AccoladStart": "{",
        "AccoladEnd": "}",
        "NoneNull": "null",
        "selfOrThis": "this",
        "selfOnFunctionParams": false,
        "semicolomn": ";"
    }
    ```
    - An example of testa config file for `PHP`:
    ```json
    {
        "path": ["./php/square.php"],
        "extensions": [".php"],
        "launcher": "php",
        "outputMethod": "print",
        "commentStartBy": "//",
        "tryCatch": "try{ \n\t **** \n}catch(Exception $e){ \n\t print($e);}",
        "function": "function ",
        "varDeclaration": "$",
        "classInstantiationNew": "new ",
        "AccoladStart": "{",
        "AccoladEnd": "}",
        "NoneNull": "null",
        "selfOrThis": "$this",
        "selfOnFunctionParams": false,
        "semicolomn": ";",
        "scriptStarter": "<?php \n",
        "scriptEnder": "\n ?>",
        "prefixVariable": "$"
    }
    ```
    - An example of testa config file for `python`:
    ```json
    {
        "path": ["./python/sha256.py"],
        "extensions": [".py"],
        "launcher": "python",
        "outputMethod": "print",
        "commentStartBy": "#",
        "tryCatch": "try: \n\t **** \nexcept Exception as es: \n\t print(str(es))\n",
        "function": "def ",
        "varDeclaration": "",
        "classInstantiationNew": "",
        "AccoladStart": ":",
        "AccoladEnd": "",
        "NoneNull": "None",
        "selfOrThis": "self",
        "selfOnFunctionParams": true,
        "semicolomn": "",
        "scriptStarter": "",
        "scriptEnder": "",
        "prefixVariable": ""
    }
    ```
    - An example of testa config file for `Ruby`:
    ```json
    {
        "path": ["./ruby/my_ruby_app/", "./ruby/square.rb"],
        "extensions": [".rb"],
        "launcher": "ruby",
        "outputMethod": "puts",
        "commentStartBy": "#",
        "tryCatch": "try: \n\t **** \nexcept Exception as es \n\t puts(es)",
        "function": "def ",
        "varDeclaration": "",
        "classInstantiationNew": "",
        "AccoladStart": "",
        "AccoladEnd": "\n end",
        "NoneNull": "None",
        "selfOrThis": "self",
        "selfOnFunctionParams": true,
        "semicolomn": "",
        "scriptStarter": "",
        "scriptEnder": "",
        "prefixVariable": ""
    }
    ```

    - Meanings :
    
<table>
        <tr>
            <td>Parameter</td>
            <td>Type</td>
            <td>Example</td>
            <td>Meaning</td>
        </tr>
        <tr>
            <td><b>path</b></td>
            <td><i>array</i></td>
            <td><b><i>["./javascript/square.js", "./javascript/my_javascript_app/"]</i></b></td>
            <td>All path where testa will perform tests.</td>
        </tr>
        <tr>
            <td> <b>extensions</b> </td>
            <td> <i>array</i> </td>
            <td> <b><i>[".js"]</i></b> </td>
            <td> All file extensions to be tests. </td>
        </tr>
        <tr>
            <td> <b>launcher</b> </td>
            <td> <i>string</i> </td>
            <td> <b><i>"node"</i></b> </td>
            <td> The program responsible fo launching the script in command line. </td>
        </tr>
        <tr>
            <td> <b>outputMethod</b> </td>
            <td> <i>string</i> </td>
            <td> <b><i>"console.log"</i></b> </td>
            <td> The default print/log for the appropriate language. </td>
        </tr>
        <tr>
            <td> <b>commentStartBy</b> </td>
            <td> <i>string</i> </td>
            <td> <b><i>"//"</i></b> </td>
            <td> The default started comment character. </td>
        </tr>
        <tr>
            <td> <b>tryCatch</b> </td>
            <td> <i>string</i> </td>
            <td> <b><i>"try{ \n\t **** \n}catch(err){ \n\t console.log(es);}"</i></b> </td>
            <td> A oneline try catch to get errors when the code crash, the **** will be were the code will be place. </td>
        </tr>
        <tr>
            <td> <b>function</b> </td>
            <td> <i>string</i> </td>
            <td> <b><i>""</i></b> </td>
            <td> The function name synthax like function or def. </td>
        </tr>
        <tr>
            <td> <b>varDeclaration</b> </td>
            <td> <i>array</i> </td>
            <td> <b><i>["var", "let", "const"]</i></b> </td>
            <td> The prefix on instantiation of a variable. </td>
        </tr>
        <tr>
            <td> <b>classInstantiationNew</b> </td>
            <td> <i>string</i> </td>
            <td> <b><i>"new"</i></b> </td>
            <td> The keyword synthax instantiation. </td>
        </tr>
        <tr>
            <td> <b>AccoladStart</b> </td>
            <td> <i>string</i> </td>
            <td> <b><i>"{"</i></b> </td>
            <td> This define the start of a function or a class. </td>
        </tr>
        <tr>
            <td> <b>AccoladEnd</b> </td>
            <td> <i>string</i> </td>
            <td> <b><i>"}"</i></b> </td>
            <td> This define the end of a method or a class. </td>
        </tr>
        <tr>
            <td> <b>NoneNull</b> </td>
            <td> <i>string</i> </td>
            <td> <b><i>"none"</i></b> </td>
            <td> None for python and null for javascript. </td>
        </tr>
        <tr>
            <td> <b>selfOrThis</b> </td>
            <td> <i>string</i> </td>
            <td> <b><i>"this"</i></b> </td>
            <td> self for python and this for javascript for example. </td>
        </tr>
        <tr>
            <td> <b>selfOnFunctionParams</b> </td>
            <td> <i>boolean</i> </td>
            <td> <b><i>false</i></b> </td>
            <td> The 'self' or 'this' parameter present on method. </td>
        </tr>
        <tr>
            <td> <b>semicolomn</b> </td>
            <td> <i>string</i> </td>
            <td> <b><i>";"</i></b> </td>
            <td>  For thoose langage that supporting instructions only with a ";" (semicolomn). </td>
        </tr>
</table>

## TEEEESSSSTTS :-)

That can look really complicated to config but in fact it's really simple and all available tsla Json file have been allready configured for you:

To test it, after cloning this repository, hit:
```shell

# First you need to cd where the json file is:
cd ./examples

# Testa will perform tests following what it is on tjs.json
python testa.py -c ./javascript/testa.json

# Or for PYTHON
python testa.py -c ./python/testa.json

# Or for PHP
python testa.py -c ./python/testa.json

# Or for Ruby
python testa.py -c ./ruby/testa.json
```
And that's where the magic of Testa is, for any language, you have only to write a simple JSON file and specify paths where you will do tests.


## DEMO

<img src="./demo.gif">


Records of the test will be saved in a .txt file with this format for example:
```php

##################################################################
#         |_   _| | ____| / ___|  | |        / \                 #
#           | |   |  _|   \___ \  | |       / _ \                #
#           | |   | |___   ___) | | |___   / ___ \               #
#           |_|   |_____| |____/  |_____| /_/   \_\ v0.1         #
#----------------------------------------------------------------#
#-------------------------------------------- By S@n1x d4rk3r ---#
##################################################################


| **********************************************************************************************************************************
| ---------------------------------------------------------------
|  Testa-Test on :./javascript/square.js
| ---------------------------------------------------------------
-Test 1----------------------------------------------------------
|
| >> output == wanted
| << False
| 
| On: square
| Statement: square(9)
| output: 44
| Wanted : 3.0
| _______________________________________________________________
| 
| Status: ✗ Failed!
| End on: 0.07390022277832031 s.
| _______________________________________________________________

| **********************************************************************************************************************************
| ---------------------------------------------------------------
|  Testa-Test on :javascript/my_javascript_app/divisionby2.js
| ---------------------------------------------------------------
-Test 2----------------------------------------------------------
|
| >> output == wanted
| << False
| 
| On: divisionby2
| Statement: divisionby2(14)
| output: 8
| Wanted : 7.0
| _______________________________________________________________
| 
| Status: ✗ Failed!
| End on: 0.07592105865478516 s.
| _______________________________________________________________

| **********************************************************************************************************************************
| ---------------------------------------------------------------
|  Testa-Test on :javascript/my_javascript_app/multiplicationby3.js
| ---------------------------------------------------------------
-Test 3----------------------------------------------------------
|
| >> output == wanted
| << True
| 
| On: multiplicationby3
| Statement: multiplicationby3(2)
| output: 6
| Wanted : 6
| _______________________________________________________________
| 
| Status: ✓ Success!
| End on: 0.08027839660644531 s.
| _______________________________________________________________

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Testa reports:
%%
%% 3 tests done! 
%%
%% 1 succeed and 2 failed!
%% 
%% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
%% Tests failing:
%%    -'square' in ./javascript/square.js
%% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
%% Tests failing:
%%    -'divisionby2' in javascript/my_javascript_app/divisionby2.js
%% ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
%% Running time: 0.23009967803955078 s
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```