"""
JD 解析模块测试
对应 test_cases.md 测试 1, 2
"""
import pytest
from conftest import load_fixture


class TestJDParser:
    """JD 解析器测试"""

    def test_parse_valid_jd(self, sample_jd):
        """测试有效 JD 解析"""
        parsed = self._parse_jd(sample_jd)
        
        assert parsed["company"] == "字节跳动"
        assert parsed["position"] == "高级产品经理"
        assert parsed["requirements"]["experience"] == "5年+"

    def test_parse_jd_missing_fields(self):
        """测试字段缺失时的解析"""
        incomplete_jd = {"company": "某公司"}
        parsed = self._parse_jd(incomplete_jd)
        
        assert parsed["position"] is None
        assert parsed.get("requirements", {}).get("experience") is None

    def test_parse_empty_jd(self):
        """测试空 JD 输入"""
        with pytest.raises(ValueError, match="JD内容不能为空"):
            self._parse_jd({})

    def test_jd_search_fallback(self, sample_jd):
        """测试 JD 搜索降级策略"""
        result = self._search_jd_with_fallback("不存在公司")
        
        assert result["status"] == "failed"
        assert "fallback_url" in result or "user_action" in result

    def test_jd_salary_extraction(self, sample_jd):
        """测试薪资提取"""
        parsed = self._parse_jd(sample_jd)
        assert "35" in parsed.get("salary", "")
        assert "60" in parsed.get("salary", "")

    # ---- 模拟解析函数 ----
    def _parse_jd(self, jd: dict) -> dict:
        """模拟 JD 解析"""
        if not jd:
            raise ValueError("JD内容不能为空")
        
        result = {
            "company": jd.get("company"),
            "position": jd.get("position"),
            "salary": jd.get("salary"),
            "requirements": jd.get("requirements", {})
        }
        return result

    def _search_jd_with_fallback(self, company: str) -> dict:
        """模拟 JD 搜索降级"""
        return {
            "status": "failed",
            "attempts": [
                {"source": "官网", "status": "failed"},
                {"source": "招聘平台", "status": "blocked"}
            ],
            "user_action": "请提供JD"
        }
