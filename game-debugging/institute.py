#!/usr/bin/env python3
"""
The Blackwood Institute
A text-based adventure game

You are a mathematician who has just arrived at a remote research
fellowship in the mountains. Something is wrong.
"""

import json
import os
import textwrap

# ─────────────────────────────────────────────
# WORLD DATA
# ─────────────────────────────────────────────

ROOMS = {
    "quarters": {
        "name": "Your Quarters",
        "description": (
            "A small, cold room on the second floor. The radiator ticks but "
            "produces no heat. Your suitcase sits unopened on a narrow bed with "
            "starched white sheets. The window looks out onto a courtyard you "
            "don't remember crossing. There's a desk with a single drawer, and "
            "a wardrobe that smells of camphor and old paper."
        ),
        "exits": {"south": "hallway"},
        "items": [],
    },
    "hallway": {
        "name": "Second Floor Hallway",
        "description": (
            "A long corridor with dark wood panelling. Gas-style lamps flicker "
            "in brass sconces, though you're fairly sure the building has "
            "electricity. Doors line both sides — most are locked. The carpet "
            "is worn thin in a path that leads south to the staircase."
        ),
        "exits": {"north": "quarters", "south": "foyer", "east": "library"},
        "items": [],
    },
    "foyer": {
        "name": "The Foyer",
        "description": (
            "The entrance hall of the Institute. A grand staircase sweeps "
            "upward. The front door is heavy oak, and through its glass panels "
            "you can see fog pressing against the mountainside. A noticeboard "
            "lists the current fellows and their research areas — your name "
            "has been added in fresh ink. The handwriting is not yours."
        ),
        "exits": {
            "north": "hallway",
            "east": "common_room",
            "west": "garden",
            "south": "directors_office",
        },
        "items": [],
    },
    "common_room": {
        "name": "The Common Room",
        "description": (
            "Leather armchairs arranged around a cold fireplace. Bookshelves "
            "line the walls, filled with journals and monographs. A large "
            "blackboard dominates one wall, covered in dense equations. You "
            "recognise some of the notation — differential geometry, topology "
            "— but there are symbols you've never seen in any textbook. The "
            "chalk dust on the floor is fresh."
        ),
        "exits": {"west": "foyer", "down": "basement"},
        "items": ["chalk_stub"],
    },
    "library": {
        "name": "The Library",
        "description": (
            "Floor-to-ceiling shelves of mathematics texts, the oldest dating "
            "to the 18th century. The room is silent in a way that feels "
            "enforced rather than natural. Reading desks with green-shaded "
            "lamps. At the far end, a heavy iron gate blocks a narrow passage "
            "into what must be the restricted section. The gate has a "
            "combination lock — four digits."
        ),
        "exits": {"west": "hallway"},
        "items": ["journal"],
        "locked_exit": {
            "direction": "north",
            "destination": "restricted_section",
            "lock_type": "combination",
            "combination": "1729",
            "locked": True,
            "description": "The iron gate to the restricted section is locked with a four-digit combination.",
        },
    },
    "restricted_section": {
        "name": "The Restricted Section",
        "description": (
            "The air is different here — thinner, colder, as if the room "
            "exists at a slightly different altitude. The shelves hold "
            "handwritten manuscripts, not printed books. Some of the pages "
            "are covered in equations that seem to move when you're not "
            "looking directly at them. One manuscript lies open on a lectern: "
            "'On the Topology of Spaces That Should Not Exist.'"
        ),
        "exits": {"south": "library"},
        "items": ["compass"],
    },
    "observatory": {
        "name": "The Observatory",
        "description": (
            "A domed room at the top of a tower you didn't notice from "
            "outside. The telescope is enormous and old, brass and mahogany. "
            "But it's not pointed at the sky — it's angled downward, into "
            "the building itself. Through the eyepiece, you can see rooms "
            "that shouldn't be there: corridors that fold back on themselves, "
            "a staircase that descends further than the basement should allow."
        ),
        "exits": {"down": "hallway"},
        "items": [],
    },
    "basement": {
        "name": "The Basement",
        "description": (
            "Damp stone walls. The ceiling is low. Pipes run overhead, "
            "sweating condensation. Storage rooms branch off to either side, "
            "filled with old furniture and filing cabinets. At the far end, "
            "a door stands slightly ajar. Beyond it, you can hear something "
            "— not quite a sound, more like the memory of a sound. A chalk "
            "line on the floor traces a path deeper into the darkness."
        ),
        "exits": {"up": "common_room"},
        "items": ["key"],
    },
    "garden": {
        "name": "The Garden",
        "description": (
            "A walled garden, overgrown but not neglected — someone tends "
            "this, but according to a logic you don't understand. The paths "
            "don't connect the way they should. You can see the garden wall "
            "from any point, but the distance to it changes depending on "
            "which direction you walk. A sundial at the centre casts a shadow "
            "that doesn't match the sun's position."
        ),
        "exits": {"east": "foyer"},
        "items": [],
    },
    "directors_office": {
        "name": "The Director's Office",
        "description": (
            "Wood-panelled, warm, orderly. A desk with neat stacks of "
            "correspondence. Framed photographs on the walls show previous "
            "cohorts of fellows — going back decades, the faces always "
            "different, except one: a woman in the back row of every photo, "
            "never aging. A door behind the desk is locked."
        ),
        "exits": {"north": "foyer"},
        "items": [],
        "locked_exit": {
            "direction": "east",
            "destination": "impossible_room",
            "lock_type": "key",
            "key_item": "key",
            "locked": True,
            "description": "A door behind the desk is locked. It looks like it needs a key.",
        },
    },
    "impossible_room": {
        "name": "The Room That Shouldn't Be There",
        "description": (
            "You step through and the door closes behind you. The room is "
            "larger than the building. The walls are covered in equations — "
            "floor to ceiling, written in dozens of hands across what must "
            "be decades. You recognise your own notation among them, though "
            "you've never been here before. In the centre of the room, a "
            "circle is drawn on the floor in chalk. The equations spiral "
            "inward toward it. The air hums."
        ),
        "exits": {"west": "directors_office"},
        "items": [],
    },
}

