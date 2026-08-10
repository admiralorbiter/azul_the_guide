# Azul 1v1 Training Playbook

This document turns the strategy guide into deliberate practice. The goal is not to memorize more advice; it is to make the important calculations **automatic**.

---

# 1. Training priorities

Train in this order:

1. **Rules-perfect scoring and floor math**
2. **Wall geometry / adjacency recognition**
3. **Pattern-line capacity**
4. **Factory residue awareness**
5. **Opponent threat recognition**
6. **Late-round exact calculation**
7. **Bag tracking**
8. **Game-end calculation**

Do not start with full bag counting if you are still missing center traps. Tactical certainty has higher immediate value.

---

# 2. Drill: score the wall instantly

## Goal

Given a wall placement, state its immediate score in under 3 seconds.

## Method

For 20 random wall positions:

1. Identify horizontal connected length.
2. Identify vertical connected length.
3. If neither exists, score 1.
4. If one exists, score its line length.
5. If both exist, add both lengths.

## Success standard

- 20/20 correct twice in a row.
- No recounting with your finger.

### Advanced variant

Give yourself 2–4 complete pattern lines and score the **whole wall-tiling phase top to bottom**, updating adjacency after each placement.

---

# 3. Drill: absorption map

## Goal

See center traps before they become forced.

At three points in each round—early, middle, late—pick every color currently in the center and record:

```text
Color     My A(c)     Opp A(c)     Center size     Toxic to whom?
Blue         4           2              3          Opponent
Yellow       1           5              4          Me
Red          0           1              2          Both / me worse
...
```

You can do this mentally once the habit forms.

## Success standard

Before either player takes a center pile that overflows by 2+, you predicted **who was more exposed** at least one turn earlier.

---

# 4. Drill: draft the leftovers

## Goal

Stop seeing a factory as only the tiles you want.

Before touching a factory, say:

> “I take X; I add Y and Z to center.”

Then ask:

- Which existing center piles merge?
- Does any pile cross someone's absorption capacity?
- Does this give the opponent a one-pick completion?

## Success standard

Play an entire game with **zero surprise center consolidations** caused by your own factory pick.

---

# 5. Drill: solve the tail

## Goal

Calculate the end of a round exactly.

When three or fewer factories remain—or whenever the total number of distinct available color groups feels manageable—stop playing by instinct.

Write or mentally enumerate:

```text
My move
  -> Opp best reply
      -> My next move
          -> Opp next move
              -> final group
```

For each branch track:

- pattern completion,
- overflow,
- marker ownership,
- last pickup.

## Success standard

Before the final two picks, you can state which player will take the last group under best play and how many floor points it causes.

---

# 6. Drill: first-player price

Each time the center is first opened, pause and record:

```text
Marker slot:          -1 / -2 / -3
Later floor shift?:   yes/no, estimated extra cost
Concrete next-round first-pick value:
Opponent value if they get marker:
Decision: take / defer
```

Do not accept “going first is good” as an answer. Name the **specific next-round advantage**.

After the next round begins, mark whether the predicted benefit actually occurred.

---

# 7. Drill: one-color bag tracking

Start simple.

Pick **one critical color** at the end of Round 2 or during Round 3. Track every copy you can account for.

At each new setup, estimate:

- copies still potentially in bag,
- whether the color is scarce/normal/abundant,
- whether your row-4/5 commitment is still sensible.

Only add a second color after you can track one without distracting yourself from the board.

---

# 8. Drill: endgame audit

Beginning in Round 4, ask at the start of every round:

```text
Current margin:
Can I complete a horizontal row this round?
Can opponent?
My projected final bonuses:
Opponent projected bonuses:
My already-forced wall scoring:
Opponent already-forced wall scoring:
Who benefits from another round?
```

If a move can trigger the end, **calculate first, trigger second**.

---

# 9. Post-game review template

Copy this after any serious game:

```markdown
## Match Review

**Result:** W/L/T  
**Final score:** Me __ / Opp __  
**Margin:** __

### Round summary
| Round | Starter | My floor | Opp floor | My wall pts | Opp wall pts | Key event |
|---|---|---:|---:|---:|---:|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6+ | | | | | | |

### Three pivotal decisions
1. **State:**
   - Move I chose:
   - Better alternative?
   - What I missed:

2. **State:**
   - Move I chose:
   - Better alternative?
   - What I missed:

3. **State:**
   - Move I chose:
   - Better alternative?
   - What I missed:

### Strategic diagnostics
- Biggest unnecessary floor loss:
- Biggest successful denial:
- Biggest failed denial:
- Row-5 commitment that stranded capacity?
- Center pile I failed to predict?
- First-player marker purchase that paid off / did not?
- Did I correctly identify the final round?
- Did I calculate bonuses before triggering the end?

### One thing to train next game
-
```

