# ⚙️ AI System

AI系统工具，支持系统管理、进程管理、资源监控。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🔍 系统诊断
- ⚙️ systemd服务生成
- ⏰ Cron任务生成
- 🚀 启动优化
- 💾 备份脚本生成
- 📊 资源分析

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_system import create_tools

tools = create_tools()

# 系统诊断
diagnosis = tools.diagnose_system("系统运行缓慢")

# systemd服务
service = tools.generate_systemd_service("myapp", "python app.py")

# Cron任务
cron = tools.generate_cron_jobs(tasks)

# 启动优化
startup = tools.optimize_startup("linux")

# 备份脚本
backup = tools.generate_backup_script("/data", "/backup", "每天凌晨2点")

# 资源分析
resources = tools.analyze_resource_usage(metrics)
```

## 📁 项目结构

```
ai-system/
├── tools.py       # 系统工具核心
└── README.md
```

## 📄 许可证

MIT License
