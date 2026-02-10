# Shared Context for Puzzle Agents

> Read this before attempting to solve your puzzle. Contains extraction clues from the Super Bowl ad and other cross-cutting intel.

## Meta-Clue Structure

The 9 answer words form an instruction with this letter pattern:
```
Word 1 (5)  Word 2 (9)  Word 3 (5)  Word 4 (7)  Word 5 (8)  Word 6 (4)  Word 7 (9)  Word 8 (6)  Word 9 (5)
```

Your puzzle number corresponds to one of these positions (assumed playlist order = clue order, unconfirmed).

## Extraction Keys from Super Bowl Ad

The ad contains clues that likely tell you HOW to extract a final answer word from your solved puzzle grid. Here's what we found:

### Vault Rim Numbers (HIGHEST PRIORITY)
Numbers engraved around the circular vault door rim, separated by `+` and `-` signs:
- Top arc: `...3-1-3+1-1-0-4+...`
- Right arc: `...1-1-9-0-4-1-0-4-2...`
- Left arc: `...1-1-8-4-3-1-1-...`
- The full sequence runs all the way around the door
- **Theory:** These may be row-column coordinates or offsets for extracting specific cells from solved puzzle grids

### Control Room Monitor Symbols
9 symbols on monitors that may correspond to the 9 puzzle videos:

| # | Symbol | Description |
|---|--------|-------------|
| 1 | Spider | Dark silhouette on blue/purple background |
| 2 | Bird | White songbird/owl silhouette |
| 3 | Sine wave | Blue curved wave |
| 4 | Ear / hearing icon | Concentric arcs from ear shape |
| 5 | Elephant | Gray elephant silhouette |
| 6 | 10^5 (100,000) | Scientific notation on screen |
| 7 | Faces grid | Multiple headshots in grid |
| 8 | Smoking device | Object on far-right monitor |
| 9 | Swiss cross | Red cross symbol |

**We don't know which symbol maps to which puzzle yet.** If your puzzle solution involves any of these symbols, note it.

### Mathematical Formulas
- **n^3 = m^2** (or n^3 = n^2) — large screen in control room
- **10^5 = 100,000** — monitor display
- **22,483 lb** — weight readout on monitor
- **">L>" or ">6>"** — symbols on left monitor

### Physical Clues in the Ad
- **Braille dots** on blast door — two groups of raised dots, likely encoding two words/numbers
- **Beam number: "3634026-1"** (or "3634B26-1") — stamped on metal beam with gear symbol
- **Electrical panel lights** — 2x4 grid of colored lights (amber, green, red) — may encode binary
- **Red-bordered dollar bills** — ~10-12 bills highlighted in vault opening scene
- **Laser beam pattern** — 8-10 red beams forming web pattern in corridor

### QR Code — DECODED
The entire military compound forms a QR code when viewed from above (frames 57-64).
- **URL**: `https://sforce.co/4bAAGMH?r=qr`
- **Redirects to**: `https://mrbeast.salesforce.com/bts` (behind the scenes page)
- Page returns 403 — may need login/registration or browser access

### Slack Emojis — IDENTIFIED
Below the "Good luck!" Slackbot message (frames 27-29), 5 emoji reactions:
1. **Camel** — possibly maps to Pyramids puzzle (P8)?
2. **Dinosaur** (sauropod) — possibly maps to Pokemon Go (P5)?
3. **Gold coin** — possibly maps to Circle puzzle (P9)?
4. **Anchor** — mapping unknown
5. **Tent with trees** — directly maps to Wilderness/Tents puzzle (P6)

## Rewatch Video Background Scenes

9 themed scenes appear behind MrBeast, possibly mapping to the 9 puzzles:
1. Medieval peasant mob
2. Cow/farm animal
3. Basketball players (#23 jersey)
4. Baton twirlers
5. Fire performers + bear mascot
6. Speech bubble ("What the HECK")
7. Ninjas + Shining twins
8. Boxing match
9. Formal waiters/butlers

## GMA Hint (Feb 9)
- "Look for numbers in photos I took at the Super Bowl"
- "Watch four videos closely and follow anything that feels off"
- Photos likely on Instagram (@mrbeast) and X (@MrBeast) from Feb 8-9
- Known post: photo with Rosé, captioned "I like football"
- **No one has publicly decoded the numbers in these photos yet**

## What We NOW Know (updated Feb 9 late session)
- **QR code DECODED**: `https://sforce.co/4bAAGMH?r=qr` → `https://mrbeast.salesforce.com/bts` (403, needs browser)
- **Slack emojis confirmed**: Camel, Dinosaur, Gold coin, Anchor, Tent — tent maps to P6
- **Vault rim numbers partially read** but 1080p video too low-res for full decode
- **Braille NOT decoded** — need higher resolution

## Community Ad Decodes (NEW — from Manifold Markets, Feb 9)

The community has decoded additional elements from the Super Bowl ad that we hadn't found:

| Decode | Source in Ad | Notes |
|--------|-------------|-------|
| **CASH TENT** | Marked dollar bills | May relate to P6 (Wilderness/Tents) |
| **LASER MIX UP** | 26 laser dots in sequence | From the laser door/corridor scene |
| **TRUST AI** | Morse code flashing | Uncertain — needs verification |
| **DINAMODI** | Birds-on-wire cipher | Anagram theories: "I AM DINO", "DOMAIN ID", "DIAM NODI" |

Also noted by community:
- Southwest direction words: Swing, Witch, Elephant, Swan's Neck, Sword, Switzerland, Sweater
- Caesar cipher reference from bust sculpture with L/R position notation
- Compass-direction imagery
- Numbered wheel sequence

**Despite all these decodes, the community reports "basically no progress" toward actual puzzle answers.**

## What We Still Don't Know
- Full vault rim number sequence (need MrBeast's Super Bowl photos or 4K video)
- Which monitor symbol maps to which puzzle (9 symbols → 9 puzzles)
- What the Braille dots on the blast door say
- What's on mrbeast.salesforce.com/bts (the QR code destination)
- How extraction works (vault rim numbers → puzzle answers)
- Whether the beam number "3634026-1" is a clue or set dressing
- What "101,007 investigators" from Salesforce tweet means (planted clue?)

## Your Task
1. Solve your puzzle grid/mechanism
2. Look for any connection to the symbols/numbers above
3. Extract a word of the expected length
4. Write everything to `puzzles/XX_*/notes.md`