# ─────────────────────────────────────────────
# CHARACTERS
# ─────────────────────────────────────────────

CHARACTERS = {
    "elena": {
        "name": "Dr. Elena Vasquez",
        "title": "Algebraic Topologist",
        "location": "common_room",
        "description": (
            "A sharp-featured woman in her fifties, sitting in an armchair "
            "with a cup of tea that has long gone cold. She watches you with "
            "an expression that might be curiosity or might be pity."
        ),
        "trust": 0,
        "dialogue": {
            "initial": {
                "text": (
                    '"You must be the new fellow. Welcome to Blackwood." '
                    "She doesn't smile. \"How much did they tell you about "
                    'the Institute before you accepted?"'
                ),
                "choices": {
                    "1": {
                        "text": '"Not much. Remote fellowship, good stipend, time to think."',
                        "response": (
                            '"Time to think. Yes, there\'s certainly that." '
                            "She looks at the blackboard. \"Do you recognise "
                            'the notation up there?"'
                        ),
                        "trust_change": 0,
                        "next": "blackboard",
                    },
                    "2": {
                        "text": '"I noticed the blackboard changes overnight. Do you know who writes on it?"',
                        "response": (
                            "Her eyes widen slightly. \"You noticed that "
                            "already? Most new fellows take weeks.\" She sets "
                            "down her tea. \"I'll say this: nobody here writes "
                            "on it. Not anymore.\""
                        ),
                        "trust_change": 2,
                        "next": "nobody_writes",
                    },
                },
            },
            "blackboard": {
                "text": (
                    '"Some of it. Differential geometry, bits of topology. '
                    'But there are symbols I don\'t recognise."'
                ),
                "choices": {
                    "1": {
                        "text": '"Can you explain the unfamiliar notation?"',
                        "response": (
                            '"Not here." She glances around the room. "The '
                            "walls have a way of... retaining things. Come "
                            "find me in the garden sometime.\""
                        ),
                        "trust_change": 1,
                        "next": None,
                    },
                    "2": {
                        "text": '"Who wrote them?"',
                        "response": (
                            '"That\'s the question, isn\'t it?" She picks up '
                            "her cold tea and drinks it anyway. \"Ask the "
                            "Director. Or don't. It depends on how much you "
                            "want to know.\""
                        ),
                        "trust_change": 0,
                        "next": None,
                    },
                },
            },
            "nobody_writes": {
                "text": '"What do you mean, nobody writes on it?"\n\nShe lowers her voice.',
                "choices": {
                    "1": {
                        "text": '"I\'m listening."',
                        "response": (
                            '"The equations appear. Every night. They\'re '
                            "proofs — correct proofs — of things that haven't "
                            "been proven yet. Riemann hypothesis partial "
                            "results. Novel approaches to Navier-Stokes. "
                            "Whoever — or whatever — writes them knows "
                            "mathematics that doesn't exist yet.\""
                        ),
                        "trust_change": 1,
                        "next": "deep_trust",
                    },
                    "2": {
                        "text": '"That sounds impossible."',
                        "response": (
                            '"You\'re at Blackwood. Get used to that word '
                            'meaning less than you think."'
                        ),
                        "trust_change": -1,
                        "next": None,
                    },
                },
            },
            "deep_trust": {
                "text": (
                    "She studies your face for a long moment.\n\n"
                    '"You have the journal? The one from the library?"'
                ),
                "choices": {
                    "1": {
                        "text": '"Yes, I found it." (requires: journal in inventory)',
                        "response": (
                            '"Read the entry from March 15th. It\'s about the '
                            "restricted section. The combination to the gate "
                            "is in there — but it's written as an equation. "
                            "1729. Hardy's taxi number. The smallest number "
                            "expressible as the sum of two cubes in two "
                            'different ways."\n\nShe pauses. "The Director '
                            "knows you're asking questions. Be careful.\""
                        ),
                        "trust_change": 2,
                        "reveals": "combination_hint",
                        "next": None,
                    },
                    "2": {
                        "text": '"What journal?"',
                        "response": (
                            '"In the library. On the third reading desk. It '
                            "belonged to the last fellow who stayed in your "
                            "room. He left in... a hurry.\""
                        ),
                        "trust_change": 0,
                        "next": None,
                    },
                },
            },
        },
    },
    "director": {
        "name": "Director Marsh",
        "title": "Director of the Blackwood Institute",
        "location": "directors_office",
        "description": (
            "An elderly man with kind eyes and precise movements. His office "
            "is immaculate. He offers you a chair with the warmth of someone "
            "who has welcomed many fellows — and the patience of someone who "
            "has watched many of them leave."
        ),
        "trust": 0,
        "dialogue": {
            "initial": {
                "text": (
                    '"Ah, welcome! Please, sit. I trust your quarters are '
                    "adequate? The Institute is old, but we maintain it as "
                    'best we can." He smiles. "You\'re here to work on... '
                    'differential geometry, yes?"'
                ),
                "choices": {
                    "1": {
                        "text": '"Yes. I have some ideas about curvature in non-standard spaces."',
                        "response": (
                            '"Non-standard spaces. How appropriate." He opens '
                            "a drawer and produces a folder. \"Your research "
                            "proposal. Excellent work. You'll find the library "
                            'well-stocked. Most sections, anyway."'
                        ),
                        "trust_change": 0,
                        "next": "research",
                    },
                    "2": {
                        "text": '"Actually, I have some questions about the Institute itself."',
                        "response": (
                            'His smile doesn\'t change, but something behind '
                            "his eyes does. \"Of course. What would you like "
                            'to know?"'
                        ),
                        "trust_change": 1,
                        "next": "questions",
                    },
                },
            },
            "research": {
                "text": '"Is there anything else I should know about working here?"',
                "choices": {
                    "1": {
                        "text": '"What\'s in the restricted section of the library?"',
                        "response": (
                            '"Manuscripts. Old ones. Fragile. Access is '
                            "limited to protect the documents.\" He says this "
                            "smoothly, as if he's said it many times before."
                        ),
                        "trust_change": 0,
                        "next": None,
                    },
                    "2": {
                        "text": '"Tell me about the other fellows."',
                        "response": (
                            '"Brilliant people, all of them. Dr. Vasquez in '
                            "topology, young Felix in number theory, Dr. Osei "
                            "in mathematical physics. You'll get along well.\""
                        ),
                        "trust_change": 0,
                        "next": None,
                    },
                },
            },
            "questions": {
                "text": '"Go ahead. I have nothing to hide."',
                "choices": {
                    "1": {
                        "text": '"The equations on the blackboard — who writes them?"',
                        "response": (
                            '"The fellows, of course. Collaboration is '
                            "encouraged here. Someone has an idea at 2am, "
                            "they write it down.\" He meets your eyes steadily. "
                            '"Is that all?"'
                        ),
                        "trust_change": -1,
                        "next": None,
                    },
                    "2": {
                        "text": '"The building seems... larger inside than outside."',
                        "response": (
                            "For the first time, his composure flickers. "
                            '"You can perceive that?" He stands and walks to '
                            "the window. \"Most people can't. Not for months. "
                            "Your spatial intuition must be... remarkable.\"\n\n"
                            "He turns back. \"Come see me again when you've "
                            'explored more. There are things I should tell you."'
                        ),
                        "trust_change": 3,
                        "next": "final_reveal",
                    },
                },
            },
            "final_reveal": {
                "text": (
                    "Director Marsh sits down heavily.\n\n"
                    '"The Institute is not a building. Not entirely. It\'s '
                    "a mathematical object — a manifold — that happens to "
                    "intersect with physical space. The equations on the "
                    "blackboard aren't written by anyone. They're the "
                    "manifold... expressing itself.\"\n\n"
                    "He opens the drawer again and produces a key.\n\n"
                    '"This opens the door behind my desk. What\'s on the '
                    "other side is the room where the manifold is thinnest. "
                    "Where mathematics and reality overlap.\"\n\n"
                    '"You can walk through that door. Or you can go home. '
                    "I won't judge either choice.\""
                ),
                "choices": {},
                "gives_item": "key",
            },
        },
    },
    "felix": {
        "name": "Felix Chen",
        "title": "Number Theorist (Doctoral Student)",
        "location": "library",
        "description": (
            "A nervous young man surrounded by towers of books. He startles "
            "when you approach, then relaxes — slightly. His notebook is "
            "covered in prime factorizations and he's chewing the end of "
            "his pencil."
        ),
        "trust": 0,
        "dialogue": {
            "initial": {
                "text": (
                    '"Oh! Hi. Sorry, you startled me. I\'m Felix. I\'m '
                    "working on — well, it doesn't matter. Are you the new "
                    'fellow? Welcome, I guess."'
                ),
                "choices": {
                    "1": {
                        "text": '"You seem nervous. Is everything okay?"',
                        "response": (
                            '"Fine! Everything\'s fine. It\'s just... have you '
                            "noticed anything strange about this place?\" He "
                            "looks around quickly. \"Never mind. Forget I said "
                            'anything."'
                        ),
                        "trust_change": 1,
                        "next": "strange",
                    },
                    "2": {
                        "text": '"What are you working on?"',
                        "response": (
                            '"Partition functions. How many ways you can break '
                            "a number into smaller pieces. It sounds simple but "
                            "it connects to... everything here.\" He stops "
                            'himself. "Just partition functions. That\'s all."'
                        ),
                        "trust_change": 0,
                        "next": None,
                    },
                },
            },
            "strange": {
                "text": (
                    "He's fidgeting with his pencil. \"I've been here four "
                    "months. Things happen here that... look, I'm probably "
                    'just stressed."'
                ),
                "choices": {
                    "1": {
                        "text": '"I\'ve noticed things too. The blackboard. The building\'s geometry."',
                        "response": (
                            '"You can feel it? The geometry?" His eyes go wide. '
                            "\"I've been mapping it. The building has eleven "
                            "rooms but only eight fit in the floor plan. The "
                            "other three... overlap somehow. Like a Klein "
                            "bottle.\"\n\nHe tears a page from his notebook "
                            "and hands it to you. It's a floor plan with "
                            "impossible angles."
                        ),
                        "trust_change": 3,
                        "reveals": "spatial_clue",
                        "next": None,
                    },
                    "2": {
                        "text": '"You\'re probably just stressed."',
                        "response": (
                            '"Right. Yeah. Of course." He turns back to his '
                            "books. The conversation is over."
                        ),
                        "trust_change": -2,
                        "next": None,
                    },
                },
            },
        },
    },
    "osei": {
        "name": "Dr. Adwoa Osei",
        "title": "Mathematical Physicist",
        "location": "garden",
        "description": (
            "A tall woman standing perfectly still by the sundial, watching "
            "its shadow with intense concentration. She has a notebook but "
            "hasn't written in it. Her stillness is unnerving."
        ),
        "trust": 0,
        "dialogue": {
            "initial": {
                "text": (
                    "She doesn't look up. \"The shadow moves counter-clockwise "
                    "between 3 and 4 in the afternoon. Every day. I've been "
                    "measuring it for six weeks.\"\n\nFinally she turns to you. "
                    '"You\'re new. How long have you been here?"'
                ),
                "choices": {
                    "1": {
                        "text": '"Just arrived. What do you mean the shadow moves counter-clockwise?"',
                        "response": (
                            '"Exactly what I said. This garden exists in a '
                            "space where the metric tensor has a sign flip. "
                            "Time flows differently here — not backward, just... "
                            "sideways.\" She says this as if it's perfectly "
                            'reasonable. "Give it a week. You\'ll see."'
                        ),
                        "trust_change": 1,
                        "next": "metric",
                    },
                    "2": {
                        "text": '"That\'s not possible."',
                        "response": (
                            '"I have six weeks of data that says otherwise. '
                            "Would you like to see the measurements?\" She "
                            "doesn't wait for an answer. \"No, you wouldn't. "
                            "Not yet. Come back when you've spent more time "
                            'in the building."'
                        ),
                        "trust_change": -1,
                        "next": None,
                    },
                },
            },
            "metric": {
                "text": (
                    '"The metric tensor... you mean the building warps space?"'
                    "\n\nShe almost smiles."
                ),
                "choices": {
                    "1": {
                        "text": '"I have a compass that behaves strangely." (requires: compass)',
                        "response": (
                            "She takes the compass and watches the needle. It "
                            "spins, then settles — pointing not north, but "
                            "toward the Institute.\n\n\"This isn't a compass. "
                            "It's a geodesic tracer. It points along the "
                            "shortest path in the manifold's geometry.\" She "
                            "hands it back. \"Follow it. It'll show you the "
                            "room that shouldn't exist.\"\n\nShe writes "
                            "something in her notebook and tears out the page. "
                            "\"The spatial puzzle. The building has three rooms "
                            "that overlap in four-dimensional space. The "
                            "impossible room is where they intersect. The "
                            "compass knows the way.\""
                        ),
                        "trust_change": 3,
                        "reveals": "spatial_solution",
                        "next": None,
                    },
                    "2": {
                        "text": '"What kind of space has a flipped metric tensor?"',
                        "response": (
                            '"A manifold with mixed signature. Pseudo-Riemannian. '
                            "The building is embedded in something that isn't "
                            "quite spacetime as we know it.\" She pauses. "
                            "\"Find the compass in the restricted section. "
                            "It'll show you what I mean.\""
                        ),
                        "trust_change": 1,
                        "next": None,
                    },
                },
            },
        },
    },
}

