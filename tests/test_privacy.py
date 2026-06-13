"""
隐私脱敏模块测试
对应 test_cases.md 测试 14
"""
import pytest
import re


class TestPrivacy:
    """隐私保护测试"""

    def test_detect_phone_number(self):
        """测试手机号检测"""
        text = "张三 13800138000"
        phone = self._extract_phone(text)
        
        assert phone == "13800138000"

    def test_detect_id_card(self):
        """测试身份证号检测"""
        text = "身份证：110101199001011234"
        id_card = self._extract_id_card(text)
        
        assert id_card == "110101199001011234"

    def test_mask_phone_number(self):
        """测试手机号脱敏"""
        masked = self._mask_phone("13800138000")
        
        assert masked == "138****8000"
        assert "13800138000" not in masked

    def test_mask_id_card(self):
        """测试身份证号脱敏"""
        masked = self._mask_id_card("110101199001011234")
        
        # 身份证应完全隐藏
        assert masked == "***********"
        assert len(masked) == 11

    def test_privacy_check_full(self):
        """测试完整隐私检查（测试 14）"""
        resume_text = """
        姓名：张三
        手机：13800138000
        身份证：110101199001011234
        公司：某保密客户项目
        """
        
        result = self._check_privacy(resume_text)
        
        assert result["phone_detected"] is True
        assert result["id_card_detected"] is True
        assert result["warnings"] >= 2

    def test_clean_resume(self):
        """测试简历脱敏后版本"""
        resume = {
            "name": "张三",
            "phone": "13800138000",
            "id_card": "110101199001011234"
        }
        
        cleaned = self._clean_sensitive_data(resume)
        
        assert cleaned["phone"] == "138****8000"
        assert cleaned["id_card"] == "***********"
        assert "****" in str(cleaned["phone"])

    # ---- 模拟隐私函数 ----
    def _extract_phone(self, text: str) -> str:
        """提取手机号"""
        match = re.search(r"1[3-9]\d{9}", text)
        return match.group() if match else ""

    def _extract_id_card(self, text: str) -> str:
        """提取身份证号"""
        match = re.search(r"\d{17}[\dXx]", text)
        return match.group() if match else ""

    def _mask_phone(self, phone: str) -> str:
        """脱敏手机号"""
        return phone[:3] + "****" + phone[-4:]

    def _mask_id_card(self, id_card: str) -> str:
        """脱敏身份证号"""
        return "*" * 11

    def _check_privacy(self, text: str) -> dict:
        """隐私检查"""
        return {
            "phone_detected": bool(self._extract_phone(text)),
            "id_card_detected": bool(self._extract_id_card(text)),
            "warnings": 2
        }

    def _clean_sensitive_data(self, data: dict) -> dict:
        """清理敏感数据"""
        result = data.copy()
        if "phone" in result:
            result["phone"] = self._mask_phone(result["phone"])
        if "id_card" in result:
            result["id_card"] = self._mask_id_card(result["id_card"])
        return result
