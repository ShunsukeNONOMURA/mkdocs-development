# Hierarchical Navigable Small Worlds (HNSW) 
論文タイトル(和訳): 階層型ナビゲータブル小世界グラフを用いた効率的かつ堅牢な近似最近傍探索

## 概要
- グラフ理論ベースの近似K最近傍探索
- クエリのレイテンシーとRecallのトレードオフが最も優れている
    - Graph based Nearest Neighbor Search:Promises and Failures
- メモリ効率は悪いので量子化ベクトルを使うなどの工夫をしたほうが良い

**NSWの探索概念図**
![](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png&w=1920&q=75)

**HNSWの探索概念図**
![](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fe63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png&w=1920&q=75)

**ネットワーク構築時の概念図**
![](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Ff105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png&w=1920&q=75)

## 特徴
- 探索
    - nswを用いてグラフ探索することで、目標のベクトルの近傍ノードを見つける。このnswを階層的に扱うのがhnsw。
    - 急行に乗って大きく移動してから各駅停車で小さく移動しなおすイメージ
        - 急行で飛ばした駅について考慮しなくていい
        - 各停に乗ったあとに急行には乗らない
    - 特性上、得られる解は近似解
- 構築
    - 全ノードのネットワークから確率（$p=exp(−m_L)$）でノード選定して濃度の薄いネットワークを階層的に構築する
        - ノード追加時は確率でどのレイヤまでノードを追加するかを決める
        - データをあとから追加しても問題がない
    - レイヤ数は経験則から$1/ln(m)$とするのが良い
- パラメータ
    - 以下のようなパラメータによりレイテンシーとRecallのトレードオフを定める。基本的には数値が大きいほど、レイテンシーとRecallが高くなる。
    - 各ノードが持てる最大リンク数：`m`
    - 検索捜査時に訪れる候補ノードのキューのサイズ:`ef_search`
    - ノード追加時に訪れる候補ノードのキューのサイズ:`ef_construction`
- インフラ特性
    - メモリを多く消費する
        - メモリ使用量（opensearchの場合）
            - `1.1 * (4 * {ベクトル次元} + 8 * {最大リンク数}) * {ベクトル数}`
            - `次元 = 384, 最大リンク数 = 16, ベクトル数 = 1000万` のとき `≒ 37GB`
        - →　ベクトル量子化などして消費メモリを抑える等工夫したほうが良い

## 参考/引用
- [pgvectorを使ってChatGPTとPostgreSQLを連携してみよう！（PostgreSQL Conference Japan 2023 発表資料）](https://www.slideshare.net/slideshow/postgresql-pgvector-chatgpt-pgcon23j-nttdata/263745966)
    - NTT データグループ の人の資料（HNSWの概要掴むのに良い）
- [日本語訳： ベクトルデータベース(パート3): すべてのインデックスが同じとは限らない](https://zenn.dev/kun432/articles/20230923-vector-databases-jp-part-3)
    - Vector databases (3): Not all indexes are created equal の和訳
- [Hierarchical Navigable Small Worlds (HNSW)](https://www.pinecone.io/learn/series/faiss/hnsw/)
    - HNSW解説サイト（英語）
- [AWSブログ：OpenSearch における 10 億規模のユースケースに適した k-NN アルゴリズムの選定](https://aws.amazon.com/jp/blogs/news/choose-the-k-nn-algorithm-for-your-billion-scale-use-case-with-opensearch/)
    - k-NNアルゴリズムに関するAWSブログ
- [Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs](https://arxiv.org/abs/1603.09320)
    - HNSWの論文
- [onensearch Approximate k-NN search](https://opensearch.org/docs/1.0/search-plugins/knn/approximate-knn/)
    - opensearchにおけるhnsw利用
- [pgvector](https://github.com/pgvector/pgvector?tab=readme-ov-file#hnsw)
    - pgvectorにおけるhnsw利用
