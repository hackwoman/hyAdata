#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置文件
管理爬虫的各种设置和参数
"""

import os
from datetime import datetime

class Config:
    """配置类"""
    
    # 项目基本信息
    PROJECT_NAME = "行业研报数据爬虫"
    VERSION = "1.0.0"
    AUTHOR = "AI Assistant"
    DESCRIPTION = "收集各券商和专业网站的行业研报数据，提取关键指标"
    
    # 数据源配置
    DATA_SOURCES = {
        "东方财富网": {
            "base_url": "http://data.eastmoney.com",
            "enabled": True,
            "delay_range": (1, 3),
            "timeout": 30
        },
        "新浪财经": {
            "base_url": "https://finance.sina.com.cn",
            "enabled": True,
            "delay_range": (1, 3),
            "timeout": 30
        },
        "和讯网": {
            "base_url": "http://www.hexun.com",
            "enabled": True,
            "delay_range": (1, 3),
            "timeout": 30
        },
        "雪球": {
            "base_url": "https://xueqiu.com",
            "enabled": True,
            "delay_range": (2, 4),
            "timeout": 30
        },
        "巨潮资讯": {
            "base_url": "http://www.cninfo.com.cn",
            "enabled": True,
            "delay_range": (1, 3),
            "timeout": 30
        },
        "证券时报": {
            "base_url": "http://www.stcn.com",
            "enabled": True,
            "delay_range": (1, 3),
            "timeout": 30
        },
        "中国证券报": {
            "base_url": "http://www.cs.com.cn",
            "enabled": True,
            "delay_range": (1, 3),
            "timeout": 30
        },
        "上海证券报": {
            "base_url": "http://www.cnstock.com",
            "enabled": True,
            "delay_range": (1, 3),
            "timeout": 30
        },
        "第一财经": {
            "base_url": "https://www.yicai.com",
            "enabled": True,
            "delay_range": (1, 3),
            "timeout": 30
        },
        "同花顺": {
            "base_url": "http://www.10jqka.com.cn",
            "enabled": False,
            "delay_range": (2, 5),
            "timeout": 30
        },
        "Wind资讯": {
            "base_url": "https://www.wind.com.cn",
            "enabled": False,
            "delay_range": (3, 6),
            "timeout": 45
        }
    }
    
    # 新兴细分行业列表
    EMERGING_INDUSTRIES = [
        "人工智能",
        "新能源汽车",
        "半导体",
        "生物医药",
        "5G通信",
        "云计算",
        "物联网",
        "区块链",
        "氢能源",
        "储能技术",
        "机器人",
        "AR/VR",
        "量子计算",
        "基因治疗",
        "碳中和技术",
        "芯片设计",
        "自动驾驶",
        "智能制造",
        "数字孪生",
        "边缘计算"
    ]
    
    # 关键指标配置
    KEY_METRICS = {
        "行业渗透率": {
            "unit": "%",
            "range": (0, 100),
            "description": "行业产品在目标市场中的普及程度"
        },
        "产能利用率": {
            "unit": "%",
            "range": (0, 100),
            "description": "企业实际产能与设计产能的比率"
        },
        "平均毛利率": {
            "unit": "%",
            "range": (0, 100),
            "description": "企业毛利润与营业收入的比率"
        },
        "市场规模": {
            "unit": "亿元",
            "range": (0, 10000),
            "description": "行业总体市场规模"
        },
        "年增长率": {
            "unit": "%",
            "range": (-50, 200),
            "description": "行业年度增长率"
        }
    }
    
    # 爬虫设置
    CRAWLER_SETTINGS = {
        "max_retries": 3,
        "retry_delay": 5,
        "user_agent_rotation": True,
        "proxy_enabled": False,
        "proxy_list": [],
        "respect_robots_txt": True,
        "max_concurrent_requests": 5,
        "request_timeout": 30
    }
    
    # 数据存储配置
    STORAGE_CONFIG = {
        "excel_filename": f"行业研报数据_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
        "csv_filename": f"行业研报数据_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        "json_filename": f"行业研报数据_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        "output_dir": "output",
        "backup_enabled": True,
        "backup_dir": "backup"
    }
    
    # 可视化配置
    VISUALIZATION_CONFIG = {
        "charts_output_dir": "reports",
        "chart_format": "png",
        "chart_dpi": 300,
        "chart_style": "seaborn-v0_8",
        "color_palette": "viridis",
        "figure_size": (12, 8),
        "chinese_font": "SimHei"
    }
    
    # 日志配置
    LOGGING_CONFIG = {
        "level": "INFO",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "file_handler": True,
        "log_filename": f"crawler_{datetime.now().strftime('%Y%m%d')}.log",
        "max_file_size": 10 * 1024 * 1024,  # 10MB
        "backup_count": 5
    }
    
    # 数据库配置（可选）
    DATABASE_CONFIG = {
        "enabled": False,
        "type": "sqlite",  # sqlite, mysql, postgresql
        "host": "localhost",
        "port": 3306,
        "database": "industry_reports",
        "username": "",
        "password": "",
        "charset": "utf8mb4"
    }
    
    # 邮件通知配置（可选）
    EMAIL_CONFIG = {
        "enabled": False,
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "username": "",
        "password": "",
        "recipients": [],
        "subject_template": "行业研报数据收集完成 - {date}"
    }
    
    @classmethod
    def get_data_sources(cls):
        """获取启用的数据源"""
        return {name: config for name, config in cls.DATA_SOURCES.items() 
                if config.get('enabled', False)}
    
    @classmethod
    def create_directories(cls):
        """创建必要的目录"""
        directories = [
            cls.STORAGE_CONFIG["output_dir"],
            cls.STORAGE_CONFIG["backup_dir"],
            cls.VISUALIZATION_CONFIG["charts_output_dir"]
        ]
        
        for directory in directories:
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                print(f"创建目录: {directory}")
    
    @classmethod
    def get_excel_filename(cls):
        """获取Excel文件名"""
        return os.path.join(
            cls.STORAGE_CONFIG["output_dir"],
            cls.STORAGE_CONFIG["excel_filename"]
        )
    
    @classmethod
    def get_csv_filename(cls):
        """获取CSV文件名"""
        return os.path.join(
            cls.STORAGE_CONFIG["output_dir"],
            cls.STORAGE_CONFIG["csv_filename"]
        )
    
    @classmethod
    def get_json_filename(cls):
        """获取JSON文件名"""
        return os.path.join(
            cls.STORAGE_CONFIG["output_dir"],
            cls.STORAGE_CONFIG["json_filename"]
        )

# 开发环境配置
class DevelopmentConfig(Config):
    """开发环境配置"""
    LOGGING_CONFIG = {
        "level": "DEBUG",
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "file_handler": True,
        "log_filename": f"crawler_dev_{datetime.now().strftime('%Y%m%d')}.log",
        "max_file_size": 10 * 1024 * 1024,
        "backup_count": 5
    }
    
    CRAWLER_SETTINGS = {
        "max_retries": 1,
        "retry_delay": 2,
        "user_agent_rotation": False,
        "proxy_enabled": False,
        "proxy_list": [],
        "respect_robots_txt": False,
        "max_concurrent_requests": 1,
        "request_timeout": 10
    }

# 生产环境配置
class ProductionConfig(Config):
    """生产环境配置"""
    CRAWLER_SETTINGS = {
        "max_retries": 5,
        "retry_delay": 10,
        "user_agent_rotation": True,
        "proxy_enabled": True,
        "proxy_list": [],
        "respect_robots_txt": True,
        "max_concurrent_requests": 3,
        "request_timeout": 60
    }
    
    EMAIL_CONFIG = {
        "enabled": True,
        "smtp_server": "smtp.gmail.com",
        "smtp_port": 587,
        "username": "",
        "password": "",
        "recipients": [],
        "subject_template": "行业研报数据收集完成 - {date}"
    }

# 根据环境变量选择配置
def get_config():
    """根据环境变量获取配置"""
    env = os.getenv('ENVIRONMENT', 'development').lower()
    
    if env == 'production':
        return ProductionConfig
    else:
        return DevelopmentConfig

# 当前使用的配置
current_config = get_config() 