# ─────────────────────────────────────────────
# ITEMS
# ─────────────────────────────────────────────

ITEMS = {
    "key": {
        "name": "An old brass key",
        "description": (
            "Heavy and cold. The bow is shaped like a Klein bottle — a "
            "surface with no inside or outside. It shouldn't be possible "
            "to manufacture this in three dimensions, but here it is."
        ),
    },
    "journal": {
        "name": "A leather-bound journal",
        "description": (
            "Belonged to Dr. Marcus Webb, the previous occupant of your "
            "quarters. The entries start normal — research notes, daily "
            "observations — then grow increasingly frantic. The last entry, "
            "dated March 15th, reads: 'The combination is the taxi number. "
            "Hardy knew. Ramanujan knew. The manifold remembers everything "
            "that is beautiful and true.' After that, blank pages."
        ),
    },
    "chalk_stub": {
        "name": "A stub of blue chalk",
        "description": (
            "Unusual chalk — slightly warm to the touch, and the colour is "
            "a blue that doesn't quite look right under electric light. "
            "It's the same chalk used on the blackboard equations."
        ),
    },
    "compass": {
        "name": "A strange brass compass",
        "description": (
            "The needle doesn't point north. It doesn't point anywhere "
            "consistent — it drifts, then snaps to a heading, then drifts "
            "again. But you notice a pattern: it always settles toward the "
            "centre of the building."
        ),
    },
}


