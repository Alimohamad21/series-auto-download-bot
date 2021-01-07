import datetime
import os
import time

from selenium import webdriver


def close_tab(n):
    while True:
        if len(driver.window_handles) == n:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            driver.switch_to.window(driver.window_handles[n - 2])
            break


series = input("series:")
series_unchanged = series
season = int(input("season you want download:"))
from_episode = int(input("from episode:"))
to_episode = int(input("to episode:"))
series = series.lower()
series = series.replace(" ", "-")
driver = webdriver.Edge('/Users/Mohamed/Downloads/msedgedriver')
first = True
i = 0
for episode in range(from_episode - 1, to_episode):
    count = 0
    driver.get(
        "https://amla.egybest.biz/episode/{}-season-{}-ep-{}/#download".format(series, season, episode + 1))
    driver.execute_script("window.scrollBy(0,600)")
    time.sleep(3)
    if first:
        driver.find_element_by_xpath("//*[text()='لاحقاً']").click()
        close_tab(2)
        first = False
    time.sleep(3)
    driver.find_elements_by_xpath("//*[text()=' تحميل']")[1].click()
    while True:
        if len(driver.window_handles) == 2:
            driver.switch_to.window(driver.window_handles[-1])
            break
    while True:
        try:
            driver.find_element_by_class_name("bigbutton").click()
            if len(driver.window_handles) == 3:
                close_tab(3)
                break
        except:
            pass
    time.sleep(3)
    for fname in os.listdir("/Users/Mohamed/Downloads"):
        if fname.endswith('.crdownload'):
            count += 1
    print(count)
    if count != (i + 1):
        driver.find_element_by_class_name("bigbutton").click()
        close_tab(3)
        close_tab(2)
    else:
        close_tab(2)
    t = datetime.datetime.now()
    print("S{}E{} of {} downloaded successfully!".format(season, episode + 1, series_unchanged))
    f = open("history.txt", "a")
    f.write(
        "S{}E{} of {} downloaded successfully at ".format(season, episode + 1, series_unchanged) + t.strftime(
            "%Y-%m-%d %H:%M:%S !") + "\n")
    i += 1
