import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestWebApplication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up headless Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chromedriver_path = "/home/ubuntu/myapp/restaurantweb/chrome-headless-shell-linux64/chromedriver-linux64"
        cls.driver = webdriver.Chrome(options=chrome_options)
        # Provide the URL of your web application
        cls.driver.get("http://65.1.1.0/restaurantweb/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_home_page_title(self):
    # Replace this URL with the actual URL of your home page
       self.driver.get("http://65.1.1.0/restaurantweb/")

    # Expected title based on the PHP code you provided
       expected_title = "VINCENT PIZZA."

    # Finding the h1 element and getting its text
       actual_title = self.driver.find_element(By.TAG_NAME, "h1").text

    # Asserting that the actual title matches the expected title
       self.assertEqual(actual_title, expected_title)

    def test_order_now_button(self):
        order_now_button = self.driver.find_element_by_link_text("Order Now")
        self.assertTrue(order_now_button.is_displayed())
        order_now_button.click()
        # Add assertions based on the behavior after clicking the "Order Now" button

    def test_menu_categories_exist(self):
        menu_categories = self.driver.find_elements_by_class_name("menu_category_name")
        self.assertGreater(len(menu_categories), 0)

    def test_gallery_images_exist(self):
        gallery_images = self.driver.find_elements_by_class_name("col-md-4")
        self.assertGreater(len(gallery_images), 0)

    def test_table_reservation_flow(self):
        # Replace these values with the actual data you want to test
        selected_date = "2023-12-31"
        selected_time = "18:00"
        number_of_guests = "2"
        client_full_name = "John Doe"
        client_email = "john.doe@example.com"
        client_phone_number = "1234567890"

        # Fill out the form
        date_input = self.driver.find_element(By.NAME, "reservation_date")
        date_input.clear()
        date_input.send_keys(selected_date)

        time_input = self.driver.find_element(By.NAME, "reservation_time")
        time_input.clear()
        time_input.send_keys(selected_time)

        guests_input = self.driver.find_element(By.NAME, "number_of_guests")
        guests_input.clear()
        guests_input.send_keys(number_of_guests)

        # Submit the form
        availability_submit_button = self.driver.find_element(By.NAME, "check_availability_submit")
        availability_submit_button.click()

        # Assert that tables are available (you may need to adjust this assertion)
        error_div = self.driver.find_element(By.CLASS_NAME, "error_div")
        self.assertFalse(error_div.is_displayed(), "All tables are reserved")

        # Fill out client details
        name_input = self.driver.find_element(By.NAME, "client_full_name")
        name_input.clear()
        name_input.send_keys(client_full_name)

        email_input = self.driver.find_element(By.NAME, "client_email")
        email_input.clear()
        email_input.send_keys(client_email)

        phone_input = self.driver.find_element(By.NAME, "client_phone_number")
        phone_input.clear()
        phone_input.send_keys(client_phone_number)

        # Submit the reservation form
        reservation_submit_button = self.driver.find_element(By.NAME, "submit_table_reservation_form")
        reservation_submit_button.click()

        # Assert the success message (you may need to adjust this assertion)
        success_alert = self.driver.find_element(By.CLASS_NAME, "alert-success")
        self.assertTrue(success_alert.is_displayed(), "Reservation successful")

if __name__ == "__main__":
    unittest.main()
