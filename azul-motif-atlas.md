# Azul Motif Atlas

A pattern-recognition companion to the 1v1 strategy guide. Each motif is a named strategic situation that recurs in competitive Azul. Learn to see these patterns and your move quality will improve faster than memorizing abstract rules.

## How to use this document

1. Read the position carefully.
2. Choose your move before reading the answer.
3. Check whether the motif's rule explains your reasoning.
4. Note when the rule fails — edge cases build real understanding.

> **Notation Key:**
> - **Colors:** 🟦 Blue (b) | 🟨 Yellow (y) | 🟥 Red (r) | ⬛ Black (k) | ⬜ White (w)
> - **Wall Grid:** Color emoji (🟦🟨🟥⬛⬜) = placed tile | Lowercase letter (b y r k w) = empty wall slot
> - **Pattern Lines:** `[◽]` = open slot | `[🟦]` = filled tile slot

---

# Strategic Families & Learning Path

The 11 motifs are organized into four strategic families across three difficulty tiers:

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
b  y  r  ⬛  w       1: [◽]               Factory 1: 3🟨, 1⬛
w  b  y  r  ⬛       2: [◽][◽]            Center: 1🟥
⬛  w  b  y  r       3: [◽][◽][◽]
r  ⬛  w  b  y       4: [🟥][🟥][🟥][◽]
y  r  k  w  b       5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. 3🟨 to Line 5  
B. 3🟨 to Line 3  
C. 1🟥 from Center → Line 1  

**Answer:** B

**Why:** Look at your Wall Grid. Black (⬛) is already placed in Row 1 (Col 4), Row 2 (Col 5), Row 3 (Col 1), and Row 4 (Col 2). Therefore, **Row 5 is Black's ONLY legal home on your board**. Yellow (🟨) is unplaced everywhere and has 4 legal open rows (Rows 1, 2, 3, 5). If you put 3🟨 into Line 5, you destroy Black's last home, making future Black tiles unplaceable and forcing them to your floor. Place flexible 3🟨 into Line 3 and save Line 5 for fragile Black.

**When the rule fails:** If all remaining Black tiles are already accounted for in the discard/lid and cannot appear this round.

---

### Position 2

```text
Wall Grid:           Pattern Lines:       Options Available:
b  y  🟥  ⬛  w       1: [◽]               Factory 1: 2⬜, 2🟥
w  b  y  🟥  ⬛       2: [◽][◽]            Center: 4🟦
⬛  w  b  y  🟥       3: [◽][◽][◽]
r  ⬛  w  b  y       4: [◽][◽][◽][◽]
y  r  k  w  b       5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. 2⬜ to Line 5  
B. 2⬜ to Line 2  
C. 2🟥 to Line 5  

**Answer:** B

**Why:** Black (⬛) is placed in Rows 1, 2, 3, 4, leaving Row 5 as Black's sole legal home. Red (🟥) is placed in Rows 1, 2, 3, leaving Rows 4 and 5 legal. White is legal in every row and is therefore highly flexible. If you take 2⬜ to Line 5, you consume Black's only remaining home. Taking 2⬜ to Line 2 preserves Line 5 for Black and Line 4 for Red.

**When the rule fails:** If taking Line 5 with White completes a column bonus that guarantees an immediate win.

---

## Motif: Traffic Jam `[Intermediate]`

**Rule:** When multiple constrained colors need the same pattern line, your board is less flexible than it appears.

**When it matters:** Rounds 3–4 when pattern lines fill up and remaining open lines are competing for the same destinations.

---

### Position 1

```text
Wall Grid:           Pattern Lines:       Options Available:
🟦  🟨  🟥  ⬛  w     1: [◽]               Factory 1: 2⬛, 2⬜
⬜  🟦  🟨  🟥  k     2: [◽][◽]            Factory 2: 3🟥, 1🟦
⬛  w  🟦  🟨  r     3: [◽][◽][◽]
r  k  w  b  y     4: [◽][◽][◽][◽]
y  r  k  w  b     5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. 2⬛ to Line 4  
B. 2⬛ to Line 2  
C. 1🟦 to Line 4  

**Answer:** B

