# Tesla

Tesla is the best, simple and UnnitTest tool "CrossPlatform" and "CrossLanguages" develop by developpers for developpers based on comments in your code.
The power in this tool is that the grammar is the same for all your implementation languages.

## Features

- Tesla can do any Unittest you want from an assertion.
- Tesla Can Save Your Tests reports so that you can check it later in a persistent file.
- Tesla is light and simple.
- Tesla have a specific and very simple grammar for testing "all methods" presents in a file in one time and generate reports.
- Tesla is build from scratch so it doesn't have any dependency or any kind of troubleshooting with potentials externals libs.
- Tesla is build in 7 programming languages to cover all kind of application you are building in many way.

## All types of programming languages:

- Interpreted Programming Languages
- Functional Programming Languages
- Compiled Programming Languages
- Procedural Programming Languages
- Scripting Programming Languages
- Markup Programming Languages
- Logic-Based Programming Languages
- Concurrent Programming Languages
- Object-Oriented Programming Languages

## Tesla can test all theese programming languages

List of languages, where you can perform tesla test:

- Python
- Java
- Javascript
- TypeScript
- PHP
- Ruby
- GO
- Pascal
- Perl
- Erlang
- Haskell
- C
- C++
- Fortran
- Objective C
- MatLab
- Rust
- R
- Swift 

## How to use it

In your code, make sure to enclose the instructions you want to test with the tesla grammar, for example:
- In Python: 
```python

    # For a Simple assertion:

    # ::tesla_start::
    # ::case_start::
    # >> tesla.isEqual(2, 2)
    # << true
    # ::case_end::
    # ::tesla_end::


    # For more instructions:

    # ::tesla_start::
    # ::case_start::
    # >> addition(2, 2)
    # << 4
    # ::case_end::
    # ::code_start::
    # --- Your specific list of instruction / functions source code here!
    def addition(a, b):
        return a+b
    # ::code_end::
    # ::tesla_end::

```

- In Javascript: 
```javascript

    // For a Simple assertion:

    // ::tesla_start::
    // ::case_start::
    // >> tesla.isEqual(2, 2)
    // << true
    // ::case_end::
    // ::tesla_end::


    // For more instructions:

    // ::tesla_start::
    // ::case_start::
    // >> addition(2, 2)
    // << 4
    // ::case_end::
    // ::code_start::
    // --- Your specific list of instruction / functions source code here!
    def addition(a, b):
        return a+b
    // ::code_end::
    // ::tesla_end::
```
## Interesting ressources:

- [Types of testing](https://www.softwaretestinghelp.com/types-of-software-testing/)
- [Group of tests](https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing)

## Author

- Sanix darker (Ange SAADJIO).