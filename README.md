# ant-social-research-simulation

蟻・蜂の集団行動システムの調査と、そのアルゴリズム応用のシミュレーションを行うプロジェクト。

---

## テーマ

### テーマ1：先行研究調査とドキュメント化

蟻・蜂の行動システムおよびその人間社会・ソフトウェアへの応用事例を調査し、なぜ・いかにそれらが効果的に機能するかをまとめる。

📄 **[調査ドキュメント](docs/research/)**

| ドキュメント | 内容 |
|-------------|------|
| [01_ant_behavior_systems.md](docs/research/01_ant_behavior_systems.md) | 蟻の行動システム（スティグマジー、フェロモン、自己組織化） |
| [02_bee_behavior_systems.md](docs/research/02_bee_behavior_systems.md) | 蜂の行動システム（ワグルダンス、民主的意思決定、分業） |
| [03_applications.md](docs/research/03_applications.md) | 人間社会・ソフトウェアへの応用事例 |
| [04_summary.md](docs/research/04_summary.md) | 調査まとめ・群知能の本質的洞察・参考文献 |

---

### テーマ2：シミュレーション実装

蟻・蜂の行動システムを応用することが有用な事案を検討し、概念検討・仕様策定・実装・検証のサイクルを実施する。

#### 第1弾：アント・コロニー最適化（ACO）による巡回セールスマン問題（TSP）の解法

🐜 **[simulation/ant_colony_optimization/](simulation/ant_colony_optimization/)**

蟻のフェロモントレイル行動をアルゴリズムとして実装し、NP困難な組み合わせ最適化問題（TSP）を解く。

**クイックスタート:**

```bash
pip install -r simulation/ant_colony_optimization/requirements.txt

python -c "
from simulation.ant_colony_optimization.aco import AntColonyOptimizer, ACOConfig

cities = [(0,0), (1,0), (1,1), (0,1), (0.5, 0.5)]
config = ACOConfig(n_ants=20, n_iterations=100, seed=42)
result = AntColonyOptimizer(cities, config).run()
print(f'最良ツアー: {result.best_tour}')
print(f'ツアー距離: {result.best_distance:.4f}')
"
```

**テストの実行:**

```bash
pytest simulation/ant_colony_optimization/tests/ -v
```

---

## プロジェクト構成

```
ant-social-research-simulation/
├── README.md
├── docs/
│   └── research/
│       ├── 01_ant_behavior_systems.md
│       ├── 02_bee_behavior_systems.md
│       ├── 03_applications.md
│       └── 04_summary.md
└── simulation/
    └── ant_colony_optimization/
        ├── aco.py
        ├── requirements.txt
        ├── README.md
        └── tests/
            └── test_aco.py
```