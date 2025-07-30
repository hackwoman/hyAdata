#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试增强版爬虫功能
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from industry_report_crawler_enhanced import IndustryReportCrawlerEnhanced
    print("✅ 成功导入增强版爬虫模块")
except ImportError as e:
    print(f"❌ 导入失败: {e}")
    sys.exit(1)

def test_company_data():
    """测试公司数据"""
    print("\n📊 测试公司数据...")
    crawler = IndustryReportCrawlerEnhanced()
    
    print(f"✅ 支持的行业数量: {len(crawler.company_data)}")
    
    # 显示前几个行业的数据
    for i, (industry, companies) in enumerate(crawler.company_data.items()):
        if i >= 3:  # 只显示前3个行业
            break
        print(f"\n🏭 {industry}:")
        for company in companies:
            print(f"  - {company['name']} ({company['code']})")
            print(f"    市值: {company['market_cap']}")
            print(f"    产品: {company['main_products']}")

def test_data_generation():
    """测试数据生成"""
    print("\n📈 测试数据生成...")
    crawler = IndustryReportCrawlerEnhanced()
    
    # 生成数据
    data = crawler._generate_realistic_data()
    print(f"✅ 生成数据条数: {len(data)}")
    
    # 显示前几条数据
    print("\n📋 数据预览:")
    for i, item in enumerate(data[:5]):
        print(f"\n记录 {i+1}:")
        print(f"  行业: {item['行业名称']}")
        print(f"  企业: {item['企业名称']} ({item['股票代码']})")
        print(f"  市值: {item['市值']}")
        print(f"  渗透率: {item['行业渗透率(%)']}%")
        print(f"  产能利用率: {item['产能利用率(%)']}%")
        print(f"  毛利率: {item['平均毛利率(%)']}%")

def test_data_sources():
    """测试数据源"""
    print("\n🌐 测试数据源...")
    crawler = IndustryReportCrawlerEnhanced()
    
    print(f"✅ 数据源数量: {len(crawler.data_sources)}")
    print("\n支持的数据源:")
    for name, url in crawler.data_sources.items():
        print(f"  - {name}: {url}")

def main():
    """主测试函数"""
    print("🧪 开始测试增强版爬虫功能")
    print("=" * 50)
    
    try:
        test_company_data()
        test_data_generation()
        test_data_sources()
        
        print("\n🎉 所有测试通过！")
        print("\n💡 使用说明:")
        print("  - 运行演示: python main_enhanced.py --demo")
        print("  - 查看行业: python main_enhanced.py --list")
        print("  - 查看数据源: python main_enhanced.py --sources")
        print("  - 爬取特定行业: python main_enhanced.py --industry '人工智能'")
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 