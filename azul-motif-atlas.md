# Azul Motif Atlas

A pattern-recognition companion to the 1v1 strategy guide. Each motif is a named strategic situation that recurs in competitive Azul. Learn to see these patterns and your move quality will improve faster than memorizing abstract rules.

## How to use this document

1. Read the position carefully.
2. Choose your move before reading the answer.
3. Check whether the motif's rule explains your reasoning.
4. Note when the rule fails — edge cases build real understanding.

> **Notation Key:**
> - **Colors:** 🟦 Blue | 🟨 Yellow | 🟥 Red | ⬛ Black | ⬜ White
> - **Wall Grid:** Color emoji (🟦🟨🟥⬛⬜) = placed tile | ◽ = empty wall slot
> - **Pattern Lines:** `[◽]` = open slot | `[🟦]` = filled tile slot

---

# Strategic Families & Learning Path

The 12 motifs are organized into four strategic families across three difficulty tiers:

### 1. Flexibility
- **Last Home** `[Core]` — Identify colors with only one legal row left.
- **Traffic Jam** `[Intermediate]` — Detect capacity collisions across shared rows.
- **Row-5 Sacrifice** `[Advanced]` — Pay floor points to preserve emergency buffer capacity.

### 2. Draft Control
- **Poison Spill** `[Core]` — Evaluate factory picks by what they dump into the center.
- **Contested Color** `[Core]` — Compare visible supply against total committed demand.
- **Poisoned Turn** `[Core]` — Control turn order when all remaining picks are bad.
- **Marker Price** `[Intermediate]` — Price first-player initiative against marginal floor cost.

### 3. Tactical Value
- **Double-Duty Move** `[Core]` — Prefer moves that score for you AND deny opponent.
- **Forced Response** `[Intermediate]` — Create forcing threats that demand immediate answers.

### 4. Wall & Endgame
- **Cross / Bridge** `[Intermediate]` — Build wall tiles that connect and create future hooks.
- **Close the Door** `[Core]` — Trigger game end when projected final score is winning.
- **Zero-Floor Discount** `[Advanced]` — Exploit the zero score bound for free floor penalties.

---

# Family 1: Flexibility

## Motif: Last Home `[Core]`

**Rule:** Before placing a flexible color, check which colors have only one legal pattern line left.

**When it matters:** Mid-to-late game when your wall starts filling up and legal line choices become restricted.

---

### Position 1

```text
Wall Grid:           Pattern Lines:       Options Available:
◽ ◽ ◽ ⬛ ◽       1: [◽]               Factory 1: 3🟨, 1⬛
◽ ◽ ◽ ◽ ⬛       2: [◽][◽]            Center: 1🟥
⬛ ◽ ◽ ◽ ◽       3: [◽][◽][◽]
◽ ⬛ ◽ ◽ ◽       4: [🟥][🟥][🟥][◽]
◽ ◽ ◽ ◽ ◽       5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. 3🟨 to Line 5  
B. 3🟨 to Line 3  
C. 1⬛ to Line 1  

**Answer:** B

**Why:** Look at your Wall Grid. Black (⬛) is already placed in Row 1 (Col 4), Row 2 (Col 5), Row 3 (Col 1), and Row 4 (Col 2). Therefore, **Row 5 is Black's ONLY legal home on your board**. Yellow (🟨) is unplaced everywhere and has 4 legal open rows (Rows 1, 2, 3, 5). If you put 3🟨 into Line 5, you destroy Black's last home, making future Black tiles unplaceable and forcing them to your floor. Place flexible 3🟨 into Line 3 and save Line 5 for fragile Black.

**When the rule fails:** If all remaining Black tiles are already accounted for in the discard/lid and cannot appear this round.

---

### Position 2

```text
Wall Grid:           Pattern Lines:       Options Available:
◽ ◽ 🟥 ⬛ ◽       1: [◽]               Factory 1: 2⬜, 2🟥
◽ ◽ ◽ 🟥 ⬛       2: [◽][◽]            Center: 4🟦
⬛ ◽ ◽ ◽ 🟥       3: [◽][◽][◽]
◽ ⬛ ◽ ◽ ◽       4: [◽][◽][◽][◽]
◽ ◽ ◽ ◽ ◽       5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. 2⬜ to Line 5  
B. 2⬜ to Line 2  
C. 2🟥 to Line 5  

