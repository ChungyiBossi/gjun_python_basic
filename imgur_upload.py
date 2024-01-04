
from secret_tokens import (
    IMGUR_CLIENT_ID,
    IMGUR_CLIENT_SECRET
)
from imgurpython import ImgurClient
def upload_to_imgur(filename):
    # 在Imgur开发者门户中获取你的客户端ID和客户端密钥
    client_id = IMGUR_CLIENT_ID
    client_secret = IMGUR_CLIENT_SECRET

    # 创建ImgurClient对象
    client = ImgurClient(client_id, client_secret)

    # 上传图像
    image_path = filename  # 替换为你的图像路径
    uploaded_image = client.upload_from_path(image_path, anon=True)

    # 获取上传后的图像链接
    image_url = uploaded_image['link']

    print(f"Image uploaded successfully! Image URL: {image_url}")

    return image_url

if __name__ == '__main__':
    upload_to_imgur('./image.jpg')