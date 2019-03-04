from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse
from .forms import ResourceForm, MeetingForm
from django.contrib.auth.models import User

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

class NewResourceFormTest(TestCase):
    def test_resource_form_is_valid(self):
        user = User.objects.create(username='carissawagner')
        form = ResourceForm(data={'resourcename': 'Official Python Documentation', 'resourcetype': 'Documentation', 'resourceurl': 'https://docs.python.org/3/', 'dateentered': '2019-03-04', 'userid': user.pk})
        self.assertTrue(form.is_valid())

    def test_resource_form_is_invalid(self):
        form = ResourceForm(data={'resourcetype': 'Documentation', 'resourceurl': 'https://docs.python.org/3/', 'dataentered': '2019-03-04', 'userid': 'carissawagner'})
        self.assertFalse(form.is_valid())

class NewMeetingFormTest(TestCase):
    def test_meeting_form_is_valid(self):
        form = MeetingForm(data={'meetingtitle': 'Meeting 1', 'meetingdate': '2019-02-15', 'meetingtime': '12:00 p.m.', 'location': 'SCCC'})
        self.assertTrue(form.is_valid())

    def test_meeting_form_is_valid(self):
        form = MeetingForm(data={'meetingdate': '2019-02-15', 'meetingtime': '12:00 p.m.', 'location': 'SCCC'})
        self.assertFalse(form.is_valid())

class GetResourcesTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/resources')
        self.assertTrue(200 <= response.status_code)
        self.assertTrue(response.status_code < 400)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('resources'))
        self.assertTemplateUsed(response, 'club/resources.html')

class GetMeetingsTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/meetings')
        self.assertTrue(200 <= response.status_code)
        self.assertTrue(response.status_code < 400)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetings'))
        self.assertTemplateUsed(response, 'club/meetings.html')
