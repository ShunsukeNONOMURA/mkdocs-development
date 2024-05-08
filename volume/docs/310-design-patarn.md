# デザインパターン
システムを構築する上でのパターンをいくつか記述する。

## Direct Object Uploadパターン
フロントエンド側がバックエンドからファイルアップロードに関する諸情報を取得した後、バックエンドを経由せずに直接S3にファイルをアップロードするパターン。  

- [CDP:Direct Object Uploadパターン](https://aws.clouddesignpattern.org/index.php/CDP_Direct_Object_Upload%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3.html)

## WebSocket チケットベース認証
予めhttpリクエストして取得した認証チケットをもとにws認証を行う。

- [Heroku Dev Centeer : WebSocket のセキュリティ](https://devcenter.heroku.com/ja/articles/websocket-security#authentication-authorization)

## 参考
- [Cloud Design Pattern](https://aws.clouddesignpattern.org/index.php/%e3%83%a1%e3%82%a4%e3%83%b3%e3%83%9a%e3%83%bc%e3%82%b8.html)
    - AWSのデザインパターン集
- [Heroku Dev Centeer](https://devcenter.heroku.com/ja)
    - Herokuのリファレンス