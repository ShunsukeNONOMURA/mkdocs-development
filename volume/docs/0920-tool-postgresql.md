# （記述中）postgresql

## pgvector
postgresqlでベクトル計算をするための拡張機能。

### 導入
簡易的に利用する場合に利用できる、拡張機能インストール済みのdockerイメージがある。

https://hub.docker.com/r/ankane/pgvector


導入と動作確認まで。
```
CREATE EXTENSION vector;
CREATE TABLE items (id bigserial PRIMARY KEY, embedding vector(3));
INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');
SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

hnswインデックスの設定（計算コストが下がることが確認できる）。
```
EXPLAIN SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
CREATE INDEX ON items USING hnsw (embedding vector_l2_ops);
EXPLAIN SELECT * FROM items ORDER BY embedding <-> '[3,1,2]' LIMIT 5;
```

### 演算子
| 演算子 | 説明                                        |
| :----- | :------------------------------------------ |
| +      | 2つのベクトルの各要素同士を加算します       |
| –      | 2つのベクトルの各要素同士を減算します       |
| *      | 2つのベクトルの各要素同士を乗算します       |
| <->    | 2つのベクトルのユークリッド距離を計測します |
| <#>    | 2つのベクトルの内積に-1を乗算します         |
| <=>    | 2つのベクトルのコサイン距離を計測します     |

### 関数
| 関数                                               | 説明               |
| :------------------------------------------------- | :----------------- |
| cosine_distance(vector, vector) → double precision | コサイン距離       |
| inner_product(vector, vector) → double precision   | 内積               |
| l2_distance(vector, vector) → double precision     | ユークリッド距離   |
| l1_distance(vector, vector) → double precision     | マンハッタン距離   |
| vector_dims(vector) → integer                      | 次元数             |
| vector_norm(vector) → double precision             | ユークリッドノルム |

### インデックス
| インデックス | 説明                                                                                                                       | インデックス構築時間 | メモリ使用量 | クエリのパフォーマンス               |
| :----------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------- | :----------- | :----------------------------------- |
| IVFFlat      | ベクトルをリストに分割してクエリベクトルに最も近いリストのサブセットを検索する                                             | 短い                 | 少ない       | 速度とリコールのトレードオフが大きい |
| HNSW         | 最下層に全てのベクトル点が含まれ上の層になるほどベクトル点が少なくなる層状のグラフ構造で上層から下層にアイテムを辿っていく | 長い                 | 多い         | 速度とリコールのトレードオフが少ない |


HNSWインデックスのオプション
```
CREATE INDEX ON table USING hnsw (embedding vector_l2_ops) WITH (m = 16, ef_construction = 64);
CREATE INDEX ON public.langchain_pg_embedding USING hnsw (embedding vector_l2_ops);
CREATE INDEX ON table USING hnsw(vec) WITH (maxelements=10000, dims=1536 efconstruction=16, efsearch=16);
```

| パラメータ     | 必須 | デフォルト値 | 意味                                                                                                           |
| -------------- | ---- | ------------ | -------------------------------------------------------------------------------------------------------------- |
| maxelements    | ○？  |              | インデックス付けされる要素の最大数。データセット内の行数に対応できる値に設定。                                 |
| dims           | ○    |              | ベクトル データの次元数                                                                                        |
| m              |      | 16           | 各ノードに作成される双方向リンクの最大数                                                                       |
| efconstruction |      | 64           | インデックスの構築中に考慮される最近傍の数。高いほどインデックスの構築時間、挿入速度を犠牲にしてリコールが向上 |
| efsearch       |      |              | インデックス検索中に考慮される最近傍の数。高いほどリコールを向上させますが、速度を犠牲にする。                 |


検索例
```
SELECT
	id,
	1 - (embedding <=> (SELECT embedding FROM public.langchain_pg_embedding WHERE id = '47ada81b-d9cf-433f-a3f4-f92532bca1af')) AS cosine_similarity,
	document,
	cmetadata
from public.langchain_pg_embedding
ORDER BY
	cosine_similarity desc
LIMIT 10;
```

### column does not have dimensions
typeにsizeの指定がない場合。

```
ALTER TABLE public.langchain_pg_embedding ALTER COLUMN embedding TYPE vector(1024);
```

https://github.com/prisma/prisma/issues/21850

### 参考
- [pgvectorの紹介](https://www.sraoss.co.jp/tech-blog/pgsql/pgvector-intro/)
- [Postgres Embedding](https://python.langchain.com/v0.1/docs/integrations/vectorstores/pgembedding/)

## ロジカルレプリケーション
未記述

## インデックス作成状況
```
SELECT phase, round(100.0 * blocks_done / nullif(blocks_total, 0), 1) AS "%" FROM pg_stat_progress_create_index;
```