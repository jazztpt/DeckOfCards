Design decisions:

Because you suggested this be a framework, I included an __init__.py file so it can be imported as a module.

Given more time, I'd create a separate Card class, which would be more versatile in terms of adding functionality.  But I went with quick.  :)

I renamed the methods with python's underline syntax rather than capitalized camel-case (get_next_card instead of GetNextCard) because that is proper PEP-8.

I assume you don't care whether I take cards from the front or back of the deck.

For "how you would determine that your framework is working correctly for the deck of playing cards", see tests.py (stubbed out, I would use unittest).

Normally I would add all .pyc files to the .gitignore file, but you specifically mentioned compiled code files.  Probably not necessary for python, but I figured I'd refrain from specifically excluding it.