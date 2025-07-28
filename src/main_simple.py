#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行业研报数据爬虫主程序 - 简化版本
不依赖selenium，只使用基本依赖包
"""

import sys
import os
import argparse
import logging
from datetime import datetime
import pandas as pd

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from industry_report_crawler_simple import IndustryReportCrawlerSimple

def setup_logging():
    """设置日志配置"""
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # 创建根日志记录器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # 清除现有的处理器
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # 添加控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

def print_banner():
    """打印程序横幅"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                行业研报数据爬虫系统 - 简化版                    ║
║                                                              ║
║  版本: 1.0.0                                                 ║
║  作者: AI Assistant                                          ║
║  描述: 收集行业研报数据，提取关键指标，生成Excel报告              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)

def crawl_data(industries=None, output_format='excel'):
    """
    爬取行业数据
    
    Args:
        industries: 指定行业列表，如果为None则爬取所有行业
        output_format: 输出格式 ('excel', 'csv', 'json', 'all')
    """
    logger = logging.getLogger(__name__)
    
    print("\n" + "="*60)
    print("开始收集行业研报数据...")
    print("="*60)
    
    # 创建爬虫实例
    crawler = IndustryReportCrawlerSimple()
    
    # 如果指定了行业，则只爬取指定行业
    if industries:
        crawler.emerging_industries = industries
        logger.info(f"将爬取指定行业: {', '.join(industries)}")
    
    # 爬取数据
    industry_data = crawler.crawl_all_industries()
    
    if not industry_data:
        logger.error("未收集到任何数据！")
        return None
    
    # 生成报告摘要
    summary = crawler.generate_report_summary(industry_data)
    
    print("\n" + "="*40)
    print("数据收集完成！")
    print("="*40)
    print(f"总行业数: {summary['总行业数']}")
    print(f"总企业数: {summary['总企业数']}")
    print(f"平均渗透率: {summary['平均渗透率']}%")
    print(f"平均产能利用率: {summary['平均产能利用率']}%")
    print(f"平均毛利率: {summary['平均毛利率']}%")
    print(f"总市场规模: {summary['总市场规模']}亿元")
    print(f"平均增长率: {summary['平均增长率']}%")
    
    # 保存数据
    saved_files = []
    
    if output_format in ['excel', 'all']:
        excel_filename = f"行业研报数据_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        excel_file = crawler.save_to_excel(industry_data, excel_filename)
        if excel_file:
            saved_files.append(excel_file)
            print(f"Excel文件已保存: {excel_file}")
    
    if output_format in ['csv', 'all']:
        csv_filename = f"行业研报数据_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df = pd.DataFrame(industry_data)
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
        saved_files.append(csv_filename)
        print(f"CSV文件已保存: {csv_filename}")
    
    if output_format in ['json', 'all']:
        json_filename = f"行业研报数据_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        df = pd.DataFrame(industry_data)
        df.to_json(json_filename, orient='records', force_ascii=False, indent=2)
        saved_files.append(json_filename)
        print(f"JSON文件已保存: {json_filename}")
    
    return {
        'data': industry_data,
        'summary': summary,
        'files': saved_files
    }

def list_industries():
    """列出所有支持的行业"""
    crawler = IndustryReportCrawlerSimple()
    
    print("\n支持的新兴细分行业:")
    print("-" * 40)
    for i, industry in enumerate(crawler.emerging_industries, 1):
        print(f"{i:2d}. {industry}")
    print(f"\n总计: {len(crawler.emerging_industries)} 个行业")

def show_sample_data():
    """显示示例数据"""
    crawler = IndustryReportCrawlerSimple()
    
    print("\n" + "="*60)
    print("示例数据预览")
    print("="*60)
    
    sample_data = crawler.sample_data[:10]  # 显示前10条
    
    print(f"总数据条数: {len(crawler.sample_data)}")
    print(f"显示前 {len(sample_data)} 条数据:")
    print("-" * 80)
    
    for i, item in enumerate(sample_data, 1):
        print(f"{i:2d}. {item['行业名称']:<12} | {item['企业名称']:<20} | "
              f"渗透率:{item['行业渗透率(%)']:>5.1f}% | "
              f"毛利率:{item['平均毛利率(%)']:>5.1f}% | "
              f"市场规模:{item['市场规模(亿元)']:>6.0f}亿元")
    
    print("-" * 80)

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="行业研报数据爬虫系统 - 简化版",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  python main_simple.py                    # 爬取所有行业数据
  python main_simple.py -i 人工智能 新能源汽车  # 爬取指定行业
  python main_simple.py -f csv             # 输出CSV格式
  python main_simple.py --list             # 列出所有行业
  python main_simple.py --sample           # 显示示例数据
        """
    )
    
    parser.add_argument('-i', '--industries', nargs='+', 
                       help='指定要爬取的行业（用空格分隔）')
    parser.add_argument('-f', '--format', choices=['excel', 'csv', 'json', 'all'], 
                       default='excel', help='输出格式 (默认: excel)')
    parser.add_argument('--list', action='store_true', 
                       help='列出所有支持的行业')
    parser.add_argument('--sample', action='store_true', 
                       help='显示示例数据')
    
    args = parser.parse_args()
    
    # 设置日志
    logger = setup_logging()
    
    # 打印横幅
    print_banner()
    
    # 处理特殊命令
    if args.list:
        list_industries()
        return
    
    if args.sample:
        show_sample_data()
        return
    
    try:
        # 开始爬取数据
        start_time = datetime.now()
        
        result = crawl_data(
            industries=args.industries,
            output_format=args.format
        )
        
        if result:
            end_time = datetime.now()
            duration = end_time - start_time
            
            print(f"\n任务完成！总耗时: {duration}")
            print(f"生成文件数量: {len(result['files'])}")
            
            if result['files']:
                print("\n生成的文件:")
                for file_path in result['files']:
                    print(f"  - {file_path}")
        
    except KeyboardInterrupt:
        print("\n\n用户中断操作")
        sys.exit(1)
    except Exception as e:
        logger.error(f"程序执行出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 