# ─────────────────────────────────────────────
# GAME STATE
# ─────────────────────────────────────────────

def new_game_state():
    """Create a fresh game state."""
    return {
        "current_room": "quarters",
        "inventory": [],
        "visited_rooms": ["quarters"],
        "character_trust": {name: 0 for name in CHARACTERS},
        "character_dialogue_state": {name: "initial" for name in CHARACTERS},
        "discoveries": [],
        "combination_known": False,
        "library_unlocked": False,
        "office_unlocked": False,
        "game_over": False,
        "ending": None,
    }


# ─────────────────────────────────────────────
# DISPLAY HELPERS
# ─────────────────────────────────────────────

def wrap_text(text, width=72):
    """Word-wrap text for the terminal."""
    paragraphs = text.split("\n")
    wrapped = []
    for p in paragraphs:
        if p.strip():
            wrapped.append(textwrap.fill(p.strip(), width=width))
        else:
            wrapped.append("")
    return "\n".join(wrapped)


def print_wrapped(text):
    """Print word-wrapped text."""
    print(wrap_text(text))
    print()


def print_separator():
    print("─" * 50)


# ─────────────────────────────────────────────
# GAME LOGIC
# ─────────────────────────────────────────────

def describe_room(state):
    """Print the description of the current room."""
    room = ROOMS[state["current_room"]]
    print_separator()
    print(f"  {room['name']}")
    print_separator()
    print()
    print_wrapped(room["description"])

    # Show items on the ground
    items_here = [i for i in room["items"] if i not in state["inventory"]]
    if items_here:
        for item_id in items_here:
            item = ITEMS[item_id]
            print(f"  You notice: {item['name']}")
        print()

    # Show characters present
    for char_id, char in CHARACTERS.items():
        if char["location"] == state["current_room"]:
            print(f"  {char['name']} ({char['title']}) is here.")
    print()

    # Show exits
    exits = list(room["exits"].keys())
    if "locked_exit" in room:
        lock = room["locked_exit"]
        if lock["locked"] and not is_exit_unlocked(state, state["current_room"]):
            pass  # Don't show locked exit as available
        else:
            exits.append(lock["direction"])
    print(f"  Exits: {', '.join(exits)}")
    print()


