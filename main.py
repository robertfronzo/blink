import os, argparse
import blink

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', dest='email', type=str, help='email')
    parser.add_argument('--password', dest='password', type=str, help='password')

    args = parser.parse_args()

    b = blink.Blink(email=args.email, password=args.password)
    b.login()

    ## Show all network IDs
    networksids = b.list_network_ids()
    print('Network IDs are:')
    for id in networksids:
        print(id)

    # Show all camera IDs
    cameraids = b.list_camera_ids()
    print('Camera IDs are:')
    for id in cameraids:
        print(id)
    cameraInfo = b.get_camera_info()
    print('Camera Info: ' + cameraInfo)
    cameraSensorInfo = b.get_camera_sensor_info()
    print('Camera Sensor Info: ' + cameraids)

    # Update all cameras and download latest thumbnails
    b.refresh_all_cameras()
    data = b.homescreen()
    for device in data['devices']:
        if device['device_type'] is not None and device['device_type'] == "camera":
            content,filename = b.download_thumbnail_home_v2(device)  
            blink.save_to_file(content, filename)
            print("Download latest thumbnails to " + filename)

    # Download latest events from all cameras
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
            