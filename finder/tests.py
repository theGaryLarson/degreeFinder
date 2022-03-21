import datetime

from django.test import TestCase
from .models import AreaOfStudy, Pathway, Degree

def aos_setup():
    area = AreaOfStudy(area_of_study="Flatulence")
    area.description = "Test description"
    area.revised_date = datetime.date.today()
    return area

def path_setup(area):
    path = Pathway(area=area)
    path.subject = 'Pork & Beans'
    path.description = 'The magical fruit'
    path.revised_date = datetime.date.today()
    return path

def deg_setup(path):
    degree = Degree(pathway=path)
    degree.title = 'SBD Certification'
    degree.description = 'No one ever has to know..'
    degree.contact = 'bigGuy@fakegmail.com'
    degree.guide = 'https://www.atomic.org'
    degree.grants = ['Opportunity Grant', 'Pell Grant']
    degree.revised_date = datetime.date.today()
    return degree


# Create your tests here.
class AreaOfStudyTest(TestCase):
    def __init__(self):
        super().__init__()
        self.area = aos_setup()

    def test_string(self):
        self.assertEqual(str(self.area), self.area.area_of_study)
        self.assertEqual(self.area.description, "Test description")

    def test_date(self):
        self.assertEqual(self.area.revised_date, datetime.date.today())

    def test_table(self):
        self.assertEqual(str(AreaOfStudy._meta.db_table), 'Area of Study')
        self.assertEqual(str(AreaOfStudy._meta.verbose_name_plural), 'Areas of Study')


class PathwayTest(TestCase):
    def __init__(self):
        super().__init__()
        self.area = AreaOfStudy(area_of_study="Flatulence")
        self.path = Pathway(area=self.area)
        self.path.subject = 'Pork & Beans'
        self.path.description = 'The magical fruit'
        self.path.revised_date = datetime.date.today()

    def test_string(self):
        self.assertEqual(str(self.area), self.area.area_of_study)
        self.assertEqual(self.area.description, "Test description")

    def test_date(self):
        self.assertEqual(self.area.revised_date, datetime.date.today())

    def test_table(self):
        self.assertEqual(str(AreaOfStudy._meta.db_table), 'Area of Study')
        self.assertEqual(str(AreaOfStudy._meta.verbose_name_plural), 'Areas of Study')
