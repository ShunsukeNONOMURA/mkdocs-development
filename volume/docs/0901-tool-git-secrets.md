# ツール：git-secrets
AWSの認証情報を誤って公開することで、リソースの不正利用が行われ、数百万単位の大金が請求されるケースがある。  
このようなポカミスを防ぐためには、git-secretsのようなツールを導入することが効果的である。  
本ページではgit-secretsを導入することでAWS用のクレデンシャルを誤ってgit repositoryにcommitしないようにする手順について記載する。  

## 導入
```
# aws labs経由
$ git clone https://github.com/awslabs/git-secrets
$ cd git-secrets
$ sudo make install

# 確認
$ git secrets -h
```

## 設定方法
導入
```
$ git secrets --install
✓ Installed commit-msg hook to .git/hooks/commit-msg
✓ Installed pre-commit hook to .git/hooks/pre-commit
✓ Installed prepare-commit-msg hook to .git/hooks/prepare-commit-msg
```

AWS用のクレデンシャルを弾く
```
$ git secrets --register-aws
OK
$ git secrets --register-aws --global # グローバル設定する場合
```

設定確認（allowd は 許可する認証を設定。defaultで設定されている）
```
$ cat .git/config 
{省略}
[secrets]
        providers = git secrets --aws-provider
        patterns = (A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}
        patterns = (\"|')?(AWS|aws|Aws)?_?(SECRET|secret|Secret)?_?(ACCESS|access|Access)?_?(KEY|key|Key)(\"|')?\\s*(:|=>|=)\\s*(\"|')?[A-Za-z0-9/\\+=]{40}(\"|')?
        patterns = (\"|')?(AWS|aws|Aws)?_?(ACCOUNT|account|Account)_?(ID|id|Id)?(\"|')?\\s*(:|=>|=)\\s*(\"|')?[0-9]{4}\\-?[0-9]{4}\\-?[0-9]{4}(\"|')?
        allowed = AKIAIOSFODNN7EXAMPLE
        allowed = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```


## 利用時の挙動

手動確認（credential_test.txtに認証情報が含まれているとき）
```
$ git secrets --scan
$ git secrets --scan --no-index # gitignoreするもの含めて全て調べる場合
credential_test.txt:1:aws_access_key=AKIAIOSFODNN7EXAMPLE
credential_test.txt:2:aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

[ERROR] Matched one or more prohibited patterns

Possible mitigations:
- Mark false positives as allowed using: git config --add secrets.allowed ...
- Mark false positives as allowed by adding regular expressions to .gitallowed at repository's root directory
- List your configured patterns: git config --get-all secrets.patterns
- List your configured allowed patterns: git config --get-all secrets.allowed
- List your configured allowed patterns in .gitallowed at repository's root directory
- Use --no-verify if this is a one-time false positive
```

コミット時の自動確認（credential_test.txtに認証情報が含まれているとき）
```
$ git add .
$ git commit -m 'my first'
credential_test.txt:1:aws_access_key=AKIAIOSFODNN7EXAMPLE
credential_test.txt:2:aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

[ERROR] Matched one or more prohibited patterns

Possible mitigations:
- Mark false positives as allowed using: git config --add secrets.allowed ...
- Mark false positives as allowed by adding regular expressions to .gitallowed at repository's root directory
- List your configured patterns: git config --get-all secrets.patterns
- List your configured allowed patterns: git config --get-all secrets.allowed
- List your configured allowed patterns in .gitallowed at repository's root directory
- Use --no-verify if this is a one-time false positive
```

なお、gitリポジトリで管理している本ページでのダミーの認証情報(AKIAIOSFODNN7EXAMPLEなど)の記載は、  
allowedに設定しているものであるため、検出対象から排除している。

## 参考
- [git-secretsを導入してみた](https://zenn.dev/kkk777/articles/8f55db1e9678f2)