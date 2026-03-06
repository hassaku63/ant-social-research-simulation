# 調査タスク: Ant Colony Optimization (ACO) 深掘り調査

## タスク概要

**目標**: ACOのアルゴリズム体系を深掘り調査し、理論的基盤・主要バリエーション・収束性・パラメータ設計の知見を整理する。既存の概要レベル調査（`docs/research/01_ant_behavior_systems.md`, `03_applications.md`）を補完する深掘り資料を作成する。

**スコープ**:
- 調査すること:
  - ACOの理論的基盤（自然界の蟻の行動からアルゴリズムへの定式化）
  - 主要バリエーション（AS, ACS, MMAS, Rank-Based AS 等）の比較
  - 収束性の理論的分析
  - パラメータ（alpha, beta, rho 等）の影響と設計指針
  - 本リポジトリの既存実装（`simulation/ant_colony_optimization/`）との対応
- 調査しないこと（除外事項）:
  - 他メタヒューリスティック（PSO, GA等）との網羅的比較
  - ACO実装コードの改修・拡張
  - TSP以外の応用問題への詳細な適用手法

**成果物**:
- [x] `docs/research/topics/aco/README.md`（調査ドキュメント）
- [x] `docs/research/references.md` の新規作成
- [x] `docs/research/index.md` の新規作成
- [x] `docs/masterplan.md` のステータス更新

**関連する既存調査**:
- [`docs/research/01_ant_behavior_systems.md`](../../01_ant_behavior_systems.md) — 蟻の行動メカニズム概要
- [`docs/research/03_applications.md`](../../03_applications.md) — ACO応用事例の概要

---

## 仕様検討（ステップ2）

### 調査項目

| # | 調査項目 | 優先度 | 状態 |
|---|---------|--------|------|
| 1 | ACOの理論的基盤（自然界からアルゴリズムへ） | 高 | 完了 |
| 2 | Ant System (AS) の詳細アルゴリズム | 高 | 完了 |
| 3 | 主要バリエーション（ACS, MMAS, Rank-Based AS） | 高 | 完了 |
| 4 | 収束性の理論的分析 | 中 | 完了 |
| 5 | パラメータの影響と設計指針 | 中 | 完了 |
| 6 | 本リポジトリ実装との対応 | 中 | 完了 |

### 出典選定基準

- 一次資料（査読論文・学術書）を優先する
- Dorigoらの原著論文・教科書を核とする
- 公開年: 特に制限なし（1991年の原著から最新のサーベイまで）
- 言語: 日本語・英語

### 整理方法

- ドキュメント形式: Markdown
- 保存先: `docs/research/topics/aco/`
- 既存概要ドキュメントとの差分（深掘り部分）を明確化する

---

## 実行（ステップ3）

### 調査記録

| 日時 | 実施内容 | 主な発見 |
|------|---------|---------|
| 2026-03-06 | ACO全体の調査・ドキュメント作成 | AS/ACS/MMAS の設計思想の違いが明確化。探索と活用のバランス制御が各バリエーションの核心 |

### 参照した資料

| タイトル | 著者 | 年 | URL/DOI |
|---------|------|----|---------|
| Optimization, Learning and Natural Algorithms (PhD Thesis) | Dorigo, M. | 1992 | Politecnico di Milano |
| Ant Colony System: A Cooperative Learning Approach to the Traveling Salesman Problem | Dorigo, M. & Gambardella, L.M. | 1997 | IEEE Trans. Evol. Comput. 1(1):53-66 |
| MAX-MIN Ant System | Stutzle, T. & Hoos, H.H. | 2000 | Future Generation Computer Systems 16(8):889-914 |
| Ant Colony Optimization | Dorigo, M. & Stutzle, T. | 2004 | MIT Press (ISBN: 978-0262042192) |
| Convergence of Ant Colony Optimization on the TSP | Stutzle, T. & Dorigo, M. | 2002 | Ants 2002, LNCS 2463 |
| The self-organizing exploratory pattern of the Argentine ant | Deneubourg, J.L. et al. | 1990 | Journal of Insect Behavior 3:159-168 |

---

## 検証（ステップ4）

### 品質チェックリスト

- [x] 出典（著者・年・タイトル・URL/DOI）が明記されている
- [x] 一次資料を少なくとも1件参照している
- [x] メカニズムが具体的に説明されている
- [x] 応用事例が1件以上記載されている
- [x] 関連トピックへのリンクが含まれている
- [x] 振り返りが記録されている

### 評価結果

合格 — 全チェック項目を満たす。

---

## 振り返り（ステップ5）

### うまくいったこと

- 既存概要ドキュメントとの差分を明確にし、深掘り部分に集中できた
- バリエーション間の設計思想の違いを比較表で整理したことで構造が明確になった

### 課題・改善点

- 収束性の理論的分析は数学的証明の詳細までは踏み込めなかった（スコープ的に適切ではあるが）
- 実験的なパラメータ比較データは含められなかった（シミュレーションタスクで補完可能）

### 新たに生まれた疑問・次のアクション

- 本リポジトリのAS実装をACSやMMASに拡張するシミュレーションタスクが有意義
- スティグマジー調査（次の高優先度タスク）でACOとの理論的接続を深められる
- パラメータチューニングの実験をシミュレーション側で実施する価値がある

### ツール・手法の評価

- Dorigoの2004年教科書がACO全体像の把握に最も有効だった
- 個別論文は各バリエーションの詳細理解に必要
