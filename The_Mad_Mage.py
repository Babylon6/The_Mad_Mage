import tkinter as tk
from tkinter import messagebox
import random

# Check if Pillow is installed
try:
    from PIL import Image, ImageTk
except ImportError:
    # If Pillow is not installed, show a message box with instructions
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showerror("Pillow Not Installed", "The Pillow library is not installed. Please install it by running:\n\npip install pillow")
    root.quit()  # Exit the program

# Function to handle character selection
def select_character(character):
    messagebox.showinfo("Character Selected", f"Great choice! You have chosen {character}.")
    display_intro()

# Function to display the game title
def display_game_title():
    for widget in root.winfo_children():
        widget.destroy()
    title_label = tk.Label(root, text="THE MAD MAGE", font=("Arial", 28, "bold"), fg="red")
    title_label.pack(pady=20)
    root.after(2000, choose_character)  # Wait for 2 seconds, then show character selection

# Function to choose character
def choose_character():
    for widget in root.winfo_children():
        widget.destroy()

    choose_label = tk.Label(root, text="Choose Your Character", font=("Arial", 18, "bold"), fg="blue")
    choose_label.pack(pady=10)

    characters = {
        "Warrior": r"https://github.com/Babylon6/The_Mad_Mage/blob/main/Warrior.jpg",
        "Mage": r"https://github.com/Babylon6/The_Mad_Mage/blob/main/Mage.jpg",
        "Ranger": r"https://github.com/Babylon6/The_Mad_Mage/blob/main/Ranger.jpg"
    }

    character_frame = tk.Frame(root)
    character_frame.pack(padx=10, pady=10)

    for character, image_path in characters.items():
        try:
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Resize the image to 200x200 pixels
            photo = ImageTk.PhotoImage(image)
            button = tk.Button(character_frame, text=character, image=photo, compound=tk.TOP, 
                               command=lambda c=character: select_character(c),
                               font=("Arial", 14, "bold"), fg="red")
            button.photo = photo  # Keep a reference to the image to prevent garbage collection
            button.pack(side=tk.LEFT, padx=10, pady=10)
        except PermissionError:
            messagebox.showerror("Error", f"Permission denied for accessing {image_path}")

    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)

