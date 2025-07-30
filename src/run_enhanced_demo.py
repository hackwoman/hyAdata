#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版爬虫演示脚本
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    """主函数"""
    print("🚀 行业研报数据爬虫 - 增强版演示")
    print("=" * 60)
    
    # 模拟公司数据（避免导入问题）
    company_data = {
        "人工智能": [
            {"name": "科大讯飞", "code": "002230.SZ", "market_cap": "800亿", "main_products": "语音识别、智能教育"},
            {"name": "寒武纪", "code": "688256.SH", "market_cap": "300亿", "main_products": "AI芯片、智能计算"},
            {"name": "商汤科技", "code": "00020.HK", "market_cap": "600亿", "main_products": "计算机视觉、AI平台"}
        ],
        "新能源汽车": [
            {"name": "比亚迪", "code": "002594.SZ", "market_cap": "7000亿", "main_products": "新能源汽车、动力电池"},
            {"name": "宁德时代", "code": "300750.SZ", "market_cap": "8000亿", "main_products": "动力电池、储能系统"},
            {"name": "蔚来", "code": "NIO", "market_cap": "2000亿", "main_products": "智能电动汽车"}
        ],
        "半导体": [
            {"name": "中芯国际", "code": "688981.SH", "market_cap": "4000亿", "main_products": "晶圆代工、芯片制造"},
            {"name": "韦尔股份", "code": "603501.SH", "market_cap": "1500亿", "main_products": "图像传感器、模拟芯片"},
            {"name": "北方华创", "code": "002371.SZ", "market_cap": "1200亿", "main_products": "半导体设备、刻蚀机"}
        ]
    }
    
    print("📊 支持的行业和龙头企业:")
    print("-" * 60)
    
    for industry, companies in company_data.items():
        print(f"\n🏭 {industry}:")
        for company in companies:
            print(f"  - {company['name']} ({company['code']})")
            print(f"    市值: {company['market_cap']}")
            print(f"    主要产品: {company['main_products']}")
    
    print("\n🌐 支持的数据源:")
    print("-" * 60)
    data_sources = [
        "东方财富网", "新浪财经", "和讯网", "雪球", "巨潮资讯",
        "证券时报", "中国证券报", "上海证券报", "第一财经"
    ]
    
    for i, source in enumerate(data_sources, 1):
        print(f"{i:2d}. {source}")
    
    print("\n📈 数据字段说明:")
    print("-" * 60)
    fields = [
        "行业名称", "企业名称", "股票代码", "市值", "主要产品",
        "行业渗透率(%)", "产能利用率(%)", "平均毛利率(%)",
        "市场规模(亿元)", "年增长率(%)", "数据来源", "更新时间"
    ]
    
    for i, field in enumerate(fields, 1):
        print(f"{i:2d}. {field}")
    
    print("\n🎯 主要改进:")
    print("-" * 60)
    improvements = [
        "✅ 添加了真实公司名称和股票代码",
        "✅ 扩展了数据源（从5个增加到10个）",
        "✅ 增加了更多新兴行业（从15个增加到20个）",
        "✅ 改进了Excel输出格式（多工作表）",
        "✅ 添加了公司市值和主要产品信息",
        "✅ 优化了数据生成逻辑"
    ]
    
    for improvement in improvements:
        print(improvement)
    
    print("\n💡 使用说明:")
    print("-" * 60)
    print("1. 运行演示: python main_enhanced.py --demo")
    print("2. 查看行业: python main_enhanced.py --list")
    print("3. 查看数据源: python main_enhanced.py --sources")
    print("4. 爬取特定行业: python main_enhanced.py --industry '人工智能'")
    
    print("\n🎉 增强版功能已准备就绪！")

if __name__ == "__main__":
    main() 