"""
M1 NumPy 向量化思維 — 課後作業
================================
請完成以下每個函式，用 NumPy 向量化寫法（不要 for-loop）。
完成後 git push，GitHub Actions 會自動批改並顯示成績與解答。

提示：
- np.array, np.where, np.argsort
- 布林遮罩: arr[arr > 10]
- 統計: .sum(), .mean(), .max(), .min()
"""
import numpy as np


# ============================================================
# 🟢 送分題（每題 10 分，共 30 分）
# ============================================================

def green_mean():
    pass
    x = np.array([10, 20, 30, 40, 50])
    return float(x.mean())

def green_double():
    pass
    x = np.array([10, 20, 30, 40, 50])
    return x * 2

def green_filter():
    pass
    x = np.array([10, 20, 30, 40, 50])
    return x[x > 25]
# ============================================================
# 🟡 核心題（每題 15 分，共 45 分）
# 以下函式會接收從 products.csv 讀出的 prices, stocks 陣列
# ============================================================

def yellow_expensive_count(prices):
    pass
    return int((prices > 1000).sum())

def yellow_top3_stock_indices(stocks):
    pass
    return stocks.argsort()[::-1][:3]

def yellow_restock_cost(prices, stocks):
    pass
    mask = prices < 500
    return float((prices[mask] * 50).sum())

# ============================================================
# 🔴 挑戰題（25 分）
# ============================================================

def red_double11_prices(prices, stocks):
    pass
    return np.where(stocks >= 100, prices * 0.7, 
                    np.where(stocks >= 20, prices * 0.9, prices))