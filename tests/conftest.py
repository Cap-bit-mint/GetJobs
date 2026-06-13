"""
GetJobs 测试配置和共享 fixtures
"""
import json
import pytest
import os
from pathlib import Path
from typing import Any

# 测试数据路径
FIXTURES_DIR = Path(__file__).parent / "fixtures"


def load_fixture(filename: str) -> Any:
    """加载测试数据 fixture"""
    with open(FIXTURES_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def sample_jd():
    """标准 JD 样本"""
    return load_fixture("sample_jd.json")


@pytest.fixture
def sample_resume():
    """标准简历样本"""
    return load_fixture("sample_resume.json")


@pytest.fixture
def sample_applications():
    """标准投递记录样本"""
    return load_fixture("sample_applications.json")


@pytest.fixture
def temp_storage(tmp_path):
    """临时存储目录"""
    storage = tmp_path / "getjobs"
    storage.mkdir()
    return storage