**Answer:** B

**Why:** Black (⬛) is placed in Rows 1, 2, 3, 4, leaving Row 5 as Black's sole legal home. Red (🟥) is placed in Rows 1, 2, 3, leaving Rows 4 and 5 legal. White (⬜) has Rows 1, 2, 4, 5 open. If you take 2⬜ to Line 5, you consume Black's only remaining home. Taking 2⬜ to Line 2 preserves Line 5 for Black and Line 4 for Red.

**When the rule fails:** If taking Line 5 with White completes a column bonus that guarantees an immediate win.

---

## Motif: Traffic Jam `[Intermediate]`

**Rule:** When multiple constrained colors need the same pattern line, your board is less flexible than it appears.

**When it matters:** Rounds 3–4 when pattern lines fill up and remaining open lines are competing for the same destinations.

---

### Position 1

```text
Wall Grid:           Pattern Lines:       Options Available:
🟦 🟨 🟥 ⬛ ◽       1: [◽]               Factory 1: 3⬛, 1⬜
⬜ 🟦 🟨 🟥 ◽       2: [◽][◽]            Factory 2: 3🟥, 1🟦
⬛ ⬜ 🟦 🟨 ◽       3: [◽][◽][◽]
◽ ◽ ◽ ◽ ◽       4: [◽][◽][◽][◽]
◽ ◽ ◽ ◽ ◽       5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. 3⬛ to Line 4  
B. 3⬛ to Line 3  
C. 1🟦 to Line 4  

**Answer:** B

**Why:** Look at your legal destinations. Blue (🟦) and Yellow (🟨) are placed in Rows 1, 2, and 3. Therefore, Blue and Yellow can ONLY go into Row 4 or Row 5. They are bottlenecked together into Rows 4 and 5. Black (⬛) is placed in Rows 1 and 3, meaning Row 2 and Row 4 are legal for Black. If you put Black into Line 4, you consume one of the only two rows Blue and Yellow can use, causing a disastrous traffic jam later. Put 3⬛ into Line 3 (or Line 2) to keep Lines 4 and 5 open for Blue and Yellow.

**When the rule fails:** If you are actively trying to end the game on this round and future board flexibility does not matter.

---

### Position 2

```text
Wall Grid:           Pattern Lines:       Options Available:
🟦 🟨 🟥 ◽ ◽       1: [◽]               Factory 1: 3⬛, 1🟨
⬜ 🟦 🟨 ◽ ◽       2: [◽][◽]            Factory 2: 2🟥, 2⬜
⬛ ⬜ 🟦 ◽ ◽       3: [◽][◽][◽]
◽ ◽ ◽ ◽ ◽       4: [◽][◽][◽][◽]
◽ ◽ ◽ ◽ ◽       5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. 3⬛ to Line 4  
B. 3⬛ to Line 3  
C. 1🟨 to Line 1  

**Answer:** B

**Why:** Red (🟥), Black (⬛), and White (⬜) are all constrained to Rows 4 and 5 because Rows 1–3 already contain them or are full. If you put Black into Line 4, you leave only Line 5 for both Red and White. Putting 3⬛ in Line 3 preserves Lines 4 and 5 for Red and White.

**When the rule fails:** When an immediate denial move takes higher priority than long-term capacity preservation.

---

## Motif: Row-5 Sacrifice `[Advanced]`

**Rule:** Sometimes paying a small floor penalty is cheaper than consuming your emergency row-5 buffer.

**When it matters:** When Row 5 is your only remaining empty pattern line and major color floods threaten to hit the center.

---

### Position 1

