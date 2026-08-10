# Competitive Azul 1v1 Strategy Guide

**Game:** Original *Azul*, standard colored wall  
**Format:** Two-player / 1v1  
**Research refresh:** 2026-08-10

> **Central idea:** Strong Azul is not “score the prettiest wall.” It is repeated management of **margin, capacity, residues, initiative, and the game-ending trigger**.

---

# 1. The strategic model

## 1.1 Optimize the score margin

`[STRUCTURAL]` In a 1v1 game, evaluate choices primarily by their effect on the final score difference:

$$\Delta = S_{\text{you}} - S_{\text{opp}}$$

This immediately explains why blocking matters. If one move scores 3 for you and another scores 1 but reliably prevents 6 for the opponent, the second move can be much stronger.

Do **not** reduce this to “always hate-draft.” A denial move has an opportunity cost: what could you have scored or prepared instead? The useful question is:

> **How much does this move change the expected final margin compared with my best alternative?**

## 1.2 Five currencies of an Azul position

Think of every position as having five interacting resources:

1. **Points** — current scoring and credible future bonuses.
2. **Capacity** — how many incoming tiles you can safely absorb.
3. **Flexibility** — how many colors/lines remain viable.
4. **Tempo / initiative** — who controls the first selection next round and who is likely to inherit ugly final picks this round.
5. **Trigger control** — who can end the game, and whether ending now helps them.

A move that appears inefficient in raw points may be excellent if it preserves capacity, wins initiative, or removes a decisive opponent threat.

---

# 2. The 10-second move algorithm

Before every pick, run this sequence.

## Step 1 — What do I gain?

Check:

- Does this complete a pattern line this round?
- Where will its wall tile score?
- Does it create horizontal **and** vertical adjacency?
- Does it advance a credible column, color, or row bonus?
- What floor cost does it create now?

## Step 2 — What do I leave behind?

If taking from a factory, **the other colors are part of your move**. They are pushed into the center.

Ask:

- Which center piles get larger?
- Do two sources of the same color consolidate?
- Am I creating a 4-, 5-, or 6-tile pile that one player cannot absorb?
- Does my opponent now get a one-pick completion?

## Step 3 — What is their best reply?

Do not compare your move against the opponent playing normally. Compare it against their **best punishment**:

- Can they steal a critical color?
- Can they complete a high-scoring line?
- Can they alter the center so your next desired pickup becomes too large?
- Can they force you to take last?

## Step 4 — What does the next board look like?

After your move and their strongest reply, ask:

- What useful groups remain?
- Who has more safe capacity?
- Who is closer to being forced onto the floor?
- Who is likely to take the first-player marker?
- Who is likely to take the final ugly group?

## Step 5 — If the round is nearly solved, calculate instead of guessing

`[STRUCTURAL]` Branching falls dramatically as factories empty. With only a few distinct groups left, mentally enumerate the remaining move/reply sequence. Late-round exact calculation is worth much more than early-round intuition.

---

# 3. Wall geometry: build scoring infrastructure

## 3.1 Central positions have option value

`[HEURISTIC]` Prefer to establish your early wall in the **middle three columns**, especially when the available colors make that natural.

Why?

- A tile near the middle can expand horizontally in either direction.
- Edge placements only have one inward horizontal direction.
- Connected central shapes give more routes to future double-direction scoring.

Board Game Arena's community tips explicitly recommend beginning in the middle columns, and an independent simplified placement-simulation project found the center tile disproportionately frequent among its high-scoring placements. The simulation ignored factory availability and pattern-line constraints, so this is support for **geometry**, not proof of an optimal opening.

### Important correction

Do not turn “central is good” into a rigid color script. Factory composition and opponent interference matter more than forcing a memorized opening sequence.

## 3.2 Build *ledges*, not only straight columns

A common beginner plan is “build one vertical column from top to bottom.” That is solid, but not always score-maximizing.

`[HEURISTIC]` Look for **crosshatch / ledge shapes** that let a future tile connect both horizontally and vertically. The newly placed tile is then counted in both scoring lines.

A useful visual target is:

```text
  X
X . X     <- filling the dot can score both directions
  X
```

You do not need the complete cross. Even a short horizontal segment intersecting a vertical segment can create high-value wall placements.

## 3.3 Wall-tiling order creates compounding