def is_exit_unlocked(state, room_id):
    """Check if a locked exit in a room has been unlocked."""
    if room_id == "library":
        return state["library_unlocked"]
    elif room_id == "directors_office":
        return state["office_unlocked"]
    return False


def move(state, direction):
    """Move to a new room."""
    room = ROOMS[state["current_room"]]

    # Check normal exits
    if direction in room["exits"]:
        state["current_room"] = room["exits"][direction]
        if state["current_room"] not in state["visited_rooms"]:
            state["visited_rooms"].append(state["current_room"])
        return True

    # Check locked exits
    if "locked_exit" in room:
        lock = room["locked_exit"]
        if direction == lock["direction"]:
            if is_exit_unlocked(state, state["current_room"]):
                state["current_room"] = lock["destination"]
                if state["current_room"] not in state["visited_rooms"]:
                    state["visited_rooms"].append(state["current_room"])
                return True
            else:
                print_wrapped(lock["description"])
                return False

    print("You can't go that way.")
    return False


def take_item(state, item_name):
    """Pick up an item from the current room."""
    room = ROOMS[state["current_room"]]
    # Match partial item names
    for item_id in room["items"]:
        if item_name.lower() in item_id.lower() or item_name.lower() in ITEMS[item_id]["name"].lower():
            if item_id in state["inventory"]:
                print("You already have that.")
                return
            state["inventory"].append(item_id)
            print(f"Taken: {ITEMS[item_id]['name']}")
            print()
            return

    print("You don't see that here.")


