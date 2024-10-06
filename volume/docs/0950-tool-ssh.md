# ツール：SSH
## install
```
sudo apt install -y openssh-server
sudo gedit /etc/ssh/sshd_config
service sshd restart
```

sshd_config
```
#PasswordAuthentication yes
　　　　　　　↓
PasswordAuthentication no
```

## ssh key
```
ssh-keygen
mv ~/.ssh/id_rsa.pub ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```
id_rsaを接続元のクライアントにコピーしてssh接続する

- [SSHの設定手順(Ubuntu20.04)とWindowsからのアクセス確認手順](https://aquarius-train.hatenablog.com/entry/SSH%E3%81%AE%E8%A8%AD%E5%AE%9A%E6%89%8B%E9%A0%86%28Ubuntu18_04%29%E3%81%A8Windows%E3%81%8B%E3%82%89%E3%81%AE%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E7%A2%BA%E8%AA%8D%E6%89%8B%E9%A0%86)
- [sshでパスワード認証を禁止するには](https://atmarkit.itmedia.co.jp/flinux/rensai/linuxtips/430dnypsswdacces.html)