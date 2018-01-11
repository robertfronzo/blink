import os, argparse
import blink

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', dest='email', type=str, help='email')
    parser.add_argument('--password', dest='password', type=str, help='password')

    args = parser.parse_args()

    b = blink.Blink(email=args.email, password=args.password)
    b.login()

    b.refresh_all_cameras()
    data = b.homescreen()
    for device in data['devices']:
        if device['device_type'] is not None and device['device_type'] == "camera":
            content,filename = b.download_thumbnail_home_v2(device)  
            blink.save_to_file(content, filename)
            print("Download latest thumbnails to " + filename)

    events = b.eventsv2()
    for event in events:
        content = b.download_video_v2(event)
        filename = b.get_event_name_v2(event)
        blink.save_to_file(content, filename)