```text
Wall Grid:           Pattern Lines:       Options Available:
🟦 🟨 🟥 ⬛ ⬜       1: [⬜]               Center: 2⬛
⬜ 🟦 🟨 🟥 ⬛       2: [🟦][🟦]            Factory 1: 3🟨, 1🟥
⬛ ⬜ 🟦 🟨 🟥       3: [🟨][🟨][🟨]
🟥 ⬛ ⬜ 🟦 🟨       4: [🟥][🟥][🟥][🟥]
◽ ◽ ◽ ◽ ◽       5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. Take 2⬛ from Center to Line 5  
B. Take 2⬛ from Center to Floor (-2 pts)  
C. Take 3🟨 from Factory 1 to Line 5  

**Answer:** B

**Why:** Lines 1–4 are completely full. Row 5 is your ONLY open pattern line on the entire board. Center has 2⬛, but Factory 1 has 3🟨 and more Yellow is coming. If you place 2⬛ into Line 5, Line 5 becomes locked to Black. Any future Yellow or Red tiles drafted will be forced to the floor (-8 or -11 pts). Taking -2 points on the floor for 2⬛ keeps Line 5 completely uncommitted as a 5-tile emergency buffer.

**When the rule fails:** If no other color floods are possible and Black can complete Row 5 for a guaranteed wall placement.

---

### Position 2

```text
Wall Grid:           Pattern Lines:       Options Available:
🟦 🟨 🟥 ⬛ ◽       1: [◽]               Center: 3🟥
⬜ 🟦 🟨 🟥 ⬛       2: [◽][◽]
⬛ ⬜ 🟦 🟨 🟥       3: [◽][◽][◽]
🟥 ⬛ ⬜ 🟦 🟨       4: [🟦][🟦][🟦][◽] (Reserved for Blue)
◽ ◽ ◽ ◽ ◽       5: [◽][◽][◽][◽][◽] (Empty Buffer)
```

**What would you take?**

A. 3🟥 from Center to Line 5  
B. 3🟥 from Center to Floor (-4 pts)  
C. Take starting player marker  

**Answer:** B

**Why:** Line 4 is your Last Home for Blue (`[🟦][🟦][🟦][◽]`). Red (🟥) is placed in Rows 1, 2, 3, 4, so Red's ONLY legal line is Row 5. However, 5 Black (⬛) tiles are in Factory 2 and opponent is about to spill them into center. If you put 3🟥 in Line 5, your absorption capacity for Black becomes A(c)=0, forcing 5 Black to your floor (-11 pts). Paying -4 pts now to drop 3🟥 to floor leaves Line 5 open to absorb the 5 Black tiles, saving 7 net points.

**When the rule fails:** If your score is too low to absorb a -4 floor penalty without hitting 0 early.

---

# Family 2: Draft Control

## Motif: Poison Spill `[Core]`

**Rule:** Choose factories by what they dump into the center, not just what they give you.

**When it matters:** Whenever a factory pick will send 2+ tiles into the common center pool.

---

### Position 1

```text
Opponent Board:      Center: Empty        Options Available:
Absorption capacity                       Factory 1: 1🟦, 3🟥
A_opp(Red) = 1                            Factory 2: 1🟦, 1🟨, 2⬜
(Lines 2-5 locked)
```
*Your board needs 1🟦 for Line 1.*

**What would you take?**

A. 1🟦 from Factory 1 (spills 3🟥 to center)  
B. 1🟦 from Factory 2 (spills 1🟨, 2⬜ to center)  
C. 3🟥 from Factory 1  

**Answer:** A

**Why:** Both factories give you the 1🟦 you need. But Factory 1 spills 3🟥 into the center. Opponent has A_opp(Red) = 1, so spilling 3🟥 forces them to take at least 2 Red onto their floor (-2 pts minimum) on a future turn. Factory 2 spills safe tiles that opponent can absorb for free.

**When the rule fails:** If the spilled 3🟥 allows opponent to complete a high-value column bonus.

---

### Position 2

```text
Opponent Board:      Center: Empty        Options Available:
A_opp(Black) = 0                          Factory 1: 1🟥, 3⬛
A_opp(Yellow) = 4                         Factory 2: 1🟥, 3🟨
```
*Your Line 4 needs 1🟥 (`[🟥][🟥][🟥][◽]`).*

**What would you take?**

A. 1🟥 from Factory 1 (spills 3⬛ to center)  
B. 1🟥 from Factory 2 (spills 3🟨 to center)  
C. 3⬛ from Factory 1  

**Answer:** A

**Why:** Both choices complete your Line 4 with 1🟥. Factory 1 spills 3⬛ into center. Opponent has zero legal capacity for Black (A_opp(Black) = 0), so all 3⬛ will go straight to their floor (-4 pts). Factory 2 spills 3🟨 which opponent can absorb for free into Line 4.

**When the rule fails:** If opponent can draft the 1-marker first and force the 3⬛ back onto your floor.

---

## Motif: Contested Color `[Core]`

**Rule:** Before delaying a pickup, check if visible supply is less than total committed demand.

**When it matters:** Early in the round when mapping out how to fill 3–5 tile pattern lines.

---

### Position 1

```text
Visible Red (🟥): 3 tiles across factories
Your Demand: 2🟥 for Line 2 ([◽][◽])
Opponent Demand: 2🟥 for Line 3 ([🟥][◽][◽])
Total Demand (4🟥) > Total Supply (3🟥)  → CONTESTED
```

**What would you take?**

A. Draft 2🟥 from Factory 1 immediately  
B. Draft 3⬜ from Factory 2 to complete Line 3 first  
C. Take starting player marker  

**Answer:** A

**Why:** Red is **contested** (S(Red) = 3 < D(Red) = 4). There is not enough Red for both players to finish their lines. If you delay and take White, opponent will draft 2🟥 on their turn, leaving you unable to complete Line 2 this round.

**When the rule fails:** If completing Line 3 with White scores +8 points and seals a column bonus immediately.

---

### Position 2

```text
Visible Yellow (🟨): 7 tiles across factories
Your Demand: 2🟨 for Line 2 ([◽][◽])
Opponent Demand: 0🟨 (Yellow on wall in all open lines)
Total Supply (7🟨) >> Total Demand (2🟨)  → UNCONTESTED
```

**What would you take?**

A. Draft 2🟨 from Factory 1 immediately  
B. Draft 1⬛ from Factory 1 to deny opponent's Line 1, delaying Yellow  
C. Draft 3🟨 from Factory 2  

**Answer:** B

**Why:** Yellow is **abundant and uncontested** (S=7 >> D=2, opponent cannot legally take Yellow). Yellow is 100% safe to delay. Take 1⬛ now to deny opponent's pick; the Yellow tiles will still be waiting for you later.

**When the rule fails:** If delaying Yellow allows opponent to merge Yellow into a massive 6-tile center pile.

---

## Motif: Poisoned Turn `[Core]`

**Rule:** When remaining groups are ugly, stop maximizing what you take and start controlling who is on move for each bad group.

**When it matters:** Late round when only unwanted or overflow-causing color groups remain.

---

### Position 1

```text
Center Pool: 3 separate color groups (3⬛, 3🟨, 1🟥)
Your Line 1: open [◽] (can absorb 1🟥)
Your Capacities: A_you(Black)=0, A_you(Yellow)=0, A_you(Red)=1
Opponent Capacities: A_opp(Black)=0, A_opp(Yellow)=0, A_opp(Red)=0
```

**What would you take?**

A. Draft 1🟥 from Center to Line 1  
B. Draft 3⬛ from Center to Floor (-4 pts)  
C. Draft 3🟨 from Center to Floor (-4 pts)  

**Answer:** A

**Why:** There are 3 color groups left in center. By taking 1🟥 now (which you absorb cleanly into Line 1), exactly 2 bad groups remain (3⬛ and 3🟨). Opponent MUST take one of the bad 3-tile groups on their turn (-4 floor pts). Then you take the remaining bad group (-4 floor pts). If you took a 3-tile group first, opponent would snatch 1🟥 for free and leave you to take BOTH bad groups (-8 pts total)!

**When the rule fails:** If opponent can take the 1-marker instead of a 3-tile group to shift parity back onto you.

---

### Position 2

```text
Center Pool: 3🟥
Factory 1: 2🟦, 2🟥
Your Line 4 needs 1🟥 ([🟥][🟥][🟥][◽])
Opponent Capacities: A_opp(Red) = 1
```

**What would you take?**

A. Draft 2🟦 from Factory 1  
B. Draft 2🟥 from Factory 1  
C. Draft 3🟥 from Center  

**Answer:** B

**Why:** If you take 2🟦 from Factory 1, its 2🟥 spills into center, merging with 3🟥 to form a single 5🟥 pile. That collapses two color groups into one, giving opponent the initiative to force 5🟥 onto your floor. Taking 2🟥 directly from Factory 1 completes your Line 4 and leaves center manageable.

**When the rule fails:** If taking 2🟦 completes a row that triggers game end in your favor.

---

## Motif: Marker Price `[Intermediate]`

**Rule:** Price first-player initiative against its exact marginal floor cost.

**When it matters:** Mid-to-late game when deciding whether to grab the starting player marker from center.

---

### Position 1

```text
Current Floor: 2 tiles already filled (-2 pts)
Marker Slot: Slot 3 (-2 pts marginal cost)
Subsequent Floor Tile: Slot 4 (-2 pts marginal cost)
Next Round Priorities: No high-value incomplete long lines on your board.
```

**What would you take?**

A. Take First Player Marker from Center (-2 pts)  
B. Take 2🟦 from Factory 1 to Line 2  
C. Take 3🟨 from Factory 2 to Line 3  

**Answer:** B

**Why:** Your floor already has 2 tiles (-2 pts). Grabbing the marker puts it in Slot 3 (-2 pts). If you overflow even one tile later, that tile moves to Slot 4 (-2 pts), making the marker's true marginal cost -4 points. Since you have no urgent first-pick target next round, paying -4 floor points for initiative is an overpay.

**When the rule fails:** If next round's bag draw is known to contain the final tile needed for a +10 color bonus.

---

### Position 2

```text
Current Floor: 0 tiles filled (-0 pts)
Marker Slot: Slot 1 (-1 pt marginal cost)
Your Line 5: [🟦][🟦][🟦][🟦][◽] (needs 1🟦 for a 15-pt placement)
Bag State: Only 3 Blue tiles remain in the bag for next round's draw.
```

**What would you take?**

A. Take First Player Marker from Center (-1 pt)  
B. Take 2🟨 from Factory 1 to Line 2  
C. Take 1⬜ from Factory 2 to Line 1  

**Answer:** A

**Why:** The marker costs only -1 floor point. It guarantees you get first pick next round to secure one of the 3 remaining Blue tiles, locking in your 15-point Row 5 completion before opponent can steal it. Initiative is worth far more than 1 point here.

**When the rule fails:** If opponent can complete a 20-point wall cascade this round while you spend a turn on the marker.

---

# Family 3: Tactical Value

## Motif: Double-Duty Move `[Core]`

**Rule:** Prefer moves that solve two strategic problems at once: score for your board AND deny your opponent.

**When it matters:** Every turn during candidate selection.

---

### Position 1

```text
Your Line 3: [🟨][🟨][◽] (needs 1🟨 for +6 wall placement)
Opponent Line 4: [🟨][🟨][🟨][◽] (needs 1🟨 for +7 Column Bonus)
Factory 1: 1🟨, 3⬛
```

**What would you take?**

A. Draft 1🟨 from Factory 1 to Line 3  
B. Draft 3🟦 from Center to Line 4 for +2 pts  
C. Draft 3⬛ from Factory 1 to Floor (-4 pts) to block  

**Answer:** A

**Why:** Drafting 1🟨 does double duty! It completes your Line 3 for a +6 wall placement AND steals the exact single 🟨 opponent needs for their +7 column bonus. Double-duty moves produce massive point swings (+13 margin effect) without taking floor penalties or wasting turns.

**When the rule fails:** If taking 3🟦 from Center triggers an immediate game end when you are leading.

---

### Position 2

```text
Your Line 2: [◽][◽] (needs 2🟦)
Opponent Board: A_opp(Red) = 0
Factory 1: 2🟦, 2🟥
```

**What would you take?**

A. Draft 2🟦 from Factory 1 to Line 2  
B. Draft 2🟥 from Factory 1 to Floor (-2 pts)  
C. Take starting player marker  

**Answer:** A

**Why:** Drafting 2🟦 fills your Line 2 (+3 pts) AND spills 2🟥 into center. Opponent has A_opp(Red) = 0, forcing the 2🟥 directly onto their floor (-2 pts). Net swing: +5 points in one move.

**When the rule fails:** If opponent can absorb Red into a newly opened Line 5.

---

## Motif: Forced Response `[Intermediate]`

**Rule:** Look for moves where ignoring your threat creates large immediate regret, forcing your opponent to react and surrender initiative.

**When it matters:** When you want to dictate opponent moves rather than react to theirs.

---

### Position 1

```text
Center Pool: 4🟥
Opponent Line 1: open [◽] (A_opp(Red) = 1)
Factory 1: 1🟨, 2🟥
Your Line 3: open [◽][◽][◽]
```

**What would you take?**

A. Draft 1🟨 from Factory 1 to Line 3 (spills 2🟥 to center)  
B. Draft 4🟥 from Center to Floor (-6 pts)  
C. Draft 1🟥 from Center to Line 1  

**Answer:** A

**Why:** Drafting 1🟨 spills 2🟥 into center, swelling the Red pile to 6🟥! Opponent has A_opp(Red) = 1. If opponent ignores this threat on their next turn, taking 6🟥 later will force 5 Red to their floor (-8 pts). Opponent is **forced** to react immediately by drafting 1🟥 to Line 1 to reduce exposure, giving up their planned scoring pick.

**When the rule fails:** If opponent can take the 1-marker and force the 6🟥 back onto your floor.

---

### Position 2

```text
Your Board: Line 1 complete ([🟦]), Line 2 complete ([🟨][🟨]), Line 3 complete ([🟥][🟥][🟥])
Current Score: You 38, Opponent 30 (+8 lead)
Line 4: [⬛][⬛][⬛][◽] (1⬛ completes Row 4 and triggers game end)
Factory 1: 1⬛, 3⬜
```

**What would you take?**

A. Draft 1⬛ from Factory 1 to Line 4  
B. Draft 3⬜ from Factory 1 to Line 3  
C. Take starting player marker  

**Answer:** A

**Why:** Drafting 1⬛ completes Line 4, placing a tile in Row 4 to complete a horizontal row and trigger game end. Since you lead 38 to 30 with superior wall bonuses, threatening immediate game end forces opponent into damage-control mode.

**When the rule fails:** If opponent has a secret +10 color bonus that activates upon game end and passes your score.

---

# Family 4: Wall & Endgame

## Motif: Cross / Bridge `[Intermediate]`

**Rule:** A good wall tile scores twice: once when placed, and again by creating future scoring hooks.

**When it matters:** Early-to-mid game wall placement decisions.

---

### Position 1

```text
Wall Grid:
◽ ◽ ◽ ◽ ◽
◽ ⬜ 🟦 ◽ ◽    (Row 2 Col 2 & 3 placed)
◽ ◽ ◽ ◽ ◽    (Row 3 Col 2 & 3 empty)
◽ 🟥 ⬛ ◽ ◽    (Row 4 Col 2 & 3 placed)
◽ ◽ ◽ ◽ ◽

