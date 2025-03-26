import requests
import time

def ngl():
    print("==========================")
    print("  Tool By https://t.me/sharesrctool")
    print("==========================")

    username = input("Nhập Username (không có @): ")
    message = input("Nhập Tin Nhắn Spam: ")
    count = 25

    print("==========================")
    print("Đang Tiến Hành Spam...")

    value = 0
    failed_attempts = 0  

    while value < count:
        headers = {
            'Host': 'ngl.link',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'origin': 'https://ngl.link',
            'referer': f'https://ngl.link/{username}',
        }

        data = {
            'username': username,
            'question': message,
            'deviceId': '0',
            'gameSlug': '',
            'referrer': '',
        }

        try:
            response = requests.post('https://ngl.link/api/submit', headers=headers, data=data, timeout=10)
            
            if response.status_code == 200:
                print(f"✅ Đã gửi thành công ({value + 1}/{count})")
                value += 1
                failed_attempts = 0  

            else:
                failed_attempts += 1

        except requests.exceptions.RequestException as e:
            failed_attempts += 1

        if failed_attempts >= 5:
            time.sleep(60)
            failed_attempts = 0  
        time.sleep(2) 
    print("🎉 Hoàn thành gửi tin nhắn!")

ngl()
