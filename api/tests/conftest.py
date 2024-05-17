from api.services.factories.api_factory import ApiFactory
from api.services.factories.check_response_factory import CheckResponseFactory
from api.services.factories.data_factory import DataFactory

import pytest

@pytest.fixture
def api():
    return ApiFactory()

@pytest.fixture
def check():
    return CheckResponseFactory()

@pytest.fixture
def data():
    return DataFactory()

def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='production')
