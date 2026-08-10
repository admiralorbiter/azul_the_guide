# Azul Strategy: Math, Evidence, and Research Notes

**Scope:** Original *Azul*, primarily 2-player standard-wall play  
**Purpose:** Make the strategy guide auditable and convert useful intuition into quantities that can later be measured by software.

---

# 1. Game model

## 1.1 Deterministic within a round, stochastic between rounds

The most useful decomposition is:

```text
Round setup:     stochastic draw without replacement
        ↓
Factory offer:   sequential + perfect public information
        ↓
Wall tiling:     deterministic resolution/scoring
        ↓
Next setup:      stochastic again, unless game ended
```

All factories, center tiles, player boards, scores, and pattern lines are visible. Once a round's 20 factory tiles are known, there is no hidden random event during the drafting phase.

This gives a practical principle:

> **Use probability across rounds; use calculation inside the current round.**

The 2021 Charles University Azul AI thesis similarly classifies the game as perfect-information but non-deterministic due to stochastic round setup.

---

# 2. Utility: why point differential is useful but not the entire story

For a two-player state $s$, define the score margin:

$$D(s) = S_1(s) - S_2(s)$$

This is a much better heuristic evaluator than $S_1$ alone because it prices denial and forced floor penalties.

For final game states, a pure competition evaluator could instead be:

$$U(s) = \begin{cases} +1 & \text{win} \\ 0 & \text{tie} \\ -1 & \text{loss} \end{cases}$$

A practical engine can combine them lexicographically:

1. maximize win probability,
2. then expected point differential,
3. then tie-break-relevant horizontal rows when necessary.

### Why “strictly zero-sum every turn” is imprecise

The printed scores are not algebraically zero-sum: both players can gain points on the same round. What is zero-sum is the **competitive result** in a 1v1 match. Point differential creates a useful zero-centered evaluation, but a midgame state also contains stochastic future value and game-ending rights.

---

# 3. Absorption capacity

This is the most useful new state feature for human tactical play and for an evaluator.

For player $p$, color $c$, and pattern line $i$, let $r_i$ be its remaining capacity.

The line is legal for $c$ if:

- it is empty or already contains $c$, and
- the corresponding wall row does not already contain $c$.

Define:

$$A_p(c) = \max_{i \in L_p(c)} r_i$$

where $L_p(c)$ is the set of legal pattern lines for color $c$. If no legal line exists, define $A_p(c) = 0$.

Because one drafted same-color group cannot be split among several pattern lines, a group of $g$ tiles has minimum forced overflow:

$$F_p(c,g) = \max(0, g - A_p(c))$$

## 3.1 Why this matters

A naïve trap detector might say “a center pile of 5 is dangerous.” Capacity is more precise:

| Center group | Player capacity | Minimum overflow |
|---:|---:|---:|
| 3 | 0 | 3 |
| 3 | 3 | 0 |
| 5 | 1 | 4 |
| 5 | 5 | 0 |
| 7 | 4 | 3 |

The same center group can be harmless to one player and catastrophic to the other.

## 3.2 Differential toxicity

Define a simple toxicity gap:

$$T(c,g) = F_{\text{opp}}(c,g) - F_{\text{you}}(c,g)$$

Positive $T$ means the pile is structurally more dangerous to the opponent.

A stronger version would use the actual marginal floor-point schedule instead of tile count:

$$T_{\text{pts}}(c,g) = P_{\text{opp}}(c,g) - P_{\text{you}}(c,g)$$

where $P$ computes the extra floor penalty from the current occupied floor slots.

This is a natural feature for move ordering or practice-tool explanations.

## 3.3 Placement feasibility: homes and collisions

Absorption capacity measures how many tiles of one color a player can absorb in the best single line. A complementary question is: how many pattern lines can legally accept a given color at all?

Define the **home count** for player $p$ and color $c$:

$$H_p(c) = |L_p(c)|
$$

where $L_p(c)$ is the set of legal pattern lines for color $c$ (as defined in Section 3).

A color with $H_p(c) = 1$ is **fragile**: if its sole legal line is consumed by another color, $c$ becomes unplaceable and all future tiles of $c$ go to the floor.

### Capacity collisions and Hall's condition

Individual home counts can be misleading. Consider colors $c_1, c_2, \ldots, c_k$ that collectively require pattern-line destinations. If the union of their legal line sets is smaller than $k$:

$$\left| \bigcup_{i=1}^{k} L_p(c_i) \right| < k$$

