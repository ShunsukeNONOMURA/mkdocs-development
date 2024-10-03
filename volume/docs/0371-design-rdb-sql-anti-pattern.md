# 設計：SQLアンチパターン
SQLに関するアンチパターンをまとめたもの。
自分が関わったことのある設計について記載。

## 1. Jaywalking（信号無視）
> 開発者はよく、「多対多」の関連を表現する交差テーブルの作成を避けるために、カンマ区切りのリストを使います。
> 私はこのアンチパターンをJaywalkingと名づけました。どちらも、"intersection"を避けようとする行為だからです。

カンマ区切りの値を入れること。半構造データみたいになる。

| book_id | book_name       | book_tags             |
| ------- | --------------- | --------------------- |
| 1       | Spring MVC      | Java,Spring,SpringMVC |
| 2       | はじめてのScala | Scala,入門            |

### 解決策：交差テーブルを作成

| book_id | book_name       |
| ------- | --------------- |
| 1       | Spring MVC      |
| 2       | はじめてのScala |

| book_tag_id | book_tag_name |
| ----------- | ------------- |
| 1           | Java          |
| 2           | Spring        |
| 3           | SpringMVC     |
| 4           | Scala         |
| 5           | 入門          |

| book_id | book_tag_id |
| ------- | ----------- |
| 1       | 1           |
| 1       | 2           |
| 2       | 3           |
| 2       | 4           |
| 2       | 5           |


## 5. EAV (Entity Attribute Value)
Entity Attribute Value（以下EAV）では次のような項目を持ったテーブルが設計される。

| 名称      | 役割                               |
| --------- | ---------------------------------- |
| Entity    | 親テーブルに対応した外部キーを格納 |
| Attribute | カラム名に相当する属性名を指定     |
| Value     | 属性の値                           |

| book_id |
| ------- |
| 1       |

| book_id | attribute    | value     |
| ------- | ------------ | --------- |
| 1       | name         | 本名      |
| 1       | release_date | 2020/9/24 |
| 1       | price        | 5         |

- メリット
    - テーブルの列数を削減できる
    - 新規の属性を追加する際に列数を増加しなくて良い
    - 属性が存在しない列にNULLが入りNULLだらけのテーブルにならない
    - データベースの構造は単純になる
- デメリット
    - データの取得が冗長化する
    - 特定の属性にNOT NULL制約を設定できない
    - データ型を使用できない
    - 外部制約キーを使用できない
    - 動的に属性名が増えるため整合性が担保しづらい


### 解決策：サブタイプでのモデリングを行う
<!-- ![](https://camo.qiitausercontent.com/3b3c8cf3b4a65cca1fd47f5765fd6c6209e4b40b/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3233363534322f62643133646131332d613063312d636234302d626365662d3434373662343830396333382e706e67) -->

大きく分けて4種類の継承方法がある。

- シングルテーブル継承
- 具象テーブル継承
- クラステーブル継承
- 半構造化データ

#### シングルテーブル継承で作成する場合

| book_id | book_name | book_release_date | book_price |
| ------- | --------- | ----------------- | ---------- |
| 1       | 本名      | 2020/9/24         | 5          |

## 7. Multi Column Attribute
複数列属性を持つようなアンチデザインパターン。Jaywalkingに似ている。

- 属性の検索が複雑になる
- 属性の追加・削除がしにくい
- 属性の一意性を保証できない
- 属性列の増加が起こりうる

| book_id | book_name       | book_tag_1 | book_tag_2 | book_tag_3 | book_tag_4 |
| ------- | --------------- | ---------- | ---------- | ---------- | ---------- |
| 1       | Spring MVC      | Java       | Spring     | SpringMVC  | NULL       |
| 2       | はじめてのScala | Scala      | 入門       | NULL       | NULL       |

### 解決策：交差テーブルを作成
同じ意味を持つ値は、1つの列に格納して別テーブルとし、1:nやn:nのリレーションを作成すれば良い。

| book_id | book_name       |
| ------- | --------------- |
| 1       | Spring MVC      |
| 2       | はじめてのScala |

| book_tag_id | book_tag_name |
| ----------- | ------------- |
| 1           | Java          |
| 2           | Spring        |
| 3           | SpringMVC     |
| 4           | Scala         |
| 5           | 入門          |

| book_id | book_tag_id |
| ------- | ----------- |
| 1       | 1           |
| 1       | 2           |
| 2       | 3           |
| 2       | 4           |
| 2       | 5           |

## 参考
- [SQLアンチパターン勉強会　第五回：EAV(エンティティ・アトリビュート・バリュー)](https://qiita.com/skyc_lin/items/37365a36416d0dc42431)
- [「SQLアンチパターン」まとめ](https://qiita.com/taiteam/items/33aebded2842808e0391)
- [ITエンジニアはSQLアンチパターンを読むべし！ 軽いまとめ](https://tech-blog.tsukaby.com/archives/857)
- [SQLアンチパターン　Entity Attribute Value](https://qiita.com/fktnkit/items/0ff462640e00deecfc6d)
