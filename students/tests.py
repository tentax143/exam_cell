from django.test import TestCase
from students.models import Student
from django.urls import reverse
class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="nithi",
            regno = '2415'
        )
    def test_student_creation(self):
        self.assertEqual(self.student.name, "nithi")
        self.assertEqual(self.student.regno, "2415")
class StudentViewTest(TestCase):
    def test_student_login_page(self):
        response = self.client.get(reverse('student_login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Student Login")

    def test_document_generation(self):
        response = self.client.post(reverse('student_login'), {
            'name': 'nithi',
            'regno':'2415'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after form submission
        student = Student.objects.get(registernumber='67890')
        response = self.client.get(reverse('generate_documents', args=[student.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
