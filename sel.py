from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("your_username")

password_box = browser.find_element_by_id("password")
password_box.send_keys("your_password")
password_box.submit()

assert "your_username" in browser.page_source  # Checks if your username id on the page

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "your_username" in link_label

browser.quit()