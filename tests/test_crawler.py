#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
行业研报数据爬虫系统 - 测试文件
"""

import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from industry_report_crawler_simple import IndustryReportCrawlerSimple

class TestIndustryCrawler(unittest.TestCase):
    """测试行业爬虫类"""
    
    def setUp(self):
        """设置测试环境"""
        self.crawler = IndustryReportCrawlerSimple()
    
    def test_init(self):
        """测试初始化"""
        self.assertIsNotNone(self.crawler)
        self.assertIsInstance(self.crawler.emerging_industries, list)
        self.assertGreater(len(self.crawler.emerging_industries), 0)
    
    def test_generate_sample_data(self):
        """测试数据生成"""
        data = self.crawler.sample_data
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        
        # 检查数据结构
        if data:
            item = data[0]
            required_fields = ['行业名称', '企业名称', '行业渗透率(%)', '平均毛利率(%)']
            for field in required_fields:
                self.assertIn(field, item)
    
    def test_save_to_excel(self):
        """测试Excel保存"""
        test_data = self.crawler.sample_data[:3]  # 只测试前3条数据
        filename = "test_output.xlsx"
        
        result = self.crawler.save_to_excel(test_data, filename)
        self.assertIsNotNone(result)
        self.assertTrue(os.path.exists(filename))
        
        # 清理测试文件
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == '__main__':
    unittest.main()