def show_inventory(state):
    """Display the player's inventory."""
    if not state["inventory"]:
        print("You're not carrying anything.")
    else:
        print("You are carrying:")
        for item_id in state["inventory"]:
            print(f"  - {ITEMS[item_id]['name']}")
    print()


def examine_item(state, item_name):
    """Look at an item in detail."""
    for item_id in state["inventory"]:
        if item_name.lower() in item_id.lower() or item_name.lower() in ITEMS[item_id]["name"].lower():
            print_wrapped(ITEMS[item_id]["description"])
            return

    # Also check items in the room
    room = ROOMS[state["current_room"]]
    for item_id in room["items"]:
        if item_name.lower() in item_id.lower() or item_name.lower() in ITEMS[item_id]["name"].lower():
            print_wrapped(ITEMS[item_id]["description"])
            return

    print("You don't see that.")


def talk_to(state, char_name):
    """Initiate or continue dialogue with a character."""
    room_id = state["current_room"]

    # Find character in current room
    char_id = None
    for cid, char in CHARACTERS.items():
        if char["location"] == room_id and (
            char_name.lower() in char["name"].lower()
            or char_name.lower() in cid.lower()
        ):
            char_id = cid
            break

    if char_id is None:
        print("There's nobody here by that name.")
        return

    char = CHARACTERS[char_id]
    dialogue_state = state["character_dialogue_state"][char_id]

    if dialogue_state not in char["dialogue"]:
        print(f'{char["name"]} has nothing more to say right now.')
        return

    node = char["dialogue"][dialogue_state]

    # Check for item-giving dialogue
    if "gives_item" in node:
        item_id = node["gives_item"]
        if item_id not in state["inventory"]:
            state["inventory"].append(item_id)
            print(f"\n  [Received: {ITEMS[item_id]['name']}]\n")

    print()
    print_wrapped(node["text"])

    if not node.get("choices"):
        return

    # Display choices
    for key, choice in node["choices"].items():
        # Check item requirements
        requires = ""
        if "requires" in choice["text"]:
            requires = " *"
        print(f"  {key}) {choice['text']}")
    print()

    while True:
        answer = input("  Your choice: ").strip()
        if answer in node["choices"]:
            break
        print("  Please choose a valid option.")

    choice = node["choices"][answer]

    # Check if choice requires an item
    choice_text = choice["text"].lower()
    if "requires:" in choice_text:
        # Extract required item
        req_start = choice_text.index("requires:") + 9
        req_end = choice_text.index(")", req_start)
        required_item = choice_text[req_start:req_end].strip()

        has_item = False
        for inv_item in state["inventory"]:
            if required_item in inv_item.lower() or required_item in ITEMS[inv_item]["name"].lower():
                has_item = True
                break

        if not has_item:
            print("\n  [You don't have the required item.]\n")
            return

    print()
    print_wrapped(choice["response"])

    # Update trust
    state["character_trust"][char_id] += choice["trust_change"]

    # Handle reveals
    if "reveals" in choice:
        discovery = choice["reveals"]
        if discovery not in state["discoveries"]:
            state["discoveries"].append(discovery)
            print(f"  [New discovery: {discovery.replace('_', ' ').title()}]")
            print()

    # Advance dialogue
    if choice.get("next"):
        state["character_dialogue_state"][char_id] = choice["next"]
    else:
        # Mark dialogue as exhausted for this branch
        state["character_dialogue_state"][char_id] = dialogue_state + "_done"


def solve_combination(state):
    """Attempt to unlock the library gate."""
    if state["library_unlocked"]:
        print("The gate is already open.")
        return

    if state["current_room"] != "library":
        print("There's nothing to unlock here.")
        return

    print_wrapped(
        "The iron gate has a four-digit combination lock. The numbers "
        "0-9 are on each wheel."
    )
    attempt = input("  Enter the combination: ").strip()

    if attempt == "1729":
        state["library_unlocked"] = True
        print_wrapped(
            "Click. The lock opens. The gate swings inward with a sound "
            "like a sigh. Cold air rushes out from the restricted section."
        )
    else:
        print_wrapped(
            "The lock doesn't budge. The combination is wrong."
        )


