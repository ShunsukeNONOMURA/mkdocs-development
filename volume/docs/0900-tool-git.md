# ツール：git
## 設定
pushを行う際などに必要。ない場合`Author identity unknown`が出る。
ここで指定しなくても、push時のオプションで指定可能。
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

- [Git Commitを実行したら、「Author identity unknown」エラー](https://yutaka-gakushu.com/tips/git/author-identity-unknown-error)
- [名前やメールアドレスを一時的に指定して git commit する方法](https://qiita.com/megane42/items/5375b54ea3570506e296)

## クローン
```
git clone https:~~
```

## ブランチ
```
# ブランチ作成と切り替え
git checkout -b <branch>
```

## ローカル更新
```
# 現在のブランチを更新
git pull
# 特定のブランチの更新を取り入れる
git rebase <branch>
# コンフリクトの確認
git status
```

## コマンドでpushするまでの一連の流れ
```
git add .
git status
git commit -m "message"
git -c user.name='foobar' -c user.email='foobar@example.com' commit -m '...'
git push
```

### キャッシュ削除
.gitignoreの変更が反映されず、ファイルが残る場合、キャッシュが原因なので削除するとよい。
削除後にコミットしてプッシュすると完了。
```
//ファイル全体のキャッシュ削除
$ git rm -r --cached .

//ファイルを指定してキャッシュ削除
$ git rm -r --cached [ファイル名]
```

## 戻す時
```
# 新しく追加した分
git checkout .
```

## 取り消し
[Git 操作の取り消し・元に戻す手順](https://softwarenote.info/p3540/)

### ローカルブランチでの編集作業の取り消し（addする前）
```
# すべて元に戻す
git checkout .

# 指定のファイルだけ元に戻す
git checkout {filename}

# 再帰的にディレクトリを辿って削除を行う
git clean -df
```

### git add の取り消し
```
git reset
```

### remote repository で reset を行う
```
# 戻したいcommit idを見つける
git log

# local repository の reset を実施
git reset {commit id}

# 余計なファイルや更新があれば削除しておく
git clean -df
git checkout .

# 差分がないことを確認
git status

# remoteに適用
git push origin main -f
```

## ブランチ切り替え
```
# 今のブランチ
git branch
# ブランチを変更（-bのときは作成する）
git checkout sample-branch
git checkout -b sample-branch
# ブランチ削除
git checkout -d sample-branch
# マージ
git checkout master
git merge sample-branch
```

## github

### アクセストークン
repositoryの更新など一部の操作ではgithubに対して認証が必要になる。
以前はパスワード認証も可能であったが、非推奨となった模様。
[Personal access tokens](https://github.com/settings/tokens)から生成可能 (profile settings -> Developer Settingsから辿れる)。
repositoryを触るだけならとりあえずrepoだけチェックで良い。

[GitHubにHTTPS接続でアクセスする方法！5ステップでトークンを作成！](https://codelikes.com/github-https-connection/)

### public <-> private
repository setting (Danger Zone) -> Change repository visibility

![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F224453%2F671958a1-45fc-dc5b-8e7c-3e2050ccb2e9.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=1586b2d1f770f85dffafa37435bc2db9)

[github private public 変更](https://qiita.com/HyunwookPark/items/1d24972dd71612eb81c9)

### delete repository
repository setting (Danger Zone) -> Delete this repository
