#!/usr/bin/env python3
"""
Anagram solver for Puzzle 4 license plates.
Attempts to find real place names by rearranging the stencil letters.
"""

from itertools import permutations
import sys

# License plates from the puzzle
plates = [
    ("GLNNCARV", "Row 1"),  # removed period
    ("WASCKEY", "Row 2 left"),
    ("ONTEL", "Row 2 right"),
    ("WESTASCA", "Row 3 left"),
    ("CAMOTY", "Row 3 right"),
    ("CSIPAIZER", "Row 4"),
    ("MCRLAY", "Row 5 left"),
    ("FLIWOKA", "Row 5 right"),  # removed period
    ("CUAPOVEA", "Row 6"),
    ("BLGLAVON", "Row 7 left"),
    ("COLFAX", "Row 7 right"),
    ("JUESEEF2RYAS", "Row 8"),
    ("TOVEBCOUT", "Row 9"),
    ("GRCKYFOREST", "Row 10"),
    ("MELIMAGLEN", "Row 11"),
    ("MCBLCGRAN", "Row 12"),
    ("AALYISC", "Row 13 left"),
    ("COSTHEN", "Row 13 right"),  # assuming COSTHEN not LOSTHEN
    ("ATRBPSCY", "Row 14 left"),
    ("HFMEOS", "Row 14 right"),
    ("LLOMCGDEGRY", "Row 15"),
]

# Known place names to check against (from video + world locations)
known_places = [
    # From video
    "EGYPT", "AFRICA", "DUBAI", "ABU DHABI", "ABUDHABI",
    "BURJ KHALIFA", "ATLANTIS", "PYRAMIDS",

    # Major world locations that might appear
    "PARIS", "LONDON", "TOKYO", "MOSCOW", "ROME",
    "BERLIN", "MADRID", "ATHENS", "VIENNA", "PRAGUE",
    "VENICE", "MILAN", "FLORENCE", "GENEVA", "ZURICH",
    "AMSTERDAM", "BRUSSELS", "STOCKHOLM", "OSLO", "HELSINKI",
    "WARSAW", "BUDAPEST", "BELGRADE", "ZAGREB", "SARAJEVO",
    "ISTANBUL", "ATHENS", "CAIRO", "NAIROBI", "LAGOS",
    "CAPE TOWN", "JOHANNESBURG", "DELHI", "MUMBAI", "KOLKATA",
    "BANGKOK", "SINGAPORE", "MANILA", "JAKARTA", "KUALA LUMPUR",
    "SYDNEY", "MELBOURNE", "AUCKLAND", "TORONTO", "MONTREAL",
    "VANCOUVER", "CHICAGO", "HOUSTON", "PHOENIX", "DENVER",
    "SEATTLE", "BOSTON", "MIAMI", "ATLANTA", "DALLAS",
    "LAS VEGAS", "SAN FRANCISCO", "LOS ANGELES",

    # Countries
    "USA", "CANADA", "MEXICO", "BRAZIL", "ARGENTINA",
    "UK", "FRANCE", "GERMANY", "ITALY", "SPAIN",
    "PORTUGAL", "GREECE", "TURKEY", "RUSSIA", "CHINA",
    "JAPAN", "INDIA", "THAILAND", "VIETNAM", "KOREA",
    "AUSTRALIA", "NEW ZEALAND",

    # Other possibilities
    "MONACO", "MALTA", "CYPRUS", "CRETE", "SICILY",
    "CORSICA", "SARDINIA", "MAJORCA", "IBIZA",
    "CROATIA", "SLOVENIA", "SLOVAKIA", "ROMANIA",
    "BULGARIA", "SERBIA", "BOSNIA", "MACEDONIA",
    "ALBANIA", "MONTENEGRO", "KOSOVO",
]

def check_anagram(plate_text, place_name):
    """Check if plate_text is an anagram of place_name (ignoring spaces)."""
    plate_sorted = sorted(plate_text.upper().replace(" ", "").replace(".", ""))
    place_sorted = sorted(place_name.upper().replace(" ", ""))
    return plate_sorted == place_sorted

def find_matches():
    """Find which plates match known places."""
    results = []

    for plate, location in plates:
        matches = []
        plate_clean = plate.replace("2", "").upper()  # Remove digit 2 from JUESEEF2RYAS

        for place in known_places:
            if check_anagram(plate_clean, place):
                matches.append(place)

        if matches:
            results.append(f"{location}: {plate} → {', '.join(matches)}")
        else:
            results.append(f"{location}: {plate} → NO MATCH")

    return results

if __name__ == "__main__":
    print("Puzzle 4: Anagram Analysis")
    print("=" * 60)

    results = find_matches()
    for result in results:
        print(result)

    print("\n" + "=" * 60)
    print("Manual checking for specific suspicious plates:")

    # Manual checks for plates that look promising
    print("\nChecking TOVEBCOUT:")
    if check_anagram("TOVEBCOUT", "YOUTUBE"):
        print("  ✓ TOVEBCOUT = YOUTUBE (but not a place)")

    print("\nChecking GRCKYFOREST:")
    if check_anagram("GRCKYFOREST", "ROCKY FOREST"):
        print("  ✓ GRCKYFOREST = ROCKY FOREST")

    print("\nChecking COLFAX:")
    print("  COLFAX appears to be a direct read (street name in many US cities)")

    print("\nChecking GLNNCARV:")
    if check_anagram("GLNNCARV", "CARACAS"):
        print("  ✓ GLNNCARV = CARACAS")
    if check_anagram("GLNNCARV", "VALENCIA"):
        print("  ✓ GLNNCARV = VALENCIA")

    print("\nChecking WASCKEY:")
    if check_anagram("WASCKEY", "HACKNEY"):
        print("  ✓ WASCKEY = HACKNEY")

    print("\nChecking MELIMAGLEN:")
    if check_anagram("MELIMAGLEN", "MAGELLAN"):
        print("  ✓ MELIMAGLEN = MAGELLAN")