def use_key(state):
    """Attempt to use the key on the director's office door."""
    if state["current_room"] != "directors_office":
        print("There's nothing to use the key on here.")
        return

    if "key" not in state["inventory"]:
        print("You don't have a key.")
        return

    if state["office_unlocked"]:
        print("The door is already unlocked.")
        return

    state["office_unlocked"] = True
    print_wrapped(
        "The Klein bottle key slides into the lock. For a moment, "
        "your hand seems to pass through itself — the key is both "
        "inside and outside the lock simultaneously. Then it turns, "
        "and the door opens onto a space that your eyes refuse to "
        "measure."
    )


def check_ending(state):
    """Check if the player has reached an ending condition."""
    if state["current_room"] != "impossible_room":
        return False

    # Need chalk and compass to reach the true ending
    has_chalk = "chalk_stub" in state["inventory"]
    has_compass = "compass" in state["inventory"]
    has_journal = "journal" in state["inventory"]

    print_separator()
    print("  THE CIRCLE")
    print_separator()
    print()

    if has_chalk and has_compass and has_journal:
        print_wrapped(
            "You stand at the centre of the circle. The equations on the "
            "walls pulse faintly, like a heartbeat. The compass needle "
            "spins wildly, then stops — pointing straight down."
        )
        print()
        print("What do you do?")
        print("  1) Complete the equations on the wall with the chalk")
        print("  2) Close the journal and walk away")
        print()

        while True:
            choice = input("  Your choice: ").strip()
            if choice in ("1", "2"):
                break
            print("  Please choose 1 or 2.")

        if choice == "1":
            # Ending: Become part of it
            state["ending"] = "become"
            state["game_over"] = True
            print()
            print_separator()
            print("  ENDING: THE NEW NOTATION")
            print_separator()
            print()
            print_wrapped(
                "You lift the chalk and begin to write. The equations flow "
                "through you — not from your memory, but from somewhere "
                "deeper. Your hand moves in patterns you don't consciously "
                "understand, but every line feels true.\n\n"
                "The walls brighten. The manifold recognises you.\n\n"
                "You write through the night. When morning comes, you "
                "don't stop. The other fellows find your quarters empty, "
                "your suitcase still unpacked. But in the common room, "
                "the blackboard has new equations — in handwriting that "
                "doesn't match anyone's.\n\n"
                "In the back row of the next cohort photograph, there is "
                "a new face that will never age.\n\n"
                "You have become part of the Blackwood Institute.\n\n"
                "You have become part of mathematics itself."
            )
            return True

        else:
            # Ending: Uncover the truth and leave
            state["ending"] = "leave"
            state["game_over"] = True
            print()
            print_separator()
            print("  ENDING: THE PROOF OF DEPARTURE")
            print_separator()
            print()
            print_wrapped(
                "You close the journal. You put the chalk in your pocket. "
                "You turn and walk out of the room that shouldn't exist.\n\n"
                "Director Marsh is waiting outside his office. He nods.\n\n"
                "\"You saw it. The manifold. The mathematics that writes "
                "itself.\" He pauses. \"And you're choosing to leave.\"\n\n"
                "\"I'm choosing to leave *knowing*,\" you say.\n\n"
                "He smiles — the first real smile you've seen from him. "
                "\"That's the hardest proof of all. Most people who see "
                "the truth can't resist completing it.\"\n\n"
                "You pack your suitcase. You walk through the fog, down "
                "the mountain path. The compass in your pocket still "
                "points back toward the Institute.\n\n"
                "It always will.\n\n"
                "But you carry something with you: the knowledge that "
                "mathematics is not a human invention. It is a landscape. "
                "And you have seen its most secret corner."
            )
            return True

    else:
        print_wrapped(
            "The circle on the floor hums with potential. The equations "
            "spiral inward. You feel like you're on the edge of "
            "understanding something vast — but you don't have "
            "everything you need.\n\n"
            "You should explore more. Find what's hidden in this "
            "Institute."
        )
        missing = []
        if not has_chalk:
            missing.append("something to write with")
        if not has_compass:
            missing.append("something to navigate by")
        if not has_journal:
            missing.append("someone's written record")
        print(f"\n  You feel you're missing: {', '.join(missing)}")
        print()
        return False


# ─────────────────────────────────────────────
# SAVE / LOAD
# ─────────────────────────────────────────────

SAVE_FILE = "blackwood_save.json"


def save_game(state):
    """Save the current game state to a file."""
    with open(SAVE_FILE, "w") as f:
        json.dump(state, f, indent=2)
    print(f"Game saved to {SAVE_FILE}.")


def load_game():
    """Load game state from a file."""
    if not os.path.exists(SAVE_FILE):
        print("No save file found.")
        return None

    with open(SAVE_FILE, "r") as f:
        state = json.load(f)
    print("Game loaded.")
    return state


# ─────────────────────────────────────────────
# HELP
# ─────────────────────────────────────────────

