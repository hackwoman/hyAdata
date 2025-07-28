#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据可视化模块
生成行业分析图表和报告
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

class IndustryDataVisualizer:
    def __init__(self, data):
        """
        初始化可视化器
        Args:
            data: 行业数据列表或DataFrame
        """
        if isinstance(data, list):
            self.df = pd.DataFrame(data)
        else:
            self.df = data
        
        # 设置图表样式
        sns.set_style("whitegrid")
        plt.style.use('seaborn-v0_8')
    
    def create_industry_overview_chart(self, save_path="行业概览图.png"):
        """创建行业概览图表"""
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('新兴行业关键指标概览', fontsize=16, fontweight='bold')
        
        # 1. 各行业渗透率对比
        industry_penetration = self.df.groupby('行业名称')['行业渗透率(%)'].mean().sort_values(ascending=True)
        axes[0, 0].barh(industry_penetration.index, industry_penetration.values, color='skyblue')
        axes[0, 0].set_title('各行业渗透率对比')
        axes[0, 0].set_xlabel('渗透率 (%)')
        
        # 2. 各行业毛利率对比
        industry_margin = self.df.groupby('行业名称')['平均毛利率(%)'].mean().sort_values(ascending=True)
        axes[0, 1].barh(industry_margin.index, industry_margin.values, color='lightcoral')
        axes[0, 1].set_title('各行业平均毛利率对比')
        axes[0, 1].set_xlabel('毛利率 (%)')
        
        # 3. 市场规模分布
        market_size = self.df.groupby('行业名称')['市场规模(亿元)'].sum().sort_values(ascending=True)
        axes[1, 0].barh(market_size.index, market_size.values, color='lightgreen')
        axes[1, 0].set_title('各行业市场规模对比')
        axes[1, 0].set_xlabel('市场规模 (亿元)')
        
        # 4. 增长率分布
        growth_rate = self.df.groupby('行业名称')['年增长率(%)'].mean().sort_values(ascending=True)
        axes[1, 1].barh(growth_rate.index, growth_rate.values, color='gold')
        axes[1, 1].set_title('各行业年增长率对比')
        axes[1, 1].set_xlabel('增长率 (%)')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        return save_path
    
    def create_correlation_heatmap(self, save_path="指标相关性热力图.png"):
        """创建指标相关性热力图"""
        # 选择数值型列
        numeric_cols = ['行业渗透率(%)', '产能利用率(%)', '平均毛利率(%)', '市场规模(亿元)', '年增长率(%)']
        correlation_data = self.df[numeric_cols].corr()
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_data, annot=True, cmap='coolwarm', center=0, 
                   square=True, linewidths=0.5, cbar_kws={"shrink": .8})
        plt.title('行业关键指标相关性分析', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        return save_path
    
    def create_top_companies_chart(self, save_path="龙头企业分析.png"):
        """创建龙头企业分析图表"""
        # 获取前15家毛利率最高的企业
        top_companies = self.df.nlargest(15, '平均毛利率(%)')
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        
        # 1. 龙头企业毛利率排名
        bars1 = ax1.barh(range(len(top_companies)), top_companies['平均毛利率(%)'], 
                        color=plt.cm.viridis(np.linspace(0, 1, len(top_companies))))
        ax1.set_yticks(range(len(top_companies)))
        ax1.set_yticklabels(top_companies['企业名称'], fontsize=10)
        ax1.set_xlabel('毛利率 (%)')
        ax1.set_title('龙头企业毛利率排名 (Top 15)')
        
        # 为柱状图添加数值标签
        for i, (bar, value) in enumerate(zip(bars1, top_companies['平均毛利率(%)'])):
            ax1.text(value + 0.5, bar.get_y() + bar.get_height()/2, 
                    f'{value:.1f}%', va='center', fontsize=9)
        
        # 2. 龙头企业市场规模分布
        ax2.scatter(top_companies['市场规模(亿元)'], top_companies['平均毛利率(%)'], 
                   s=top_companies['年增长率(%)']*10, alpha=0.7, 
                   c=range(len(top_companies)), cmap='viridis')
        
        # 添加企业标签
        for i, (company, x, y) in enumerate(zip(top_companies['企业名称'], 
                                               top_companies['市场规模(亿元)'], 
                                               top_companies['平均毛利率(%)'])):
            ax2.annotate(company, (x, y), xytext=(5, 5), textcoords='offset points', 
                        fontsize=8, alpha=0.8)
        
        ax2.set_xlabel('市场规模 (亿元)')
        ax2.set_ylabel('毛利率 (%)')
        ax2.set_title('龙头企业市场规模 vs 毛利率 (气泡大小=增长率)')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        return save_path
    
    def create_industry_radar_chart(self, save_path="行业雷达图.png"):
        """创建行业雷达图"""
        # 选择前8个行业进行雷达图分析
        top_industries = self.df.groupby('行业名称').agg({
            '行业渗透率(%)': 'mean',
            '产能利用率(%)': 'mean',
            '平均毛利率(%)': 'mean',
            '年增长率(%)': 'mean'
        }).round(2).head(8)
        
        # 标准化数据 (0-100)
        normalized_data = top_industries.copy()
        for col in normalized_data.columns:
            normalized_data[col] = (normalized_data[col] - normalized_data[col].min()) / \
                                 (normalized_data[col].max() - normalized_data[col].min()) * 100
        
        # 设置雷达图角度
        categories = list(normalized_data.columns)
        N = len(categories)
        angles = [n / float(N) * 2 * np.pi for n in range(N)]
        angles += angles[:1]  # 闭合图形
        
        # 创建雷达图
        fig, ax = plt.subplots(figsize=(12, 10), subplot_kw=dict(projection='polar'))
        
        colors = plt.cm.Set3(np.linspace(0, 1, len(normalized_data)))
        
        for i, (industry, row) in enumerate(normalized_data.iterrows()):
            values = row.values.tolist()
            values += values[:1]  # 闭合图形
            
            ax.plot(angles, values, 'o-', linewidth=2, label=industry, color=colors[i])
            ax.fill(angles, values, alpha=0.25, color=colors[i])
        
        # 设置标签
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.set_ylim(0, 100)
        ax.set_title('行业综合实力雷达图', size=16, y=1.08)
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        return save_path
    
    def create_growth_trend_chart(self, save_path="增长趋势分析.png"):
        """创建增长趋势分析图表"""
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('行业增长趋势分析', fontsize=16, fontweight='bold')
        
        # 1. 渗透率 vs 增长率散点图
        axes[0, 0].scatter(self.df['行业渗透率(%)'], self.df['年增长率(%)'], 
                          alpha=0.6, s=50, c=self.df['平均毛利率(%)'], cmap='viridis')
        axes[0, 0].set_xlabel('渗透率 (%)')
        axes[0, 0].set_ylabel('增长率 (%)')
        axes[0, 0].set_title('渗透率 vs 增长率 (颜色=毛利率)')
        
        # 添加趋势线
        z = np.polyfit(self.df['行业渗透率(%)'], self.df['年增长率(%)'], 1)
        p = np.poly1d(z)
        axes[0, 0].plot(self.df['行业渗透率(%)'], p(self.df['行业渗透率(%)']), "r--", alpha=0.8)
        
        # 2. 毛利率 vs 产能利用率散点图
        axes[0, 1].scatter(self.df['平均毛利率(%)'], self.df['产能利用率(%)'], 
                          alpha=0.6, s=50, c=self.df['市场规模(亿元)'], cmap='plasma')
        axes[0, 1].set_xlabel('毛利率 (%)')
        axes[0, 1].set_ylabel('产能利用率 (%)')
        axes[0, 1].set_title('毛利率 vs 产能利用率 (颜色=市场规模)')
        
        # 3. 市场规模分布直方图
        axes[1, 0].hist(self.df['市场规模(亿元)'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
        axes[1, 0].set_xlabel('市场规模 (亿元)')
        axes[1, 0].set_ylabel('频次')
        axes[1, 0].set_title('市场规模分布')
        axes[1, 0].axvline(self.df['市场规模(亿元)'].mean(), color='red', linestyle='--', 
                          label=f'平均值: {self.df["市场规模(亿元)"].mean():.0f}亿元')
        axes[1, 0].legend()
        
        # 4. 增长率分布直方图
        axes[1, 1].hist(self.df['年增长率(%)'], bins=15, alpha=0.7, color='lightcoral', edgecolor='black')
        axes[1, 1].set_xlabel('增长率 (%)')
        axes[1, 1].set_ylabel('频次')
        axes[1, 1].set_title('增长率分布')
        axes[1, 1].axvline(self.df['年增长率(%)'].mean(), color='red', linestyle='--', 
                          label=f'平均值: {self.df["年增长率(%)"].mean():.1f}%')
        axes[1, 1].legend()
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        return save_path
    
    def generate_comprehensive_report(self, output_dir="reports"):
        """生成综合报告"""
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        print("正在生成综合可视化报告...")
        
        # 生成所有图表
        charts = {
            "行业概览": self.create_industry_overview_chart(f"{output_dir}/行业概览图.png"),
            "指标相关性": self.create_correlation_heatmap(f"{output_dir}/指标相关性热力图.png"),
            "龙头企业分析": self.create_top_companies_chart(f"{output_dir}/龙头企业分析.png"),
            "行业雷达图": self.create_industry_radar_chart(f"{output_dir}/行业雷达图.png"),
            "增长趋势分析": self.create_growth_trend_chart(f"{output_dir}/增长趋势分析.png")
        }
        
        # 生成统计摘要
        summary_stats = self.df.describe()
        summary_stats.to_csv(f"{output_dir}/统计摘要.csv", encoding='utf-8-sig')
        
        # 生成行业排名
        industry_rankings = self.df.groupby('行业名称').agg({
            '行业渗透率(%)': 'mean',
            '产能利用率(%)': 'mean',
            '平均毛利率(%)': 'mean',
            '市场规模(亿元)': 'sum',
            '年增长率(%)': 'mean'
        }).round(2).sort_values('平均毛利率(%)', ascending=False)
        
        industry_rankings.to_csv(f"{output_dir}/行业排名.csv", encoding='utf-8-sig')
        
        print(f"综合报告已生成到 {output_dir} 目录")
        print("包含以下文件:")
        for name, path in charts.items():
            print(f"- {name}: {path}")
        print(f"- 统计摘要: {output_dir}/统计摘要.csv")
        print(f"- 行业排名: {output_dir}/行业排名.csv")
        
        return charts

def main():
    """测试可视化功能"""
    # 创建示例数据
    from industry_report_crawler import IndustryReportCrawler
    
    crawler = IndustryReportCrawler()
    sample_data = crawler.sample_data
    
    # 创建可视化器
    visualizer = IndustryDataVisualizer(sample_data)
    
    # 生成综合报告
    visualizer.generate_comprehensive_report()

if __name__ == "__main__":
    main() 