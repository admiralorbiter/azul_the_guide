"""
Azul Rules Engine & Validation Module
Formal reference implementation of 1v1 Azul rules for validating strategy guide examples and motif puzzles.
"""

from typing import List, Tuple, Dict, Optional, Set

WALL_MATRIX = [
    ['B', 'Y', 'R', 'K', 'W'],  # Row 0
    ['W', 'B', 'Y', 'R', 'K'],  # Row 1
    ['K', 'W', 'B', 'Y', 'R'],  # Row 2
    ['R', 'K', 'W', 'B', 'Y'],  # Row 3
    ['Y', 'R', 'K', 'W', 'B']   # Row 4
]

COLOR_EMOJIS = {
    'B': '🟦',
    'Y': '🟨',
    'R': '🟥',
    'K': '⬛',
    'W': '⬜'
}

COLOR_NAMES = {
    'B': 'Blue',
    'Y': 'Yellow',
    'R': 'Red',
    'K': 'Black',
    'W': 'White'
}

FLOOR_SCHEDULE = [-1, -1, -2, -2, -2, -3, -3]


def get_wall_color(row: int, col: int) -> str:
    """Returns color code ('B','Y','R','K','W') for wall grid position (row, col)."""
    return WALL_MATRIX[row][col]


def get_wall_column_for_color(row: int, color: str) -> int:
    """Returns column index (0..4) where color belongs on wall row."""
    return WALL_MATRIX[row].index(color)


def calc_floor_cost(count: int) -> int:
    """Calculates total floor penalty points for N floor tiles."""
    if count <= 0:
        return 0
    return sum(FLOOR_SCHEDULE[:min(count, 7)])


def score_tile_placement(wall_grid: List[List[bool]], row: int, col: int) -> int:
    """
    Calculates exact score for placing a tile at (row, col) on wall_grid.
    wall_grid is 5x5 boolean matrix including the newly placed tile at (row, col).
    """
    # Horizontal count
    h_count = 1
    # Check left
    c = col - 1
    while c >= 0 and wall_grid[row][c]:
        h_count += 1
        c -= 1
    # Check right
    c = col + 1
    while c < 5 and wall_grid[row][c]:
        h_count += 1
        c += 1

    # Vertical count
    v_count = 1
    # Check up
    r = row - 1
    while r >= 0 and wall_grid[r][col]:
        v_count += 1
        r -= 1
    # Check down
    r = row + 1
    while r < 5 and wall_grid[r][col]:
        v_count += 1
        r += 1

    if h_count > 1 and v_count > 1:
        return h_count + v_count
    elif h_count > 1:
        return h_count
    elif v_count > 1:
        return v_count
    else:
        return 1


def is_legal_line_assignment(
    wall_grid: List[List[bool]],
    line_idx: int,
    color: str,
    line_color: Optional[str],
    line_count: int
) -> Tuple[bool, str]:
    """
    Checks whether drafting `color` into pattern line `line_idx` (0..4) is legal.
    """
    capacity = line_idx + 1

    # Check wall row collision
    col = get_wall_column_for_color(line_idx, color)
    if wall_grid[line_idx][col]:
        return False, f"Line {line_idx+1} cannot accept {COLOR_NAMES[color]} because {color} is already on Wall Row {line_idx+1}."

    # Check remaining capacity
    if line_count >= capacity:
        return False, f"Line {line_idx+1} has 0 remaining capacity (full)."

    # Check line color compatibility
    if line_color is not None and line_color != color:
        return False, f"Line {line_idx+1} holds {COLOR_NAMES[line_color]}, cannot accept {COLOR_NAMES[color]}."

    return True, ""


def check_active_round_legality(wall_grid: List[List[bool]]) -> Tuple[bool, str]:
    """
    Checks that no horizontal row is completely filled mid-round (game ends after wall-tiling).
    """
    for r in range(5):
        if all(wall_grid[r]):
            return False, f"Wall Row {r+1} is complete — game would already have ended prior to this draft round!"
    return True, ""
