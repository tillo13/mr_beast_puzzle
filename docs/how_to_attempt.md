# Agent Workflow & Techniques

> Operational playbook for AI agents working on the MrBeast Million Dollar Puzzle.
> For puzzle architecture, URLs, and clue inventory see `CLAUDE.md` and `results/`.

## Agent Workflow — Phased Attack Plan

### PHASE 1: GATHER ALL MATERIALS
- Download Super Bowl ad at max resolution → frame extraction
- Download all teaser/promo videos
- Find and record all 9 pinned comment puzzle links (DONE → `clues/puzzle_links.md`)
- Find MrBeast's Super Bowl photos (GMA hint: "look for numbers in photos")
- Check Tonight Show Feb 6 appearance for puzzle content
- Monitor mrbeast.salesforce.com for new hints

### PHASE 2: DECODE THE SUPER BOWL AD
- Frame-by-frame extraction of all visual symbols
- OCR all visible text (screens, doors, signs, uniforms)
- Catalog every symbol and research meaning
- Determine if ad symbols provide extraction keys for the playlist puzzles
- Analyze the bank teaser video using info FROM the ad

### PHASE 3: SOLVE THE 9 PLAYLIST PUZZLES
- Open each puzzle link, identify puzzle type
- Solve each puzzle to base completion
- Apply extraction method (from ad) to get the answer word
- Verify each word fits expected letter count (5,9,5,7,8,4,9,6,5)
- See `docs/parallel_agent_strategy.md` for the 1-agent-per-puzzle plan

### PHASE 4: ASSEMBLE & FOLLOW THE META-CLUE
- Order the 9 words (playlist order assumed = clue order)
- Validate: does the assembled phrase read as an instruction?
- Follow the instruction to find the hidden code
- Cross-reference community findings from Reddit/Discord

### PHASE 5: WIN
- Slack the code to Jimmy Donaldson

---

## AI Techniques to Deploy

### Pattern Recognition
- **Brute-force phrase matching:** Generate English phrases fitting 5-9-5-7-8-4-9-6-5
- **Cipher identification:** Test encoded strings against all common cipher types
- **Anagram solving:** Rearrange puzzle outputs if needed

### Image Analysis
- **OCR:** Extract text from every video frame
- **Barcode/QR scanning:** Decode codes found in video frames
- **Steganography detection:** Check images for hidden data (LSB encoding)
- **Color analysis:** Look for patterns in pixel colors encoding information
- **EXIF/metadata analysis:** Check photos for GPS coordinates, hidden comments

### Audio Analysis
- **Spectrogram analysis:** Visual representation of audio may hide images/text
- **Reverse audio playback:** Check for backward messages
- **DTMF tone decoding:** Phone dial tones → numbers
- **Frequency analysis:** Data encoded in specific frequencies

### Text/Code Analysis
- **Acrostic detection:** First letters of words/lines
- **Caesar/ROT13:** Try all 26 rotations on any text
- **Vigenere cipher:** Try keywords related to MrBeast/Salesforce/Slack
- **Base64/hex decoding:** Check suspicious strings
- **Morse code:** Dots/dashes hidden in visual patterns
- **Semaphore/flag signals:** Ad symbols may represent flag positions

### Web Analysis
- **Page source inspection:** HTML comments, hidden elements on all linked pages
- **Monitor Reddit user BeastForce67** for new puzzle posts
- **Track mrbeast.salesforce.com** for hint drops and site changes

---

## Strategic Insights

1. **Designed for collaboration** — "it's probably not possible for one person to find and solve everything." AI advantage: cross-reference faster than a Discord full of people.
2. **New clues drop regularly** — living puzzle, check daily.
3. **"Codes you can find online"** = standard cryptographic references. Try well-known ciphers before exotic theories.
4. **The 9-word clue is step ONE, not the end.** It launches a further search.
5. **"Look up, down, forward, backward, and behind the scenes"** — likely literal. Check things in reverse, upside down. Also check the BTS video specifically.
6. **Bank video needs Super Bowl ad content** — interconnected, can't solve one without the other.

---

*For the parallel agent execution plan, see `docs/parallel_agent_strategy.md`.*
*For daily progress, see `docs/progress.md`.*
