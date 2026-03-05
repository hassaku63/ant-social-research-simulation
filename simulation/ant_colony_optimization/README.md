# Ant Colony Optimization シミュレーション

## 概要

このモジュールは、蟻の行動システムを応用した **アント・コロニー最適化（ACO）** アルゴリズムを実装し、**巡回セールスマン問題（TSP: Traveling Salesman Problem）** を解く。

Marco Dorigo が1992年に提案した元祖 ACO アルゴリズム「Ant System（AS）」に基づく実装。

---

## アルゴリズムの背景

### なぜ TSP を選んだか

TSP は「N個の都市を全て一度ずつ訪れ、出発点に戻る最短経路を求める」問題で、組み合わせ爆発的な計算量（N! 通りの候補）から NP困難に分類される。この問題はACOが最初に成功裏に適用された問題であり、アルゴリズムの能力を明確に検証できる。

### 蟻の行動との対応

| 蟻の自然行動 | ACOアルゴリズムの実装 |
|------------|---------------------|
| 蟻が経路上にフェロモンを置く | 各イテレーションで優れたルートのエッジにフェロモンを付加 |
| フェロモンが時間とともに蒸発する | 毎イテレーション、全エッジのフェロモンを `(1 - ρ)` 倍に減衰 |
| 蟻は濃いフェロモンの経路を好む | 移動確率が `τ^α * η^β` に比例（τ: フェロモン、η: ヒューリスティック） |
| 短い経路はより多くの蟻が通る | 短いルートの蟻はより多くのフェロモンを付加（`Q/L_k` に比例） |

---

## ファイル構成

```
simulation/ant_colony_optimization/
├── aco.py            # ACOアルゴリズム本体
├── requirements.txt  # Python依存パッケージ
├── README.md         # 本ドキュメント
└── tests/
    └── test_aco.py   # 単体テスト
```

---

## セットアップ

```bash
# プロジェクトルートから
pip install -r simulation/ant_colony_optimization/requirements.txt
```

---

## 使い方

### 基本的な使い方

```python
from simulation.ant_colony_optimization.aco import AntColonyOptimizer, ACOConfig

# 都市の座標リストを定義（(x, y) のリスト）
cities = [
    (0.0, 0.0),
    (1.0, 0.0),
    (1.0, 1.0),
    (0.0, 1.0),
]

# デフォルト設定で実行
optimizer = AntColonyOptimizer(cities)
result = optimizer.run()

print(f"最良ツアー: {result.best_tour}")
print(f"ツアー距離: {result.best_distance:.4f}")
```

### 設定のカスタマイズ

```python
from simulation.ant_colony_optimization.aco import AntColonyOptimizer, ACOConfig

config = ACOConfig(
    n_ants=30,          # アントの数（多いほど探索が広い）
    n_iterations=200,   # イテレーション数
    alpha=1.0,          # フェロモンの重み（大きいほどフェロモン追従）
    beta=3.0,           # ヒューリスティックの重み（大きいほど近くを優先）
    rho=0.5,            # フェロモン蒸発率（大きいほど忘れやすい）
    q=100.0,            # フェロモン付加量の定数
    seed=42,            # 再現性のためのランダムシード
)

cities = [(0, 0), (2, 0), (2, 2), (0, 2), (1, 1)]
optimizer = AntColonyOptimizer(cities, config)
result = optimizer.run()

print(f"最良ツアー: {result.best_tour}")
print(f"ツアー距離: {result.best_distance:.4f}")
print(f"収束履歴（最初の10イテレーション）: {result.history[:10]}")
```

---

## テストの実行

```bash
# プロジェクトルートから
pytest simulation/ant_colony_optimization/tests/ -v
```

---

## アルゴリズムの詳細

### パラメータ説明

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| `n_ants` | 20 | 各イテレーションで動かすアントの数 |
| `n_iterations` | 100 | アルゴリズムを繰り返す回数 |
| `alpha` (α) | 1.0 | フェロモンの影響度（大きいほど強く追従） |
| `beta` (β) | 2.0 | 距離ヒューリスティックの影響度（大きいほど近くを選びやすい） |
| `rho` (ρ) | 0.5 | フェロモン蒸発率（0〜1、大きいほど速く蒸発） |
| `q` | 100.0 | フェロモン付加量の定数（ツアー距離の逆数に掛ける） |
| `initial_pheromone` | 1.0 | フェロモンの初期値 |
| `seed` | None | 乱数シード（再現性のため） |

### フェロモン更新式

```
τ_ij(t+1) = (1 - ρ) * τ_ij(t) + Σ_k Δτ_ij^k

Δτ_ij^k = Q / L_k  （アントkがエッジ(i,j)を通った場合）
         = 0         （通らなかった場合）
```

- `τ_ij`: エッジ(i,j)のフェロモン濃度
- `ρ`: 蒸発率
- `L_k`: アントkのツアー総距離

### 移動確率

```
p_ij^k = [τ_ij]^α * [η_ij]^β / Σ_l∈N_k [τ_il]^α * [η_il]^β
```

- `η_ij = 1 / d_ij`: ヒューリスティック情報（距離の逆数）
- `N_k`: アントkがまだ訪問していない都市の集合
