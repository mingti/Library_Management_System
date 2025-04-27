使用 Django REST Framework + Vue3 的前后端分离项目

# 安装django_extensions
使用下面的脚本替换 Django控制台的启动脚本, 实现点击Python控制台自动倒入和shell_plus一样的模块

```python
# 文件 | 设置 | 构建、执行、部署 | 控制台 | Django 控制台

import sys; print('Python %s on %s' % (sys.version, sys.platform))
import django; print('Django %s' % django.get_version())
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
if 'setup' in dir(django): django.setup()

#import django_manage_shell; django_manage_shell.run(PROJECT_ROOT)

# ==== 使用 import_objects 加载所有模型 ====
from django_extensions.management.shells import import_objects
from django.core.management.color import no_style

# 加载所有模型到字典
model_dict = import_objects(
    options={'dont_load': [], 'quiet_load': False}, 
    style=no_style()
)

# ==== 将模型注入当前全局环境 ====
globals().update(model_dict)

```


# 配置数据库
lms_backend/DB_config.py
```python
# ================================================= #
# *************** SSH 连接Msql配置 *************** #
# ================================================= #
# 数据库服务器的ip地址或主机名
ssh_host = ""
# 数据库服务器的SSH连接端口号，一般都是22，必须是数字
ssh_port = 22
# 数据库服务起的用户名
ssh_user = ""
# 数据库服务器的用户名密码
# ssh_password = "123456"
ssh_pkey = ""

# 数据库服务起的mysql的主机名或ip地址
mysql_host = '127.0.0.1'
# 数据库服务起的mysql的端口，默认3306
mysql_port = 3306
# 数据库mysql的用户名
mysql_user = ""
# 数据库mysql密码
mysql_password = ""
# 数据库的库名
mysql_db = ""


```
# 解决 vite.condif.js 中 path 不能识别的问题
```bash
  npm install @types/node
```