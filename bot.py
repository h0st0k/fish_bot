import os
import time
import random
import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

MAX_ACTIVITIES = 300  
activity_count = 0
PHONE_IP = "10.219.115.234:5555" # Наш стабильный Realme

def send_phone_activity():
    try:
        start_y = random.randint(1200, 1600)
        end_y = random.randint(300, 700)
        x = random.randint(400, 600)
        subprocess.run(
            f"adb -s {PHONE_IP} shell input swipe {x} {start_y} {x} {end_y} 400", 
            shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        print(f"[📱 Realme] Имитация свайпа выполнена успешно.", flush=True)
    except Exception:
        pass

chrome_options = Options()
chrome_options.add_argument("--headless=new") # Скрытый стабильный режим
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
chrome_options.add_argument("--autoplay-policy=no-user-gesture-required") 
chrome_options.add_argument("--mute-audio") 

profile_path = os.path.expanduser("~/odin_chrome_profile")
chrome_options.add_argument(f"--user-data-dir={profile_path}")

print("[+] Подключаем Realme...", flush=True)
subprocess.run(f"adb connect {PHONE_IP}", shell=True, stdout=subprocess.DEVNULL)

try:
    driver = webdriver.Chrome(options=chrome_options)
    print("[+] Фоновый Google Chrome запущен!", flush=True)
except Exception as e:
    print(f"[-] Ошибка запуска браузера: {e}", flush=True)
    sys.exit(1)

try:
    print("[+] Открываем учебную страницу Odin...", flush=True)
    driver.get("https://odin.study")
    time.sleep(7)
    
    print(f"[+] КОМПЛЕКС В РАБОТЕ (ПК + Realme)! Лимит: {MAX_ACTIVITIES} действий.", flush=True)
    
    while activity_count < MAX_ACTIVITIES:
        try:
            videos = driver.find_elements(By.TAG_NAME, "video")
            if len(videos) > 0:
                video = videos[0]
                driver.execute_script("arguments.scrollIntoView({block: 'center'});", video)
                time.sleep(2)
                try:
                    actions = ActionChains(driver)
                    actions.move_to_element(video).click().perform()
                except:
                    pass
                driver.execute_script("arguments.play();", video)
                time.sleep(3)
                
                duration = driver.execute_script("return arguments.duration;", video)
                if duration and duration > 0:
                    target_time = duration * 0.75
                    print(f"[+] Видео запущено! Длительность: {int(duration)}с.", flush=True)
                    current_time = 0
                    while current_time < target_time:
                        current_time = driver.execute_script("return arguments.currentTime;", video)
                        time.sleep(15)
                        if random.random() > 0.4:
                            send_phone_activity()
                    driver.execute_script("arguments.pause();", video)
                    activity_count += 5
        except Exception:
            pass
        
        scroll_y = random.randint(200, 850)
        driver.execute_script(f"window.scrollTo(0, {scroll_y});")
        activity_count += 1
        print(f"[{activity_count}/{MAX_ACTIVITIES}] Скролл страницы на ПК на {scroll_y}px", flush=True)
        
        if random.random() > 0.3:
            send_phone_activity()
        
        time.sleep(random.randint(40, 85))

except Exception as e:
    print(f"[-] Произошла ошибка: {e}", flush=True)
finally:
    driver.quit()
    print("[+] Браузер закрыт.", flush=True)
