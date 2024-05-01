# 使用官方的 Python 3 镜像作为基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . /app

# 安装项目依赖
#RUN pip install --no-cache-dir -r requirements -i https://mirrors.aliyun.com/pypi/simple/
RUN pip install -r requirements -i https://mirrors.aliyun.com/pypi/simple/

# Expose the port used by the app
EXPOSE 8000

# 定义容器启动时运行的命令，启动 Django 应用
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



# docker build -t django-app .
# docker run -p 8000:8000 django-app  [运行 Django 项目的 Docker 容器]
# docker build --no-cache -t django-app .    清除镜像缓存，重构镜像