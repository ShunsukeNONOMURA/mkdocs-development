# （記述中）ツール：ollama
ローカルでLLMを動かすツール。  
REST実行可能で、langchainやdifyなどの他のライブラリやツールと連携できる。  

## インストール
https://ollama.com/download/linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 公開モデル取得

取得（[multilingual-e5-small](https://ollama.com/karuniaperjuangan/multilingual-e5-small)）
```bash
ollama pull karuniaperjuangan/multilingual-e5-small
```

動作確認
```bash
curl -X POST http://localhost:11434/api/embeddings -d '{
  "model": "karuniaperjuangan/multilingual-e5-small:latest",
  "prompt":"ラーメンとうどんはどっちが美味しい？"
}'
```

レスポンス
```json
{"embedding":[0.2444828599691391,0.0738295242190361, ... ,0.3108423352241516]}
```

## プライベートモデル登録
guff形式のモデルをModelファイルを介して登録する。

## 一覧
```bash
# モデルを一覧
ollama list
# モデルを更新
ollama list | tail -n +2 | cut -f1 | xargs -n1 ollama pull
```

## 公開
デフォルトだと他ホストからのアクセスを許可していないので設定が必要。  
https://github.com/ollama/ollama/blob/main/docs/faq.md#setting-environment-variables-on-linux

nanoエディタを立ち上げる
```
sudo systemctl edit ollama.service
```

`### Lines below this comment will be discarded`より上に記述。  
`Ctrl-O Enter`で保存。`Ctrl-X`で終了。
```
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
```

サービスを再起動
```
sudo systemctl daemon-reload
sudo systemctl restart ollama
```