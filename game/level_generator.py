import random
from utils.constants import ROTATIONS, NEIGHBOURS, DIRECTIONS

def in_bounds(x, y, size):
    return 0 <= x < size and 0 <= y < size

def classify_tile(conns):
    for rotation, connections in NEIGHBOURS.items():
        if conns == connections:
            for cell_type, rotations in ROTATIONS.items():
                if rotation in rotations:
                    return cell_type

    print(f"Unknown: {conns}")
    return "cross"

def add_cycles(conns, num_cycles):
    size = len(conns)
    added = 0
    attempts = 0
    max_attempts = num_cycles * 20
    
    while added < num_cycles and attempts < max_attempts:
        attempts += 1
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        
        dirs = list(DIRECTIONS.items())
        random.shuffle(dirs)
        
        for d, (dx, dy, opposite) in dirs:
            nx, ny = x + dx, y + dy
            
            if in_bounds(nx, ny, size) and d not in conns[y][x]:
                conns[y][x].add(d)
                conns[ny][nx].add(opposite)
                added += 1
                break
    
    return conns

def pick_random_cells(size, count, avoid=None):
    all_cells = [(x, y) for y in range(size) for x in range(size)]
    
    if avoid:
        all_cells = [c for c in all_cells if c not in avoid]

    random.shuffle(all_cells)
    return all_cells[:count]

def generate_spanning_tree_with_dead_ends(size, num_dead_ends):
    if num_dead_ends > size * size - 1:
        num_dead_ends = size * size - 1
    
    grid = [[set() for _ in range(size)] for _ in range(size)]
    all_cells = [(x, y) for y in range(size) for x in range(size)]
    random.shuffle(all_cells)
    
    start = all_cells[0]
    stack = [start]
    visited = {start}
    leaf_candidates = []
    
    while len(visited) < size * size:
        if not stack:
            unvisited = [c for c in all_cells if c not in visited]
            if unvisited:
                stack.append(unvisited[0])
                visited.add(unvisited[0])
        
        x, y = stack[-1]
        dirs = list(DIRECTIONS.items())
        random.shuffle(dirs)
        
        found = False
        for d, (dx, dy, opposite) in dirs:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny, size) and (nx, ny) not in visited:
                grid[y][x].add(d)
                grid[ny][nx].add(opposite)
                visited.add((nx, ny))
                stack.append((nx, ny))
                found = True
                break
        
        if not found:
            if len(grid[y][x]) == 1:
                leaf_candidates.append((x, y))
            stack.pop()
    
    leaf_nodes = leaf_candidates[:num_dead_ends]
    
    for y in range(size):
        for x in range(size):
            if (x, y) not in leaf_nodes and len(grid[y][x]) < 2:
                dirs = list(DIRECTIONS.items())
                random.shuffle(dirs)
                
                for d, (dx, dy, opposite) in dirs:
                    nx, ny = x + dx, y + dy
                    
                    if in_bounds(nx, ny, size) and d not in grid[y][x]:
                        grid[y][x].add(d)
                        grid[ny][nx].add(opposite)
                        if len(grid[y][x]) >= 2:
                            break
    
    return grid, leaf_nodes

def generate_map(size, source_count, house_count, cycles=15):
    conns, dead_ends = generate_spanning_tree_with_dead_ends(size, house_count)
    conns = add_cycles(conns, cycles)
    
    houses = dead_ends[:house_count]
    available_cells = [(x, y) for y in range(size) for x in range(size) if (x, y) not in houses]
    random.shuffle(available_cells)
    sources = available_cells[:source_count]
    
    grid = []
    for y in range(size):
        grid.append([])
        
        for x in range(size):
            if (x, y) in sources:
                grid[-1].append("power_source")
            elif (x, y) in houses:
                grid[-1].append("house")
            else:
                grid[-1].append(classify_tile(conns[y][x]))

    return grid