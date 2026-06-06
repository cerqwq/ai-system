"""
AI System - AI系统工具
支持系统管理、进程管理、资源监控
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AISystemTools:
    """
    AI系统工具
    支持：管理、进程、资源
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def diagnose_system(self, symptoms: str) -> Dict:
        """诊断系统问题"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请诊断以下系统问题：

症状：{symptoms}

请返回JSON格式：
{{
    "possible_causes": ["可能原因"],
    "diagnostic_commands": ["诊断命令"],
    "solutions": ["解决方案"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"diagnosis": content}

    def generate_systemd_service(self, app_name: str, command: str) -> str:
        """生成systemd服务"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{app_name}生成systemd服务配置：

启动命令：{command}

要求：
1. 服务定义
2. 自动重启
3. 日志配置
4. 安全限制"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_cron_jobs(self, tasks: List[Dict]) -> str:
        """生成Cron任务"""
        if not self.client:
            return "LLM客户端未配置"

        tasks_text = json.dumps(tasks, ensure_ascii=False)

        prompt = f"""请生成Cron定时任务：

任务：{tasks_text}

要求：
1. Crontab配置
2. 任务脚本
3. 日志记录
4. 错误处理"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def optimize_startup(self, os_type: str = "linux") -> Dict:
        """优化启动项"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请优化{os_type}系统启动项：

请返回JSON格式：
{{
    "unnecessary": ["可禁用项"],
    "recommendations": ["优化建议"],
    "scripts": ["优化脚本"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"optimization": content}

    def generate_backup_script(self, source: str, destination: str, schedule: str) -> str:
        """生成备份脚本"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成备份脚本：

源：{source}
目标：{destination}
计划：{schedule}

要求：
1. 增量备份
2. 压缩
3. 日志
4. 错误处理"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def analyze_resource_usage(self, metrics: Dict) -> Dict:
        """分析资源使用"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        metrics_text = json.dumps(metrics, ensure_ascii=False)

        prompt = f"""请分析系统资源使用：

{metrics_text}

请返回JSON格式：
{{
    "summary": "总结",
    "bottlenecks": ["瓶颈"],
    "recommendations": ["优化建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}


def create_tools(**kwargs) -> AISystemTools:
    """创建系统工具"""
    return AISystemTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI System Tools")
    print()

    # 测试
    diagnosis = tools.diagnose_system("系统运行缓慢，CPU占用高")
    print(json.dumps(diagnosis, ensure_ascii=False, indent=2))
