from selenium import webdriver
import config

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

browser = webdriver.Chrome(options=options)
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click();

username_box = browser.find_element_by_id("login_field")
username_box.send_keys(config.user)
password_box = browser.find_element_by_id("password")
password_box.send_keys(config.password)
password_box.submit()

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "jftucker" in link_label

browser.quit()