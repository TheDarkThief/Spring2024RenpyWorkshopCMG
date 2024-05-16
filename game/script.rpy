# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color = "#be1de4")

define money = 100
# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    python:
        x=5
        if x < money:
            money = 5
    
    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    "Eilieen" "I am Elieen not a variable"

    e "I am Elieen except I am defined"
    $ money = money + 5
    "I am the narrator"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
