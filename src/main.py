#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行业研报数据爬虫主程序
整合所有功能模块，提供完整的行业数据收集和分析功能
"""

import sys
import os
import argparse
import logging
from datetime import datetime
import pandas as pd

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config import current_config
from industry_report_crawler import IndustryReportCrawler
from data_visualization import IndustryDataVisualizer

def setup_logging():
    """设置日志配置"""
    log_config = current_config.LOGGING_CONFIG
    
    # 创建日志格式
    formatter = logging.Formatter(log_config["format"])
    
    # 创建根日志记录器
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_config["level"]))
    
    # 清除现有的处理器
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # 添加控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 添加文件处理器
    if log_config["file_handler"]:
        from logging.handlers import RotatingFileHandler
        log_file = os.path.join("logs", log_config["log_filename"])
        os.makedirs("logs", exist_ok=True)
        
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=log_config["max_file_size"],
            backupCount=log_config["backup_count"],
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

def print_banner():
    """打印程序横幅"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                    行业研报数据爬虫系统                        ║
║                                                              ║
║  版本: {version:<50} ║
║  作者: {author:<50} ║
║  描述: {description:<50} ║
╚══════════════════════════════════════════════════════════════╝
""".format(
        version=current_config.VERSION,
        author=current_config.AUTHOR,
        description=current_config.DESCRIPTION
    )
    print(banner)

def crawl_data(industries=None, output_format='excel', generate_charts=True):
    """
    爬取行业数据
    
    Args:
        industries: 指定行业列表，如果为None则爬取所有行业
        output_format: 输出格式 ('excel', 'csv', 'json', 'all')
        generate_charts: 是否生成图表
    """
    logger = logging.getLogger(__name__)
    
    print("\n" + "="*60)
    print("开始收集行业研报数据...")
    print("="*60)
    
    # 创建爬虫实例
    crawler = IndustryReportCrawler()
    
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
        excel_file = crawler.save_to_excel(industry_data, current_config.get_excel_filename())
        if excel_file:
            saved_files.append(excel_file)
            print(f"Excel文件已保存: {excel_file}")
    
    if output_format in ['csv', 'all']:
        csv_file = current_config.get_csv_filename()
        df = pd.DataFrame(industry_data)
        df.to_csv(csv_file, index=False, encoding='utf-8-sig')
        saved_files.append(csv_file)
        print(f"CSV文件已保存: {csv_file}")
    
    if output_format in ['json', 'all']:
        json_file = current_config.get_json_filename()
        df = pd.DataFrame(industry_data)
        df.to_json(json_file, orient='records', force_ascii=False, indent=2)
        saved_files.append(json_file)
        print(f"JSON文件已保存: {json_file}")
    
    # 生成图表
    if generate_charts:
        print("\n正在生成可视化图表...")
        try:
            visualizer = IndustryDataVisualizer(industry_data)
            charts = visualizer.generate_comprehensive_report()
            print("图表生成完成！")
        except Exception as e:
            logger.error(f"生成图表时出错: {e}")
    
    return {
        'data': industry_data,
        'summary': summary,
        'files': saved_files
    }

def list_industries():
    """列出所有支持的行业"""
    print("\n支持的新兴细分行业:")
    print("-" * 40)
    for i, industry in enumerate(current_config.EMERGING_INDUSTRIES, 1):
        print(f"{i:2d}. {industry}")
    print(f"\n总计: {len(current_config.EMERGING_INDUSTRIES)} 个行业")

def show_data_sources():
    """显示数据源信息"""
    print("\n配置的数据源:")
    print("-" * 40)
    for name, config in current_config.DATA_SOURCES.items():
        status = "✓ 启用" if config.get('enabled', False) else "✗ 禁用"
        print(f"{name:<15} - {status:<10} - {config['base_url']}")

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="行业研报数据爬虫系统",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例:
  python main.py                    # 爬取所有行业数据
  python main.py -i 人工智能 新能源汽车  # 爬取指定行业
  python main.py -f csv             # 输出CSV格式
  python main.py --list             # 列出所有行业
  python main.py --sources          # 显示数据源
  python main.py --no-charts        # 不生成图表
        """
    )
    
    parser.add_argument('-i', '--industries', nargs='+', 
                       help='指定要爬取的行业（用空格分隔）')
    parser.add_argument('-f', '--format', choices=['excel', 'csv', 'json', 'all'], 
                       default='excel', help='输出格式 (默认: excel)')
    parser.add_argument('--no-charts', action='store_true', 
                       help='不生成可视化图表')
    parser.add_argument('--list', action='store_true', 
                       help='列出所有支持的行业')
    parser.add_argument('--sources', action='store_true', 
                       help='显示配置的数据源')
    parser.add_argument('--config', action='store_true', 
                       help='显示当前配置信息')
    
    args = parser.parse_args()
    
    # 设置日志
    logger = setup_logging()
    
    # 打印横幅
    print_banner()
    
    # 创建必要的目录
    current_config.create_directories()
    
    # 处理特殊命令
    if args.list:
        list_industries()
        return
    
    if args.sources:
        show_data_sources()
        return
    
    if args.config:
        print("\n当前配置信息:")
        print("-" * 40)
        print(f"环境: {os.getenv('ENVIRONMENT', 'development')}")
        print(f"数据源数量: {len(current_config.get_data_sources())}")
        print(f"行业数量: {len(current_config.EMERGING_INDUSTRIES)}")
        print(f"输出目录: {current_config.STORAGE_CONFIG['output_dir']}")
        print(f"图表目录: {current_config.VISUALIZATION_CONFIG['charts_output_dir']}")
        return
    
    try:
        # 开始爬取数据
        start_time = datetime.now()
        
        result = crawl_data(
            industries=args.industries,
            output_format=args.format,
            generate_charts=not args.no_charts
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