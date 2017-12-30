import sys, json, unittest
from blink import Blink

class TestBlink(unittest.TestCase):
    email = ""
    password = ""

    def setUp(self):
        self.b = Blink(self.email, self.password)
        self.b.connect()
        
    def test_info(self):
        print('email', self.email)
        print('password', self.password)

    def test_connect(self):
        self.assertTrue(self.b.connected)

    def test_homescreen(self):
        data = self.b.homescreen()
        self.assertTrue(data['account'] is not None)
        self.assertTrue(data['network'] is not None)

    def test_events(self):
        events = self.b.events(self.b.networks[0])
        self.assertEqual(type(events), list)

    def test_events_v2(self):
        events = self.b.eventsv2()
        self.assertEqual(type(events), list)

    def test_events_v2_download(self):
        event = self.b.eventsv2()[0]
        content = self.b.download_video_v2(event)
        filename = self.b.get_event_name_v2(event)
        f = open(filename, 'wb')
        f.write(content)
        f.close()
        print('Save downloaded event to ' + filename)

    def test_cameras(self):
        cameras = self.b.cameras(self.b.networks[0])
        self.assertEqual(type(cameras), list)

    def test_clients(self):
        clients = self.b.clients()
        self.assertTrue(clients['clients'] is not None)
        print(clients)

    def test_sync_modules(self):
        sync_modules = self.b.sync_modules(self.b.networks[0])
        print(sync_modules)

    def test_regions(self):
        regions = self.b.regions()
        print(regions)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestBlink.password = sys.argv.pop()
        TestBlink.email = sys.argv.pop()
    unittest.main()
