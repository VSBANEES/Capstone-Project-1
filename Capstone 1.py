from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Function to test successful login
def test_successful_login(username, password):
    driver = webdriver.Chrome()  # Change this path to your Chrome driver path
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Entering username and password
    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)

    # Clicking login button
    driver.find_element_by_id("btnLogin").click()

    # Verifying successful login
    time.sleep(2)  # Giving some time for the page to load
    assert "dashboard" in driver.current_url.lower(), "Login unsuccessful!"

    # Close the browser
    driver.quit()


# Function to test invalid login
def test_invalid_login(username, password):
    driver = webdriver.Chrome()  # Change this path to your Chrome driver path
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Entering username and password
    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)

    # Clicking login button
    driver.find_element_by_id("btnLogin").click()

    # Verifying error message
    time.sleep(2)  # Giving some time for the page to load
    error_message = driver.find_element_by_id("spanMessage").text
    assert "invalid credentials" in error_message.lower(), f"Expected 'Invalid credentials' error message not found: {error_message}"

    # Close the browser
    driver.quit()


# Function to test adding a new employee
def test_add_new_employee(username, password):
    driver = webdriver.Chrome()  # Change this path to your Chrome driver path
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Logging in
    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)
    driver.find_element_by_id("btnLogin").click()

    # Navigating to PIM module
    driver.find_element_by_id("menu_pim_viewPimModule").click()
    driver.find_element_by_id("menu_pim_addEmployee").click()

    # Adding new employee details
    driver.find_element_by_id("firstName").send_keys("John")
    driver.find_element_by_id("lastName").send_keys("Doe")
    driver.find_element_by_id("btnSave").click()

    # Verifying successful addition message
    time.sleep(2)  # Giving some time for the page to load
    success_message = driver.find_element_by_css_selector(".message.success").text
    assert "Successfully Saved" in success_message, f"Expected 'Successfully Saved' message not found: {success_message}"

    # Close the browser
    driver.quit()


# Function to test editing an existing employee
def test_edit_existing_employee(username, password):
    driver = webdriver.Chrome()  # Change this path to your Chrome driver path
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Logging in
    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)
    driver.find_element_by_id("btnLogin").click()

    # Navigating to PIM module
    driver.find_element_by_id("menu_pim_viewPimModule").click()

    # Editing existing employee
    driver.find_element_by_css_selector(".odd > td > a").click()
    driver.find_element_by_id("firstName").clear()
    driver.find_element_by_id("firstName").send_keys("Jane")
    driver.find_element_by_id("btnSave").click()

    # Verifying successful edit message
    time.sleep(2)  # Giving some time for the page to load
    success_message = driver.find_element_by_css_selector(".message.success").text
    assert "Successfully Updated" in success_message, f"Expected 'Successfully Updated' message not found: {success_message}"

    # Close the browser
    driver.quit()


# Function to test deleting an existing employee
def test_delete_existing_employee(username, password):
    driver = webdriver.Chrome()  # Change this path to your Chrome driver path
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Logging in
    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)
    driver.find_element_by_id("btnLogin").click()

    # Navigating to PIM module
    driver.find_element_by_id("menu_pim_viewPimModule").click()

    # Deleting existing employee
    driver.find_element_by_css_selector(".odd > td > input").click()
    driver.find_element_by_id("btnDelete").click()
    driver.find_element_by_id("dialogDeleteBtn").click()

    # Verifying successful deletion message
    time.sleep(2)  # Giving some time for the page to load
    success_message = driver.find_element_by_css_selector(".message.success").text
    assert "Successfully Deleted" in success_message, f"Expected 'Successfully Deleted' message not found: {success_message}"

    # Close the browser
    driver.quit()


# Run test cases
test_successful_login("Admin", "admin123")
test_invalid_login("Admin", "Invalid password")
test_add_new_employee("Admin", "admin123")
test_edit_existing_employee("Admin", "admin123")
test_delete_existing_employee("Admin", "admin123")
