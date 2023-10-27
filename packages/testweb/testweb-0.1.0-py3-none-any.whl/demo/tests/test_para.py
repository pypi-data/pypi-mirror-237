import testweb


LIST_DATA = [
    {"name": "李雷", "age": "33"},
    {"name": "韩梅梅", "age": "30"}
]


class TestParameter(testweb.TestCase):
    """
    参数化demo
    """

    @testweb.data(LIST_DATA)
    def test_list(self, param):
        testweb.logger.info(param)

    @testweb.file_data(file='../data/data.json')
    def test_json(self, param):
        testweb.logger.info(param)

    @testweb.file_data(file='../data/data.yml', key='names')
    def test_yaml(self, param):
        print(param)


if __name__ == '__main__':
    testweb.main()
