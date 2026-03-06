# 調査タスク: スティグマジー（Stigmergy）深掘り調査

## タスク概要

**目標**: スティグマジーの理論的基盤を深掘りし、定義・分類・メカニズム・ACOとの理論的接続・ソフトウェアや人間社会への応用を整理する。

**スコープ**:
- 調査すること:
  - スティグマジーの定義と歴史（Grasse 1959）
  - 分類（定量的/定性的）
  - 自然界の事例（蟻・シロアリ・蜂等）
  - ACOとの理論的接続
  - ソフトウェア/Web/人間社会への応用
- 調査しないこと（除外事項）:
  - ACOアルゴリズム自体の再説明（ACO調査で完了済み）
  - 各応用の実装詳細

**成果物**:
- [x] `docs/research/topics/stigmergy/README.md`（調査ドキュメント）
- [x] `docs/research/references.md` への追記
- [x] `docs/research/index.md` の更新
- [x] `docs/masterplan.md` のステータス更新

**関連する既存調査**:
- [`docs/research/01_ant_behavior_systems.md`](../../01_ant_behavior_systems.md) — スティグマジーの概要記述
- [`docs/research/topics/aco/`](../aco/) — ACO深掘り調査（スティグマジーの形式化）

---

## 仕様検討（ステップ2）

### 調査項目

| # | 調査項目 | 優先度 | 状態 |
|---|---------|--------|------|
| 1 | 定義と語源 | 高 | 完了 |
| 2 | 分類（定量的/定性的） | 高 | 完了 |
| 3 | 自然界の事例 | 高 | 完了 |
| 4 | ACOとの理論的接続 | 高 | 完了 |
| 5 | ソフトウェア/Webへの応用 | 中 | 完了 |
| 6 | 人間社会への応用 | 中 | 完了 |
| 7 | なぜ機能するか（考察） | 中 | 完了 |

### 出典選定基準

- 一次資料（査読論文・学術書）を優先する
- Grasse (1959) の原著概念から Heylighen, Elliott 等の応用研究まで
- 言語: 日本語・英語

### 整理方法

- ドキュメント形式: Markdown
- 保存先: `docs/research/topics/stigmergy/`
- ACO調査との重複を避け、相互参照で補完する

---

## 実行（ステップ3）

### 調査記録

| 日時 | 実施内容 | 主な発見 |
|------|---------|---------|
| 2026-03-06 | スティグマジー全体の調査・ドキュメント作成 | 定量的/定性的の分類がACOと巣構築の違いを明確に説明する。ソフトウェア（Wikipedia, Git等）への適用が想像以上に広い |

### 参照した資料

| タイトル | 著者 | 年 | URL/DOI |
|---------|------|----|---------|
| La theorie de la stigmergie | Grasse, P.P. | 1959 | Insectes Sociaux 6:41-80 |
| A Brief History of Stigmergy | Theraulaz, G. & Bonabeau, E. | 1999 | Artificial Life 5(2):97-116 |
| Ant Colony Optimization | Dorigo, M. & Stutzle, T. | 2004 | MIT Press |
| Why is Open Access Development so Successful? | Heylighen, F. | 2007 | Open Source Jahrbuch 2007 |
| Stigmergic Collaboration | Elliott, M. | 2006 | M/C Journal 9(2) |
| Swarm Intelligence: From Natural to Artificial Systems | Bonabeau, E. et al. | 1999 | Oxford University Press |
| Stigmergic epistemology, stigmergic cognition | Marsh, L. & Onof, C. | 2008 | Cognitive Systems Research 9(1-2):136-149 |
| The Death and Life of Great American Cities | Jacobs, J. | 1961 | Random House |

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

- ACO調査との相互参照により、重複を避けつつ理論的接続を明確にできた
- 定量的/定性的の分類フレームワークが自然界の事例整理に有効だった
- ソフトウェアへの応用（Wikipedia, Git, Stack Overflow等）を含めたことで、抽象概念が具体化された

### 課題・改善点

- Grasse (1959) の原著はフランス語であり、二次資料経由の情報が主となった
- 人間社会への応用（都市、組織）は事例が広範で、深さよりも広さを優先した

### 新たに生まれた疑問・次のアクション

- タスク分担・役割分化の調査でスティグマジーとの関係（環境が役割を誘導するメカニズム）を深掘りできる
- 「デジタルスティグマジー」をソフトウェアアーキテクチャパターンとして体系化する可能性
- 本リポジトリのACO実装をスティグマジーの観点で再分析する価値がある

### ツール・手法の評価

- Theraulaz & Bonabeau (1999) のサーベイ論文が分類フレームワークの基盤として最も有効だった
- ACO調査を先に実施していたことで、理論的接続の記述がスムーズだった