**Why:** Look at your legal destinations. Blue (🟦) and Yellow (🟨) are placed in Rows 1, 2, and 3. Therefore, Blue and Yellow can ONLY go into Row 4 or Row 5. They are bottlenecked together into Rows 4 and 5. Black (⬛) is placed in Rows 1 and 3, meaning Row 2 and Row 4 are legal for Black. If you put Black into Line 4, you consume one of the only two rows Blue and Yellow can use, causing a disastrous traffic jam later. Put 2⬛ into Line 2 to fit Line 2 exactly and keep Lines 4 and 5 open for Blue and Yellow.

**When the rule fails:** If you are actively trying to end the game on this round and future board flexibility does not matter.

---

## Motif: Row-5 Sacrifice `[Advanced]`

**Rule:** Sometimes paying a small floor penalty is cheaper than consuming your emergency row-5 buffer.

**When it matters:** When Row 5 is your only remaining empty pattern line and major color floods threaten to hit the center.

---

### Position 1

```text
Pattern Lines:       Options Available:
1: [⬜]               Center: 2⬛
2: [🟦][🟦]            Factory 1: 3🟨, 1🟥
3: [🟨][🟨][🟨]
4: [🟥][🟥][🟥][🟥]
5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. Take 2⬛ from Center to Line 5  
B. Take 2⬛ from Center to Floor (-2 pts)  
C. Take 3🟨 from Factory 1 to Line 5  

**Answer:** B

**Why:** Lines 1–4 are already completely full this round. Line 5 is empty and is your ONLY open pattern line on the entire board. Center has 2⬛, while Factory 1 has 3🟨. If you put 2⬛ into Line 5, Line 5 becomes locked to Black. When the 3🟨 from Factory 1 are drafted later, all 3🟨 will be forced straight to your floor (-6 pts). Taking 2⬛ to the floor now costs -2 points, but preserves Line 5 as an open buffer to cleanly absorb the 3🟨, saving net points.

**When the rule fails:** If no other color floods are possible and Black can complete Row 5 for a guaranteed wall placement.

---

# Family 2: Draft Control

## Motif: Poison Spill `[Core]`

**Rule:** Choose factories by what they dump into the center, not just what they give you. Poison needs delivery — absorption capacity tells you who gets hurt, but turn order decides who drinks it.

**When it matters:** Whenever a factory pick will send toxic tiles into the common center pool.

---

### Position 1

```text
Pattern Lines:       Options Available:
1: [◽]               Factory 1: 1🟦, 3🟥  (Final Factory of Round)
2: [◽][◽]            Center: Empty
3: [◽][◽][◽]
4: [◽][◽][◽][◽]
5: [◽][◽][◽][◽][◽]
```
*Opponent Absorption Capacity: A_opp(Red) = 1 (Line 1 open for Red; Lines 2-5 locked).*

**What would you take?**

A. 1🟦 from Factory 1 to Line 1 (spills 3🟥 to center)  
B. 3🟥 from Factory 1 to Line 3  

**Answer:** A

**Why:** Factory 1 is the final factory of the round, and Center is currently empty. Taking 1🟦 fills your Line 1 and dumps 3🟥 into Center. Because Factory 1 was the last factory, opponent is next on turn and is forced to take the 3🟥 from Center. Since opponent has A_opp(Red) = 1, they absorb 1 Red and drop 2 Red to their floor (-2 pts). If you had taken 3🟥 yourself, opponent would get 1🟦 for free.

**When the rule fails:** If the spilled 3🟥 allows opponent to complete a high-value column bonus.

---

## Motif: Contested Color `[Core]`

**Rule:** Before delaying a pickup, check if visible supply is less than total committed demand.

**When it matters:** Early in the round when mapping out how to fill 3–5 tile pattern lines.

---

### Position 1

```text
Wall Grid:           Pattern Lines:       Options Available:
b  y  r  k  w       1: [◽]               Factory 1: 2🟥, 2🟦
w  b  y  r  k       2: [◽][◽]            Factory 2: 1🟥, 3⬜
k  w  b  y  r       3: [◽][◽][◽]            Visible Red: 3 tiles
r  k  w  b  y       4: [◽][◽][◽][◽]            Your Demand: 2🟥 (Line 2)
y  r  k  w  b       5: [◽][◽][◽][◽][◽]        Opp Demand: 2🟥 (Line 3)
```

**What would you take?**

A. Draft 2🟥 from Factory 1 immediately  
B. Draft 3⬜ from Factory 2 to complete Line 3 first  
C. Take starting player marker  

**Answer:** A

**Why:** Red is **contested** (Visible Red = 3 < Total Demand = 4). There is not enough Red for both players to finish their lines. If you delay and take White, opponent will draft 2🟥 on their turn, leaving you unable to complete Line 2 this round.

**When the rule fails:** If completing Line 3 with White scores +8 points and seals a column bonus immediately.

---

### Position 2

```text
Wall Grid:           Pattern Lines:       Options Available:
b  y  r  k  w       1: [◽]               Factory 1: 1⬛, 2🟨, 1⬜
w  b  y  r  k       2: [◽][◽]            Factory 2: 4🟨
k  w  b  y  r       3: [◽][◽][◽]            Visible Yellow: 6 tiles
r  k  w  b  y       4: [◽][◽][◽][◽]            Your Demand: 2🟨 (Line 2)
y  r  k  w  b       5: [🟥][🟥][🟥][🟥][🟥]     Opp Demand: 0🟨 (No line)
```

**What would you take?**

A. Draft 2🟨 from Factory 1 immediately  
B. Draft 1⬛ from Factory 1 to deny opponent's Line 1, delaying Yellow  
C. Draft 4🟨 from Factory 2  

**Answer:** B

**Why:** Yellow is **abundant and uncontested** for board-building (Visible Yellow = 6 >> Demand = 2, opponent has no open line for Yellow). Yellow is safe to delay. Take 1⬛ now to deny opponent's pick; the Yellow tiles will still be waiting for you later.

**When the rule fails:** If opponent is willing to draft 4🟨 directly to their floor purely to deny you.

---

## Motif: Poisoned Turn `[Core]`

**Rule:** When remaining groups are ugly, stop maximizing what you take and start controlling who is on move for each bad group.

**When it matters:** Late round when only unwanted or overflow-causing color groups remain.

---

### Position 1

```text
Pattern Lines:       Options Available:
1: [◽]               Center: 3⬛, 3🟨, 1🟥
2: [🟦][🟦]            (3 separate color groups)
3: [🟨][🟨][🟨]         A_you: Black=0, Yellow=0, Red=1 (Line 1 open for Red)
4: [🟥][🟥][🟥][🟥]     A_opp: Black=0, Yellow=0, Red=0
5: [⬛][⬛][⬛][⬛][⬛]
```

**What would you take?**

A. Draft 1🟥 from Center → Line 1  
B. Draft 3⬛ from Center → Floor  
C. Draft 3🟨 from Center → Floor  

**Answer:** A

**Why:** There are 3 color groups left in center (3⬛, 3🟨, 1🟥). Line 1 is your only open line, which accepts 1🟥. Taking 1🟥 now absorbs cleanly into Line 1 and leaves exactly 2 bad groups (3⬛ and 3🟨). Opponent MUST take one 3-tile bad group on their turn (-4 floor pts). You will then take the remaining 3-tile bad group on your turn (-4 floor pts). If instead you took a 3-tile bad group first (-4 pts), opponent would take 1🟥 into Line 1, leaving you to take BOTH 3-tile bad groups (6 tiles total = -11 floor pts)!

**When the rule fails:** If opponent can take the 1-marker instead of a 3-tile group to shift parity back onto you.

---

## Motif: Marker Price `[Intermediate]`

**Rule:** Price first-player initiative against its exact marginal floor cost.

**When it matters:** Mid-to-late game when deciding whether to grab the starting player marker from center.

---

### Position 1

```text
Pattern Lines:       Options Available:
1: [◽]               Center: 1-Marker, 1🟦
2: [◽][◽]            Factory 1: 2🟦, 2🟨
3: [◽][◽][◽]            Current Floor: 4 tiles filled (-6 pts)
4: [◽][◽][◽][◽]        Expected Overflow Later: 1 tile
5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. Take 1🟦 + First Player Marker from Center  
B. Take 2🟦 from Factory 1 to Line 2  
C. Take 2🟨 from Factory 1 to Line 2  

