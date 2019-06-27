# mq-ws
mq-ws

安装依赖
```
pip install -r requirements.txt
```

Flask导入

```
export FLASK_APP=iot.py
```

数据库初始化
```
flask db init
flask db migrate -m "iot table"
flask db upgrade
```

运行
```
flask run
```