Target Placement Options for Row 3:
Choice A: Place at Row 3 Col 2 (⬜) -> connects (2,2) ⬜ and (4,2) 🟥 vertically!
Choice B: Place at Row 1 Col 5 (⬜) -> isolated placement.
```

**What pattern line do you fill?**

A. Fill Line 3 with White (⬜) to place at (3,2)  
B. Fill Line 1 with White (⬜) to place at (1,5)  
C. Fill Line 5 with White (⬜)  

**Answer:** A

**Why:** Placing White at (3,2) on Row 3 forms a **bridge** between (2,2) ⬜ and (4,2) 🟥! It scores 3 points vertically immediately AND creates 4 future scoring hooks (left, right, up, down) for surrounding tiles. Placing at (1,5) scores only 1 point with 1 hook.

**When the rule fails:** If completing Line 1 takes 1 turn while Line 3 takes 3 turns and you need quick points.

---

### Position 2

```text
Wall Grid:
◽ ◽ ◽ ◽ ◽
◽ ◽ 🟨 ◽ ◽    (Row 2 Col 3 placed)
◽ ◽ ◽ ◽ ◽    (Row 3 Col 3 empty)
◽ ◽ ⬜ ◽ ◽    (Row 4 Col 3 placed)
◽ ◽ ◽ ◽ ◽
```

**What pattern line do you fill?**

A. Fill Line 3 with Blue (🟦) to place at (3,3)  
B. Fill Line 1 with Blue (🟦) to place at (1,1)  
C. Fill Line 5 with Blue (🟦)  

**Answer:** A

**Why:** Row 3 Col 3 is Blue (🟦). Placing Blue at (3,3) bridges (2,3) 🟨 and (4,3) ⬜ into a 3-tile vertical column (+3 pts) plus horizontal connections (+2 pts) = 5 points total! It transforms two isolated tiles into a high-scoring cluster.

**When the rule fails:** If Blue is needed to block opponent's Line 5 completion.

---

## Motif: Close the Door `[Core]`

**Rule:** If ending now gives you a winning projected final score (wall + floor + bonuses), close the door. If ending loses and another round offers comeback value, keep it open.

**When it matters:** Rounds 4–5 when a horizontal row completion is possible.

---

### Position 1

```text
Current Score: You 42, Opponent 38 (+4 lead)
Line 3: [🟨][🟨][🟨] (Complete! Will place tile in Row 3 to finish horizontal row)
Projected Endgame Audit:
- Wall Tiling Phase: You +5, Opponent +4
- Bonuses: You +2 (1 Row), Opponent +7 (1 Column)
- Floor: You 0, Opponent -1
- Projected Final Score: YOU 49, OPPONENT 48  (YOU WIN BY 1)
```

**What do you do?**

A. Complete Row 3 and trigger game end  
B. Intentionally dump Line 3 to floor to extend game  
C. Delay wall placement  

**Answer:** A

**Why:** Your projected final score after wall tiling and end-game bonuses is **49 to 48 in your favor**. Even though opponent gets a +7 column bonus, you still win by 1 point. Triggering game end now locks in your victory before opponent can build more bonuses next round.

**When the rule fails:** If an uncounted floor penalty drops your projected total below 48.

---

### Position 2

```text
Current Score: You 35, Opponent 40 (-5 behind)
Line 1: [🟦] (Complete! Placing in Row 1 triggers game end)
Projected Endgame Audit if Game Ends Now:
- You score +6 wall pts -> Final: 41
- Opponent scores +9 wall/bonus pts -> Final: 49  (YOU LOSE BY 8)
If Game Extends to Round 5:
- You have Line 4 & Line 5 set up for +14 points; Opponent has no long lines.
```

**What do you do?**

A. Trigger game end now with Line 1  
B. Intentionally delay completing Line 1 to keep game open for Round 5  
C. Draft floor tiles  

**Answer:** B

**Why:** Ending the game now results in a projected loss (41 to 49). Current score lead is not the decision metric — **projected final score** is. Keeping the door open gives you Round 5 where your superior Line 4/5 setup can generate a +14 point comeback.

**When the rule fails:** If opponent will complete a full color bonus (+10) in Round 5.

---

## Motif: Zero-Floor Discount `[Advanced]`

**Rule:** Once your already-committed floor loss will reduce your post-wall score to zero, additional floor penalties up to that same zero bound have zero marginal scoreboard cost.

**When it matters:** Rounds 1–2 when scores are low and heavy floor penalties are being taken.

---

### Position 1

```text
Score before Round 1 Tiling: 0 pts
Expected Wall Scoring this round: +2 pts
Current Floor Status: 3 tiles filled (-4 floor pts: -1, -1, -2)
Net Score Calculation: 2 wall pts - 4 floor pts = -2 → Bounded at 0 pts (Score cannot drop below 0!)