**Answer:** B

**Why:** Your floor already has 4 tiles (-6 pts). Without the marker, your 1 later spilled tile takes Floor Slot 5 (-2 pts), for -8 pts total floor penalty. Grabbing 1🟦 + Marker takes Floor Slot 5 (-2 pts) and pushes your later spilled tile to Floor Slot 6 (-3 pts), making total floor penalty -11 pts. The marker's true marginal cost is 3 points (-11 vs -8). Since you have no urgent first-pick target next round, paying 3 marginal floor points for initiative is an overpay.

**When the rule fails:** If next round's bag draw is known to contain the final tile needed for a +10 color bonus.

---

### Position 2

```text
Pattern Lines:       Options Available:
1: [◽]               Center: 1-Marker, 1🟥
2: [◽][◽]            Factory 1: 2🟨, 2⬜
3: [◽][◽][◽]            Current Floor: 0 tiles (-0 pts)
4: [◽][◽][◽][◽]        Bag Status: Exactly 20 tiles remain (incl. 3 Blue)
5: [🟦][🟦][🟦][🟦][◽] (Needs 1🟦 to complete Line 5)
```

**What would you take?**

A. Take 1🟥 + First Player Marker from Center (-1 pt floor)  
B. Take 2🟨 from Factory 1 to Line 2  
C. Take 2⬜ from Factory 1 to Line 2  

