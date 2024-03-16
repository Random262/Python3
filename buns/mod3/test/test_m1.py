import datetime
import unittest
from freezegun import freeze_time

from app.m1 import app

day_to_word_map = {
    0: "Хорошего понедельника",
    1: "Хорошего вторника",
    2: "Хорошей среды",
    3: "Хорошего четверга",
    4: "Хорошей пятницы",
    5: "Хорошей субботы",
    6: "Хорошего воскресенья"
}

class TestWeekdayApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = "/hello-world/"

    def _get_weekday(self):
        current_day = datetime.datetime.today().weekday()
        return day_to_word_map[current_day]

    def test_can_get_correct_weekday(self):
        username = "some"
        weekday = self._get_weekday()
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

    @freeze_time("2024-03-11")
    def test_can_get_correct_username(self):
        username = "Хорошей среды"
        weekday = day_to_word_map[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

    @freeze_time("2024-03-11")
    def test_can_get_correct_mon(self):
        username = "some"
        weekday = day_to_word_map[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

    @freeze_time("2024-03-12")
    def test_can_get_correct_tue(self):
        username = "some"
        weekday = day_to_word_map[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

    @freeze_time("2024-03-13")
    def test_can_get_correct_wed(self):
        username = "some"
        weekday = day_to_word_map[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

    @freeze_time("2024-03-14")
    def test_can_get_correct_thu(self):
        username = "some"
        weekday = day_to_word_map[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

    @freeze_time("2024-03-15")
    def test_can_get_correct_fri(self):
        username = "some"
        weekday = day_to_word_map[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

    @freeze_time("2024-03-16")
    def test_can_get_correct_sat(self):
        username = "some"
        weekday = day_to_word_map[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

    @freeze_time("2024-03-17")
    def test_can_get_correct_sun(self):
        username = "some"
        weekday = day_to_word_map[datetime.datetime.today().weekday()]
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(weekday in response_text)

if __name__ == '__main__':
    unittest.main()


