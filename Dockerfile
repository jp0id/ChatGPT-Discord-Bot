# 使用 Python 官方 slim 镜像（基于 Debian）替代 Alpine
FROM python:3.9-slim

# 设置工作目录
WORKDIR /DiscordBot

# 先复制 requirements.txt 以利用 Docker 缓存
COPY requirements.txt .

# 安装系统依赖（如果需要）和 Python 依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove build-essential && \
    rm -rf /var/lib/apt/lists/*

# 复制整个项目
COPY . .

# 设置环境变量
ENV PYTHONPATH=/DiscordBot

# 运行应用
CMD ["python", "main.py"]