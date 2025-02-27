import time
import Sign

token = {
    "x-legacy-smid": "20241201002052dfbec0c6a9179fb604fde1182a66db9c01f867aaa6e302c2",
    "x-legacy-did": "283863a9-ed55-3523-a053-d2f37ca05f75",
    "x-legacy-fid": "173298364610417612da23987ec865af31d2daa014d6",
    "x-legacy-sid": "session.1732983709043320934796",
    "x-mini-gid": "7c583d3f4cea546d79734234c4771a8f650cdd9947359ced77344525",
    "x-mini-sig": "539b3190c42330a2e20ab84a5168c7ba905bae73ce0e035612101fe8cf35d96e",
    "x-mini-mua": "eyJhIjoiRUNGQUFGMDEiLCJjIjoxMywiayI6ImE0ODUyMzQ5NzBhNmQzYjdkNzAwYWU2NWRkMjU0MTRjMjIyNGJjZTM0ZmNiNWEwNjM0MTU4ZmJhNjk1NmMwNmMiLCJwIjoiYSIsInMiOiI4OGIxMTgzZjZjNjY1ZjYwYjAxMGRmZDcyNDczNmNmMiIsInQiOnsiYyI6MCwiZCI6MCwiZiI6MCwicyI6NDA5OCwidCI6MCwidHQiOltdfSwidSI6IjAwMDAwMDAwYzI0YTJjNWIxYTNiMTUyMzM0ZjdiNjIxM2Q0NzdhNWQiLCJ2IjoiMi43LjQifQ.__nSMRZRIRwlZwdlfCEihZXN_brJxSD60V6L_919_j9x8Uiy4rY2HrUBqROQlq3gU9OYIQv2L5rpgNOxTdnHt5WSKznqw5casRH2Uodvp_yRW3clCkhh_vTAVyv1rpd3KdBOzgno0wBRg6NbN7KSEhbt3x3_4R35OLRLr5kHnuDohmQ1JNN4bb9qVKQDE6Uwx9ukwRf3bGe1u8zJOsiRrWCJ-TTgkCyDQ5Y5fvk8ce8DFZTTCM3HXJwjwfab7DcJyAFtABQuXY8xk4Gp7KsVvXhgfce3lZNOr9bScnGnHRegAnZd6IYRJMxPV87Ow084-EV-5oP9LXxLmNP-HrhYdrxFIkWcvK0brKI9AkVaDHB-hIj2Azc4mFUsA1CxLA2mCvldm3kpgfczvCuDCn8wpEX1dFWaHAz1sT5PXSOFc7tgL_kGSsbD6BexbFlxl2XwAvnkXCpPg-9DD3vIZ9IUQXehqNFZUDPC6hghfokJ-zWXjFBC35T28xbf_aLlsx_drPFruH1c3cIcSlpg7C5kTHC_1IwRUHoDFbQIiDxiimqu1y3iX485Fb5_Hdx6vlLswWBfMpfzsWMfGYY4SW7ZIgPuUu2qzxDDI59ZKyg_tHGB6QeIqLpVWgcO7GezOZEo4N5LkbqEbxwi53NL0cMittrwT_Kkmkiwrap98Ze7Py6rQRi0viwKU1tatS6td3VS2zh7ZUDXwPr5AWqevGVVFTKan_x-Yhd9qlztV5J-GV-_BaloxJvmDQdGrBCc5NaL7uLksqw0QIMtqQcoy1z1nc4iR4taJvPypK1vdNP9GYijB5mW-PXTx3wJllpoK2sBbWB0yyw-UmytLzUxko5N_CYZMcl80eO6Zv30SYh0lAdTgxvMMCFMuIHFp4dyooWGakpQbTO7NCWe6jaSoIXUmxlERbhC-oBtTVLwrZ5nbtVvOjI4HapR18km0MewNphfnKqgCOItIWtBAMUL6DH-_A.",
    "xy-common-params": "fid=173298364610417612da23987ec865af31d2daa014d6&device_fingerprint=20241201002052dfbec0c6a9179fb604fde1182a66db9c01f867aaa6e302c2&device_fingerprint1=20241201002052dfbec0c6a9179fb604fde1182a66db9c01f867aaa6e302c2&cpu_name=qcom&gid=7c583d3f4cea546d79734234c4771a8f650cdd9947359ced77344525&device_model=phone&launch_id=1732983748&tz=Asia%2FShanghai&channel=share_package_common&versionName=8.60.1&overseas_channel=0&deviceId=283863a9-ed55-3523-a053-d2f37ca05f75&platform=android&sid=session.1732983709043320934796&identifier_flag=4&t=1732983748&project_id=ECFAAF&build=8601104&x_trace_page_current=explore_feed&lang=zh-Hans&app_id=ECFAAF01&uis=light&teenager=0",
    "xy-platform-info": "platform=android&build=8601104&deviceId=283863a9-ed55-3523-a053-d2f37ca05f75",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; SM-A715F Build/TP1A.220624.014) Resolution/720*1280 Version/8.60.1 Build/8601104 Device/(samsung;SM-A715F) discover/8.60.1 NetType/CellNetwork",
    "main_hmac": "sRLePFN+L2tfXdXDZIRp4767JpeFMsFkLdX2RLTtShOq79kIwybN8L1WVIUYiiUANCWlkMvnKcM89mGBMLrpJ+c44XFnUnsS5z9jQVPJMAEIRFInOGUM3yGWOfF7Rj0q"
}