import unittest
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def test_default_password_length(self):
        generator = PasswordGenerator()
        password = generator.generate()
        self.assertEqual(len(password), 12)
    
    def test_custom_password_length(self):
        generator = PasswordGenerator(length=20)
        password = generator.generate()
        self.assertEqual(len(password), 20)
    
    def test_exclude_uppercase(self):
        generator = PasswordGenerator(include_uppercase=False)
        password = generator.generate()
        self.assertTrue(all(char.islower() or not char.isalpha() for char in password))
    
    def test_exclude_numbers(self):
        generator = PasswordGenerator(include_numbers=False)
        password = generator.generate()
        self.assertTrue(all(not char.isdigit() for char in password))
    
    def test_exclude_symbols(self):
        generator = PasswordGenerator(include_symbols=False)
        password = generator.generate()
        self.assertTrue(all(char.isalnum() for char in password))

if __name__ == "__main__":
    unittest.main()
