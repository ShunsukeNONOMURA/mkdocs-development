# （記述中）分析：ロバストネス分析
システムのユースケースを記述した文章を基に、オブジェクトを用いた図(ロバストネス図)を作成する作業。  
ユースケースを記述した文章からクラス図やシーケンス図といったUML静的モデルが作りやすくなる。  
ユースケース記述を単純に図に変換するわけではないことに注意する。  
ロバストネス図はスプリントプランニングの前に書かれているのが望ましい。  
修正はロバストネス図から行う。  
ロバストネス図の追加や編集を気軽にできる状態にしておく。  

| 要素         | 概要                                                     |
| ------------ | -------------------------------------------------------- |
| アクター     | 操作主体。「管理者」「ユーザ」「システム」「バッチ」など |
| バウンダリ   | アクターが相互作用する画面やボタン                       |
| エンティティ | ソフトウェアシステム内部で半永久的に管理するデータ       |
| コントロール | バウンダリとエンティティをつないでシステムが行う処理     |

## ツール

## 参考
- [アジャイル開発の設計にロバストネス分析を活用する](https://engineering.visional.inc/blog/264/robustness-analysys/)