`[RULE]` Completed pattern lines are resolved **top to bottom**, with each moved tile scoring immediately.

`[STRUCTURAL]` Therefore a tile placed from a lower pattern line in the same wall-tiling phase can score using a tile that was just placed above it. The reverse is not true: the upper tile was scored before the lower tile existed.

This creates a real sequencing advantage when several pattern lines complete in a connected vertical shape.

### Illustrative geometry, not a normal opening

If five wall tiles in one column could all be placed in the same wall phase with an otherwise empty board, top-to-bottom scoring would produce:

$$1 + 2 + 3 + 4 + 5 = 15$$

before the +7 endgame column bonus. This example is mainly a demonstration of the scoring mechanism; actual factory constraints make such perfect sequences uncommon.

## 3.4 Finish with adjacency whenever possible

`[HEURISTIC]` Two end positions containing the same wall tiles can score different totals depending on the order in which those tiles arrived. Prefer lines that **create an adjacency and then exploit it**, rather than placing multiple isolated tiles and connecting them later unless the timing math favors the latter.

---

# 4. Pattern lines: capacity is a strategic resource

## 4.1 Rows 1–3 are your reliable production system

Rows 1, 2, and 3 require fewer tiles and are therefore easier to complete in a single round.

`[HEURISTIC]` In the opening and middle game, completing the top three pattern lines consistently is usually more important than over-investing in an ambitious row 5. Board Game Arena community analysis repeatedly emphasizes this priority.

But “always fill rows 1–3” is still too rigid. A decisive denial, a high-value cross score, or a final-round bonus can outweigh it.

## 4.2 Rows 4–5 are projects **and buffers**

Long lines have two roles:

1. They eventually create wall placements and bonuses.
2. They absorb large tile groups that would otherwise hit the floor.

This second role is easy to undervalue.

### The row-5 shock absorber

`[STRUCTURAL]` An empty legal row 5 can absorb up to five tiles of a single color. Once you commit it to a color, it cannot absorb other colors that round; once the corresponding wall row already contains that color, that color is permanently illegal for that line.

`[HEURISTIC]` Avoid casually seeding row 5 with a lone tile just because you can. A weak commitment can cost more in lost future capacity than the single floor point you were trying to avoid.

This is why intentionally taking a small floor penalty can be correct: paying -1 or -2 may preserve a five-space defensive buffer.

## 4.3 Partial long lines are not automatically bad

The earlier rule “never carry a partial row 4/5” is too strong.

A partial long line is dangerous when:

- its remaining color is scarce,
- the opponent can easily deny that color,
- it blocks your only large-capacity buffer,
- the game is likely to end before completion.

It is reasonable when:

- the needed color is abundant or countable,
- you already have multiple visible sources,
- the line is aligned with a high-value wall position,
- you need that commitment to avoid a worse overflow elsewhere.

The right mental model is **stranded-capacity risk**, not a blanket prohibition.

---

# 5. Absorption capacity: the cleanest way to see traps

For a player $p$ and color $c$, define:

$$A_p(c) = \max(\text{remaining spaces in any single legal pattern line for } c)$$

If no pattern line can legally accept the color, $A_p(c) = 0$.

Because a drafted color group must go into **one** pattern line, not be split among several, a group of $g$ tiles forces at least

$$F_p(c,g) = \max(0, g - A_p(c))$$

onto that player's floor if they take it and choose the best available pattern line.

## Example

The center contains **5 red**.

- You have a legal row 5 with 4 spaces open: $A_{\text{you}}(R) = 4$.
- Opponent's best legal red line has 1 space open: $A_{\text{opp}}(R) = 1$.

Then:

- your minimum red overflow is $5 - 4 = 1$,
- their minimum red overflow is $5 - 1 = 4$.

That pile is much more toxic to them than to you.

### Practical use

You do not need to calculate $A(c)$ for every color every turn. When the center begins consolidating, identify the **one or two danger colors** and compare your capacity to theirs.

> A center flood trap is not “there are lots of red tiles.” It is “the red pile is larger than one player's best legal single-line capacity.”

---

# 6. Factory drafting: you are choosing a residue vector

When you select a color from a factory, every other tile on that factory moves to the center.

Represent those leftovers informally as a **residue vector**:

```text
Factory: Blue, Blue, Red, Yellow
Take:    Blue, Blue
Residue: +1 Red, +1 Yellow to center
```