Tactical Opportunity:
Factory 1 has 2⬛. Opponent needs 1⬛ for a +7 Column Bonus.
Taking 2⬛ to Floor adds 2 floor tiles (-2 pts each = -4 pts, total floor -8 pts).
New Net Score: 2 wall pts - 8 floor pts = -6 → STILL Bounded at 0 pts!
Marginal Scoreboard Cost of the 2 additional floor tiles = 0 POINTS!
```

**What would you take?**

A. Take 2⬛ from Factory 1 to Floor to deny opponent's +7 Column Bonus  
B. Take 2🟨 from Factory 2 to Line 2  
C. Take starting player marker  

**Answer:** A

**Why:** Because your score is already hitting the 0 floor bound (-2 rounds up to 0), taking 2 additional floor tiles has **zero marginal cost on the scoreboard** (-6 also rounds up to 0!). You deny opponent a +7 column bonus for ZERO actual point loss to yourself.

**When the rule fails:** If your wall scoring this round unexpectedly produces +9 points instead of +2.

---

### Position 2

```text
Score before Tiling: 1 pt
Expected Wall Scoring: +3 pts (Total before floor: 4 pts)
Current Floor Status: 4 tiles filled (-6 floor pts: -1, -1, -2, -2)
Net Score: 4 - 6 = -2 → Bounded at 0 pts.

