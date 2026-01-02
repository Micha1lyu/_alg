from collections import deque

def is_valid(state):
    m, w, g, c = state
    if w == g and m != w:
        return False
    if g == c and m != g:
        return False
    return True

def get_next_states(current_state):
    m, w, g, c = current_state
    moves = []
    new_m = 1 - m
    
    new_state = (new_m, w, g, c)
    if is_valid(new_state):
        moves.append((new_state, "人獨自過河"))
        
    if m == w:
        new_state = (new_m, 1-w, g, c)
        if is_valid(new_state):
            moves.append((new_state, "人帶【狼】過河"))
            
    if m == g:
        new_state = (new_m, w, 1-g, c)
        if is_valid(new_state):
            moves.append((new_state, "人帶【羊】過河"))
            
    if m == c:
        new_state = (new_m, w, g, 1-c)
        if is_valid(new_state):
            moves.append((new_state, "人帶【甘藍菜】過河"))
            
    return moves

def solve_river_crossing():
    start_state = (0, 0, 0, 0)
    goal_state = (1, 1, 1, 1)
    
    queue = deque([(start_state, [])])
    visited = set([start_state])
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path
        
        for next_state, action_desc in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action_desc]))
                
    return None

def print_solution(solution):
    if not solution:
        print("找不到解決方案！")
        return

    print(f"找到解答！總共需要 {len(solution)} 個步驟：\n")
    print(f"{'步驟':<5} | {'動作描述':<20}")
    print("-" * 30)
    
    for i, step in enumerate(solution, 1):
        direction = "->" if i % 2 != 0 else "<-"
        print(f"Step {i} | {step} ({direction})")
        
    print("-" * 30)
    print("成功將所有物品運送到對岸！")

if __name__ == "__main__":
    solution = solve_river_crossing()
    print_solution(solution)
