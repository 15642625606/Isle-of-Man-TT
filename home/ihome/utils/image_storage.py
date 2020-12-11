# flake8: noqa
from qiniu import Auth, put_data, etag
import qiniu.config
#需要填写你的 Access Key 和 Secret Key
access_key = '3RDDi4IKNy-grwu4dxgX5idGeN7k--WTrsrFA8UA'
secret_key = 'XAJwPF1JHSbhXARWpUj9WB1c-BIoREtEC3rpUaSj'
def storage(file_data):
    """
    上传文件到七牛
    :param file_data: 要上传的文件数据
    :return:
    """
    #构建鉴权对象
    q = Auth(access_key, secret_key)
    #要上传的空间
    bucket_name = 'i--home'

    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, None, 3600)
    ret, info = put_data(token, None, file_data)
    # print("info=",info)
    # print("ret=",ret)
    if info.status_code == 200:
        # 表示上传成功，返回文件名
        return ret.get("key")
    else:
        # 上传失败
        raise Exception("上传图片到七牛失败")

if __name__ == "__main__":
    with open("./1.png","rb") as f:
        file_data = f.read()
        storage(file_data)