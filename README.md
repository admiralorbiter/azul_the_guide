# Competitive Azul Strategy Suite

**Scope:** Original *Azul*, standard colored wall, primarily **2-player / 1v1** play.  
**Research refresh:** 2026-08-10.

This suite turns the existing Azul notes into a practical strategy system while separating:

- **`[RULE]`** — supported directly by the official rulebook.
- **`[STRUCTURAL]`** — follows from the rules or simple mathematics.
- **`[HEURISTIC]`** — useful competitive advice, but position-dependent rather than universally optimal.
- **`[EVIDENCE]`** — backed by a cited simulation, thesis, or substantial community analysis.
- **`[TEST]`** — plausible claim worth validating with replay data or the practice engine.

## Documents

1. **[azul-motif-atlas.md](./azul-motif-atlas.md)** — A pattern-recognition companion: 11 named strategic motifs across 4 families with concrete board positions, multiple-choice puzzles, answers, and explanations. The tactics book for Azul.
2. **[azul-1v1-strategy-guide.md](./azul-1v1-strategy-guide.md)** — The main play guide: move selection, wall geometry, pattern-line management, factory/center tactics, denial, initiative, bag tracking, phase strategy, and endgame calculation. Includes the compressed move algorithm (THREAT → TAKE+SPILL → FLEX → TAIL) and the unified flexibility framework (Capacity → Choice → Collision).
3. **[azul-training-playbook.md](./azul-training-playbook.md)** — A deliberate-practice program: drills, post-game review, measurable statistics, and experiments that can later feed the Rust/WASM practice tool.
4. **[azul-strategy-math-and-research.md](./azul-strategy-math-and-research.md)** — Formalizes the game with useful quantities such as absorption capacity, factory residue vectors, point-differential evaluation, exact bag probabilities, and a claim audit of earlier notes.

## Learning path

The repository is designed for progressive depth:

1. **Start with the Motif Atlas** ([`azul-motif-atlas.md`](./azul-motif-atlas.md)) — Build visual pattern recognition across 11 core and advanced motifs.
2. **Graduate to the Strategy Guide** ([`azul-1v1-strategy-guide.md`](./azul-1v1-strategy-guide.md)) — Learn the 4-step decision algorithm, flexibility framework, and phase strategies.
3. **Use the Training Playbook** ([`azul-training-playbook.md`](./azul-training-playbook.md)) — Build game habits with targeted drills and review templates.
4. **Consult Math & Research** ([`azul-strategy-math-and-research.md`](./azul-strategy-math-and-research.md)) — Explore formal definitions, evaluator features, and research hypotheses.

## The five ideas to learn first

If you only have ten minutes, start here:

1. **Play the margin, not your board in isolation.** In 1v1, a move that gains 2 while preventing 6 is often better than a move that scores 4 for you.
2. **Protect flexibility.** Rows 4 and 5 are both scoring projects *and* your largest buffers for absorbing ugly center piles.
3. **Draft the leftovers.** Every factory pick also pushes its non-selected colors into the center. Evaluate the pile you create, not only the tiles you take.
4. **Build adjacency infrastructure.** Central wall positions and connected shapes create more ways for future placements to score in both directions. Central is an option-value heuristic, not an absolute opening law.
5. **Solve the end of the round exactly.** As the number of remaining groups becomes small, stop using broad heuristics and calculate the move/reply sequence, forced overflow, first-player marker, and final pick.

## Research base

### Primary / high-confidence

- Next Move / Plan B Games, **official Azul rulebook**:  
  https://cdn.svc.asmodee.net/production-nextmove/uploads/sites/4/2024/06/EN-Azul-Rules-Next-Move-web.pdf
- Michal Počatko, **AI for the Board Game Azul**, Charles University bachelor thesis, defended 2021:  
  https://dspace.cuni.cz/handle/20.500.11956/127953?locale-attribute=en
- Guillaume Chaslot et al., **Monte-Carlo Tree Search: A New Framework for Game AI**, AIIDE 2008:  
  https://ojs.aaai.org/index.php/AIIDE/article/view/18700

### Competitive/community evidence — useful, not authoritative

- Board Game Arena, **Tips azul**:  
  https://en.doc.boardgamearena.com/Tips_azul
- Community competitive guide:  
  https://www.reddit.com/r/boardgames/comments/rw06tt/azul_strategy_guide/
- Strategy/scoring discussion emphasizing wall-tiling order and adjacency:  
  https://www.reddit.com/r/boardgames/comments/tz9qor/azul_strategy_scoring_pacing/
- Strategy discussion on central columns, negatives, and crosshatching:  
  https://www.reddit.com/r/boardgames/comments/w1jtf6/i_am_good_at_board_games_but_suck_at_azul_advice/
- Undergraduate placement-simulation project and its limitations:  
  https://www.reddit.com/r/boardgames/comments/hxodaf/update_i_wrote_my_dissertation_on_azul/

## How to use the suite

For playing better immediately, read the main guide through **The Move Algorithm**, **Absorption Capacity**, and **Endgame**. Then play 5–10 games using only the checklist in the training playbook. The math/research document is for validating why the heuristics work and for turning them into features for an evaluator later.

## Verification & Tooling

The repository includes a standalone Python rules engine and verification test suite to ensure that all board positions in the Motif Atlas and strategy guides strictly adhere to standard Azul rules and mechanics:

```bash
python scripts/verify_atlas.py
```

The current validator performs basic wall-state parsing and checks that no horizontal row is already complete.
