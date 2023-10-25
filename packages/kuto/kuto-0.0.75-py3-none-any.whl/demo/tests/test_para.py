import kuto

from kuto import logger


LIST_DATA = [
    {"name": "李雷", "age": "33"},
    {"name": "韩梅梅", "age": "30"}
]


class TestParameter(kuto.Case):
    """
    参数化demo
    """

    @kuto.data(LIST_DATA)
    def test_list(self, param):
        logger.info(param)

    @kuto.file_data(file='../static/data.json')
    def test_json(self, param):
        logger.info(param)

    @kuto.file_data(file='../static/data.yml', key='names')
    def test_yaml(self, param):
        print(param)


if __name__ == '__main__':
    """仅执行本模块"""
    kuto.main()
