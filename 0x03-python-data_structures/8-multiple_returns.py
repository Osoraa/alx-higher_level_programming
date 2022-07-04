#!/usr/bin/python3

def multiple_returns(sentence):
    return len(sentence), sentence[0] if sentence else None


if __name__ == "__main__":
    multiple_returns()