def show_help():
    print("""
Commands:
  look              - Describe the current room
  go <direction>    - Move (north, south, east, west, up, down)
  take <item>       - Pick up an item
  inventory / i     - Show what you're carrying
  examine <item>    - Look at an item closely
  talk <character>  - Talk to someone in the room
  unlock            - Try to unlock something in the room
  use key           - Use the key on a locked door
  save              - Save your progress
  load              - Load a saved game
  help              - Show this help
  quit              - Exit the game
""")


# ─────────────────────────────────────────────
# MAIN GAME LOOP
# ─────────────────────────────────────────────

def main():
    print()
    print("=" * 50)
    print("  T H E   B L A C K W O O D   I N S T I T U T E")
    print("=" * 50)
    print()
    print_wrapped(
        "You step off the bus at the end of a gravel road. The fog is "
        "thick. Ahead, the Blackwood Institute rises from the mountainside "
        "like a theorem — inevitable, austere, and slightly wrong in "
        "proportions your eye can't quite pin down.\n\n"
        "You are a mathematician. You are here for a one-year research "
        "fellowship. Your suitcase is heavy. The front door is open.\n\n"
        "A note has been slipped under your door. It reads:\n\n"
        '  "The previous fellow in your room left in a hurry.\n'
        '   He left a journal behind. Find it before they do.\n'
        '   Trust no one until they earn it.\n'
        '   The blackboard knows more than anyone here."\n\n'
        "The note is unsigned.\n\n"
        "Type 'help' for a list of commands."
    )

    # New game or load
    print()
    print("  1) New game")
    print("  2) Load saved game")
    print()
    choice = input("  Choose: ").strip()

    if choice == "2":
        state = load_game()
        if state is None:
            print("Starting new game instead.")
            state = new_game_state()
    else:
        state = new_game_state()

    describe_room(state)

    while not state["game_over"]:
        try:
            command = input("> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if not command:
            continue

        parts = command.split(maxsplit=1)
        verb = parts[0]
        arg = parts[1] if len(parts) > 1 else ""

        if verb == "quit" or verb == "exit":
            print("Goodbye. The Institute will be here when you return.")
            break

        elif verb == "help":
            show_help()

        elif verb == "look":
            describe_room(state)

        elif verb == "go" or verb in ("north", "south", "east", "west", "up", "down", "n", "s", "e", "w", "u", "d"):
            direction = arg if verb == "go" else verb
            # Handle abbreviations
            abbrevs = {"n": "north", "s": "south", "e": "east", "w": "west", "u": "up", "d": "down"}
            direction = abbrevs.get(direction, direction)
            if move(state, direction):
                describe_room(state)
                if state["current_room"] == "impossible_room":
                    check_ending(state)

        elif verb == "take" or verb == "get" or verb == "pick":
            if arg:
                take_item(state, arg)
            else:
                print("Take what?")

        elif verb in ("inventory", "i"):
            show_inventory(state)

        elif verb == "examine" or verb == "look" and arg:
            if arg:
                examine_item(state, arg)
            else:
                describe_room(state)

        elif verb == "talk" or verb == "speak":
            if arg:
                # Strip "to" if present
                if arg.startswith("to "):
                    arg = arg[3:]
                talk_to(state, arg)
            else:
                print("Talk to whom?")

        elif verb == "unlock":
            solve_combination(state)

        elif verb == "use":
            if "key" in arg:
                use_key(state)
            elif "chalk" in arg:
                print_wrapped(
                    "The chalk feels warm in your hand. You could write "
                    "with it, but where? You'd need the right surface..."
                )
            elif "compass" in arg:
                if "compass" in state["inventory"]:
                    print_wrapped(
                        "The needle spins, then settles. It points deeper "
                        "into the building — always toward the centre."
                    )
                else:
                    print("You don't have a compass.")
            elif "journal" in arg:
                if "journal" in state["inventory"]:
                    examine_item(state, "journal")
                else:
                    print("You don't have a journal.")
            else:
                print("Use what?")

        elif verb == "save":
            save_game(state)

        elif verb == "load":
            loaded = load_game()
            if loaded:
                state = loaded
                describe_room(state)

        else:
            print(
                "I don't understand that command. Type 'help' for options."
            )

    if state["game_over"]:
        print()
        print_separator()
        print("  GAME OVER")
        print_separator()
        print()
        rooms_visited = len(state["visited_rooms"])
        total_rooms = len(ROOMS)
        items_found = len(state["inventory"])
        total_items = len(ITEMS)
        discoveries = len(state["discoveries"])
        print(f"  Rooms explored: {rooms_visited}/{total_rooms}")
        print(f"  Items found: {items_found}/{total_items}")
        print(f"  Discoveries: {discoveries}")
        print(f"  Ending: {state['ending'].replace('_', ' ').title()}")
        print()
        print("  Thank you for visiting the Blackwood Institute.")
        print()


if __name__ == "__main__":
    main()
