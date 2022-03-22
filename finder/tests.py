import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, reverse_lazy
from .forms import StudentForm
from .models import AreaOfStudy, Pathway, Degree

# i didn't need these to test my views
from .views import index, get_data_entry_page, get_areas, get_all_pathways, get_pathways, get_pathway_detail, \
    get_area_detail, get_degree_detail, new_area, new_degree, new_pathway, new_class, new_student


# model tests
class AreaOfStudyTest(TestCase):

    def aos_setup(self):
        area = AreaOfStudy(area_of_study="Flatulence")
        area.description = "Test description"
        area.revised_date = datetime.date.today()
        return area

    def test_string(self):
        area = self.aos_setup()
        self.assertEqual(str(area), area.area_of_study)
        self.assertEqual(area.description, "Test description")

    def test_date(self):
        area = self.aos_setup()
        self.assertEqual(area.revised_date, datetime.date.today())

    def test_table(self):
        self.assertEqual(str(AreaOfStudy._meta.db_table), 'Area of Study')
        self.assertEqual(str(AreaOfStudy._meta.verbose_name_plural), 'Areas of Study')


class PathwayTest(TestCase):

    def path_setup(self):
        path = Pathway()
        path.area = AreaOfStudy(area_of_study="Flatulence")
        path.subject = 'Pork & Beans'
        path.description = 'The magical fruit'
        path.revised_date = datetime.date.today()
        return path

    def test_string(self):
        self.path = self.path_setup()
        self.assertEqual(str(self.path), self.path.subject)
        self.assertEqual(self.path.description, 'The magical fruit')

    def test_date(self):
        self.path = self.path_setup()
        self.assertEqual(self.path.revised_date, datetime.date.today())

    def test_table(self):
        self.assertEqual(str(AreaOfStudy._meta.db_table), 'Area of Study')
        self.assertEqual(str(AreaOfStudy._meta.verbose_name_plural), 'Areas of Study')


class DegreeTest(TestCase):

    def deg_setup(self):
        degree = Degree()
        degree.pathway = Pathway()
        degree.title = 'SBD Certification'
        degree.description = 'No one ever has to know..'
        degree.contact = 'bigGuy@fakegmail.com'
        degree.guide = 'https://www.atomic.org'
        degree.grants = ['Opportunity Grant', 'Pell Grant']
        degree.revised_date = datetime.date.today()
        return degree

    def test_string(self):
        self.area = AreaOfStudy(area_of_study="Flatulence")
        self.path = Pathway()
        self.degree = self.deg_setup()
        self.assertEqual(str(self.degree), 'SBD Certification')
        self.assertEqual(str(self.degree.description), 'No one ever has to know..')


# view tests
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class DataEntryTest(TestCase):
    def test_get_data_entry_page(self):
        response = self.client.get(reverse('data_entry'))
        self.assertEqual(response.status_code, 200)


class AreasOfStudyTest(TestCase):
    def test_get_areas_page(self):
        response = self.client.get(reverse('areas'))
        self.assertEqual(response.status_code, 200)


# view tests with input
class AreaOfStudyDetailTest(TestCase):
    def setup(self):
        self.area = AreaOfStudy.objects.create(area_of_study='Testing', description='just testing',
                                               revised_date=datetime.date.today())

    # todo: is failing but is working fine in the app ??!!
    def test_area_detail_success(self):
        self.area = AreaOfStudy.objects.create(area_of_study='Testing', description='just testing',
                                               revised_date=datetime.date.today())
        print(f'AoS id: {self.area.id}')
        response = self.client.get(reverse('path_detail', args=(self.area.id,)))
        self.assertEqual(response.status_code, 200)


# form tests
class StudentFormTest(TestCase):
    def test_studentform_is_valid(self):
        degree = Degree.objects.create(title='Test')
        form = StudentForm(data={'first_name': 'User', 'last_name': 'Test', 'ctc_link_id': 123456789,
                                 'is_enrolled': 'Yes', 'degree': degree, 'path_interests': ['stuff']})
        self.assertTrue(form.is_valid())

    def test_studentform_is_valid_with_blank_options(self):
        degree = Degree.objects.create(title='Test')
        form = StudentForm(data={'first_name': 'User', 'last_name': 'Test', 'ctc_link_id': 123456789,
                                 'is_enrolled': 'Yes', 'degree': degree, 'path_interests': None})
        self.assertTrue(form.is_valid())

    def test_studentform_is_empty(self):
        form = StudentForm(data={'first_name': ''})
        self.assertFalse(form.is_valid())


class NewPathAuthenticationTest(TestCase):
    def setup(self):
        self.test_user = User.objects.create_user(username='testuser1', password='p@$$w0rd1')
        self.area = AreaOfStudy.objects.create(area_of_study='Testing', description='some testing',
                                               revised_date=datetime.date.today())
        self.path = Pathway.objects.create(area=self.area, subject='still testing', description='yep still testing',
                                           revised_date=datetime.date.today())

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('new_pathway'))
        self.assertRedirects(response, '/accounts/login/?next=/finder/new_pathway')

