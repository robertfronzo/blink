import os, argparse
import blink

if __name__=='__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--email', dest='email', type=str, help='email')
  parser.add_argument('--password', dest='password', type=str, help='password')

  args = parser.parse_args()

  b = blink.Blink(email=args.email, password=args.password)
  b.connect()
  print b.health