**Answer:** A

**Why:** With exactly 20 tiles left in the bag including 3 Blue, all 20 tiles will form next round's 5 factories, guaranteeing Blue appears. Taking the marker costs only -1 floor point (Slot 1) and guarantees you first pick next round to secure Blue, locking in your 15-point Row 5 completion (+2 pt tile + 3 pt col + 10 pt color) before opponent can steal it. Initiative is worth far more than 1 point here.

**When the rule fails:** If opponent can complete a 20-point wall cascade this round while you spend a turn on the marker.

---

# Family 3: Tactical Value

## Motif: Double-Duty Move `[Core]`

**Rule:** Prefer moves that solve two strategic problems at once: score for your board AND deny your opponent.

**When it matters:** Every turn during candidate selection.

---

### Position 1

```text
Wall Grid:           Pattern Lines:       Options Available:
b  y  r  k  w       1: [◽]               Factory 1: 1🟨, 3⬛
w  b  y  r  k       2: [◽][◽]            Your Line 3: [🟨][🟨][◽]
k  w  b  y  r       3: [🟨][🟨][◽]         Opp Line 4: [🟨][🟨][🟨][◽]
r  k  w  b  y       4: [◽][◽][◽][◽]        (Opp needs 1🟨 to complete Line 4)
y  r  k  w  b       5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. Draft 1🟨 from Factory 1 to Line 3  
B. Draft 3⬛ from Factory 1 to Floor (-4 pts)  
C. Take starting player marker  

**Answer:** A

**Why:** Drafting 1🟨 does double duty! It completes your Line 3 for wall placement while simultaneously removing the exact single 🟨 opponent needs for their Line 4 completion. Double-duty moves produce major point swings without taking floor penalties or wasting turns.

**When the rule fails:** If taking a center group triggers an immediate game end when you are leading.

---

### Position 2

```text
Pattern Lines:       Options Available:
1: [◽]               Factory 1: 2🟦, 2🟥  (Final Factory of Round)
2: [◽][◽]            Center: Empty
3: [◽][◽][◽]            Your Line 2: [◽][◽] (needs 2🟦)
4: [◽][◽][◽][◽]        Opponent Absorption Capacity: A_opp(Red) = 0
5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. Draft 2🟦 from Factory 1 to Line 2  
B. Draft 2🟥 from Factory 1 to Floor (-2 pts)  
C. Take starting player marker  

**Answer:** A

**Why:** Factory 1 is the final factory of the round and Center is empty. Drafting 2🟦 fills your Line 2 and spills 2🟥 into Center. Since Center was empty and Factory 1 was the last factory, opponent MUST draft the 2🟥 from Center on their turn. With A_opp(Red) = 0, opponent takes both 2🟥 straight to their floor (-2 pts).

**When the rule fails:** If opponent can absorb Red into a newly opened Line 5.

---

# Family 4: Wall & Endgame

## Motif: Cross / Bridge `[Intermediate]`

**Rule:** A good wall tile scores twice: once when placed, and again by creating future scoring hooks.

**When it matters:** Early-to-mid game wall placement decisions.

---

### Position 1

```text
Wall Grid:           Pattern Lines:       Options Available:
b  y  r  k  w       1: [◽]               Choice A: Place ⬜ at Row 3 Col 2 (w)
w  🟦 🟨 r  k       2: [◽][◽]            (bridges (2,2)🟦 and (4,2)⬛)
k  w  b  y  r       3: [◽][◽][◽]            Choice B: Place ⬜ at Row 1 Col 5 (w)
r  ⬛ ⬜ b  y       4: [◽][◽][◽][◽]        (isolated placement)
y  r  k  w  b       5: [◽][◽][◽][◽][◽]
```