Available Pick: Center has 2 Red tiles. Taking them adds 2 floor tiles (Slot 5: -2, Slot 6: -3 = -5 pts).
Total Floor: -11 pts. New Net Score: 4 - 11 = -7 → STILL Bounded at 0 pts!
```

**What would you take?**

A. Take 2 Red to Floor to deny opponent's Row 4 completion  
B. Take safe 1 White to Line 1  
C. Take starting player marker  

**Answer:** A

**Why:** Your post-wall score (4 pts) is already completely wiped out by your existing -6 floor penalty (bounded at 0). Adding -5 more floor points changes your net calculation from -2 to -7, but both result in **0 points on the scoreboard**. The denial move is 100% free.

**When the rule fails:** In later rounds (R3–5) when you have built up a bank of points above zero.

---

# Motif Checklist

Use this quick-reference checklist during games until pattern recognition becomes automatic:

### 1. Flexibility
- [ ] **Last Home** — Is any color down to its sole remaining legal row?
- [ ] **Traffic Jam** — Are multiple constrained colors competing for the same open row?
- [ ] **Row-5 Sacrifice** — Is paying a small floor penalty cheaper than locking Row 5?

### 2. Draft Control
- [ ] **Poison Spill** — What toxic tiles does this factory dump into the center?
- [ ] **Contested Color** — Is visible supply less than total committed demand?
- [ ] **Poisoned Turn** — Who gets stuck with the move when remaining groups are ugly?
- [ ] **Marker Price** — What is the marker's true marginal floor cost vs. initiative value?

### 3. Tactical Value
- [ ] **Double-Duty** — Does any move score for your board AND deny your opponent?
- [ ] **Forced Response** — Can you create a threat that forces an immediate opponent reaction?

### 4. Wall & Endgame
- [ ] **Cross / Bridge** — Does this wall tile connect existing tiles and create future hooks?
- [ ] **Close the Door** — Does triggering game end now yield a winning projected final score?
- [ ] **Zero-Floor Discount** — Is your score low enough that extra floor tiles cost 0 points?
