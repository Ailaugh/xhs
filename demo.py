import requests,base64

headers = {
    'Host': 'mall.xiaohongshu.com',
    'User-Agent': 'discover/8.69.4 (iPhone; iOS 17.6.1; Scale/3.00) Resolution/1179*2556 Version/8.69.4 Build/8694110 Device/(Apple Inc.;iPhone16,1) NetType/CellNetwork',
    'xy-direction': '49',
    'xy-scene': 'point=0&fs=0',
    'X-B3-TraceId': '63e1c77f1bb23d61',
    'Accept-Language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
    'x-legacy-did': '49879933-4925-4F79-BFA6-F3F49479EDD6',
    'shield': 'XYAAAAAQAAAAEAAABTAAAAUzUWEe4xG1IYD9/c+qCLOlKGmTtFa+lG434IdeVXRa1GzIy3l79kT5389uJaz8Rc28R+o9RDFgw4EhOMbb/z1V4U8uKvdEay6+keYq8QUbO4nBSi',
    'x-legacy-smid': '20240122173844e7ff1943e8893b4b3780e5c16529b60e0111c8c644120589',
    'xy-platform-info': 'platform=iOS&version=8.69.4&build=8694110&deviceId=49879933-4925-4F79-BFA6-F3F49479EDD6&bundle=com.xingin.discover',
    'Mode': 'gslb',
    'xy-common-params': 'app_id=ECFAAF02&build=8694110&channel=AppStore&deviceId=49879933-4925-4F79-BFA6-F3F49479EDD6&device_fingerprint=20240122173844e7ff1943e8893b4b3780e5c16529b60e0111c8c644120589&device_fingerprint1=20240122173844e7ff1943e8893b4b3780e5c16529b60e0111c8c644120589&device_model=phone&dlang=zh&fid=1738247685-0-0-9fc8d3c2e56b47692721596b943bfc8e&gid=7c23a6f3aa545476dcd26476edff05fcdf679cd8473597ac770b1864&identifier_flag=0&is_mac=0&lang=zh-Hans&launch_id=760154420&overseas_channel=0&platform=iOS&project_id=ECFAAF&sid=session.1738245861699845576114&t=1738461691&teenager=0&tz=Asia/Shanghai&uis=light&version=8.69.4',
}

url = "https://mall.xiaohongshu.com/api/store/jpd/edith/detail/vision/primary?ext_query=%7B%22goodsId%22%3A%22678cc83bbac251000178c386%22%7D&sku_id=678cc83bbac251000178c386&source=user_page&trade_ext=eyJjaGFubmVsSW5mbyI6eyJjaGFubmVsIjoic2hvcCIsImV4dHJhSW5mbyI6IntcImdvb2RzTm90ZUlkXCI6XCI2NzVlNTFhNDAwMDAwMDAwMDYwMGY0ZjVcIn0ifX0%3D"
response = requests.get(
    url,
    headers=headers,
)
print(response.json())
