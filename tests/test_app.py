import unittest
import app

class AppTests(unittest.TestCase):
    def test_project_name_exists(self):
        self.assertEqual(app.PROJECT_NAME, "Git Practice Lab")

    def test_greeting_is_not_empty(self):
        self.assertTrue(app.GREETING.strip())

if __name__ == "__main__":
    unittest.main()
