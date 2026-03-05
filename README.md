# ant-social-research-simulation

蟻・蜂などの社会性昆虫の集団知性（Swarm Intelligence）を研究・応用するためのリポジトリです。

## 目的

社会性昆虫（蟻・蜂）が、個体としては単純なルールに従いながら、集団として驚くほど効率的な行動を実現するメカニズムを深く理解し、そのモデルを人間社会やソフトウェアに応用することを目的としています。

---

## 2つの研究テーマ

### テーマ1: 先行研究の調査・整理

蟻・蜂の行動システムに関する先行研究を収集・整理し、人間社会やソフトウェアへの応用事例を調査します。なぜ・いかにそれが機能するかを明らかにし、ドキュメントとしてまとめます。

📄 **[調査ドキュメント](docs/research/)**

| ドキュメント | 内容 |
|-------------|------|
| [01_ant_behavior_systems.md](docs/research/01_ant_behavior_systems.md) | 蟻の行動システム（スティグマジー、フェロモン、自己組織化） |
| [02_bee_behavior_systems.md](docs/research/02_bee_behavior_systems.md) | 蜂の行動システム（ワグルダンス、民主的意思決定、分業） |
| [03_applications.md](docs/research/03_applications.md) | 人間社会・ソフトウェアへの応用事例 |
| [04_summary.md](docs/research/04_summary.md) | 調査まとめ・群知能の本質的洞察・参考文献 |

---

### テーマ2: シミュレーション・応用実装

蟻・蜂の行動システムを応用できる実際の問題を検討し、コンセプト検討→計画→仕様策定→実装→検証のサイクルを反復します。

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

## タスクサイクル

すべてのタスクは以下のサイクルを反復します:

```
計画の言語化 → 詳細化（仕様検討）→ 実行（実装）→ 検証 → 振り返りを記録
```

詳細: [`docs/workflow/task-cycle.md`](docs/workflow/task-cycle.md)

---

## ディレクトリ構成

```
.
├── docs/
│   ├── masterplan.md            # プロジェクト全体の計画・ステータス管理
│   ├── ai-guidelines-master.md  # AIガイドラインのマスター文書
│   ├── research/                # テーマ1: 先行研究・調査ドキュメント
│   ├── simulation/              # テーマ2: シミュレーション設計・仕様
│   └── workflow/                # タスク進行ガイドライン・テンプレート
├── simulation/                  # 実装コード
└── README.md
```

---

## AI アシスタント向けガイドライン

ガイドラインのマスター文書: [`docs/ai-guidelines-master.md`](docs/ai-guidelines-master.md)

各AIシステムが参照するガイドラインファイル（マスター文書から派生）:

| システム | 常時有効（システムプロンプト）| 必要時参照 |
|---------|--------------------------|------------|
| GitHub Copilot | `.github/copilot-instructions.md` | `docs/` 配下の各ドキュメント |
| Claude Code | `CLAUDE.md` | `docs/` 配下の各ドキュメント |
| OpenAI Codex / 汎用エージェント | `AGENTS.md` | `docs/` 配下の各ドキュメント |
| Amazon Kiro | `.kiro/steering/project.md` | `.kiro/specs/` 配下の仕様ファイル |
