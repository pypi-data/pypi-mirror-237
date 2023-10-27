import os.path
import sys


case_content = """import testapis
from testapis import FormEncoder


class TestApiDemo(testapis.TestCase):

    @testapis.title("一般请求")
    def test_normal_req(self):
        payload = {"type": 2}
        headers = {
            "user-agent-web": "X/b67aaff2200d4fc2a2e5a079abe78cc6"
        }
        self.post('/qzd-bff-app/qzd/v1/home/getToolCardListForPc',
                  json=payload, headers=headers)
        self.assert_eq('code', 0)

    @testapis.title("文件上传")
    def test_upload_file(self):
        path = '/qzd-bff-patent/patent/batch/statistics/upload'
        files = {'static': open('../static/号码上传模板_1.xlsx', 'rb')}
        self.post(path, files=files)
        self.assert_eq('code', 0)

    @testapis.title("form请求")
    def test_form_req(self):
        url = '/qzd-bff-patent/image-search/images'
        file_data = (
            'logo.png',
            open('../static/logo.png', 'rb'),
            'image/png'
        )
        fields = {
            'key1': 'value1',  # 参数
            'imageFile': file_data  # 文件
        }
        form_data = FormEncoder(fields=fields)
        headers = {'Content-Type': form_data.content_type}
        self.post(url, data=form_data, headers=headers)
        self.assert_eq("code", 0)


if __name__ == '__main__':
    testapis.main(host='https://app-test.qizhidao.com')
"""

run_content = """import testapis


if __name__ == '__main__':

    testapis.main(
        host='https://app-pre.qizhidao.com',
        case_path="tests"
    )
"""


def create_scaffold(projectName):
    """create scaffold with specified project name."""

    def create_folder(path):
        os.makedirs(path)
        msg = f"created folder: {path}"
        print(msg)

    def create_file(path, file_content=""):
        with open(path, "w", encoding="utf-8") as f:
            f.write(file_content)
        msg = f"created file: {path}"
        print(msg)

    # 新增测试数据目录
    root_path = projectName
    create_folder(root_path)
    create_folder(os.path.join(root_path, "tests"))
    create_folder(os.path.join(root_path, "report"))
    create_folder(os.path.join(root_path, "data"))
    create_file(
        os.path.join(root_path, "tests", "test_api.py"),
        case_content,
    )
    create_file(
        os.path.join(root_path, "run.py"),
        run_content,
    )