The visible value of your move is the blue pair. The strategic value may be the red and yellow you just consolidated.

## 6.1 Delay safe pickups

`[HEURISTIC]` If you need a group that exists in multiple safe sources and your opponent has little reason to take it, consider doing something else first.

This can let you:

- get two objectives with two turns instead of spending both turns on one objective,
- consolidate your desired color into the center,
- force your opponent to reveal a commitment.

But do not delay when the opponent can combine the sources into a pile too large for your target line.

## 6.2 Center versus factory

Once the first-player marker has been taken, a center pick often has a tempo advantage because it **removes one color group without adding new residues**. A factory pick removes one group but adds leftovers to the center and may collapse future choices.

`[HEURISTIC]` If two picks are otherwise similar, prefer the one that leaves the future draft structure better for you. Sometimes that is the center; sometimes deliberately feeding the center creates the trap you want.

## 6.3 Count drafting actions late in the round

The total number of future *drafting actions* is not fixed at 20 tiles / 2 players because a single action can take multiple same-color tiles.

Near the end of the round, count remaining **color groups**, not tiles. Ask who receives the last selection if current groups are consumed in the most likely order—and whether a factory pick merges two groups into one, changing parity.

This is a major source of forced-floor tactics in 1v1.

---

# 7. The first-player marker: buy initiative at the right price

## 7.1 What the marker actually costs

`[RULE]` The first player to draft from the center takes the starting-player marker and places it on the **leftmost free floor space**. It counts as a normal floor tile when penalties are scored.

The floor schedule is:

```text
-1  -1  -2  -2  -2  -3  -3
```

So “first player costs -1” is only true when the marker occupies one of the first two slots and does not worsen later floor placement.

`[STRUCTURAL]` Its true marginal cost can include:

- the penalty of the slot the marker occupies, **plus**
- any extra penalty caused by pushing later floor tiles one slot to the right.

## 7.2 What initiative is worth

Starting next round can provide:

- first access to a rare 3- or 4-tile factory group,
- a one-pick completion of row 3/4/5,
- the ability to shape the center before your opponent,
- protection against a color your opponent would otherwise take immediately.

So evaluate the marker as:

$$\text{Initiative Value} - \text{Marginal Floor Cost}$$

not as “always take it.”

## 7.3 Final round

`[STRUCTURAL]` If the current round will certainly end the game, next-round initiative is worth zero. The marker may still come attached to a useful center group or matter to floor sequencing, but there is no future first-move benefit.

This is one of the cleanest places to override the usual first-player instinct.

---

# 8. Blocking and denial

## 8.1 Block *credible* value, not theoretical bonuses

A +7 column or +10 color bonus looks tempting to block, but ask whether the opponent is actually going to get it.

A denial is valuable when the opponent has:

- a near-complete target,
- visible required tiles,
- legal capacity to take them,
- enough remaining rounds to finish,
- no strong pivot.

## 8.2 Marginal denial value

Suppose:

- letting the opponent take a tile makes a +7 column effectively guaranteed,
- denying it costs you -2 floor points,
- your alternative move would score +1 for you.

A rough swing from the denial is not simply +5. Compare complete alternatives:

```text
A: Ignore threat -> +1 for you, +7 for them    margin effect = -6
B: Deny threat  -> -2 for you, +0 for them    margin effect = -2
Improvement from B over A                       = +4 margin
```

This comparison prevents overvaluing “I stopped seven points!” while ignoring what you gave up.

## 8.3 The single-tile snatch

`[HEURISTIC]` Stealing a single tile is strongest when it strands a nearly complete row 4/5 or prevents a bonus whose remaining requirements are otherwise easy.

It is weakest when the opponent can simply pivot to another color or when the stolen tile damages your board much more than the denial hurts theirs.

## 8.4 Center flood trap

Use absorption capacity rather than a fixed “4+ tiles” rule.

A three-tile pile can be devastating if $A_{\text{opp}}(c) = 0$. A six-tile pile may be acceptable if the opponent has five open spaces and the first floor slot is cheap.

The trap is about **pile size relative to legal capacity**, not an arbitrary pile threshold.

---

# 9. Completing a full color: bonus and liability

`[RULE]` A wall row may never accept the same color twice.

