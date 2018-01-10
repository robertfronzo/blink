import sys, json, unittest
from blink import Blink

class TestBlink(unittest.TestCase):
    email = ""
    password = ""

    def setUp(self):
        self.b = Blink(self.email, self.password)
        self.b.login()

    def save_to_file(self, content, filename):
        f = open(filename, 'wb')
        f.write(content)
        f.close()
        print('Save downloaded event to ' + filename)

###############################################################################
##  Client APIs     
###############################################################################
    def test_login(self):
        self.assertTrue(self.b.connected)

    def test_homescreen(self):
        data = self.b.homescreen()
        self.assertTrue(data['account'] is not None)
        self.assertTrue(data['network'] is not None)
        for device in data['devices']:
            if device['device_type'] is not None and device['device_type'] == "camera":
                content,filename = self.b.download_thumbnail_home_v2(device)
                self.save_to_file(content, "home_"+filename)

#     def test_events_v2(self):
#         events = self.b.eventsv2()
#         self.assertEqual(type(events), list)

#     def test_video_count(self):
#         count = self.b.get_video_count()
#         print("video count = " + str(count))

#     def test_events_v2_download(self):
#         event = self.b.eventsv2()[0]
#         content = self.b.download_video_v2(event)
#         filename = self.b.get_event_name_v2(event)
#         self.save_to_file(content, "event_"+filename)

#     def test_thumbnail_event_v2_download(self):
#         event = self.b.eventsv2()[0]
#         content = self.b.download_thumbnail_event_v2(event)
#         filename = self.b.get_thumbnail_name(event, "event")
#         f = open(filename, 'wb')
#         f.write(content)
#         f.close()
#         print('Save downloaded image to ' + filename)

# ###############################################################################
# ##  System APIs     
# ###############################################################################
#     def test_cameras(self):
#         cameras = self.b.cameras(self.b.networks[0])
#         self.assertEqual(type(cameras), list)

#     def test_clients(self):
#         clients = self.b.clients()
#         self.assertTrue(clients['clients'] is not None)
#         print(clients)

#     def test_sync_modules(self):
#         sync_modules = self.b.sync_modules(self.b.networks[0])
#         print(sync_modules)

#     def test_regions(self):
#         regions = self.b.regions()
#         print(regions)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestBlink.password = sys.argv.pop()
        TestBlink.email = sys.argv.pop()
    unittest.main()
