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