`[STRUCTURAL]` On the standard colored wall, once you have all five wall tiles of one color, **every wall row already contains that color**. Therefore no pattern line can legally accept that color in a later round. Future tiles of that color must go to the floor if you draft them.

This makes the +10 color bonus strategically unusual:

- **Late game:** excellent, because there may be no later round in which the color becomes toxic.
- **Early game:** potentially dangerous, because one fifth of the tile set has become unusable to you.

`[HEURISTIC]` In 2-player games, treat a full-color set mainly as a late-game opportunity unless the position strongly supports it. Do not chase it just because +10 is printed on the board.

---

# 10. Floor management: penalties are prices, not sins

`[RULE]` Floor penalties are cumulative by slot: -1, -1, -2, -2, -2, -3, -3. Your score cannot fall below zero.

A zero-floor game is not necessarily a good game.

## 10.1 When taking floor points is correct

Consider a small penalty when it:

- preserves row 5 as a flexible buffer,
- secures a much better wall position,
- steals a critical opponent tile,
- avoids committing a long line to a bad color,
- buys valuable next-round initiative,
- changes who is stuck with the last center pile.

## 10.2 The floor is nonlinear

Your first -1 can be cheap. Your sixth and seventh floor positions are -3 each. Therefore “one more bad tile” becomes increasingly expensive as the floor fills.

Evaluate **marginal floor cost**, not only the number of overflow tiles.

---

# 11. Bag tracking without turning Azul into accounting

There are 20 tiles of each of the 5 colors.

`[RULE]` In 2-player play, each round begins with 5 factories × 4 tiles = **20 tiles** drawn from the bag.

`[STRUCTURAL]` The initial 100-tile bag therefore supplies exactly five full two-player factory setups before recycled discards are needed for a sixth setup.

This makes Round 5 a natural counting breakpoint.

## 11.1 Practical counting system

Do **not** track all five colors from move one unless you enjoy it.

Track a color when:

- you have committed row 4 or row 5 to it,
- your opponent needs it for a decisive bonus,
- you are considering forcing an extra round,
- a future flood risk depends on how many remain.

For color $c$:

```text
20 total
- tiles currently on both walls
- tiles currently in pattern lines
- tiles visible in factories/center
- tiles known to be in the lid/discard pile
= possible copies still in bag
```

## 11.2 Exact probability when it matters

If the bag contains $B$ tiles, $B_c$ of which are the color you need, and the next setup will draw $n$ tiles, then the chance of seeing at least one copy is:

$$P(\ge 1 \text{ copy of } c) = 1 - \frac{\binom{B - B_c}{n}}{\binom{B}{n}}$$

This is most useful for an important late-game commitment, not routine early-game play.

---

# 12. Phase strategy

## 12.1 Rounds 1–2: build options

**Primary goals**

- Establish connected wall infrastructure in the middle three columns when practical.
- Complete short lines reliably.
- Avoid unnecessary long-line commitments.
- Observe opponent column/color direction before you lock into the same resources.
- Buy the first-player marker only when the next-round first pick has concrete value.

**What not to do**

- Force a memorized opening through bad factories.
- Seed row 5 with one tile only to avoid -1.
- Chase a color bonus before you know the game shape.

## 12.2 Rounds 3–4: become adversarial

This is where 1v1 Azul stops being mostly architectural.

Before each turn, inspect:

- opponent's near-complete pattern lines,
- their $A_{\text{opp}}(c)$ for center danger colors,
- their likely endgame column/color,
- whether you can strand a long line,
- whether factory residues change the last-pick sequence.

Start tracking one or two critical colors from the bag.

## 12.3 Round 5 and later: solve the finish

By now, broad heuristics should give way to arithmetic.

Calculate:

1. current score difference,
2. likely wall scores from already-complete pattern lines,
3. guaranteed/credible floor penalties,
4. final bonuses,
5. whether either player completes a horizontal row and triggers the end,
6. whether extending one round benefits you more than the opponent.

---

# 13. Game-ending control

`[RULE]` The game ends immediately after the wall-tiling phase of a round in which at least one player has completed a horizontal row of five.

## 13.1 If you are ahead

`[HEURISTIC]` Prefer ending when the **fully calculated final margin** is favorable. Ending denies future opponent opportunities, but it can also cut off your own bonuses. “Ahead now” is not enough—score the wall phase and bonuses first.

## 13.2 If you are behind

