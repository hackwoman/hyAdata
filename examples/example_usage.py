#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行业研报数据爬虫系统 - 使用示例
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from industry_report_crawler_simple import IndustryReportCrawlerSimple

def main():
    """示例：爬取人工智能行业数据"""
    print("🚀 行业研报数据爬虫系统 - 使用示例")
    print("=" * 50)
    
    # 创建爬虫实例
    crawler = IndustryReportCrawlerSimple()
    
    # 只爬取人工智能行业
    crawler.emerging_industries = ["人工智能"]
    
    # 爬取数据
    print("📊 正在爬取人工智能行业数据...")
    data = crawler.crawl_all_industries()
    
    # 显示结果
    print(f"✅ 成功收集 {len(data)} 条数据")
    
    # 保存到Excel
    filename = "人工智能行业数据.xlsx"
    crawler.save_to_excel(data, filename)
    print(f"💾 数据已保存到: {filename}")
    
    # 显示数据摘要
    summary = crawler.generate_report_summary(data)
    print(f"📈 平均渗透率: {summary['平均渗透率']}%")
    print(f"💰 平均毛利率: {summary['平均毛利率']}%")
    print(f"📊 总市场规模: {summary['总市场规模']}亿元")

if __name__ == "__main__":
    main()
