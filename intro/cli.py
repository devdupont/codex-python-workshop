"""
CLI demo with begins

Ex:
python cli.py -h
python cli.py Megan --times 5
"""

import begin


@begin.start
@begin.convert(times=int)
def main(name: "Your name", times: "The number of times to say hi" = 1):
    """
    Saying Hi 👋
    """
    # Alternatively, we can prompt the user for a name during run
    # name = input("What is your name:")
    print("Was given", name)
    print(f"Will print {times} times")
    # We use "_" to signify that we don't intend to use the variable
    for _ in range(times):
        print(f"Hello, {name}")