`[HEURISTIC]` Preserve another round only when you have a plausible way to gain more from it than your opponent. An extra round is not automatically comeback equity; it may simply give the leader more adjacency scoring.

## 13.3 Tie-break

`[RULE]` If final scores tie, the player with more completed horizontal rows wins; if still tied, victory is shared.

That means a horizontal completion can carry **trigger value +2 bonus + tie-break value**.

---

# 14. Common strategic mistakes

## Mistake 1 — Only looking at your board

**Fix:** On every turn identify the opponent's best immediate pickup and their most fragile commitment.

## Mistake 2 — Evaluating only the tiles you take

**Fix:** Read every factory pick as **take + residues**.

## Mistake 3 — Avoiding all negatives

**Fix:** Price floor points against lost flexibility and opponent denial.

## Mistake 4 — Overcommitting row 5

**Fix:** Treat empty capacity as insurance.

## Mistake 5 — Chasing printed bonuses

**Fix:** A +10 color set can make a color completely unusable to you in later rounds. A +7 column may not be worth destroying your top-three-line production.

## Mistake 6 — Treating first player as automatically good

**Fix:** Identify the specific first pick you expect to gain next round and compare it with the marker's marginal floor cost.

## Mistake 7 — Using a fixed “points per tile” target

**Fix:** A tile's value includes adjacency, capacity, residues, denial, initiative, and trigger effects. Track points-per-wall-placement as a diagnostic, not a move rule.

---

# 15. One-page competitive checklist

## Start of round

- [ ] What colors do I need for rows 3–5?
- [ ] Which of those are abundant/scarce in the visible 20 tiles?
- [ ] What does my opponent need?
- [ ] Which color is most dangerous if it consolidates in the center?
- [ ] Is next-round initiative especially valuable?
- [ ] Can either player end the game this round?

## Before each move

- [ ] What do I score/complete?
- [ ] What residues do I push to center?
- [ ] What is opponent's strongest reply?
- [ ] What are our absorption capacities for the danger color?
- [ ] Do I preserve a useful row-4/5 buffer?
- [ ] Does this change who takes the final pile?

## End of round / final rounds

- [ ] Solve remaining groups exactly if feasible.
- [ ] Add floor penalties by **slot**, not by tile count alone.
- [ ] If game may end, calculate wall scoring + bonuses before choosing the trigger.
- [ ] In the final round, do not assign future value to the first-player marker.

---

# 16. What is deliberately *not* claimed here

The following ideas may be useful, but the sources reviewed do not justify treating them as universal truths:

- “First player in Round 1 is almost always optimal.”
- “2.0 points per placed tile is the competitive threshold.”
- “Never carry a partial row 4/5.”
- “One exact opening pattern is the best opening.”
- “Always block a +7/+10 bonus if the floor cost is smaller.”

Those are better turned into experiments. See `azul-strategy-math-and-research.md` and `azul-training-playbook.md`.

---

# Sources and provenance

## Rules / formal research

1. Next Move / Plan B Games, *Azul* official rulebook:  
   https://cdn.svc.asmodee.net/production-nextmove/uploads/sites/4/2024/06/EN-Azul-Rules-Next-Move-web.pdf
2. Michal Počatko, *AI for the Board Game Azul*, Charles University, 2021:  
   https://dspace.cuni.cz/handle/20.500.11956/127953?locale-attribute=en

## Community competitive analysis

3. Board Game Arena, *Tips azul*:  
   https://en.doc.boardgamearena.com/Tips_azul
4. Community strategy guide:  
   https://www.reddit.com/r/boardgames/comments/rw06tt/azul_strategy_guide/
5. Strategy/scoring/pacing discussion:  
   https://www.reddit.com/r/boardgames/comments/tz9qor/azul_strategy_scoring_pacing/
6. Strategy discussion on central columns and crosshatching:  
   https://www.reddit.com/r/boardgames/comments/w1jtf6/i_am_good_at_board_games_but_suck_at_azul_advice/
7. Simplified placement-simulation dissertation discussion, including stated limitations:  
   https://www.reddit.com/r/boardgames/comments/hxodaf/update_i_wrote_my_dissertation_on_azul/

## Existing project notes incorporated

- `azul-competitive-strategy-guide.md`
- `azul-game-theory-and-ai.md`
- `azul-practice-tool-architecture.md`
- `azul-research-and-tooling.md`
