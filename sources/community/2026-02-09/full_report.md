# Community Progress Report: MrBeast Million Dollar Puzzle
## February 9, 2026 (Day 1) -- Web Search Compilation

> **Search conducted:** February 9, 2026 ~10:00 PM ET
> **Status:** UNSOLVED -- No one has solved or come close to solving the puzzle
> **Prize:** $1,000,000 USD to the first person to Slack the correct code to Jimmy Donaldson
> **Deadline:** April 2, 2026, 11:59 PM ET (or when solved, whichever is first)

---

## 1. OVERALL STATUS

### MrBeast's Official Statements (Feb 9)
- **X/Twitter (Monday morning):** "No one has solved the $1,000,000 puzzle in our Super Bowl ad yesterday. For the record it's very hard and lots of steps. Good luck!"
- **Additional statement:** "No one is even close to winning it."
- **GMA appearance (Monday morning):** Gave the hint: **"Look for some numbers in photos that I took at the Super Bowl."**
- **Scale:** Approximately **60 million people** visited the contest website by Sunday night (Feb 8).
- **Technical issues:** Some users reported problems receiving "magic link" registration emails. Salesforce acknowledged this on X and said they were working on it with email providers.

### Key Takeaway
As of ~24 hours post-launch, the puzzle is firmly in its earliest stage. No public evidence of anyone having solved even a single sub-puzzle's extraction step (i.e., getting the actual answer word), let alone assembling the 9-word meta-clue.

---

## 2. PUZZLE ARCHITECTURE (CONFIRMED)

The following structure has been confirmed from Official Hint #1 (posted on mrbeast.salesforce.com) and corroborated by ARGNet's analysis:

### The Pipeline
1. **Super Bowl Ad ("The Vault")** -- 30-second commercial packed with frame-by-frame clues
2. **Bank Heist Teaser Video** -- Contains clues but REQUIRES content from the Super Bowl ad to solve
3. **9-Video Playlist** -- 9 past MrBeast videos, each with a pinned comment linking to an external sub-puzzle
4. **9 Sub-Puzzles** -- Each solved puzzle yields ONE WORD
5. **9-Word Meta-Clue** -- Word lengths: **5, 9, 5, 7, 8, 4, 9, 6, 5**
6. **Meta-Clue = INSTRUCTION** -- "defines the nature of the search" / "you'll take the first step on your journey"
7. **Follow the instruction** -- leads to a hidden code
8. **Slack the code** -- to Jimmy Donaldson via Salesforce Slackbot

