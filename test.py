from database.database import create_base, create_session

from unittest import TestCase, defaultTestLoader, TextTestRunner, TestSuite


class TestUserDBCommand(TestCase):

    class TestCreateUser(TestCase):
        def test_correct_data(self):
            ...



async def test_all():
    suite_test_create_user = TestSuite(TestCreateUser)

if __name__ == "__main__":
    test_all()