**What pattern line do you fill?**

A. Fill Line 3 with White (⬜) to place at Row 3 Col 2  
B. Fill Line 1 with White (⬜) to place at Row 1 Col 5  
C. Fill Line 5 with White (⬜)  

**Answer:** A

**Why:** Placing White at Row 3 Col 2 forms a **bridge** between Row 2 Col 2 (🟦) and Row 4 Col 2 (⬛)! It scores 3 points vertically immediately (vertical: Row 2, Row 3, Row 4 = 3 pts) AND leaves 2 horizontal hooks (Row 3 Col 1 and Row 3 Col 3) for future cross-scoring. Placing at Row 1 Col 5 scores only 1 point with 1 hook.

**When the rule fails:** If completing Line 1 takes 1 turn while Line 3 takes 3 turns and you need quick points.

---

### Position 2

```text
Wall Grid:           Pattern Lines:       Options Available:
b  y  r  k  w       1: [◽]               Choice A: Place 🟦 at Row 3 Col 3 (b)
w  b  🟨 r  k       2: [◽][◽]            (bridges (2,2)🟦 and (4,4)🟦)
k  w  b  y  r       3: [◽][◽][◽]            Choice B: Place 🟦 at Row 1 Col 1 (b)
r  k  w  🟦 y       4: [◽][◽][◽][◽]
y  r  k  w  b       5: [◽][◽][◽][◽][◽]
```

**What pattern line do you fill?**

A. Fill Line 3 with Blue (🟦) to place at Row 3 Col 3  
B. Fill Line 1 with Blue (🟦) to place at Row 1 Col 1  
C. Fill Line 5 with Blue (🟦)  

**Answer:** A

**Why:** Placing Blue at Row 3 Col 3 connects existing column tiles to form a three-tile vertical spine (+3 points) and leaves left/right spaces as future cross-score opportunities.

**When the rule fails:** If Blue is needed to block opponent's Line 5 completion.

---

## Motif: Close the Door `[Core]`

**Rule:** If ending now gives you a winning projected final score (wall + floor + bonuses), close the door. If ending loses and another round offers comeback value, keep it open.

**When it matters:** Rounds 4–5 when filling a pattern line will complete a horizontal row during wall tiling.

---

### Position 1

```text
Wall Grid:           Pattern Lines:       Options Available:
b  y  r  k  w       1: [◽]               Current Score: You 42, Opponent 38
w  b  y  r  k       2: [◽][◽]            Line 3: [🟨][🟨][◽] (needs 1🟨)
⬛  ⬜  🟦  y  🟥    3: [🟨][🟨][◽]         Factory 1: 1🟨, 3⬛
r  k  w  b  y       4: [◽][◽][◽][◽]        Projected Score: You 49, Opp 48
y  r  k  w  b       5: [◽][◽][◽][◽][◽]
```

**What do you do?**

A. Draft 1🟨 to fill Line 3 and trigger game end  
B. Draft 3⬛ to Line 4 to avoid completing Row 3  
C. Take starting player marker  

**Answer:** A

**Why:** Wall Row 3 is currently `⬛ ⬜ 🟦 y 🟥` with Yellow (`y`) as the single missing cell. Drafting 1🟨 fills Line 3, guaranteeing wall tiling places Yellow at Row 3 Col 4, completing Row 3 and triggering game end. Your projected final score after wall tiling and end-game bonuses is **49 to 48 in your favor**. Triggering game end now locks in your victory.

**When the rule fails:** If an uncounted floor penalty drops your projected total below 48.

---

### Position 2

```text
Wall Grid:           Pattern Lines:       Options Available:
b  🟨  🟥  ⬛  w     1: [◽]               Current Score: You 35, Opponent 40
w  b  y  r  k       2: [◽][◽]            Line 1: [◽] (needs 1🟦)
k  w  b  y  r       3: [◽][◽][◽]            Factory 1: 1🟦, 3⬛
r  k  w  b  y       4: [◽][◽][◽][◽]        Projected if End Now: You 41, Opp 49
y  r  k  w  b       5: [◽][◽][◽][◽][◽]
```

**What do you do?**

A. Draft 1🟦 to Line 1 to trigger game end  
B. Draft 3⬛ to Line 4 to keep game open for Round 5  
C. Draft floor tiles  

