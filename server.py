from __future__ import absolute_import, print_function
import argparse
import server

def main():
    parser = argparse.ArgumentParser(description='Run the bycombat server.')
    parser.add_argument('--build', choices=['debug', 'release'], default='debug', required=False, help='build to run with server')
    parser.add_argument('--debug', action='store_const', const='debug', dest='build', help='run debug server using local cocos project')
    parser.add_argument('--release', action='store_const', const='release', dest='build', help='run release server using built cocos project')

    args = parser.parse_args()
    debug = args.build == 'debug'
    print('Running server in {} mode'.format(args.build))
    server.run()

if __name__ == '__main__':
    main()
