# 行业研报数据爬虫系统

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Beta-orange.svg)]()

一个专业的行业研报数据收集和分析系统，通过爬虫程序从各券商和专业网站收集行业研报数据，提取关键指标，并以Excel表格形式呈现和保存。

## 🌟 功能特点

- 🕷️ **多源数据收集**: 支持从东方财富网、新浪财经、和讯网等多个数据源收集数据
- 📊 **关键指标提取**: 自动提取行业渗透率、产能利用率、平均毛利率等关键指标
- 🏢 **龙头企业分析**: 每个细分行业包含3家龙头企业实例
- 📈 **数据可视化**: 生成多种图表和报告，直观展示行业趋势
- 📋 **多格式输出**: 支持Excel、CSV、JSON等多种数据格式
- 🔧 **灵活配置**: 支持自定义行业列表、数据源配置等
- 📝 **详细日志**: 完整的操作日志记录

## 🚀 快速开始

### 安装依赖

```bash
# 克隆仓库
git clone https://github.com/hackwoman/pydata.git
cd pydata

# 安装依赖
pip install -r src/requirements.txt
```

### 基本使用

```bash
# 查看帮助
python src/main_simple.py --help

# 列出所有支持的行业
python src/main_simple.py --list

# 爬取所有行业数据
python src/main_simple.py

# 爬取指定行业数据
python src/main_simple.py -i 人工智能 新能源汽车 半导体

# 输出CSV格式
python src/main_simple.py -f csv
```

## 📊 支持的新兴细分行业

系统支持以下15个新兴细分行业的数据收集：

| 序号 | 行业名称 | 描述 |
|------|----------|------|
| 1 | 人工智能 | AI技术应用和产业化 |
| 2 | 新能源汽车 | 电动汽车、氢能源汽车 |
| 3 | 半导体 | 芯片设计、制造、封装 |
| 4 | 生物医药 | 创新药物、基因治疗 |
| 5 | 5G通信 | 5G网络建设、应用 |
| 6 | 云计算 | 云服务、边缘计算 |
| 7 | 物联网 | IoT设备、平台服务 |
| 8 | 区块链 | 数字货币、智能合约 |
| 9 | 氢能源 | 氢燃料电池、制氢技术 |
| 10 | 储能技术 | 电池储能、抽水蓄能 |
| 11 | 机器人 | 工业机器人、服务机器人 |
| 12 | AR/VR | 增强现实、虚拟现实 |
| 13 | 量子计算 | 量子算法、量子通信 |
| 14 | 基因治疗 | 基因编辑、细胞治疗 |
| 15 | 碳中和技术 | 碳捕集、清洁能源 |

## 📈 关键指标说明

| 指标 | 单位 | 范围 | 说明 |
|------|------|------|------|
| 行业渗透率 | % | 0-100 | 行业产品在目标市场中的普及程度 |
| 产能利用率 | % | 0-100 | 企业实际产能与设计产能的比率 |
| 平均毛利率 | % | 0-100 | 企业毛利润与营业收入的比率 |
| 市场规模 | 亿元 | 0-10000 | 行业总体市场规模 |
| 年增长率 | % | -50到200 | 行业年度增长率 |

## 📁 项目结构

```
industry-report-crawler/
├── src/                           # 源代码目录
│   ├── main_simple.py             # 简化版主程序
│   ├── industry_report_crawler_simple.py  # 简化版爬虫
│   ├── main.py                    # 完整版主程序
│   ├── industry_report_crawler.py # 完整版爬虫
│   ├── data_visualization.py      # 数据可视化模块
│   ├── config.py                  # 配置文件
│   └── requirements.txt           # 依赖包列表
├── docs/                          # 文档目录
│   ├── README.md                  # 详细说明文档
│   ├── 安装指南.md                # 安装指南
│   └── 项目总结.md                # 项目总结
├── examples/                      # 示例代码
│   └── example_usage.py           # 使用示例
├── tests/                         # 测试文件
│   └── test_crawler.py            # 单元测试
├── output/                        # 输出目录
├── logs/                          # 日志目录
├── setup.py                       # 安装配置
├── LICENSE                        # 许可证
└── README.md                      # 项目说明
```

## 📋 输出文件说明

### Excel文件结构

生成的Excel文件包含以下工作表：

1. **行业数据** - 详细的行业和企业数据
   - 行业名称、企业名称
   - 关键指标数据
   - 数据来源、更新时间

2. **行业汇总** - 各行业关键指标汇总
   - 按行业分组的平均值和总和
   - 便于行业间对比分析

3. **龙头企业排名** - 按毛利率排名的前20家企业
   - 企业名称、所属行业
   - 关键指标数据

## 🛠️ 高级功能

### 命令行参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `-i, --industries` | 指定要爬取的行业 | `-i 人工智能 新能源汽车` |
| `-f, --format` | 输出格式 | `-f excel` (excel/csv/json/all) |
| `--list` | 列出所有行业 | `--list` |
| `--sample` | 显示示例数据 | `--sample` |

### 配置自定义

可以通过修改 `src/config.py` 文件来自定义：

- 数据源配置
- 行业列表
- 爬虫参数
- 输出格式

## 📊 示例输出

```
========================================
数据收集完成！
========================================
总行业数: 15
总企业数: 45
平均渗透率: 18.5%
平均产能利用率: 78.2%
平均毛利率: 28.7%
总市场规模: 15680亿元
平均增长率: 32.1%
```

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进项目！

### 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/hackwoman/pydata.git
cd pydata

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r src/requirements.txt

# 运行测试
python -m pytest tests/
```

### 提交规范

- 使用清晰的提交信息
- 包含测试用例
- 更新相关文档

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## ⚠️ 免责声明

本工具仅用于学习和研究目的，请遵守相关网站的使用条款和robots.txt文件。使用者应自行承担使用风险。

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 [GitHub Issue](https://github.com/hackwoman/pydata/issues)
- 发送邮件至项目维护者

## ⭐ 如果这个项目对您有帮助，请给我们一个星标！

---

**行业研报数据爬虫系统** - 让行业数据分析更简单、更高效！ 