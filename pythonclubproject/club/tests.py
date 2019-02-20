from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse

# Create your tests here.
class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting = Meeting(meetingtitle = 'Meeting 1')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tableName(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def test_stringOutput(self):
        meeting = Meeting(meetingtitle = 'Meeting 2')
        meetingminutes = MeetingMinutes(meetingid = meeting)
        self.assertEqual(str(meetingminutes), 'Meeting minutes for ' + str(meetingminutes.meetingid))

    def test_tableName(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource = Resource(resourcename = 'Resource 1')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tableName(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def test_stringOutput(self):
        event = Event(eventtitle = 'Event 1')
        self.assertEqual(str(event), event.eventtitle)

    def test_tableName(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class TestIndex(TestCase):
    def test_viewUrlAccessibleByName(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_viewUsesCorrectTemplate(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'club/index.html')
