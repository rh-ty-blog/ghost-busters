#!/bin/python

import os
import subprocess

PINKY = "Hi I'm Pinky"
INKY = "Hi I'm Inky"
BLINKY = "Hi I'm Blinky"
CLYDE = "What's up I'm Clyde"
GHOSTS = {"Pinky":PINKY,
          "Inky":INKY,
          "Blinky":BLINKY,
          "Clyde":CLYDE}

MENU_SCREEN = """
                                ┌───────────────────────────────────┐
                                │    0) :  exit                     │
                                │    1) :  check if you are done    │
                                │    2) :  restart                  │
                                └───────────────────────────────────┘
"""


GHOST_BUSTERS_ASKI_ART="""
 🭻🭻🭻🭻🭻🭻  🭻🭻  🭻🭻  🭻🭻🭻🭻🭻🭻  🭻🭻🭻🭻🭻🭻  🭻🭻🭻🭻🭻🭻     🭻🭻🭻🭻🭻🭻  🭻🭻  🭻🭻  🭻🭻🭻🭻🭻🭻  🭻🭻🭻🭻🭻🭻  🭻🭻🭻🭻🭻🭻  🭻🭻🭻🭻🭻🭻  🭻🭻🭻🭻🭻🭻    
╱╲  🭻🭻🭻╲╱╲ ╲🭻╲ ╲╱╲  🭻🭻 ╲╱╲  🭻🭻🭻╲╱╲🭻🭻  🭻╲   ╱╲  == ╲╱╲ ╲╱╲ ╲╱╲  🭻🭻🭻╲╱╲🭻🭻  🭻╲╱╲  🭻🭻🭻╲╱╲  == ╲╱╲  🭻🭻🭻╲   
╲ ╲ ╲🭻🭻 ╲ ╲  🭻🭻 ╲ ╲ ╲╱╲ ╲ ╲🭻🭻🭻  ╲╱🭻╱╲ ╲╱   ╲ ╲  🭻🭻<╲ ╲ ╲🭻╲ ╲ ╲🭻🭻🭻  ╲╱🭻╱╲ ╲╱╲ ╲  🭻🭻╲╲ ╲  🭻🭻<╲ ╲🭻🭻🭻  ╲  
 ╲ ╲🭻🭻🭻🭻🭻╲ ╲🭻╲ ╲🭻╲ ╲🭻🭻🭻🭻🭻╲╱╲🭻🭻🭻🭻🭻╲ ╲ ╲🭻╲    ╲ ╲🭻🭻🭻🭻🭻╲ ╲🭻🭻🭻🭻🭻╲╱╲🭻🭻🭻🭻🭻╲ ╲ ╲🭻╲ ╲ ╲🭻🭻🭻🭻🭻╲ ╲🭻╲ ╲🭻╲╱╲🭻🭻🭻🭻🭻╲ 
  ╲╱🭻🭻🭻🭻🭻╱╲╱🭻╱╲╱🭻╱╲╱🭻🭻🭻🭻🭻╱╲╱🭻🭻🭻🭻🭻╱  ╲╱🭻╱     ╲╱🭻🭻🭻🭻🭻╱╲╱🭻🭻🭻🭻🭻╱╲╱🭻🭻🭻🭻🭻╱  ╲╱🭻╱  ╲╱🭻🭻🭻🭻🭻╱╲╱🭻╱ ╱🭻╱╲╱🭻🭻🭻🭻🭻╱ 
"""


def is_directory_structure_ok()->tuple[str,bool]:
    directory = os.listdir()
    if "jail" not in directory:
        return "jail is missing", False
    if "kitchen" not in directory:
        return "kitchen is missing",False
    if "livingRoom" not in directory:
        return "livingRoom is missing",False
    if "corridor" not in directory:
        return "corridor is missing", False
    else:
        corridor_dir = os.listdir("./corridor")
        if "bedRoom" not in corridor_dir:
            return "bedRoom is missing", False
        if "toilet" not in corridor_dir:
            return "toilet is missing", False

    return "File structure is correct", True

def check_if_done():
    message, is_directory_ok = is_directory_structure_ok()
    

    #ask to restart if the directory sturcture is broken
    while not is_directory_ok:
        choice = input(f"oops, looks like {message}. Would you like to restart Yes/No: ")
        if choice[0].capitalize == "N":
            return
        elif choice[0].capitalize == "Y":
            restart()
            return
        else:
            print("Sorry that was not one of the options")

    #Check if all the ghosts are in jail
    jail = os.listdir("jail")
    missingFile = None
    for key in GHOSTS.keys():
        if key not in jail:
            missingFile = key
            print(f"{missingFile} is missing")

    if missingFile != None:
        return

    #verify if the contents of all the files is correct
    for i in jail:
        if i =="jail.txt": continue
        with open(f"jail/{i}", "r") as f:
            content = f.read()
            fake_ghost = None
            for ghost in GHOSTS.keys():
                if content[:-1] != GHOSTS[ghost]:
                    fake_ghost = i
                else:
                    fake_ghost = None
                    break


            if fake_ghost:
                print(f"{fake_ghost} is fake")                
                return
    print("Well done you did it!!!")



def restart():
    subprocess.call(["git", "stash", "--include-untracked"])
    subprocess.call(["git", "stash", "drop"])
    subprocess.call(["git", "restore", "."])
    subprocess.call(["git", "reset", "origin/main"])


choice = input(f"""{GHOST_BUSTERS_ASKI_ART}
               {MENU_SCREEN}""")
while True:
    if choice == "0":
        exit()
    if choice == "1":
        check_if_done()
        break
    if choice == "2":
        restart()
        break
    else:
        print("Sorry that was not one of the options")
        choice = input(MENU_SCREEN)
    

