
# Blink Home Security Camera System
This project is based on [BlinkMonitorProtocol](https://github.com/MattTW/BlinkMonitorProtocol) and [Blink](https://github.com/keredson/blink), including:

+ Python API for Blink Cameras (python 2.7)
+ **[Unofficial API documentation](https://duangenquan.github.io/slate/) with sample requests (shell/python/javascript) and sample results **

Highlighted functions based on blink client APIs:
+ **Refresh all cameras by capturing thumbnails**
+ List all onboarded clied networks IDs 
+ List all onbaorded camera IDs
+ **Download video clips from all cameras or one camera**

The following experiments are carried out with Blink XT cameras. 

--- 
## How To Use
Run examples
```
python main.py --email youremail --password yourpassword
```
Run unittests
```
python unittests.py youremail yourpassword
```


### Step 1. Initialize blink

```python
import blink
b = blink.Blink(*youremail*, *yourpassword*)
```

### Step 2. List onboarded networks and cameras
```python
networksids = b.list_network_ids()
cameraids = b.list_camera_ids()
cameraInfo = b.get_camera_info()
print('Camera Info: ' + str(cameraInfo))
cameraSensorInfo = b.get_camera_sensor_info()
print('Camera Sensor Info: ' + str(cameraSensorInfo))
```

### Step 3. Capture and download latest thumnail
```python
b.refresh_all_cameras_thumbnail()
data = b.homescreen()
for device in data['devices']:
    if device['device_type'] is not None and device['device_type'] == "camera":
        content,filename = b.download_thumbnail_home_v2(device)
        blink.save_to_file(content, filename)
        print("Download latest thumbnails to " + filename)
```

### Step 4. Download events from camera(s)
```python
# Download events from a network
print("Download latest events from all cameras")
events = b.eventsv2()
for event in events:
    content = b.download_video_v2(event)
    filename = b.get_event_name_v2(event)
    blink.save_to_file(content, filename)

# Download latest events from one camera
print("Download latest events from one camera")
if len(cameraids) > 0:
    id = cameraids[0]
    # Download at most 5 event from this camera
    events = b.events_from_camera(id, 5)
    for event in events:
        content = b.download_video_v2(event)
        filename = b.get_event_name_v2(event)
        blink.save_to_file(content, str(id) + "_" + filename)
```

## API Summary
|Function|Description|Implemented|Works|
|--------|-----------|-----------|-----|
|`login`|Client login to the Blink Servers. | yes | yes | 
|`networks`|Obtain information about the Blink networks defined for the logged in user. | yes | yes | 
|`cameras`|Gets a list of cameras. | yes | yes | 
|`homescreen`|Return information displayed on the home screen of the mobile client. | yes | yes | 
|`download_thumbnail (event/device) `|Get a thumbnail from the event or device. | yes | yes | 
|`eventsv2`|Gets a paginated set of video information. | yes | yes | 
|`download_video_v2`|Get a video clip from the events list. | yes | yes | 
|`get_video_count`|Get total number of videos. | yes | yes | 
|`refresh_all_cameras_thumbnail`|Refresh all cameras by capturing thumbnails. | yes | yes | 
|`refresh_all_cameras_video`|Refresh all cameras by capturing videos. | yes | yes | 
|`sync_modules`|Obtain information about the Blink Sync Modules on the given network. | yes | yes | 
|`arm`|Arm the given network (start recording/reporting motion events). | yes | yes | 
|`disarm`|Disarm the given network (stop recording/reporting motion events. | yes | yes | 
|`command_status`|Get status info on the given command. | yes | yes | 
|`events`|Get events for a given network (sync module). | yes | yes | 
|`get_video_info`|Gets information for a specific video by ID. | yes | yes | 
|`unwatched_videos`|Gets a list of unwatched videos. | yes | yes | 
|`delete(video)`|Deletes a video. | yes | yes | 
|`delete(videos)`|Deletes all videos. | no |  | 
|`get_camera_info`|Gets camera information. | yes | yes | 
|`get_camera_sensor_info`|Gets camera sensor information. | yes | yes | 
|`clients`|Gets information about devices that have connected to the blink service. | yes | yes | 
|`regions`|Gets information about supported regions. | yes | yes | 
|`health`|Gets information about system health. | yes | no | 
|`program info`|Gets information about programs. | yes | no | 

## Contact
duangenquan@gmail.com