# Function to display intro text
def display_intro():
    for widget in root.winfo_children():
        widget.destroy()

    intro_text = """
    Welcome, brave hero, to the Mad Mage's Fortress—a place shrouded in darkness and mystery.
    The land of Eldoria lies in torment, its people enslaved by the Mad Mage's wicked spell.
    Only a few heroes remain resilient, and you are among them. Your quest is to navigate this treacherous dungeon,
    solving puzzles and vanquishing foes, until you confront the Mad Mage themself and free Eldoria from their tyranny.
    Adventure awaits—may your courage and wit guide you!
    """
    label = tk.Label(root, text=intro_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add image beneath the intro text
    image_path = r"https://github.com/Babylon6/The_Mad_Mage/blob/main/fortress.jpg"  # Replace with the actual path to your image
    image = Image.open(image_path)
    image = image.resize((400, 200), Image.Resampling.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack(pady=10)

    # Add ready button
    ready_button = tk.Button(root, text="Are you ready?", command=prompt_ready, font=("Arial", 14))
    ready_button.pack(pady=10)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

    # Allow window to resize automatically
    root.resizable(True, True)

# Function to prompt readiness
def prompt_ready():
    response = messagebox.askyesno("Ready?", "Are you ready to begin?")
    if response:
        adventure_begins()
    else:
        messagebox.showinfo("Goodbye", "I see the quest is too much for you. Maybe another day you'll be ready.")
        root.quit()  # Close the window

# Function to start adventure
def adventure_begins():
    for widget in root.winfo_children():
        widget.destroy()

    adventure_text = """
    You find yourself in a dimly lit, ancient stone dungeon, the walls just visible through the ghostly sunbeams that somehow find their way down from the distant sky.
    Strange, echoing noises from the dark corridor ahead make your senses tingle with unease.
    Before you stands a mangled metal door, beyond which burns a single flame, hinting at the mysteries that lie beyond.
    As you approach, the metal moves apart to let you through, as if it had been expecting your arrival.
    """
    label = tk.Label(root, text=adventure_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add image beneath the adventure text
    image_path = r"https://github.com/Babylon6/The_Mad_Mage/blob/main/dungeon_image.jpg"  # Replace with the actual path to your image
    image = Image.open(image_path)
    image = image.resize((400, 200), Image.Resampling.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack(pady=10)

    # Add options to go through the door or run away
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    sword_button = tk.Button(button_frame, text="Go through the door", command=go_through_door, font=("Arial", 14))
    sword_button.pack(side=tk.LEFT, padx=5)

    mace_button = tk.Button(button_frame, text="Run away", command=run_away, font=("Arial", 14))
    mace_button.pack(side=tk.LEFT, padx=5)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)

# Function for going through the door
def go_through_door():
    display_first_puzzle_scene()

# Function for running away
def run_away():
    messagebox.showinfo("Coward!", "You run away from the adventure. Maybe another time you'll be brave enough.")
    root.quit()  # Close the window
# Function to display the first puzzle scene
def display_first_puzzle_scene():
    for widget in root.winfo_children():
        widget.destroy()

    puzzle_text = """
    You enter a dark room with a single torch lighting the way. The walls are covered in ancient runes, and a voice whispers in your ear:

    "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
    """
    label = tk.Label(root, text=puzzle_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Image for the puzzle scene
    image_path = r"https://github.com/Babylon6/The_Mad_Mage/blob/main/torch.jpg"  # Replace with actual path to your image
    image = Image.open(image_path)
    image = image.resize((400, 400), Image.Resampling.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack(pady=10)

    # Options for the riddle
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    option1_button = tk.Button(button_frame, text="Echo", command=solve_first_riddle_correct, font=("Arial", 14))
    option1_button.pack(side=tk.LEFT, padx=5)

    option2_button = tk.Button(button_frame, text="Wind", command=solve_first_riddle_incorrect, font=("Arial", 14))
    option2_button.pack(side=tk.LEFT, padx=5)

    option3_button = tk.Button(button_frame, text="Shadow", command=solve_first_riddle_incorrect, font=("Arial", 14))
    option3_button.pack(side=tk.LEFT, padx=5)

    option4_button = tk.Button(button_frame, text="Fire", command=solve_first_riddle_incorrect, font=("Arial", 14))
    option4_button.pack(side=tk.LEFT, padx=5)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)
# Function for correct riddle answer
def solve_first_riddle_correct():
    messagebox.showinfo("Correct!", """
    You speak aloud the word “Echo” and the walls vibrate with the sound of your voice, revealing a hidden door that slowly creaks open.
    """)
    display_fight_scene()  # Call the function to display the Stone Guardian fight scene

# Function for incorrect riddle answer
def solve_first_riddle_incorrect():
    messagebox.showerror("Incorrect", """
    Failing to utter the correct answer to the riddle, the walls start to close in on you. You try to escape, but the door slams shut, trapping you inside.

    Better luck next time.
    """)
    root.quit()  # End the game
# Initialize variables to track hits for the Stone Guardian fight
player_hits_guardian = 0
guardian_hits = 0

# Function to display the Stone Guardian fight scene
def display_fight_scene():
    global player_hits_guardian, guardian_hits
    player_hits_guardian = 0
    guardian_hits = 0

    for widget in root.winfo_children():
        widget.destroy()

    fight_text = """
    As you step into the chamber, a Stone Guardian materializes before your eyes, held together by tendrils of raw arcane energy. The massive creature raises its axe, ready to strike. Prepare for battle!
    """
    label = tk.Label(root, text=fight_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add image of the Stone Guardian
    image_path = r"https://github.com/Babylon6/The_Mad_Mage/blob/main/stone_guardian.jpg"  # Replace with the actual path to your image
    image = Image.open(image_path)
    image = image.resize((400, 400), Image.Resampling.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack(pady=10)

    # Add options to sword or mace
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    sword_button = tk.Button(button_frame, text="Sword", command=sword_guardian, font=("Arial", 14))
    sword_button.pack(side=tk.LEFT, padx=5)

    mace_button = tk.Button(button_frame, text="Mace", command=mace_guardian, font=("Arial", 14))
    mace_button.pack(side=tk.LEFT, padx=5)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)
# Function to handle sword action against the Stone Guardian
def sword_guardian():
    global player_hits_guardian, guardian_hits

    outcome = random.choices(["hit", "miss"], weights=[70, 30], k=1)[0]
    if outcome == "hit":
        player_hits_guardian += 1
        messagebox.showinfo("Sword", f"Great hit! The Stone Guardian staggers back. ({player_hits_guardian}/3)")
    else:
        guardian_hits += 1
        messagebox.showinfo("Sword", f"Your blow misses. The Stone Guardian strikes you! ({guardian_hits}/3)")

    check_guardian_fight_outcome()

# Function to handle mace action against the Stone Guardian
def mace_guardian():
    global player_hits_guardian, guardian_hits

    outcome = random.choices(["hit", "miss"], weights=[70, 30], k=1)[0]
    if outcome == "hit":
        player_hits_guardian += 1
        messagebox.showinfo("Mace", f"Great hit! The Stone Guardian staggers back. ({player_hits_guardian}/3)")
    else:
        guardian_hits += 1
        messagebox.showinfo("Mace", f"Your blow misses. The Stone Guardian strikes you! ({guardian_hits}/3)")

    check_guardian_fight_outcome()

# Function to check fight outcome for the Stone Guardian fight
def check_guardian_fight_outcome():
    global player_hits_guardian, guardian_hits

    if player_hits_guardian >= 3:
        display_guardian_win()
    elif guardian_hits >= 3:
        display_guardian_fail()

# Function to display win outcome for the Stone Guardian fight
def display_guardian_win():
    global player_hits_guardian, guardian_hits
    player_hits_guardian = 0
    guardian_hits = 0

    for widget in root.winfo_children():
        widget.destroy()
    
    win_text = """
    The Stone Guardian crumbles to the ground, defeated. You have won the battle!
    """
    label = tk.Label(root, text=win_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add button to proceed to the next scene
    continue_button = tk.Button(root, text="Continue", command=display_library_scene, font=("Arial", 14))
    continue_button.pack(pady=10)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)

# Function to display fail outcome for the Stone Guardian fight
def display_guardian_fail():
    global player_hits_guardian, guardian_hits
    player_hits_guardian = 0
    guardian_hits = 0

    for widget in root.winfo_children():
        widget.destroy()

    fail_text = """
    The Stone Guardian's axe strikes you down. You have been defeated.
    """
    label = tk.Label(root, text=fail_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add options to retry or quit
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    retry_button = tk.Button(button_frame, text="Retry", command=adventure_begins, font=("Arial", 14))
    retry_button.pack(side=tk.LEFT, padx=5)

    quit_button = tk.Button(button_frame, text="Quit", command=quit_game, font=("Arial", 14))
    quit_button.pack(side=tk.LEFT, padx=5)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)
# Function to display the library puzzle scene
def display_library_scene():
    for widget in root.winfo_children():
        widget.destroy()

    library_text = """
    After defeating the Stone Guardian, you enter a grand library filled with ancient books and scrolls. As you explore, you notice a glowing inscription on the wall:

    "I have keys but open no locks. I have space but no room. You can enter, but you can't go outside. What am I?"
    """
    label = tk.Label(root, text=library_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Image for the library puzzle scene
    image_path = r"https://github.com/Babylon6/The_Mad_Mage/blob/main/library.jpg"  # Replace with actual path to your image
    image = Image.open(image_path)
    image = image.resize((400, 400), Image.Resampling.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack(pady=10)

    # Options for the riddle
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    option1_button = tk.Button(button_frame, text="A Map", command=solve_library_riddle_incorrect, font=("Arial", 14))
    option1_button.pack(side=tk.LEFT, padx=5)

    option2_button = tk.Button(button_frame, text="A Code", command=solve_library_riddle_incorrect, font=("Arial", 14))
    option2_button.pack(side=tk.LEFT, padx=5)

    option3_button = tk.Button(button_frame, text="A Keyboard", command=solve_library_riddle_correct, font=("Arial", 14))
    option3_button.pack(side=tk.LEFT, padx=5)

    option4_button = tk.Button(button_frame, text="A Book", command=solve_library_riddle_incorrect, font=("Arial", 14))
    option4_button.pack(side=tk.LEFT, padx=5)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)
# Function for correct riddle answer in the library
def solve_library_riddle_correct():
    messagebox.showinfo("Correct!", """
    You speak aloud the word “Keyboard” and the inscription fades, revealing a hidden passage that opens up. You brace yourself for the next challenge.
    """)
    display_horned_fight_scene()  # Proceed to the Horned Enemy fight

# Function for incorrect riddle answer in the library
def solve_library_riddle_incorrect():
    messagebox.showerror("Incorrect", """
    The inscription glows brighter, and the room begins to shake. You try to find an escape, but the room collapses around you.

    Better luck next time.
    """)
    root.quit()  # End the game
# Initialize variables to track hits for the Horned Enemy fight
player_hits_horned = 0
horned_hits = 0

# Function to display the Horned Enemy fight scene
def display_horned_fight_scene():
    global player_hits_horned, horned_hits
    player_hits_horned = 0
    horned_hits = 0

    for widget in root.winfo_children():
        widget.destroy()

    fight_text = """
    You step into the chamber, and a horned enemy emerges from the shadows, pulsating with dark energy. The creature snarls, baring its fangs, and prepares to attack. Get ready for battle!
    """
    label = tk.Label(root, text=fight_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add image of the Horned Enemy
    image_path = r"https://github.com/Babylon6/The_Mad_Mage/blob/main/enemy.jpg"  # Replace with the actual path to your image
    image = Image.open(image_path)
    image = image.resize((300, 400), Image.Resampling.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack(pady=10)

    # Add options to sword or mace
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    sword_button = tk.Button(button_frame, text="Sword", command=sword_horned_enemy, font=("Arial", 14))
    sword_button.pack(side=tk.LEFT, padx=5)

    mace_button = tk.Button(button_frame, text="Mace", command=mace_horned_enemy, font=("Arial", 14))
    mace_button.pack(side=tk.LEFT, padx=5)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)
# Function to handle sword action against the Horned Enemy
def sword_horned_enemy():
    global player_hits_horned, horned_hits

    outcome = random.choices(["hit", "miss"], weights=[70, 30], k=1)[0]
    if outcome == "hit":
        player_hits_horned += 1
        messagebox.showinfo("Sword", f"Great hit! The Horned Enemy staggers back. ({player_hits_horned}/3)")
    else:
        horned_hits += 1
        messagebox.showinfo("Sword", f"Your blow misses. The Horned Enemy strikes you! ({horned_hits}/3)")

    check_horned_fight_outcome()

# Function to handle mace action against the Horned Enemy
def mace_horned_enemy():
    global player_hits_horned, horned_hits

    outcome = random.choices(["hit", "miss"], weights=[70, 30], k=1)[0]
    if outcome == "hit":
        player_hits_horned += 1
        messagebox.showinfo("Mace", f"Great hit! The Horned Enemy staggers back. ({player_hits_horned}/3)")
    else:
        horned_hits += 1
        messagebox.showinfo("Mace", f"Your blow misses. The Horned Enemy strikes you! ({horned_hits}/3)")

    check_horned_fight_outcome()

# Function to check fight outcome for the Horned Enemy fight
def check_horned_fight_outcome():
    global player_hits_horned, horned_hits

    if player_hits_horned >= 3:
        display_horned_win()
    elif horned_hits >= 3:
        display_horned_fail()

# Function to display win outcome for the Horned Enemy fight
def display_horned_win():
    global player_hits_horned, horned_hits
    player_hits_horned = 0
    horned_hits = 0

    for widget in root.winfo_children():
        widget.destroy()
    
    win_text = """
    The Horned Enemy collapses, defeated. You have won the battle!
    """
    label = tk.Label(root, text=win_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add button to proceed to the new puzzle scene
    continue_button = tk.Button(root, text="Continue", command=display_new_puzzle_scene, font=("Arial", 14))
    continue_button.pack(pady=10)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)

# Function to display fail outcome for the Horned Enemy fight
def display_horned_fail():
    global player_hits_horned, horned_hits
    player_hits_horned = 0
    horned_hits = 0

    for widget in root.winfo_children():
        widget.destroy()

    fail_text = """
    The Horned Enemy's attack overpowers you. You have been defeated.
    """
    label = tk.Label(root, text=fail_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add options to retry or quit
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    retry_button = tk.Button(button_frame, text="Retry", command=adventure_begins, font=("Arial", 14))
    retry_button.pack(side=tk.LEFT, padx=5)

    quit_button = tk.Button(button_frame, text="Quit", command=quit_game, font=("Arial", 14))
    quit_button.pack(side=tk.LEFT, padx=5)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)
# Function to display the final puzzle scene
def display_new_puzzle_scene():
    for widget in root.winfo_children():
        widget.destroy()

    puzzle_text = """
    You descend deeper into the tomb, the door creaking open and inviting you to continue. An overwhelming stench of rot and the sea fills your lungs with each breath.
    After descending a flight of stairs, you emerge into a brightly lit chamber, the sound of crashing waves echoing, yet no water in sight.
    Before you stands a door with a simple glowing script in an eerie blue sheen:

    "The more of this there is, the less you see. What is it?"
    """
    label = tk.Label(root, text=puzzle_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Image for the puzzle scene
    image_path = r"https://github.com/Babylon6/The_Mad_Mage/blob/main/tomb.jpg"  # Replace with actual path to your image
    image = Image.open(image_path)
    image = image.resize((400, 200), Image.Resampling.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack(pady=10)

    # Options for the riddle
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    option1_button = tk.Button(button_frame, text="Light", command=solve_new_riddle_incorrect, font=("Arial", 14))
    option1_button.pack(side=tk.LEFT, padx=5)

    option2_button = tk.Button(button_frame, text="Air", command=solve_new_riddle_incorrect, font=("Arial", 14))
    option2_button.pack(side=tk.LEFT, padx=5)

    option3_button = tk.Button(button_frame, text="Space", command=solve_new_riddle_incorrect, font=("Arial", 14))
    option3_button.pack(side=tk.LEFT, padx=5)

    option4_button = tk.Button(button_frame, text="Darkness", command=solve_new_riddle_correct, font=("Arial", 14))
    option4_button.pack(side=tk.LEFT, padx=5)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)
# Function for correct riddle answer
def solve_new_riddle_correct():
    messagebox.showinfo("Correct!", """
    You speak aloud the word “Darkness” and the lights in the room go out, snuffed by the arcane energy that bursts from the door.
    You hold your breath, waiting in the silence until you hear a faint click of the lock and the creaking of the door swinging open before you.
    """)
    display_mad_mage_battle_scene()  # Proceed to the Mad Mage battle scene

# Function for incorrect riddle answer
def solve_new_riddle_incorrect():
    messagebox.showerror("Incorrect", """
    Failing to utter the correct answer to the riddle, you hear a sound of clanging, and feel the earth start to shake as the ground beneath you cracks and crumbles,
    sending you spiraling to the pits beneath the castle.

    Better luck next time.
    """)
    root.quit()  # End the game
# Initialize variables to track hits for the Mad Mage fight
player_hits_mage = 0
mage_hits = 0

# Function to display the Mad Mage fight scene
def display_mad_mage_battle_scene():
    global player_hits_mage, mage_hits
    player_hits_mage = 0
    mage_hits = 0

    for widget in root.winfo_children():
        widget.destroy()

    fight_text = """
    You step into the ominous chamber, your senses assaulted by a cacophony of chaos. Flames erupt from the ground, and rivers of molten lava flow from towering volcanoes, casting a hellish glow.
    Lightning crackles from the tempestuous sky, illuminating waves that crash violently against jagged rocks. Dark clouds roil above, obscuring the twin suns—one real, the other a sinister artificial orb.
    The wind howls through the chamber, carrying the acrid scent of burning earth. Trees are uprooted and sent crashing to the ground,
    their demise accompanied by the relentless hammering of rain. Thunder booms, a deafening drumbeat that echoes through the air, while eerie sounds emanate from the depths of the ocean.
    Suddenly, the ground beneath you begins to split, fissures spreading rapidly. Without warning, booby traps descend from the ceiling, poised to claim any unwary adventurers.
    The battle with the Mad Mage has begun.
    """
    label = tk.Label(root, text=fight_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add image of the Mad Mage
    image_path = r"https://github.com/Babylon6/The_Mad_Mage/blob/main/mad_mage.jpg"  # Replace with the actual path to your image
    image = Image.open(image_path)
    image = image.resize((400, 400), Image.Resampling.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack(pady=10)

    # Add options to sword or mace
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    sword_button = tk.Button(button_frame, text="Sword", command=sword_mage, font=("Arial", 14))
    sword_button.pack(side=tk.LEFT, padx=5)

    mace_button = tk.Button(button_frame, text="Mace", command=mace_mage, font=("Arial", 14))
    mace_button.pack(side=tk.LEFT, padx=5)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)
# Function to handle sword action against the Mad Mage
def sword_mage():
    global player_hits_mage, mage_hits

    outcome = random.choices(["hit", "miss"], weights=[70, 30], k=1)[0]
    if outcome == "hit":
        player_hits_mage += 1
        messagebox.showinfo("Sword", f"Great hit! The Mad Mage staggers back. ({player_hits_mage}/3)")
    else:
        mage_hits += 1
        messagebox.showinfo("Sword", f"Your blow misses. The Mad Mage strikes you with a bolt of dark magic! ({mage_hits}/3)")

    check_mage_fight_outcome()

# Function to handle mace action against the Mad Mage
def mace_mage():
    global player_hits_mage, mage_hits

    outcome = random.choices(["hit", "miss"], weights=[70, 30], k=1)[0]
    if outcome == "hit":
        player_hits_mage += 1
        messagebox.showinfo("Mace", f"Great hit! The Mad Mage staggers back. ({player_hits_mage}/3)")
    else:
        mage_hits += 1
        messagebox.showinfo("Mace", f"Your blow misses. The Mad Mage strikes you with a bolt of dark magic! ({mage_hits}/3)")

    check_mage_fight_outcome()

# Function to check fight outcome for the Mad Mage fight
def check_mage_fight_outcome():
    global player_hits_mage, mage_hits

    if player_hits_mage >= 3:
        display_mage_win()
    elif mage_hits >= 3:
        display_mage_fail()

# Function to display win outcome for the Mad Mage fight
def display_mage_win():
    global player_hits_mage, mage_hits
    player_hits_mage = 0
    mage_hits = 0

    for widget in root.winfo_children():
        widget.destroy()
    
    win_text = """
    The Mad Mage collapses, defeated. Their dark magic dissipates, and the chamber fills with a radiant light. You feel a sense of victory, but one final choice remains.
    """
    label = tk.Label(root, text=win_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add button to proceed to the final choice
    continue_button = tk.Button(root, text="Final Choice", command=display_final_choice, font=("Arial", 14))
    continue_button.pack(pady=10)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)

# Function to display fail outcome for the Mad Mage fight
def display_mage_fail():
    global player_hits_mage, mage_hits
    player_hits_mage = 0
    mage_hits = 0

    for widget in root.winfo_children():
        widget.destroy()

    fail_text = """
    The Mad Mage's dark magic overwhelms you. You have been defeated. Eldoria remains under the Mad Mage's tyranny.
    """
    label = tk.Label(root, text=fail_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add options to retry or quit
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    retry_button = tk.Button(button_frame, text="Retry", command=adventure_begins, font=("Arial", 14))
    retry_button.pack(side=tk.LEFT, padx=5)

    quit_button = tk.Button(button_frame, text="Quit", command=quit_game, font=("Arial", 14))
    quit_button.pack(side=tk.LEFT, padx=5)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)
# Function to display the final choice scene
def display_final_choice():
    for widget in root.winfo_children():
        widget.destroy()

    final_choice_text = """
    In the now skeletal hand of the Mad Mage, you find a glowing sphere pulsating with energy. The fate of Eldoria lies within it.
    Do you choose to smash the sphere, releasing its power, or leave it intact, risking the return of the Mad Mage's tyranny?
    """
    label = tk.Label(root, text=final_choice_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add image of the glowing sphere
    image_path = r"https://github.com/Babylon6/The_Mad_Mage/blob/main/artifact.jpg"  # Replace with the actual path to your image
    image = Image.open(image_path)
    image = image.resize((200, 400), Image.Resampling.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack(pady=10)

    # Add options to smash or leave the sphere
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    smash_button = tk.Button(button_frame, text="Smash the Sphere", command=smash_sphere, font=("Arial", 14))
    smash_button.pack(side=tk.LEFT, padx=5)

    leave_button = tk.Button(button_frame, text="Leave the Sphere", command=leave_sphere, font=("Arial", 14))
    leave_button.pack(side=tk.LEFT, padx=5)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)

# Function for smashing the sphere
def smash_sphere():
    for widget in root.winfo_children():
        widget.destroy()

    smash_text = """
    You raise your weapon and bring it down on the sphere with all your might. The sphere shatters, releasing a blinding light that engulfs the room.
    As the light fades, you feel a sense of calm and peace wash over you. The dark magic is gone, and Eldoria is free at last. Congratulations, hero!
    """
    label = tk.Label(root, text=smash_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add button to proceed to the final congratulations scene
    continue_button = tk.Button(root, text="Continue", command=display_congratulations_scene, font=("Arial", 14))
    continue_button.pack(pady=10)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)

# Function for leaving the sphere intact
def leave_sphere():
    for widget in root.winfo_children():
        widget.destroy()

    leave_text = """
    You decide to leave the sphere intact, unsure of the consequences. As you step away, the room grows darker, and you feel a sense of foreboding.
    The Mad Mage's influence may still linger, and Eldoria's fate remains uncertain. Perhaps another hero will rise to face this challenge in the future.
    """
    label = tk.Label(root, text=leave_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add button to end the game
    end_button = tk.Button(root, text="End Game", command=root.quit, font=("Arial", 14))
    end_button.pack(pady=10)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)
# Function to display the final congratulations scene
def display_congratulations_scene():
    for widget in root.winfo_children():
        widget.destroy()

    congratulations_text = """
    Congratulations! You have brought the light back to Eldoria. You are a true hero.
    """
    label = tk.Label(root, text=congratulations_text, justify=tk.LEFT, wraplength=500, font=("Arial", 14))
    label.pack(pady=10)

    # Add image for the congratulations scene
    image_path = r"https://github.com/Babylon6/The_Mad_Mage/blob/main/victory.jpg"  # Replace with the actual path to your image
    image = Image.open(image_path)
    image = image.resize((400, 400), Image.Resampling.LANCZOS)  # Adjust the size as needed
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.photo = photo
    image_label.pack(pady=10)

    # Add button to end the game
    end_button = tk.Button(root, text="End Game", command=root.quit, font=("Arial", 14))
    end_button.pack(pady=10)

    # Resize the window to fit content after the content is fully loaded
    root.update_idletasks()
    root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")
    root.resizable(True, True)
# Function to quit the game
def quit_game():
    root.quit()
# Initialize the main window
root = tk.Tk()
root.title("The Mad Mage's Fortress")
display_game_title()
root.mainloop()
