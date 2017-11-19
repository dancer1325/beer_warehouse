from django.test import TestCase


class BasicTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Aquí definimos lo que necesitemos para los tests, cosas que no vayan a ser modificadas - nada
        print("setUpTestData()")
        pass

    def setUp(self):
        # Este método se ejecuta antes de cada test - nada
        print("setUp()")
        pass

    def test_false_is_true(self):
        # Primer test básico
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        # Segundo test básico
        self.assertEqual(10 + 10, 20)