### Critical Design Notes
- "Real, nonlinear, and interconnected" -- puzzles are NOT independent
- "Some of these puzzles use codes you can find online" -- standard cipher references
- The Super Bowl ad likely contains **extraction keys** for the playlist puzzles
- Solving a puzzle grid is only step 1; you still need to know **which cells to read**
- "There is a direct way through this ultra-hard puzzle hunt"
- Designed by **Lone Shark Games** (creators of puzzles for Wired, Cards Against Humanity, Planet Word Museum's Lexicon Lane)

---

## 3. CONFIRMED CLUES AND ASSETS

### A. Super Bowl Ad Visual Elements (Confirmed by Multiple Sources)
These symbols flash rapidly across the screen during the 30-second ad:
| Symbol | Description | Potential Meaning |
|--------|-------------|-------------------|
| Spider | Image of a spider | Unknown -- possibly web/net reference? |
| Sine wave | Mathematical wave pattern | Unknown -- frequency, oscillation? |
| Bird on a wire | Bird sitting on a wire | Unknown -- could reference music, telegraph? |
| Elephant | Image of an elephant | Unknown -- memory, size, ivory? |
| 10^5 | Mathematical notation | = 100,000 -- a number clue? |
| Red security lasers | Pattern of laser beams | Could form letters or a grid pattern |
| Computer screen formulas | Scientists' screens show formulas | Need OCR extraction |
| Codes on blast doors | Text/numbers on vault doors | Need OCR extraction |
| QR code | Aerial view of complex forms a QR code | Links to mrbeast.salesforce.com |
| Smoking device | MrBeast holds something smoking | "Is it a clue? I don't know" |

**From Hint #1:** "Almost everything Jimmy passes by is a clue. Look up, down, forward, backward, and behind the scenes. Figure out how to get an answer from each weird thing."

### B. Bank Heist Teaser Video Clues
| Element | Description | Status |
|---------|-------------|--------|
| "Red Herring Bank" name | The bank's name in the video | CONFIRMED RED HERRING (the name itself is the hint) |
| Barcode on armored tank | Tank receiving a parking violation has a barcode | NOT YET DECODED |
| Calendar dates | Bank teller's desk calendars have dates circled in red | NOT YET DECODED |
| Acrostic message | First letters of rapidly flashing text | Spells: "this means nothing I just wanted to waste your time lol" -- CONFIRMED RED HERRING |
| Pinned comment | Comment on this video | Links to the 9-video playlist (CRITICAL ENTRY POINT) |

**From Hint #1:** "In the bank, the same is true, but you will need specific content from the Super Bowl ad to solve anything there."

### C. Cryptic Sign Messages (from X/Twitter teaser)
**Message 1:** "First I am ash, hanging and burning and roasting and smoking. No condition. Just ash. Maybe exotic."

**Message 2:** "I can't see two eyes. Every breath an explosion. Time stopped. Beast. Every culture. You're in for a. Enter all of. Some are."

Status: NOT DECODED. Community has not publicly cracked these.

### D. Tonight Show Appearance (Feb 6, 2026)
MrBeast appeared on The Tonight Show with Jimmy Fallon two days before the Super Bowl. Multiple sources confirm clues may have been embedded in this appearance. **No specific clues from this appearance have been publicly identified yet.**

### E. MrBeast's GMA Hint (Feb 9)
**"Look for some numbers in photos that I took at the Super Bowl."**
- This directs solvers to MrBeast's social media photos (X/Twitter, Instagram) from the Super Bowl
- The numbers hidden in those photos are likely part of the puzzle
- **No one has publicly identified the numbers yet**

---

## 4. THE 9-VIDEO PLAYLIST -- KNOWN DETAILS

### Playlist URL
https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7

### Known Videos and Puzzle Assignments (from our repo)
| # | Folder Name | Video Topic | Puzzle Type | Status |
|---|-------------|-------------|-------------|--------|
| 1 | 01_wells_africa | Wells/Africa | Unknown | Not started |
| 2 | 02_lifechange | Changing the Lives of 600 Strangers | Sudoku variant (LIF(E)CHANGE) | GRID SOLVED, extraction unknown |
| 3 | 03_dirtiest_beach | Dirtiest beach | Unknown | Not started |
| 4 | 04_experiences | Experiences | Unknown | Not started |
| 5 | 05_pokemon_go | Pokemon Go | Unknown | Not started |
| 6 | 06_wilderness | Wilderness | Unknown | Not started |
| 7 | 07_adopted_dogs | Adopted dogs | Unknown | Not started |
| 8 | 08_pyramids | Pyramids | Unknown | Not started |
| 9 | 09_circle | Circle | Unknown | Not started |
| - | crossword | (Unknown which video) | Crossword puzzle | PDF downloaded, not yet solved |

### Puzzle #2 Detail: LIFECHANGE Sudoku
- **Reddit location:** https://www.reddit.com/user/BeastForce67/comments/1qxxmdn/puzzle/
- **Format:** 9x9 Sudoku grid using letters L, I, F, E, C, H, A, N, G (from "LIFECHANGE") instead of digits 1-9
- **Grid status:** SOLVED (with correction: F in Row 7 shifted from col 3 to col 2)
- **Extraction status:** UNKNOWN -- the completed grid alone is not the answer. Need to know which cells to read to get the 9-letter answer word (position 2 in the meta-clue).
- **From ARGNet:** "Solving that grid on its own doesn't lead to any additional instructions, but additional information on which letters to select from the completed grid might emerge through other parts of the campaign."

### Crossword Puzzle
- A "Million Dollar Crossword" PDF has been found and downloaded
- Not yet determined which playlist video this corresponds to
- Not yet solved

---

## 5. COMMUNITY ACTIVITY

### Reddit
- **r/MrBeast:** Megathreads and discussion threads have formed, though no public solutions emerged in the first 24 hours
- **u/BeastForce67:** Official puzzle-posting Reddit account. Posted the LIFECHANGE Sudoku variant. Should be monitored for additional puzzle posts.
- No publicly shared solved answer words found in search results

### Discord
- **Lone Shark Games Discord:** Has a dedicated channel for the Salesforce + MrBeast Million Dollar Puzzle (lonesharkgames.com/discord)
- **MrBeast Discord:** discord.com/invite/mrbeast -- active discussion
- **MrBeast Gaming Discord:** discord.com/invite/mrbeastgaming
- Multiple independent puzzle-solving Discord servers have formed
- **No public solution breakthroughs reported**

### Twitter/X
- MrBeast's original announcement: https://x.com/MrBeast/status/2020689211528253479
- Community actively analyzing frames, sharing screenshots, and debating theories
- Marc Benioff (Salesforce CEO) also posting about the puzzle: https://x.com/Benioff/status/2006517835175170178

### Streaming
- Streamers on Twitch and YouTube have launched dedicated puzzle-solving streams
- No breakthroughs reported from live streams

### ARGNet (Alternate Reality Gaming Network)
- Published the most detailed analytical breakdown of the puzzle structure
- URL: https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/
- Confirmed Lone Shark Games' involvement
- Provided the LIFECHANGE Sudoku example
- Noted the interconnected nature of the puzzles

### Game Detectives
- https://gamedetectives.net/ -- ARG community likely tracking this, but no specific page found in searches

---

## 6. HINT TIMELINE AND FUTURE HELP

### Confirmed Hint Schedule
- **Hint #1:** Already released (on mrbeast.salesforce.com) -- the one about 9-word clue structure and word lengths
- **24-hour mark:** If unsolved after 24 hours, another clue would be released (should be coming very soon or already out)
- **48-hour mark:** "More serious help" promised
- **Salesforce Slackbot:** Will eventually be activated to help people "solve certain parts of the puzzle" by answering questions and pointing people "in the right direction"
- **New clues dropping daily** across social media and future MrBeast videos

### Official Guidance
- "We're starting in hard mode on purpose. No walkthroughs, hints or next steps."
- "Clues are everywhere: videos, websites, and the real world."
- "Anytime you see MrBeast with Salesforce, assume there's something there."
- The puzzle was designed for collaboration: "it's probably not possible for one person to find and solve everything"

---

## 7. TECHNICAL / LOGISTICAL NOTES

### Registration Issues
Salesforce acknowledged that some registration emails were not being delivered due to the overwhelming volume (60M+ visitors). Their teams were working with major email providers to resolve this.

### Ad Production
The ad was produced in an unusually compressed **27-day timeline** (versus typical 6-month production), with AI assistance from Slackbot credited as accelerating the creative process between Salesforce and Beast Industries teams.

### Eligibility
- US, Canada, Mexico residents
- Age 18+
- Must register at mrbeast.salesforce.com
- Must submit answer via Slack

---

## 8. WHAT NO ONE HAS DONE YET (AS OF FEB 9)

Based on all available search results, the following have NOT been publicly accomplished by the community:

1. No one has decoded the Super Bowl ad symbols (spider, sine wave, bird, elephant, 10^5)
2. No one has identified the extraction method for any of the playlist puzzles
3. No one has extracted any of the 9 answer words
4. No one has assembled any part of the 9-word meta-clue
5. No one has decoded the barcode on the armored tank
6. No one has identified which dates are circled on the bank teller's calendars
7. No one has decoded the cryptic sign messages
8. No one has identified the "numbers in photos" from MrBeast's Super Bowl photos
9. No one has identified specific clues from the Tonight Show appearance
10. No one has identified all 9 puzzle types from the playlist pinned comments

---

## 9. OUR REPO'S CURRENT ADVANTAGE

Based on the session summaries in our repo, we have:
- The LIFECHANGE Sudoku grid SOLVED (ahead of most public solvers)
- All 4 hub video MP4s downloaded for frame-by-frame analysis
- All 12 subtitle files for hub + playlist videos
- All 14 metadata files (info.json) for all videos
- Crossword puzzle PDF and images downloaded
- Structured approach with 9 puzzle directories ready
- Comment extraction running (to get all pinned comment links)

---

## 10. RECOMMENDED NEXT STEPS

### Immediate Priority (Night of Feb 9)
1. **Check for Hint #2** -- should be dropping around the 24-hour mark (Mon evening)
2. **Extract all 9 pinned comment links** from playlist videos (comments download may have completed)
3. **Frame-by-frame analysis** of the Super Bowl ad -- identify all symbols and text via OCR
4. **Find MrBeast's Super Bowl photos** on X/Instagram and look for hidden numbers
5. **Solve the crossword puzzle** and determine which video it belongs to

### Short-Term (Feb 10-11)
6. **Identify all 9 puzzle types** and begin solving each one
7. **Decode the barcode** on the armored tank in the bank teaser
8. **OCR the calendar dates** from the bank teller's desk
9. **Analyze the Tonight Show appearance** for embedded clues
10. **Connect Super Bowl ad symbols** to extraction methods for the puzzles

### Medium-Term
11. **Extract answer words** from solved puzzles using discovered extraction keys
12. **Assemble the 9-word meta-clue**
13. **Follow the meta-clue instruction** to the next phase
14. **Discover the hidden code**

---

## SOURCES

All URLs referenced in this report:

### Official
- MrBeast x Salesforce Hub: https://mrbeast.salesforce.com/
- Terms & Conditions: https://mrbeast.salesforce.com/terms
- MrBeast X announcement: https://x.com/MrBeast/status/2020689211528253479

### News Coverage
- ABC News / GMA (MrBeast hint): https://abcnews.go.com/GMA/Culture/mrbeast-drops-big-hint-1m-puzzle-salesforce-super/story?id=129987912
- Newsweek (status update): https://www.newsweek.com/mrbeast-shares-update-on-1-million-puzzle-advertised-during-super-bowl-11490124
- Yahoo News (no one has won): https://ca.news.yahoo.com/mrbeast-confirms-nobody-won-1m-164714124.html
- Yahoo Exclusive (launch details): https://ca.news.yahoo.com/exclusive-mrbeast-launches-million-dollar-023026226.html
- Benzinga (how to participate): https://www.benzinga.com/markets/tech/26/02/50471320/mrbeast-says-first-person-to-crack-his-super-bowl-ad-puzzle-wins-1-million-heres-what-you-have-to-do
- IBTimes (community reaction): https://www.ibtimes.co.uk/mrbeast-drops-1-million-puzzle-during-super-bowl-internet-goes-wild-1777533
- FilmoGaz (puzzle structure): https://www.filmogaz.com/141896
- Stocktwits (Salesforce glitch): https://stocktwits.com/news-articles/markets/equity/salesforce-ties-up-with-mr-beast-for-a-million-dollar-super-bowl-stunt/cZbHspTR48V
- LBBOnline (ad analysis): https://lbbonline.com/news/mrbeast-super-bowl-puzzle-clues
- Startland News (KC artist in ad): https://www.startlandnews.com/2026/02/mrbeast-super-bowl-commercial/
- NTD (overview): https://www.ntd.com/million-dollars-up-for-grabs-in-salesforces-mrbeast-super-bowl-puzzle-ad_1124961.html
- SportBible: https://www.sportbible.com/nfl/mrbeast-super-bowl-puzzle-million-dollar-prize-371850-20260209
- LADbible: https://www.ladbible.com/news/sport/mrbeast-puzzle-super-bowl-advert-million-172203-20260209

### Puzzle Analysis
- ARGNet (best breakdown): https://www.argn.com/2026/02/start_slacking_off_with_mrbeasts_million_dollar_puzzle_hunt/
- Grand Pinnacle Tribune (launch): https://evrimagaci.org/gpt/mrbeast-and-salesforce-launch-million-dollar-puzzle-hunt-527833
- Grand Pinnacle Tribune (ignite): https://evrimagaci.org/gpt/mrbeast-and-salesforce-ignite-super-bowl-with-1-million-puzzle-527887
- Grand Pinnacle Tribune (hunt): https://evrimagaci.org/gpt/mrbeast-turns-super-bowl-ad-into-million-dollar-hunt-527875
- TheInfoHatch (guide): https://theinfohatch.com/mrbeast-million-dollar-puzzle-guide-2026/
- Streamer.Guide: https://streamer.guide/blog/mrbeast-salesforce-super-bowl-puzzle-2026
- Backyard Drunkard: https://backyarddrunkard.com/celebrity-news/mrbeast-million-dollar-puzzle-super-bowl/
- Oddschecker: https://www.oddschecker.com/us/insight/football/nfl/20260208-mr-beasts-$1-million-prize-code-slack-mrbeast-the-code-to-win-the-salesforce-big-game-prize

### Community & Collaboration
- Reddit BeastForce67 Sudoku puzzle: https://www.reddit.com/user/BeastForce67/comments/1qxxmdn/puzzle/
- Lone Shark Games Discord: https://lonesharkgames.com/discord/
- MrBeast Discord: https://discord.com/invite/mrbeast
- MrBeast Gaming Discord: https://discord.com/invite/mrbeastgaming
- Game Detectives: https://gamedetectives.net/
- MrBeast Wiki (Fandom): https://mrbeast.fandom.com/wiki/MrBeast_Riddle

### YouTube
- 9-Video Playlist: https://www.youtube.com/playlist?list=PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7
- Bank Heist Teaser: https://www.youtube.com/watch?v=OBQELGS13XA
- Slack BTS Video: https://www.youtube.com/watch?v=rKg5OZNM1aU
- Marc Benioff X post: https://x.com/Benioff/status/2006517835175170178

### Social Media
- MrBeast TikTok teaser: https://www.tiktok.com/@mrbeast/video/7596006307111390495
- MrBeast Instagram (Freleng Door Gag): https://www.instagram.com/p/DURNPK6Eear/
- Salesforce Instagram: https://www.instagram.com/p/DUZAR6YiaYs/
- iSpot (ad analytics): https://www.ispot.tv/ad/gOWo/salesforce-super-bowl-2026-pre-release-the-vault-featuring-mrbeast

---

*Report compiled from 20+ web searches across news, community, and analysis sources. No community-compiled solution wiki or comprehensive tracker was found -- this likely reflects Day 1 status where everyone is still in the exploration phase.*