**Answer:** B

**Why:** Wall Row 1 is `b 🟨 🟥 ⬛ ⬜` with Blue (`b`) as the single missing cell. Drafting 1🟦 into Line 1 places Blue at Row 1 Col 1, completing Row 1 and triggering game end. However, ending now yields a projected loss (41 to 49). Current score lead is not the decision metric — **projected final score** is. Keeping the door open gives you Round 5 where your superior Line 4/5 setup can generate a +14 point comeback.

**When the rule fails:** If opponent will complete a full color bonus (+10) in Round 5.

---

## Motif: Zero-Floor Discount `[Advanced]`

**Rule:** Once your already-committed floor loss will reduce your post-wall score to zero, additional floor penalties up to that same zero bound have zero marginal scoreboard cost. The floor can be free. The turn never is.

**When it matters:** Early game when scores are low and floor penalties are being taken.

---

### Position 1

```text
Pattern Lines:       Options Available:
1: [◽]               Game State: Early game, score 0
2: [◽][◽]            Expected Wall Score: +2 pts
3: [◽][◽][◽]            Current Floor: 3 tiles (-4 pts)
4: [◽][◽][◽][◽]        Factory 1: 2⬛, 2🟨
5: [◽][◽][◽][◽][◽]        (Opponent needs 1⬛ for Column Bonus)
```

**What would you take?**

A. Take 2⬛ from Factory 1 to Floor to deny opponent's +7 Column Bonus  
B. Take 2🟨 from Factory 1 to Line 2  
C. Take starting player marker  

**Answer:** A

**Why:** Expected wall score is +2 pts. Your current 3 floor tiles (-4 pts) already wipe out your score (-2 pts net, bounded at 0). Taking 2 additional floor tiles brings total floor to 5 slots (-8 pts), giving -6 pts net, which also rounds up to 0 on the scoreboard. The additional floor penalty costs **0 marginal scoreboard points**. You deny opponent a +7 column bonus for zero actual point loss. Note: The floor penalty costs 0 scoreboard points, but you still spend your turn on denial instead of building.

**When the rule fails:** If your wall scoring this round unexpectedly produces +9 points instead of +2.

---

### Position 2

```text
Pattern Lines:       Options Available:
1: [◽]               Score before Tiling: 1 pt
2: [◽][◽]            Expected Wall Score: +3 pts
3: [◽][◽][◽]            Current Floor: 4 tiles (-6 pts)
4: [◽][◽][◽][◽]        Center: 2🟥
5: [◽][◽][◽][◽][◽]
```

**What would you take?**

A. Take 2🟥 to Floor to deny opponent's Row 4 completion  
B. Take safe 1🟨 from Factory 1 to Line 1  
C. Take starting player marker  

**Answer:** A

**Why:** Your post-wall score (4 pts) is already completely wiped out by your existing -6 floor penalty (bounded at 0). Adding 2 more floor tiles changes your net calculation from -2 to -7, but both result in **0 points on the scoreboard**. The additional floor penalty costs 0 scoreboard points; the move still has opportunity cost.

**When the rule fails:** In later rounds (R3–5) when you have built up a bank of points above zero.

---

# Motif Checklist

Use this quick-reference checklist during games until pattern recognition becomes automatic:

### 1. Flexibility
- [ ] **Last Home** — Is any color down to its sole remaining legal row?
- [ ] **Traffic Jam** — Are multiple constrained colors competing for the same open row?
- [ ] **Row-5 Sacrifice** — Is paying a small floor penalty cheaper than locking Row 5?

### 2. Draft Control
- [ ] **Poison Spill** — What toxic tiles does this factory dump into the center? (Poison needs delivery!)
- [ ] **Contested Color** — Is visible supply less than total committed demand?
- [ ] **Poisoned Turn** — Who gets stuck with the move when remaining groups are ugly?
- [ ] **Marker Price** — What is the marker's true marginal floor cost vs. initiative value?

### 3. Tactical Value
- [ ] **Double-Duty** — Does any move score for your board AND deny your opponent?

### 4. Wall & Endgame
- [ ] **Cross / Bridge** — Does this wall tile connect existing tiles and create future hooks?
- [ ] **Close the Door** — Does triggering game end now yield a winning projected final score?
- [ ] **Zero-Floor Discount** — Is your score low enough that extra floor tiles cost 0 points? (The floor can be free. The turn never is.)
