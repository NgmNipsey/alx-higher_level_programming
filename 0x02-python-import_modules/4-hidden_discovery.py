#!/usr/bin/python3
"""Print all the names in hidden_4.pyc."""

if __name__ == "__main__":
    import hidden_4

    myNames = dir(hidden_4)
    for name in myNames:
        if name[:2] != "__":
            print(name)
