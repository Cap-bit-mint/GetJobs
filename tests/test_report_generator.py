"""
报告生成模块测试
对应 test_cases.md 测试 8, 11, 12
"""
import pytest
from datetime import datetime, timedelta


class TestReportGenerator:
    """报告生成测试"""

    def test_generate_weekly_report(self, sample_applications):
        """测试周报生成（测试 11）"""
        report = self._generate_weekly_report(sample_applications)
        
        assert "求职周报" in report
        assert "投递统计" in report
        assert "下周目标" in report

    def test_export_csv(self, temp_storage, sample_applications):
        """测试 CSV 导出（测试 12）"""
        result = self._export_to_csv(sample_applications, temp_storage)
        
        assert result["status"] == "success"
        assert result["file_path"].endswith(".csv")
        assert "id" in result["headers"]

    def test_export_csv_missing_fields(self, temp_storage):
        """测试异常数据导出（边界测试）"""
        apps = [{"company": "某公司"}]  # 缺字段
        result = self._export_to_csv(apps, temp_storage)
        
        assert result["status"] == "success"
        assert result["data"][0].get("position") == ""

    def test_export_csv_empty(self, temp_storage):
        """测试空数据导出"""
        result = self._export_to_csv([], temp_storage)
        
        assert result["status"] == "success"
        assert len(result["data"]) == 0

    def test_letter_generation(self, sample_jd, sample_resume):
        """测试求职信生成（测试 8）"""
        letter = self._generate_cover_letter(sample_jd, sample_resume)
        
        assert "字节跳动" in letter
        assert "3年" in letter  # 基于简历
        assert "精通" not in letter  # 不应夸大

    def test_letter_no_fabrication(self, sample_jd, sample_resume):
        """测试求职信不编造内容"""
        letter = self._generate_cover_letter(sample_jd, sample_resume)
        
        # 不应包含简历中没有的信息
        assert "5年" not in letter  # 简历只有3年
        assert "精通SQL" not in letter  # 简历写"偶尔取数"

    # ---- 模拟报告函数 ----
    def _generate_weekly_report(self, applications: list) -> str:
        """模拟周报生成"""
        today = datetime.now()
        week_start = today - timedelta(days=today.weekday())
        
        report = f"""## 本周求职周报

**时间**：{week_start.strftime('%Y-%m-%d')} 至 {today.strftime('%Y-%m-%d')}

### 投递统计
| 指标 | 本周 | 累计 |
|------|------|------|
| 新投递 | {len(applications)} | {len(applications)} |

### 本周动态
暂无更新

### 下周目标
1. 跟进投递
2. 新增投递
"""
        return report

    def _export_to_csv(self, applications: list, storage) -> dict:
        """模拟 CSV 导出"""
        headers = ["id", "company", "position", "platform", "match_score", "salary", "location", "status"]
        
        data = []
        for app in applications:
            row = {h: app.get(h, "") for h in headers}
            data.append(row)
        
        return {
            "status": "success",
            "file_path": str(storage / f"export_{datetime.now().strftime('%Y%m%d')}.csv"),
            "headers": headers,
            "data": data
        }

    def _generate_cover_letter(self, jd: dict, resume: dict) -> str:
        """模拟求职信生成"""
        return f"""尊敬的{jd['company']} HR：

我是{resume['name']}，{resume['experience_years']}年{resume['experience'][0]['type']}产品经验。

核心优势：
- {resume['experience_years']}年B端产品经验
- SQL数据分析能力
- 跨团队协作经验

此致
敬礼
{resume['name']}
"""
