from itertools import permutations as combos
from os import system as sys; sys('clear')
from items import items
from os import environ

if environ["REPL_OWNER"] not in ["HyperHacker"]:
    print(f"Welcome, {environ['REPL_OWNER']}\n")
    print("The Materials Can Be Made With Both 2 Or 3 Items!\n")
    input("ENTER To Continue: ")

got = ["fire", "water", "dirt", "air"]

while True:

    sys('clear')

    print("Items That You Know Of:\n")

    printednum = 0
    for i, v in enumerate(items):
        if printednum <= 5:
            if any(j in got for j in items[v]) and v not in got and v != "hyperhacker":
                print(v.title())
                printednum += 1
        else: break
    
    print("\nYour Items:\n")
    
    for i, v in enumerate(got): print(str(i + 1) + ": " + v.title())

    try: q = [got[int(i.strip()) - 1] for i in input("\n(Numbers Seperated By Commas) Materials: ").split(",")]
    except: pass

    for i in items:
        try:
            if q in [list(j) for j in combos(items[i])]:
                if i not in got:
                    got.append(i)
                    input(f"\nYou Made {i.title()}!\n\n[ENTER] ")
        except: pass

else: print("How Does This Happen")