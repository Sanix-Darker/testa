# Testa

Testa is the best, simple and Test tool "CrossPlatform" and "CrossLanguages" (Only Script language for now) develop by developpers for developpers based on comments in your code.
The power in this tool is that the grammar is the same for all your implementation languages.

**Note:** This project is completly experimental, am still working on it, not sure where am going with it lol.

## Features

- Testa can do any Unittest you want from an assertion.
- Testa Can Save Your Tests reports so that you can check it later in a persistant file.
- Testa is light and simple because it is based on comments in your code.
- Testa have a specific and very simple grammar for testing "all methods" presents in a file in one time and generate reports.
- Testa is build from scratch so it doesn't have any dependency or any kind of troubleshooting with potentials externals libs.
- Testa can generate for you a small and readable documentation whatever the language you're using

## Testa can test all theese programming languages

List of languages, where you can perform testa test:

- [Done] Python
- [Done] Javascript
- [Done] PHP
- [Done] Ruby

## Documentation

Some few things to know before using testa.

## How to config it

### Config files

You need to config a `testa json file` or just use default one for the appropriate language.
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
    "AccoladeStart": "{",
    "AccoladeEnd": "}",
    "NoneNull": "null",
    "selfOrThis": "this",
    "selfOnFunctionParams": false,
    "semicolon": ";"
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
    "AccoladeStart": "{",
    "AccoladeEnd": "}",
    "NoneNull": "null",
    "selfOrThis": "$this",
    "selfOnFunctionParams": false,
    "semicolon": ";",
    "scriptStarter": "<?php \n",
    "scriptEnd": "\n ?>",
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
    "AccoladeStart": ":",
    "AccoladeEnd": "",
    "NoneNull": "None",
    "selfOrThis": "self",
    "selfOnFunctionParams": true,
    "semicolon": "",
    "scriptStarter": "",
    "scriptEnd": "",
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
    "AccoladeStart": "",
    "AccoladeEnd": "\n end",
    "NoneNull": "None",
    "selfOrThis": "self",
    "selfOnFunctionParams": true,
    "semicolon": "",
    "scriptStarter": "",
    "scriptEnd": "",
    "prefixVariable": ""
}
```

### Legend
    
<table>
    <tr>
        <th>Parameter</th>
        <th>Example</th>
        <th>Meaning</th>
    </tr>
    <tr>
        <td><b>path</b></td>
        <td><b><i>["./javascript/square.js", "./javascript/my_javascript_app/"]</i></b></td>
        <td>All path where testa will perform tests.</td>
    </tr>
    <tr>
        <td> <b>extensions</b> </td>
        <td> <b><i>[".js"]</i></b> </td>
        <td> All file extensions to be tests. </td>
    </tr>
    <tr>
        <td> <b>launcher</b> </td>
        <td> <b><i>"node"</i></b> </td>
        <td> The program responsible fo launching the script in command line. </td>
    </tr>
    <tr>
        <td> <b>outputMethod</b> </td>
        <td> <b><i>"console.log"</i></b> </td>
        <td> The default print/log for the appropriate language. </td>
    </tr>
    <tr>
        <td> <b>commentStartBy</b> </td>
        <td> <b><i>"//"</i></b> </td>
        <td> The default started comment character. </td>
    </tr>
    <tr>
        <td> <b>tryCatch</b> </td>
        <td> <b><i>"try{ \n\t **** \n}catch(err){ \n\t console.log(es);}"</i></b> </td>
        <td> A oneline try catch to get errors when the code crash, the **** will be were the code will be place. </td>
    </tr>
    <tr>
        <td> <b>function</b> </td>
        <td> <b><i>""</i></b> </td>
        <td> The function name synthax like function or def. </td>
    </tr>
    <tr>
        <td> <b>varDeclaration</b> </td>
        <td> <b><i>["var", "let", "const"]</i></b> </td>
        <td> The prefix on instantiation of a variable. </td>
    </tr>
    <tr>
        <td> <b>classInstantiationNew</b> </td>
        <td> <b><i>"new"</i></b> </td>
        <td> The keyword synthax instantiation. </td>
    </tr>
    <tr>
        <td> <b>AccoladeStart</b> </td>
        <td> <b><i>"{"</i></b> </td>
        <td> This define the start of a function or a class. </td>
    </tr>
    <tr>
        <td> <b>AccoladeEnd</b> </td>
        <td> <b><i>"}"</i></b> </td>
        <td> This define the end of a method or a class. </td>
    </tr>
    <tr>
        <td> <b>NoneNull</b> </td>
        <td> <b><i>"none"</i></b> </td>
        <td> None for python and null for javascript. </td>
    </tr>
    <tr>
        <td> <b>selfOrThis</b> </td>
        <td> <b><i>"this"</i></b> </td>
        <td> self for python and this for javascript for example. </td>
    </tr>
    <tr>
        <td> <b>selfOnFunctionParams</b> </td>
        <td> <b><i>false</i></b> </td>
        <td> The 'self' or 'this' parameter present on method. </td>
    </tr>
    <tr>
        <td> <b>semicolon</b> </td>
        <td> <b><i>";"</i></b> </td>
        <td>  For thoose langage that supporting instructions only with a ";" (semicolon). </td>
    </tr>
</table>


## How to use it

In your code, make sure to enclose the instructions you want to test with the testa grammar, for example:
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
// ::testa_start::
// ::case_start::
// >> square(9)
// << 3
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

## How to test it

This can look really complicated to config but in fact it's really simple and all available testa Json files have been 
allready configured for you:

To test it, after cloning this repository, hit:

```shell
# First clone the repo
git clone https://github.com/sanix-darker/testa

# now, you need to cd where the json file is:
cd ./path/to/testa/examples

# Testa will perform tests following what it is on tjs.json
python testacli.py -c ./javascript/tjs.json

# Or for PYTHON
python testacli.py -c ./python/tpy.json

# Or for PHP
python testacli.py -c ./php/tphp.json

# Or for Ruby
python testacli.py -c ./ruby/trb.json
```
And that's where the magic of Testa is, for any language, you have only to write a simple JSON file and specify paths where you will do tests.

## Author

- Sanix darker
