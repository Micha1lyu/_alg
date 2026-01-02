def min_edit_distance(word1, word2):
    """
    計算兩個字串之間的最小編輯距離 (Levenshtein Distance)
    :param word1: 來源字串
    :param word2: 目標字串
    :return: 最小操作次數
    """
    m = len(word1)
    n = len(word2)

    # 1. 建立一個 (m+1) x (n+1) 的表格 (DP Table)
    # dp[i][j] 代表 word1 的前 i 個字 變換成 word2 的前 j 個字 需要的最少步數
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 2. 初始化邊界條件 (Base Cases)
    # 如果 word2 是空的，word1 需要刪除所有字母變成空
    for i in range(m + 1):
        dp[i][0] = i
    # 如果 word1 是空的，需要插入 word2 的所有字母
    for j in range(n + 1):
        dp[0][j] = j

    # 3. 開始填表 (由左至右，由上至下)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            
            # 情況 A: 字母相同 (不用做任何事)
            # 注意：字串索引是從 0 開始，所以要用 i-1 和 j-1
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            
            # 情況 B: 字母不同 (取三種操作的最小值 + 1)
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # 刪除 (Delete): 來源少一個字，看能否變成目標
                    dp[i][j - 1],    # 插入 (Insert): 來源不變，假裝已經變成了目標的前 j-1 個字
                    dp[i - 1][j - 1] # 替換 (Replace): 兩個都退一步
                )

    # 4. 回傳右下角的數字，即為最終答案
    return dp[m][n]

# --- 測試範例 ---
s1 = "horse"
s2 = "ros"
distance = min_edit_distance(s1, s2)

print(f"'{s1}' 轉換成 '{s2}' 的最小編輯距離為: {distance}")
# 預期輸出: 3 
# (解釋: horse -> rorse (替換 h->r) -> rose (刪除 r) -> ros (刪除 e))
