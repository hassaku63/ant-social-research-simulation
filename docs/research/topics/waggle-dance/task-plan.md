# 調査タスク: 蜂のワッグルダンス（Waggle Dance）深掘り調査

## タスク概要

**目標**: 蜂のワッグルダンスによる情報伝達メカニズムを深掘りし、信号構造・情報符号化の精度・集団意思決定（Honeybee Democracy）・アルゴリズムや人間社会への応用を整理する。

**スコープ**:
- 調査すること:
  - ワッグルダンスの発見と信号構造（von Frisch）
  - 方向・距離・品質の符号化メカニズムと精度
  - 集団意思決定プロセス（Honeybee Democracy, Seeley）
  - スティグマジーとの比較
  - Bee Algorithm / ABCへの応用
  - 人間社会の意思決定モデルへの示唆
- 調査しないこと（除外事項）:
  - ABCアルゴリズムの実装詳細（応用事例で概要記載済み）
  - 蜂の生態全般（温度管理、カースト制度等は概要調査で記載済み）

**成果物**:
- [x] `docs/research/topics/waggle-dance/README.md`（調査ドキュメント）
- [x] `docs/research/references.md` への追記
- [x] `docs/research/index.md` の更新
- [x] `docs/masterplan.md` のステータス更新

**関連する既存調査**:
- [`docs/research/02_bee_behavior_systems.md`](../../02_bee_behavior_systems.md) — ワッグルダンスの概要
- [`docs/research/topics/stigmergy/`](../stigmergy/) — 対照的なコミュニケーション機構
- [`docs/research/topics/aco/`](../aco/) — スティグマジーベースのアルゴリズム

---

## 仕様検討（ステップ2）

### 調査項目

| # | 調査項目 | 優先度 | 状態 |
|---|---------|--------|------|
| 1 | ワッグルダンスの信号構造 | 高 | 完了 |
| 2 | 方向・距離・品質の符号化メカニズム | 高 | 完了 |
| 3 | 情報伝達の精度と限界 | 高 | 完了 |
| 4 | Honeybee Democracy（集団意思決定） | 高 | 完了 |
| 5 | スティグマジーとの比較 | 中 | 完了 |
| 6 | アルゴリズムへの応用（BA, ABC） | 中 | 完了 |
| 7 | 人間社会への応用と示唆 | 中 | 完了 |

### 出典選定基準

- 一次資料を優先: von Frisch (1967), Seeley (2010) を核とする
- Seeley et al. (2012) の停止信号に関する Science 論文
- 言語: 日本語・英語

---

## 実行（ステップ3）

### 調査記録

| 日時 | 実施内容 | 主な発見 |
|------|---------|---------|
| 2026-03-06 | ワッグルダンス全体の調査・ドキュメント作成 | 停止信号がデッドロック回避に不可欠。ノイズの機能的役割がACOの確率的遷移と類似。スティグマジーとの対比が集団知性の構造的理解に有効 |

### 参照した資料

| タイトル | 著者 | 年 | URL/DOI |
|---------|------|----|---------|
| The Dance Language and Orientation of Bees | von Frisch, K. | 1967 | Harvard University Press |
| Honeybee Democracy | Seeley, T.D. | 2010 | Princeton University Press |
| Stop Signals Provide Cross Inhibition... | Seeley, T.D. et al. | 2012 | Science 335(6064):108-111 |
| Nest-site selection in honey bees | Seeley, T.D. & Buhrman, S.C. | 2001 | Behav. Ecol. Sociobiol. 49(5):416-427 |
| Why do honey bees dance? | Dornhaus, A. & Chittka, L. | 2004 | Behav. Ecol. Sociobiol. 55(4):395-401 |
| The Bees Algorithm | Pham, D.T. et al. | 2005 | Proc. IPROMS 2006 |
| An Idea Based on Honey Bee Swarm... | Karaboga, D. | 2005 | TR06, Erciyes University |
| Democracy in animal groups | List, C. | 2004 | TREE 19(4):168-169 |

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

- スティグマジー調査との対比構造を取り入れたことで、直接通信と間接通信の違いが明確になった
- 停止信号の役割に焦点を当てることで、正のフィードバックだけでは不十分な理由を説明できた
- 人間社会への示唆（Seeleyの教訓）を含めたことで、実践的な価値が高まった

### 課題・改善点

- Bee Algorithm / ABCの性能比較データは含められなかった
- 円形ダンスと振動信号等、ワッグルダンス以外の蜂のコミュニケーション手段は深掘りしなかった

### 新たに生まれた疑問・次のアクション

- タスク分担調査でスカウト/フォロワーの動的な役割切替メカニズムを深掘りできる
- Honeybee Democracyモデルを意思決定シミュレーションとして実装する可能性
- ACOとBee Algorithmの性能比較実験が有意義

### ツール・手法の評価

- Seeley (2010) が集団意思決定の全体像把握に最も有効だった
- von Frisch (1967) は信号構造の原典として不可欠
- スティグマジー調査を先に実施していたことで対比がスムーズだった
