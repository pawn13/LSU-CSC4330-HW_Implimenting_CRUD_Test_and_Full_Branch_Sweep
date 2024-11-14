import unittest
from student_crud import StudentRegistrationSystem

class TestRegistrationSystem(unittest.TestCase):
    def setUp(self):
        self.registration = StudentRegistrationSystem()
        self.registration.create_student(student_id=1, name='Mike', age=8, major='Roar Management')

    def test_create_student(self):
        print("Test #1: Creation.")
        self.assertIn(1, self.registration.students)
        self.assertEqual(self.registration.students[1].name, 'Mike')
        self.assertEqual(self.registration.students[1].age, 8)
        self.assertEqual(self.registration.students[1].major, 'Roar Management')

        self.assertFalse(self.registration.create_student(student_id=1, name='John', age=20, major='Physics'))
        #double checking if it didn't write over
        self.assertEqual(self.registration.students[1].name, 'Mike')
        self.assertEqual(self.registration.students[1].age, 8)
        self.assertEqual(self.registration.students[1].major, 'Roar Management')


    def test_read_student(self):
        print("Test #2: Reading.")
        self.assertEqual(self.registration.read_student(student_id=1), 1)
        self.assertIsNone(self.registration.read_student(student_id=999))

    def test_read_all_students(self):
        print("Test #3: Reading All.")
        output = self.registration.read_all_students()
        self.assertEqual(len(output), 1)
        self.registration.students.clear()
        self.assertEqual(self.registration.read_all_students(), [])
        self.assertEqual(len(self.registration.read_all_students()), 0)
        self.registration.create_student(student_id=1, name='Mike', age=8, major='Roar Management')

    def test_delete_student(self):
        print("Test #4: Delete.")
        self.assertTrue(self.registration.delete_student(student_id=1))
        self.assertFalse(self.registration.delete_student(student_id=999))

    def test_update_student(self):
        print("Test #5: Update")
        self.assertTrue(self.registration.update_student(student_id=1, name='Tony', age=24, major="CSC"))
        self.assertTrue(self.registration.update_student(student_id=1, name=None, age=22, major="ME"))
        self.assertEqual(self.registration.students[1].name, 'Tony')
        self.assertEqual(self.registration.students[1].age, 22)
        self.assertEqual(self.registration.students[1].major, 'ME')
        self.assertTrue(self.registration.update_student(student_id=1, name='Tiger', age=None, major="ABC"))
        self.assertEqual(self.registration.students[1].name, 'Tiger')
        self.assertEqual(self.registration.students[1].age, 22)
        self.assertEqual(self.registration.students[1].major, 'ABC')
        self.assertTrue(self.registration.update_student(student_id=1, name='Kitty', age=20, major=None))
        self.assertEqual(self.registration.students[1].name, 'Kitty')
        self.assertEqual(self.registration.students[1].age, 20)
        self.assertEqual(self.registration.students[1].major, 'ABC')
        self.assertFalse(self.registration.update_student(student_id=2, name='Tony', age=24, major="CSC"))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestRegistrationSystem('test_create_student'))
    suite.addTest(TestRegistrationSystem('test_read_student'))
    suite.addTest(TestRegistrationSystem('test_read_all_students'))
    suite.addTest(TestRegistrationSystem('test_delete_student'))
    suite.addTest(TestRegistrationSystem('test_update_student'))
    return suite


if __name__ == '__main__':
    unittest.main()
    #runner = unittest.TextTestRunner()
    #runner.run(suite())