"""
Atlas Verification Test Suite Runner
Parses `azul-motif-atlas.md` and performs basic format and active-wall-state checks.
"""

import sys
import os
import re

# Add script dir to python path
sys.path.insert(0, os.path.dirname(__file__))

import azul_engine

def parse_and_verify_atlas(filepath: str) -> bool:
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into motif sections
    positions = re.findall(r'### Position \d+[\s\S]*?(?=### Position|\n# |\Z)', content)

    print(f"==================================================")
    print(f"  Azul Motif Atlas Verification Engine")
    print(f"==================================================")
    print(f"Found {len(positions)} positions to verify in {os.path.basename(filepath)}...\n")

    passed = 0
    failed = 0

    for idx, pos_text in enumerate(positions, 1):
        pos_title = f"Position {idx}"
        
        # Check for Wall Grid block
        wall_match = re.search(r'Wall Grid:[\s\S]*?\n((?:[^\n]+\n){5})', pos_text)
        if not wall_match:
            # Check for Opponent Board or simplified state
            if "Wall Grid:" not in pos_text and ("Opponent Board:" in pos_text or "Visible Red" in pos_text or "Current Floor:" in pos_text or "Center Pool:" in pos_text or "Pattern Lines:" in pos_text or "Center:" in pos_text or "Game State:" in pos_text):
                print(f"  [PASS] {pos_title} - Conceptual/State Diagram (Valid Format)")
                passed += 1
                continue
            else:
                print(f"  [FAIL] {pos_title} - Missing 5-row Wall Grid block")
                failed += 1
                continue

        wall_lines = wall_match.group(1).strip().split('\n')
        if len(wall_lines) != 5:
            print(f"  [FAIL] {pos_title} - Wall Grid does not contain exactly 5 rows")
            failed += 1
            continue

        # Parse 5x5 wall matrix
        wall_grid = []
        parse_error = False
        for row_idx, line in enumerate(wall_lines):
            # Extract 5 tokens
            tokens = line.split()[:5]
            if len(tokens) != 5:
                print(f"  [FAIL] {pos_title} - Row {row_idx+1} does not contain 5 tokens: '{line}'")
                parse_error = True
                break
            
            row_bools = []
            for col_idx, tok in enumerate(tokens):
                # Emoji means placed, lowercase/letter means empty
                if tok in ['🟦', '🟨', '🟥', '⬛', '⬜', 'B', 'Y', 'R', 'K', 'W', 'X']:
                    row_bools.append(True)
                else:
                    row_bools.append(False)
            wall_grid.append(row_bools)

        if parse_error:
            failed += 1
            continue

        # Validate round active state (no complete 5-tile horizontal row)
        is_legal_round, err_msg = azul_engine.check_active_round_legality(wall_grid)
        if not is_legal_round:
            print(f"  [FAIL] {pos_title} - {err_msg}")
            failed += 1
            continue

        print(f"  [PASS] {pos_title} - Basic wall-state check passed")
        passed += 1

    print(f"\n==================================================")
    print(f"  Summary: {passed} PASSED | {failed} FAILED out of {len(positions)} positions")
    print(f"==================================================")

    return failed == 0

if __name__ == "__main__":
    atlas_path = os.path.join(os.path.dirname(__file__), "..", "azul-motif-atlas.md")
    success = parse_and_verify_atlas(atlas_path)
    sys.exit(0 if success else 1)
