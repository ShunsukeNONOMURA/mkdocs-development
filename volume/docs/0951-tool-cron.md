# ツール：cron

## 設定方法
通常、1か2のどちらかを選択すれば良いと思う。

1. crontab -e
2. /etc/cron.d
3. /etc/crontab
    - この方法はややこしい上、2の方法で足りるのでここでは触らない

## crontab -e
- ユーザごとに管理する形で、sudo不要
```
# エディタが表示されるので直接編集して保存する
# 保存後は /var/spool/cron/crontabs/[USER] にファイルが作られる
crontab -e

# sudo権限がある場合は以下のよう直接編集可能
sudo gedit /var/spool/cron/crontabs/[USER]

# 設定確認 
crontab -l

# すべて削除（部分的に削除する場合はcrontab -eから編集が良い）
crontab -r
```

### 記述ルール
分　時　日　月　曜日　コマンド　の順で記述
```
* * * * * cd ~/tmp && ./tmp.sh # 毎分
0 * * * * cd ~/tmp && ./tmp.sh # 毎時0分
0 12 * * * cd ~/tmp && ./tmp.sh # 毎日12時0分
```

## /etc/cron.d
- sudo権限必要
- システムによる定期実行を記す場合に適する

```
# スケジュール作成/更新
sudo gedit /etc/cron.d/[filename]

# 止める場合は削除すれば良い
sudo rm /etc/cron.d/[filename]
```

### 記述ルール
分　時　日　月　曜日　実行ユーザ　コマンド　の順で記述  
`crontab -e`とは違い、実行ユーザも必要
```
* * * * * [USER] cd ~/tmp && ./tmp.sh # 毎分

# cron.d以下にすでに作られているファイルを参考にできる
cat /etc/cron.d/anacron
```

## その他コマンド
```
# 現在のcron状態や直近実行されたジョブを確認できる
systemctl status cron
```

## 二重起動対策
cronで定期実行する際に二重起動する場合があるので対策が必要。

### 起動プロセスを確認する方法
pidofコマンドと組み合わせる方法。シェルの場合は素直にプロセス名からpidを引けるので使いやすい。

cronで書く場合はOR演算子でつなぐとプロセスがない場合に実行するような記述が取れる。
```
# 実行プログラムのpidofが取れない場合、プログラム実行する。
* * * * * pidof -x （実行プログラム） || （実行プログラム）
```

シェルの中で実行時に重複確認する場合、現在実行しているプロセス以外にプロセスがある場合に終了する。　　
shebangを1行目に記載することに注意する。
```shell
#!/bin/bash                                                                                                             
PNUM=$(pidof -x $0)
echo $0
echo $PNUM
if [ "$(echo $PNUM | awk '{print NF}')" != "1" ]; then
    echo "2重起動です"
    exit 1
fi

# 実行
echo start
python run.py
echo end
```


## 参考
- [色々なcronの場所と違い【Ubuntu 18.04.4 LTS】](https://penpen-dev.com/blog/cron/)