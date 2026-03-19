import sys
import os
import pytest
from fastapi.testclient import TestClient

# ✅ path add
sys.path.append(os.path.abspath("day5_config"))

# ✅ env set
os.environ["API_KEY"] = "test-key"
os.environ["APP_NAME"] = "Test API"
os.environ["DEBUG"] = "false"

from src.app.api import app


@pytest.fixture(scope="session")
def client():
    return TestClient(app)
