import time
import subprocess

from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path='../google/version_79/chromeDriver')
    driver.get('https://www.google.com/')
    time.sleep(5)
    search_box = driver.find_element_by_name("q")
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)

    #スクリーンショットを撮る
    driver.save_screenshot('test.png')

    screenShotFull(driver, filename='screenshot')

    driver.quit()


def screenShotFull(driver, filename, timeout=30):
    '''フルページ スクリーンショット'''
    # url取得
    url = driver.current_url
    # ページサイズ取得
    w = driver.execute_script("return document.body.scrollWidth;")
    h = driver.execute_script("return document.body.scrollHeight;")
    # コマンド作成
    cmd = 'gtimeout ' + str(timeout)  \
        + ' "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary"' \
        + ' --headless' \
        + ' --hide-scrollbars' \
        + ' --incognito' \
        + ' --screenshot=' + filename + '.png' \
        + ' --window-size=' + str(w) + ',' + str(h) \
        + ' ' + url
    # コマンド実行
    subprocess.Popen(cmd, shell=True,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)

main()