then not all of them can be placed simultaneously. This is a direct application of Hall's marriage theorem: a perfect matching between colors and pattern lines exists if and only if every subset of colors has at least as many collectively available lines.

In practice, the most common violation is the simplest: **two or more one-home colors sharing the same sole legal line**.

### Bottleneck index

A useful evaluator feature:

$$\text{BN}_p = \sum_c \max\left(0, \frac{1}{H_p(c)} - \frac{1}{5}\right)$$

This scores zero for a color with all five rows available and increases as placement options narrow. A differential version $\text{BN}_{\text{opp}} - \text{BN}_{\text{you}}$ captures relative constraint pressure.

The simple human version: count homes per color, watch for ones and twos, and flag any row that multiple constrained colors share.

---

# 4. Residue vectors: formalizing factory effects

Let the center contain a color-count vector

$$C = (b,y,r,k,w)$$

for the five tile colors.

A factory $f$ has count vector $F_f$. If a move takes color $c$, define $e_c$ as the vector containing the count of color $c$ on the factory and zero elsewhere.

The leftovers moved to center are:

$$R(f,c) = F_f - e_c$$

and the new center is:

$$C' = C + R(f,c)$$

This is simple, but strategically important: a factory move changes both **your pattern line** and the **future common-pool state**.

## 4.1 Residue danger score

One potential evaluator feature:

$$\text{RD}(m) = \sum_c w_c \, [F_{\text{you}}(c,C'_c) - F_{\text{opp}}(c,C'_c)]$$

where $C'_c$ is the center pile size of color $c$ after move $m$, and $w_c$ weights colors by likelihood that someone will actually be forced to take them.

Interpretation:

- positive: your factory choice makes the center relatively safer for you / worse for opponent,
- negative: you may be feeding your opponent a favorable center.

Do not treat this exact equation as “solved Azul”; it is a feature proposal.

## 4.2 Spill classification

Human players benefit from a small taxonomy of factory spills. For a move $m$ taking color $c$ from factory $f$, the spill $R(f,c)$ can be classified by its effect on center toxicity:

