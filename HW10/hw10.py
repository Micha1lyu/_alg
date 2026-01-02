import random

# ==========================================
# 方法一：遞迴黎曼積分 (Recursive Riemann Sum)
# ==========================================
def riemann_integral_nd(func, bounds, steps=10):
    """
    計算 n 維黎曼積分 (使用中點法則 Middle Riemann Sum 以提高精度)。
    
    :param func: 被積函數 f(x)，接受一個 list 作為參數
    :param bounds: 積分範圍，格式為 list of tuples，例如 [(0, 1), (0, 1)] 代表 2維
    :param steps: 每個維度切成幾份 (預設 10)
    :return: 積分結果
    """
    n = len(bounds)
    
    # 計算每個維度的步長 (dx, dy, dz...)
    deltas = [(b - a) / steps for a, b in bounds]
    
    # 計算體積元素 dV = dx * dy * dz ...
    dv = 1.0
    for d in deltas:
        dv *= d

    def recursive_sum(current_dim, current_coords):
        # Base Case: 如果已經深入到最後一個維度，計算函數值
        if current_dim == n:
            return func(current_coords)
        
        # Recursive Step: 在當前維度遍歷
        start, _ = bounds[current_dim]
        delta = deltas[current_dim]
        total_value = 0.0
        
        for i in range(steps):
            # 使用中點法則 (Midpoint Rule)，取區間中心點
            coord = start + (i + 0.5) * delta
            
            # 遞迴呼叫下一層
            # current_coords + [coord] 會建立新的座標列表傳下去
            total_value += recursive_sum(current_dim + 1, current_coords + [coord])
            
        return total_value

    # 開始遞迴，從第 0 維，空座標開始
    sum_f = recursive_sum(0, [])
    
    return sum_f * dv

# ==========================================
# 方法二：蒙地卡羅積分 (Monte Carlo Integration)
# ==========================================
def monte_carlo_integral_nd(func, bounds, num_samples=100000):
    """
    使用蒙地卡羅方法計算 n 維積分。
    
    原理: Integral = V * <f>
    其中 V 是總體積，<f> 是函數在區域內的平均值。
    """
    n = len(bounds)
    
    # 1. 計算總體積 Volume = (b1-a1) * (b2-a2) * ...
    volume = 1.0
    for a, b in bounds:
        volume *= (b - a)
    
    total_value = 0.0
    
    # 2. 隨機採樣並累加
    for _ in range(num_samples):
        # 在 bounds 範圍內生成隨機座標點
        random_point = [random.uniform(a, b) for a, b in bounds]
        total_value += func(random_point)
    
    # 3. 計算平均值
    average_value = total_value / num_samples
    
    return volume * average_value

# ==========================================
# 測試與驗證
# ==========================================
if __name__ == "__main__":
    # 定義一個測試函數：3維球體半徑平方 f(x,y,z) = x^2 + y^2 + z^2
    # 積分範圍：x, y, z 都在 [0, 1]
    # 理論值計算：
    # Integral(x^2)dx from 0 to 1 is 1/3.
    # Triple integral (x^2 + y^2 + z^2) over unit cube 
    # = 1*1*(1/3) + 1*1*(1/3) + 1*1*(1/3) = 1.0
    
    def test_func(coords):
        return sum(x**2 for x in coords)

    bounds_3d = [(0, 1), (0, 1), (0, 1)] # 3維
    
    print("--- 測試函數: f(x) = sum(x_i^2) 在 3維單位立方體 [0,1]^3 ---")
    print("理論值應該為: 1.0")
    print("-" * 30)

    # 1. 測試黎曼積分
    # 注意：steps=100 在 3維就是 100^3 = 1,000,000 次運算
    steps = 50 
    riemann_result = riemann_integral_nd(test_func, bounds_3d, steps=steps)
    print(f"[黎曼積分] 切分={steps}^3 : {riemann_result:.5f}")

    # 2. 測試蒙地卡羅
    samples = 100000
    mc_result = monte_carlo_integral_nd(test_func, bounds_3d, num_samples=samples)
    print(f"[蒙地卡羅] 樣本={samples} : {mc_result:.5f}")

    print("\n--- 高維度壓力測試 (5維) ---")
    # 5維積分，黎曼積分若 steps=20，運算量為 20^5 = 3,200,000
    bounds_5d = [(0, 1)] * 5
    print(f"[黎曼積分] 5維, steps=10 (10^5 ops): {riemann_integral_nd(test_func, bounds_5d, steps=10):.5f}")
    print(f"[蒙地卡羅] 5維, samples=100000:   {monte_carlo_integral_nd(test_func, bounds_5d, num_samples=100000):.5f}")
