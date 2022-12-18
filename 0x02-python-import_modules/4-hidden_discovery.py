#!/usr/bin/python3
# 4-hidden_discovery.py

if __name__ == "__main__":
    """Print all names defined bu hidden_4 module."""
    import hidden_4

    for item in dir(hidden_4):
        if item.startswith('_'):
            continue
        print(item)
