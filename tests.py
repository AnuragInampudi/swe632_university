import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UniversityPortalTests(unittest.TestCase):

    def setUp(self):
        # Initialize the WebDriver (e.g., using Chrome)
        self.driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
        self.driver.implicitly_wait(10)  # Implicit wait for 10 seconds

    def tearDown(self):
        self.driver.quit()

    def test_index_page_role_navigation(self):
        """Test that the role selection on the index page correctly navigates to each portal."""
        driver = self.driver
        # Replace with the correct path or URL to your index.html file.
        driver.get("file:///path/to/your/index.html")
        
        # Verify that the header contains the correct title.
        header_title = driver.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(header_title, "University Academic Advisor Portal")
        
        # Test navigation to Student Portal.
        student_link = driver.find_element(By.LINK_TEXT, "Login as Student")
        student_link.click()
        # Wait until the student dashboard is visible.
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dashboard")))
        dashboard_heading = driver.find_element(By.XPATH, "//section[@id='dashboard']/h2").text
        self.assertEqual(dashboard_heading, "Dashboard")
        
        # Navigate back to index.
        driver.get("file:///path/to/your/index.html")
        
        # Test navigation to University Admin Portal.
        admin_link = driver.find_element(By.LINK_TEXT, "Login as University Admin")
        admin_link.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "adminSidebar")))
        admin_portal_title = driver.find_element(By.CLASS_NAME, "navbar-brand").text
        self.assertIn("Admin Portal", admin_portal_title)
        
        # Navigate back to index.
        driver.get("file:///path/to/your/index.html")
        
        # Test navigation to Financial Aid Admin Portal.
        financial_link = driver.find_element(By.LINK_TEXT, "Login as Financial Aid Admin")
        financial_link.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "faSidebar")))
        fa_portal_title = driver.find_element(By.CLASS_NAME, "navbar-brand").text
        self.assertIn("Financial Aid Portal", fa_portal_title)

    def test_student_major_selection_modal(self):
        """Test that the major selection assistant on the student page works and displays the modal."""
        driver = self.driver
        # Replace with the correct path or URL to your student.html file.
        driver.get("file:///path/to/your/student.html")
        
        # Fill in the "Interests" and "Strengths" fields.
        interests_input = driver.find_element(By.ID, "interests")
        interests_input.send_keys("Math, Science")
        strengths_input = driver.find_element(By.ID, "strengths")
        strengths_input.send_keys("Problem Solving")
        
        # Click the "Suggest My Major" button.
        suggest_major_btn = driver.find_element(By.ID, "suggestMajorBtn")
        suggest_major_btn.click()
        
        # Wait until the modal appears.
        major_modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "majorModal"))
        )
        modal_title = driver.find_element(By.ID, "majorModalLabel").text
        self.assertEqual(modal_title, "Recommended Majors")
        
        # Verify that at least one recommended major is displayed.
        recommended_major = driver.find_element(By.XPATH, "//div[@id='majorModal']//div[@class='card-body']//h5").text
        self.assertIn(recommended_major, ["Computer Science", "Business Administration", "Engineering"])
        
        # Close the modal by clicking the "Close" button.
        close_modal_btn = driver.find_element(By.XPATH, "//div[@id='majorModal']//button[contains(@class, 'btn-secondary')]")
        close_modal_btn.click()
        
        # Optionally, assert that the modal is no longer visible.
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "majorModal")))

if __name__ == "__main__":
    unittest.main()
