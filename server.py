from __future__ import absolute_import, print_function
import argparse
import server

def main():
    parser = argparse.ArgumentParser(description='Run the bycombat server.')
    parser.add_argument('--build', choices=['debug', 'release'], default='debug', required=False, help='build to run with server')
    parser.add_argument('--debug', action='store_const', const='debug', dest='build', help='run debug server using local cocos project')
    parser.add_argument('--release', action='store_const', const='release', dest='build', help='run release server using built cocos project')
    parser.add_argument('--port', type=int, dest='port', default=5000, help='run the server on a different port')

    args = parser.parse_args()
    debug = args.build == 'debug'
    port = args.port
    print('Running server in {} mode'.format(args.build))
    server.run(debug, port)

if __name__ == '__main__':
    main()
