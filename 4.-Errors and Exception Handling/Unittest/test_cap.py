import unittest
import cap

# Crear clase y hereda de unittest.TestCase
class TestCap(unittest.TestCase):
    
    # Crea método de clase
    def test_one_word(self):
        text = 'python' # Variable a pasar a la función como input
        result = cap.cap_text(text) # variable que llama la función y guarda el retorno
        self.assertEqual(result,'Python') # método que verifíca que el resultado sea el esperado

    def test_multiple_words(self):
        text = 'monthy python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monthy Python')

if __name__ == '__main__':
    unittest.main()