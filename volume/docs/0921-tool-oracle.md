# （記述中）ツール：oracle

## 導入
docker-compose.yml
```yml
version: '3'
services:
  db:
    image: container-registry.oracle.com/database/free:23.4.0.0
    # container_name: oracle
    ports:
      - 1521:1521
      - 5500:5500
    volumes:
      - ./oradata:/opt/oracle/oradata
      - ./startup:/opt/oracle/scripts/startup
    environment:
      - ORACLE_PWD=oracle
      - ORACLE_PDB=FREEPDB1
```

setup (ここでは簡易的に権限設定している)
```
mkdir oradata
mkdir startup
chmod 777 oradata
chmod 777 startup
```

起動（# DATABASE IS READY TO USE! が表示される）
```
docker compose up
```

以下実行して初期設定
```
docker compose exec db ./setPassword.sh password123
docker compose exec db sqlplus sys/password123@freepdb1 as sysdba

# SQL内で接続情報作成
CREATE USER myuser
IDENTIFIED BY password123
DEFAULT TABLESPACE users
TEMPORARY TABLESPACE temp
QUOTA UNLIMITED ON users;

GRANT CONNECT, RESOURCE TO myuser;

exit;
```

接続確認
```
docker compose exec db sqlplus myuser/password123@freepdb1
```

## ベクトル検索
vector_memory_sizeの変更が必要。CDBレベルで設定して再起動する。
```
docker compose exec db sqlplus sys/password123@freepdb1 as sysdba

# SQL内で設定更新
show parameter vector_memory_size;

# CDBレベルで更新
alter session set container=CDB$ROOT;
alter system set vector_memory_size = 512M scope=spfile;
shutdown immediate;

# docker再起動してパラメータ更新
docker compose exec db sqlplus sys/password123@freepdb1 as sysdba
show parameter vector_memory_size;
```

## 参考
- https://github.com/ShunsukeNONOMURA/oracle-master.git
    - 構築一式
- [Oracle Database Free](https://container-registry.oracle.com/ords/f?p=113:4:103964643960397:::4:P4_REPOSITORY,AI_REPOSITORY,AI_REPOSITORY_NAME,P4_REPOSITORY_NAME,P4_EULA_ID,P4_BUSINESS_AREA_ID:1863,1863,Oracle%20Database%20Free,Oracle%20Database%20Free,1,0&cs=3elILP2QyPpWaLXPK3HnCwbeJr7Z9ATR98UrqEJigk6rGV-6knchnmVKYEnwAFxAqr8AZtlomHXrcdD6VKtxKUw)
- [Oracle Database 23ai のベクトル機能を試す手順 (1)](https://qiita.com/ryotayamanaka/items/156932a48e65d3ddc5ac)
- [ORA-51955 when attempting to alter vector memory size on 23ai free](https://forums.oracle.com/ords/apexds/post/ora-51955-when-attempting-to-alter-vector-memory-size-on-23-9413)
    - Connect to CDB$ROOT as SYSDBA の記載から vector_memory_size の変更にはCDBレベルでの設定が必要と思われる