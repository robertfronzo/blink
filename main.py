import os, argparse
import blink

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--email', dest='email', type=str, help='email')
    parser.add_argument('--password', dest='password', type=str, help='password')

    args = parser.parse_args()

    b = blink.Blink(email=args.email, password=args.password)
    b.connect()

    events = b.eventsv2()
    for event in events:
        content = b.download_video_v2(event)
        
        f = open(b.get_event_name_v2(event), 'wb')
        f.write(content)
        f.close()