| Spill type | Condition | Strategic meaning |
|---|---|---|
| Safe | $F_p(c', C'_{c'}) = 0$ for both players, all spilled $c'$ | Neither player is hurt |
| Opponent-toxic | $F_{\text{opp}}(c', C'_{c'}) > F_{\text{you}}(c', C'_{c'})$ for some spilled $c'$ | Spill favors you |
| Self-toxic | $F_{\text{you}}(c', C'_{c'}) > F_{\text{opp}}(c', C'_{c'})$ for some spilled $c'$ | Spill hurts you |
| Consolidating | Spill merges with existing center to create $C'_{c'} > \max(A_{\text{you}}(c'), A_{\text{opp}}(c'))$ | Creates a forced-overflow pile |

A move's total value should include both the take value and the spill classification, not just the tiles entering the player's board.

---

# 5. Floor penalties are marginal, not linear

The official floor schedule is:

$$[-1,-1,-2,-2,-2,-3,-3]$$

If a player currently occupies $q$ floor slots, the cost of $x$ additional floor tiles is the sum of the next $x$ entries rather than $-x$.

Define cumulative floor loss:

$$P(q,x) = \sum_{j=q+1}^{\min(q+x,7)} |f_j|$$

This makes late overflow considerably more expensive than early overflow.

## 5.1 Starting-player marker cost

The marker goes on the leftmost free floor position and counts as a tile there.

Its marginal cost is therefore not always one point. A better evaluator computes the difference between the floor score **with** and **without** the marker, including any later tiles shifted to more expensive slots.

This is also why a static “initiative = +1” or “marker = -1” rule is too crude.

## 5.2 Position complexity and calculation allocation

Not all positions warrant equal analysis depth. Define a simple **temperature** heuristic:

$$\text{Temp}(s) = w_1 \cdot \text{groups}_{\text{remaining}}^{-1} + w_2 \cdot \text{overflow}_{\text{risk}} + w_3 \cdot \text{trigger}_{\text{proximity}} + w_4 \cdot \text{forcing}_{\text{count}}$$

where:

- $\text{groups}_{\text{remaining}}^{-1}$ increases as fewer color groups remain (late round),
- $\text{overflow}_{\text{risk}}$ measures maximum $F_p(c, C_c)$ across dangerous center colors,
- $\text{trigger}_{\text{proximity}}$ flags whether either player can complete a horizontal row this round,
- $\text{forcing}_{\text{count}}$ counts moves that create unavoidable opponent overflow or threaten game end.

High temperature signals that heuristic play is insufficient and deeper search or exact calculation is warranted.

### Forcing moves

A move $m$ is **forcing** if the opponent's best reply to $m$ is strictly dominated by responding to $m$'s threat—i.e., ignoring $m$ leads to a substantially worse outcome than any non-threat-related alternative.

In search, forcing moves should be evaluated first (analogous to threat-space search in connection games). For human play, the priority ordering is: forcing threats → forced responses → ordinary improvements.

---

# 6. Wall scoring geometry

## 6.1 Single placement

If a newly placed tile has no orthogonally adjacent tile, it scores 1.

If connected horizontally, it scores the size of its connected horizontal line. If connected vertically, it scores the size of its connected vertical line. If both apply, both lines are scored and the new tile is counted in each.

This creates **super-additive local value** for intersection placements.

## 6.2 Top-to-bottom wall resolution

Complete pattern lines resolve top to bottom.

Consider an otherwise empty wall where one complete pattern line in each row will place into the same vertical column that round. Scores are:

$$1, 2, 3, 4, 5$$

for a total of 15, because each lower tile sees the already-placed tiles above it.

This example illustrates why *temporal geometry* matters: the same final wall may have scored differently if constructed in a different sequence of rounds.

## 6.3 Centrality as option value

A central cell has up to four orthogonal neighbors; an edge non-corner has three; a corner has two.

That alone does not prove central cells are optimal, because fixed colors, factory availability, row capacities, and opponent behavior constrain what can be placed. It does explain why central placements are attractive **starting infrastructure**.

A simplified undergraduate placement simulation reported the central tile as the most frequent first placement among its top-scoring sampled layouts, but its author explicitly noted that factory availability and pattern-line requirements were omitted. Treat the result as geometry evidence only.

---

# 7. Bag tracking

There are 100 tiles: 20 of each color.

In a 2-player game, each normal setup uses:

$$5 \text{ factories} \times 4 \text{ tiles} = 20 \text{ tiles}$$

So the initial bag supplies exactly five complete setups.

## 7.1 Hypergeometric model

Suppose the bag currently has $B$ tiles, $B_c$ of color $c$. If $n$ tiles will be drawn before you next make a relevant decision, then

$$P(X=k) = \frac{\binom{B_c}{k} \binom{B-B_c}{n-k}}{\binom{B}{n}}$$

and

$$P(X \ge 1) = 1 - \frac{\binom{B-B_c}{n}}{\binom{B}{n}}$$

### Strategic use

The probability is only as good as your inventory accounting. It is most worthwhile when one color decides whether a row 4/5 commitment completes or whether an opponent can finish a bonus.

---

# 8. Game tree evidence and what the existing AI notes got right

## 8.1 Branching factor

Michal Počatko's defended 2021 thesis derives a maximum initial branching factor of:

$$5 \text{ factories} \times 4 \text{ possible colors} \times 6 \text{ destinations} = 120$$

where destinations are the 5 pattern lines plus floor.

The same thesis observes a minimum branching factor of 1 in constrained late-round states. In one sample minimax-vs-minimax game, the arithmetic mean branching factor was 25.68 and median 19.5. Those sample statistics should **not** be generalized as universal game averages.

### Human implication

The search tree naturally narrows as a round empties. Therefore:

- early round: use heuristics and preserve options,
- late round: calculate more deeply and, eventually, exactly.

This supports the “solve the tail” recommendation in the main guide.

## 8.2 Minimax and MCTS evidence

The same thesis implemented Minimax, Monte Carlo Tree Search, and a hand-built StrategyAI.

Important configuration-specific results (300-game samples):

- **MCTS, 500 iterations, C=0.2, heavy playouts** reported **87% ±3.8%** against depth-3 Minimax.
- The same 500-iteration MCTS reported **70.3% ±5.2%** against a Minimax player using 500 ms per move.
- A separate table evaluating 500-ms Minimax against a 5,000-iteration MCTS showed Minimax winning only **2.7% ±1.8%**, i.e. that particular 5,000-iteration MCTS was overwhelmingly stronger in that test.

These are results from one implementation, hardware/software setup, evaluator, and playout policy. They are useful evidence that search is viable for Azul—not universal benchmark truth.

## 8.3 Heavy playouts

The thesis uses heuristic-weighted (“heavy”) playouts rather than purely random simulated moves and notes that domain-specific playout strategy can improve play. This aligns with broader MCTS literature: complex games often benefit from domain-specific modifications or hybrid approaches.

For the planned practice tool, this supports using a fast strategic policy during rollouts rather than pure randomness.

---

# 9. Audit of the earlier Azul notes

| Existing claim | Assessment | Revised status |
|---|---|---|
| 5 factories, 4 tiles each in 2p | Official rule | **Keep `[RULE]`** |
| 100 tiles, 20 each color | Official rule | **Keep `[RULE]`** |
| Point differential is the correct 1v1 lens | Strong modeling choice | **Keep `[STRUCTURAL]`**, but distinguish score system from strict algebraic zero-sum |
| “Every turn is strictly zero-sum” | Too strong | **Refine** to competitive zero-sum outcome / differential evaluation |
| Bag tracking can calculate exact probabilities | Correct if inventory is known | **Keep**, add hypergeometric formula |
| Avoid casual partial 4/5 lines | Strong practical heuristic | **Keep `[HEURISTIC]`**, not rule |
| “Take first-player token Round 1; -1 and almost always optimal” | Cost and value are state dependent | **Downgrade to `[TEST]/[HEURISTIC]`** |
| 2.0+ points per placed tile competitive threshold | No reviewed source validates this threshold | **Move to `[TEST]`** |
| Middle column / middle three columns are valuable | Multiple community sources + structural geometry + simplified simulation | **Keep `[HEURISTIC]` / `[EVIDENCE]`** |
| “Center flood trap = 4+ tiles” | Arbitrary fixed threshold | **Replace with absorption capacity** |
| Exact max branching factor ≈120 | Supported by 2021 thesis | **Keep with citation** |
| State space ≈10^42 | Not verified in the sources reviewed | **Do not present as fact yet** |
| MCTS 500 = 68% vs Minimax D3 | Does not match the defended thesis configuration we found | **Correct:** 500-iteration C=0.2 heavy MCTS = 87% ±3.8 vs depth-3 Minimax in that thesis |
| MCTS 5000 = 97% vs Minimax D3 | Source/configuration unclear | **Do not state this exact matchup.** A 5,000-iteration MCTS beat 500-ms Minimax very strongly in the thesis's reciprocal table. |
| DQN weak / Top-k policy accuracy exact percentages | Exact source not established in reviewed materials | **Treat as unverified until source or experiment is attached** |
| WASM evaluator can be exact in <300 ms | Product target, not established fact | **Keep as engineering target** |
| K=200 heuristic rollouts “dramatically” match K=5000 | Not validated in reviewed evidence | **Treat as benchmark hypothesis** |

---

# 10. A practical heuristic evaluation function

For training or move ordering, a useful interpretable score could be:

$$H(s) = D_{\text{score}} + \alpha D_{\text{wallEV}} + \beta D_{\text{capacity}} + \gamma D_{\text{bonus}} + \delta D_{\text{initiative}} - \eta D_{\text{floorRisk}} + \theta D_{\text{trigger}}$$

where each $D$ is **your value minus opponent value**.

Possible features:

### `D_score`
Current point differential.

### `D_wallEV`
Estimated value of complete and partially complete pattern lines based on where the future wall tile will score.

### `D_capacity`
Difference in total or color-specific safe capacity, especially for center colors.

### `D_bonus`
Credible—not merely possible—column/color/row endgame bonus value.

### `D_initiative`
Estimated value of first pick next round minus marginal floor cost of taking the marker.

### `D_floorRisk`
Expected marginal floor penalties from already-visible forced piles.

### `D_trigger`
Value of ending or extending the game given the projected final score.

This should be learned/tuned or experimentally calibrated rather than assigned arbitrary permanent weights.

---

# 11. Research questions worth answering with the practice engine

## H1 — Central opening value

**Question:** How much expected point differential is gained by first wall placements in columns 2–4 compared with columns 1/5, conditioning on equivalent factory availability?

**Method:** Generate symmetric opening states, force candidate first-target regions, then self-play with the same policy thereafter.

## H2 — First-player marker value

**Question:** When is buying initiative worth its marginal floor cost?

**Features:** round, floor occupancy, best opening group next round, opponent threats, current score margin.

**Output:** estimated EV of taking marker versus declining.

## H3 — Row-5 commitment risk

**Question:** How much does a one-tile seed in row 5 reduce future expected margin compared with taking an immediate -1/-2 floor cost?

**Key variable:** color abundance + opponent denial ability.

## H4 — Absorption-capacity advantage

**Question:** Does the toxicity gap $T(c,g)$ predict successful center flood tactics better than raw center pile size?

**Prediction:** yes, substantially.

## H5 — Points-per-wall-placement

**Question:** Is there a meaningful competitive threshold such as the existing “2.0+” claim?

Track:

$$E = \frac{\text{wall-tiling points}}{\text{wall tiles placed}}$$

Then compare $E$ by winning/losing player, round, and rating/agent strength. Do not assume 2.0 beforehand.

## H6 — Game-end control

**Question:** Conditional on score margin and projected bonuses, when does deliberately avoiding a horizontal completion improve win probability?

## H7 — Search horizon

Compare:

- greedy / depth-1,
- depth-3 minimax with action ordering,
- end-of-round MCTS,
- full-game MCTS with stochastic refill sampling.

Measure both strength and explanation quality.

## H8 — Constraint-based placement

**Question:** Does home count $H_p(c)$ predict move quality for pattern-line assignment decisions better than absorption capacity alone?

**Method:** For states where the player must choose which pattern line to assign a drafted color to, compare:

- greedy (choose line with best immediate score),
- capacity-preserving (choose line that maximizes remaining $A_p$ across colors),
- constraint-aware (choose line that maximizes minimum $H_p(c)$ across remaining colors).

**Secondary question:** How often do real game states violate Hall's condition (i.e., contain an infeasible color-to-line matching)?

## H9 — Spill classification

**Question:** Does explicit spill-type classification improve human factory-selection accuracy compared with unstructured evaluation?

**Method:** Present identical board states to players with and without spill annotations. Measure move quality against engine evaluation.

## H10 — Position temperature

**Question:** Can a simple temperature heuristic reliably identify positions where deeper calculation changes the optimal move?

**Method:** For each state in a self-play corpus, compare depth-1 and depth-N best moves. Correlate disagreement rate with temperature features.

**Prediction:** High-temperature states show significantly more depth-1 vs. depth-N disagreement.

## H11 — Risk posture switching

**Question:** At what score margin and game stage should a player switch from "close" to "complicate" (or vice versa)?

**Method:** From self-play data, bin states by margin and round. For each bin, compare conservative policies (short lines, safe picks, trigger-seeking) against aggressive policies (long commitments, contested bonuses, round extension). Identify the crossover where conservative dominates.

**Prediction:** The threshold is not a fixed margin but depends on remaining bonus potential and round number.

---

# 12. Recommended evaluator output for a human practice tool

Rather than “best move = 7.23 EV,” explain moves in human strategic dimensions:

```text
Move A: Take 2 blue from Factory 3 -> row 2
+ completes row 2 this round
+ creates 4-point cross placement
+ preserves row 5 buffer
- pushes 2 red to center
- opponent can then complete row 4

Move B: Take 1 red from center -> row 1
+ denies opponent's row-4 completion
+ reduces red center toxicity
- scores only 1 immediately
- takes first-player marker in -2 floor slot

Estimated margin: B +1.8 over A
Primary reason: denial + reduced opponent capacity outweighs lost wall score
```

This is both more teachable and more debuggable than a single opaque value.

---

# 13. Source hierarchy

## Tier 1 — Rules / primary research

- Official *Azul* rulebook:  
  https://cdn.svc.asmodee.net/production-nextmove/uploads/sites/4/2024/06/EN-Azul-Rules-Next-Move-web.pdf
- Michal Počatko, *AI for the Board Game Azul*, Charles University, 2021:  
  https://dspace.cuni.cz/handle/20.500.11956/127953?locale-attribute=en
- Chaslot et al., *Monte-Carlo Tree Search: A New Framework for Game AI*, 2008:  
  https://ojs.aaai.org/index.php/AIIDE/article/view/18700
- Świechowski et al., *Monte Carlo Tree Search: a review of recent modifications and applications*:  
  https://arxiv.org/abs/2103.04931

## Tier 2 — structured community evidence

- Board Game Arena *Tips azul*:  
  https://en.doc.boardgamearena.com/Tips_azul

## Tier 3 — useful player analysis / exploratory research

- https://www.reddit.com/r/boardgames/comments/rw06tt/azul_strategy_guide/
- https://www.reddit.com/r/boardgames/comments/tz9qor/azul_strategy_scoring_pacing/
- https://www.reddit.com/r/boardgames/comments/w1jtf6/i_am_good_at_board_games_but_suck_at_azul_advice/
- https://www.reddit.com/r/boardgames/comments/hxodaf/update_i_wrote_my_dissertation_on_azul/

Use Tier 3 to generate hypotheses; use the engine/replay data to decide which survive.