---

# 10. Metrics worth tracking over 20+ games

Do not judge strategy from one memorable win. Track repeated behavior.

## 10.1 Floor differential

$$\text{FD} = \text{Opponent floor penalty} - \text{Your floor penalty}$$

Positive is good for you.

Separate:

- unavoidable floor,
- intentional strategic floor,
- tactical mistake floor.

## 10.2 Wall-placement efficiency

$$E = \frac{\text{wall-tiling points}}{\text{number of wall tiles placed}}$$

Do not assume a target of 2.0. Build your own distribution and see whether winners consistently differ from losers.

## 10.3 Cross-score rate

Percentage of wall placements that scored both horizontal and vertical lines.

This measures whether your geometry is creating intersections rather than isolated placements.

## 10.4 Stranded long-line turns

Count rounds in which row 4 or 5 begins and ends partially filled **without the partial line having served a deliberate strategic purpose**.

This is more informative than simply counting incomplete long lines.

## 10.5 Forced overflow created

Total opponent floor tiles that were a direct result of a center pile you intentionally consolidated beyond their absorption capacity.

## 10.6 Initiative conversion

When you take the starting-player marker, did first pick next round produce the benefit you predicted?

Track:

```text
marker taken: yes
marginal floor cost: 2
predicted benefit: secure 3 blue for row 3
realized benefit: yes/no
```

## 10.7 End-trigger accuracy

For every game-ending decision, record whether your pre-trigger final-score projection was correct within 2 points.

---

# 11. Five-game focused training blocks

## Block A — No-surprise center

For five games, your only special focus is residues and absorption capacity.

**Rule:** Before each factory pick, identify what goes to center.

## Block B — Geometry

For five games, track every wall placement as:

- isolated,
- horizontal-only,
- vertical-only,
- cross-score.

Review whether early placement choices created later high-value placements.

## Block C — Initiative

For five games, record every marker decision and its realized next-round value.

Goal: learn when first player is worth paying for in *your* style of games.

## Block D — Long-line discipline

For five games, every time you start row 4/5, state:

1. why this color,
2. likely completion horizon,
3. how much buffer capacity you are giving up.

## Block E — Endgame

For five games, begin explicit final-score projection in Round 4. Do not trigger the end without writing/mentally calculating bonuses.

---

# 12. Experiments for the Rust/WASM practice tool

The existing practice-tool architecture is well suited to generating tactical puzzles, but scenario selection should be tied to learnable strategic motifs.

## Scenario tags

Every generated state should be taggable with one or more of:

- `CROSS_SCORE`
- `CENTER_FLOOD`
- `ABSORPTION_ASYMMETRY`
- `FIRST_PLAYER_PRICE`
- `LAST_PICK_PARITY`
- `ROW5_BUFFER`
- `DENIAL_COLUMN`
- `DENIAL_COLOR`
- `BAG_SCARCITY`
- `GAME_END_TRIGGER`
- `EXTEND_GAME`
- `EXACT_TAIL`

## Scenario quality

Prefer positions where:

- at least two moves are plausible,
- the best move wins for a *specific explainable reason*,
- the EV gap is meaningful but not obvious,
- the evaluator can show a short principal variation or rollout summary.

Do not train mostly on states where one move is trivially 10 points better. Those test arithmetic, not strategy.

## Feedback format

After a choice, show:

1. **Your move rank**
2. **Estimated margin difference**
3. **Primary reason**
4. **Opponent's best reply**
5. **One strategic concept to remember**

Example:

```text
Your move: #2 of 7
Estimated loss vs best: 2.4 points of margin

Why:
You completed row 3, but your factory leftovers created 5 yellow in center.
Opponent's yellow absorption capacity was 5; yours was only 1.
After their reply, you were forced into four yellow overflow.

Concept: Draft the leftovers.
```

---

# 13. When to move beyond heuristics

Once you can consistently:

- predict center consolidations,
- calculate floor penalties by slot,
- see cross-score wall opportunities,
- solve the final few picks,
- identify the likely final round,

then replay/engine analysis becomes much more valuable. At that point the goal is not to learn basic rules—it is to discover where your intuition systematically disagrees with stronger search.
