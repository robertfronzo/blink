import sys, json, unittest
import blink
from blink import Blink

class TestBlink(unittest.TestCase):
    email = ""
    password = ""

    def setUp(self):
        self.b = Blink(self.email, self.password)
        self.b.login()

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
                blink.save_to_file(content, "home_"+filename)

    def test_events_v2(self):
        events = self.b.eventsv2()
        self.assertEqual(type(events), list)

    def test_video_count(self):
        count = self.b.get_video_count()
        print("video count = " + str(count))

    def test_events_v2_download(self):
        events = self.b.eventsv2()
        if len(events) == 0:
            return ;
        event = events[0]
        content = self.b.download_video_v2(event)
        filename = self.b.get_event_name_v2(event)
        blink.save_to_file(content, "event_"+filename)

    def test_thumbnail_event_v2_download(self):
        events = self.b.eventsv2()
        if len(events) == 0:
            return ;
        event = events[0]
        content = self.b.download_thumbnail_event_v2(event)
        filename = self.b.get_thumbnail_name_event(event, "event")
        f = open(filename, 'wb')
        f.write(content)
        f.close()
        print('Save downloaded image to ' + filename)

###############################################################################
##  Middleware Functions    
###############################################################################
    def test_list_network_ids(self):
        ids = self.b.list_network_ids()
        self.assertEqual(type(ids), list)

    def test_list_camera_ids(self):
        ids = self.b.list_camera_ids()
        self.assertEqual(type(ids), list)

    def test_events_from_camera(self):
        ids = self.b.list_camera_ids()
        if len(ids) > 0:
            id = ids[0]
            events = self.b.events_from_camera(id, 1)
            if len(events) > 0:
                event = events[0]
                content = self.b.download_video_v2(event)
                filename = self.b.get_event_name_v2(event)
                blink.save_to_file(content, "event_camera_"+filename)


###############################################################################
##  System APIs     
###############################################################################
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
