# Problems - Mastermind

Mastermind is a commandline game, where the user will guess the digits in a randomly generated code.

### Key features

* Generates a code of four digits, with numbers ranging from 1-8
* User has 12 chances to guess the 4 digits
* Calculate correctness of digits in guess.
* Output results.

### To Run

* `python3 mastermind.py`
* follow the input prompts to get the desired output

### To Test

* To run all the unittests: `python3 -m unittest tests/test_main.py`
* To run a specific step's unittest, e.g step *1*: `python3 -m unittest tests.test_main.MyTestCase.test_step1`
* _Note_: at the minimum, these (*unedited*) tests must succeed before you may submit the solution for review.
