
# Blink Home Security Camera System
This project is based on [BlinkMonitorProtocol](https://github.com/MattTW/BlinkMonitorProtocol) and [Blink](https://github.com/keredson/blink).

+ Python API for Blink Cameras
+ Unofficial API documentation with Shell/Python/JavaScript example codes and with sample results

Highlighted functions based on blink client APIs:
+ Refresh all cameras by capturing thumbnails
+ List all onboarded clied networks IDs 
+ List all onbaorded camera IDs
+ Download video clips from all cameras or one camera

--- 
# How To Use

## Step 1. Initialize blink

```python
    import blink
    b = blink.Blink(*youremail*, *yourpassword*)
```

## Step 2. List onboarded networks and cameras
```python
    networksids = b.list_network_ids()
    cameraids = b.list_camera_ids()
```

## Step 3. Capture and download latest thumnail
```python
    b.refresh_all_cameras()
    data = b.homescreen()
    for device in data['devices']:
        if device['device_type'] is not None and device['device_type'] == "camera":
            content,filename = b.download_thumbnail_home_v2(device)  
            blink.save_to_file(content, filename)
            print("Download latest thumbnails to " + filename)
```

## Step 4. Download events from camera(s)
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

# Blink API Summary in this repo
|Function|Description|Implemented|Works|
|--------|-----------|-----------|-----|
|`login`|Client login to the Blink Servers. | yes | yes | 
|`networks()`|Obtain information about the Blink networks defined for the logged in user. | yes | yes | 
|`sync_modules(network)`|Obtain information about the Blink Sync Modules on the given network. | yes | yes | 
|`arm(network)`|Arm the given network (start recording/reporting motion events). | yes | no | 
|`disarm(network)`|Disarm the given network (stop recording/reporting motion events. | yes | no | 
|`command_status()`|Get status info on the given command. | yes | unknown | 
|`homescreen()`|Return information displayed on the home screen of the mobile client. | yes | yes | 
|`events(network)`|Get events for a given network (sync module). | yes | yes | 
|`download_video(event)`|Get a video clip from the events list. | yes | yes | 
|`download_thumbnail(event)`|Get a thumbnail from the events list. | yes | no | 
|`cameras(network)`|Gets a list of cameras. | yes | yes | 
|`clients()`|Gets information about devices that have connected to the blink service. | yes | yes | 
|`regions()`|Gets information about supported regions. | yes | yes | 
|`health()`|Gets information about system health. | yes | yes | 
|`capture_video(camera)`|Captures a new video for a camera. | no |  | 
|`capture_thumbnail(camera)`|Captures a new thumbnail for a camera. | no |  | 
|`unwatched_videos()`|Gets a list of unwatched videos. | no |  | 
|`delete(video)`|Deletes a video. | no |  | 

# Unofficial API Doc
