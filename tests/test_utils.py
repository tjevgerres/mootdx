import unittest

import mock
import pytest

from mootdx.consts import MARKET_SH, MARKET_SZ
from mootdx.utils import get_config_path, md5sum, to_data, get_stock_market

data = [
    ('600036', MARKET_SH),
    ('000001', MARKET_SZ),
]


@pytest.mark.parametrize('symbol,market', data)
def test_stock_market(symbol, market):
    assert get_stock_market(symbol) == market


class TestMd5sum(unittest.TestCase):

    def test_md5sum_error(self):
        self.assertIsNone(md5sum('/ad/sd/sd'))

    def test_md5sum_success(self):
        self.assertIsNotNone(md5sum('/vagrant/mootdx/setup.cfg'))


class TestToData(unittest.TestCase):

    def test_to_data_list(self):
        self.assertTrue(not to_data([{'aa': 'aa'}]).empty)

    def test_to_data_dict(self):
        self.assertTrue(not to_data({'abc': 123}).empty)

    def test_to_data_empty(self):
        self.assertTrue(to_data(None).empty)
        self.assertTrue(to_data({}).empty)
        self.assertTrue(to_data([]).empty)
        self.assertTrue(to_data('aaa').empty)
        self.assertTrue(to_data(123).empty)


class TestConfigPath(unittest.TestCase):

    @mock.patch('unipath.Path.mkdir')
    @mock.patch('platform.system')
    def test_platform_windows(self, platform_system, unipath_path_mkdir):
        platform_system.return_value = 'Windows'
        config = get_config_path(config='config.json')
        self.assertTrue('/mootdx/' in config)

    @mock.patch('unipath.Path.mkdir')
    @mock.patch('platform.system')
    def test_platform_linux(self, platform_system, unipath_path_mkdir):
        platform_system.return_value = 'Linux'
        config = get_config_path(config='config.json')
        self.assertTrue('/.mootdx/' in config)

    @mock.patch('unipath.Path.mkdir')
    @mock.patch('platform.system')
    def test_platform_Darwin(self, platform_system, unipath_path_mkdir):
        platform_system.return_value = 'Darwin'
        config = get_config_path(config='config.json')
        self.assertTrue('/.mootdx/' in config)


if __name__ == '__main__':
    unittest.main()
