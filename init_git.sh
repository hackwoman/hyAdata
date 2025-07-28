#!/bin/bash
# Git仓库初始化脚本

echo "🚀 初始化Git仓库..."

# 初始化Git仓库
git init

# 添加所有文件
git add .

# 创建初始提交
git commit -m "Initial commit: 行业研报数据爬虫系统

- 支持15个新兴细分行业数据收集
- 关键指标提取（渗透率、毛利率、市场规模等）
- Excel/CSV/JSON多格式输出
- 模块化设计，易于扩展"

echo "✅ Git仓库初始化完成！"
echo ""
echo "📋 下一步操作："
echo "1. 添加远程仓库: git remote add origin <repository-url>"
echo "2. 推送到远程: git push -u origin main"
echo "3. 创建Release: 在GitHub/GitLab上创建Release"
