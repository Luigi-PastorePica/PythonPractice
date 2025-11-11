"""
Let's refresh the match-case logic and throw in enumerators.
Using an Enumerator object provides two benefits:
- String changes are made in a single place, avoiding potential bugs due to misspelling and simplifying maintenance.
- Linters, like those in IDE's, catch misspellings of the Enum's attributes.
"""

from enum import Enum

class MenuOption(Enum):
    FRONT_DESK = "front desk"
    BILLING = "billing"
    TECH_SUPPORT = "tech support"
    OTHER = "other"

def redirect(option:str):
    match option:
        case MenuOption.FRONT_DESK.value:
            return MenuOption.FRONT_DESK.value
        case MenuOption.BILLING.value:
            return MenuOption.BILLING.value
        case MenuOption.TECH_SUPPORT.value:
            return MenuOption.TECH_SUPPORT.value
        case MenuOption.OTHER.value:
            return MenuOption.OTHER.value
        case _:
            raise ValueError("Invalid option")

def main():
    print(redirect("front desk"))
    print(redirect("billing"))
    print(redirect("tech support"))
    print(redirect("other"))
    try:
        print(redirect("otther"))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
