import datetime

from django.test import TestCase
from .models import AreaOfStudy, Pathway, Degree


# Create your tests here.
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
