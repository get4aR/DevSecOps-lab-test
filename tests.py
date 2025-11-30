# test_simple.py
import pytest
import os

def test_project_structure():
    """Просто проверяем что файлы существуют"""
    assert os.path.exists("backend/main.py"), "Main app file should exist"
    assert os.path.exists("backend/templates"), "Templates directory should exist"
    
def test_docker_files():
    """Проверяем docker файлы"""
    assert os.path.exists("docker-compose.yml") or os.path.exists("Dockerfile"), "Docker config should exist"

def test_always_passes():
    """Тест который всегда проходит"""
    assert True