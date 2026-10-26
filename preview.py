#!/usr/bin/env python3
"""Build and serve the static sample on loopback only."""
import argparse
from functools import partial
import http.server
from pathlib import Path
import subprocess
import sys
import webbrowser

ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser(description='Build and preview Seven Tech Newsroom locally. No deployment.')
p.add_argument('--port',type=int,default=4173)
p.add_argument('--no-open',action='store_true')
args=p.parse_args()
class PreviewHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self,path):
        kind=super().guess_type(path)
        if str(path).endswith('.md'):return 'text/plain; charset=utf-8'
        if kind.startswith('text/') or kind in ['application/json','application/javascript','application/xml']:
            return kind+'; charset=utf-8'
        return kind
    def end_headers(self):
        self.send_header('Cache-Control','no-store')
        super().end_headers()
handler=partial(PreviewHandler,directory=str(ROOT/'dist'))
try: server=http.server.ThreadingHTTPServer(('127.0.0.1',args.port),handler)
except OSError as exc: raise SystemExit(f'Cannot listen on 127.0.0.1:{args.port}: {exc}. Choose another --port.')
origin=f'http://127.0.0.1:{server.server_address[1]}'
try:
    subprocess.run([sys.executable,str(ROOT/'scripts'/'build.py'),'--base-url',origin],check=True)
except BaseException:
    server.server_close();raise
print(f'LOCAL_PREVIEW_URL={origin}/',flush=True)
print('Serving static files on loopback only. Ctrl+C stops the preview.',flush=True)
if not args.no_open:webbrowser.open(origin+'/')
try:server.serve_forever()
except KeyboardInterrupt:pass
finally:server.server_close()
