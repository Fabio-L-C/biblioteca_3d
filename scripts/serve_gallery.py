"""Servidor local da galeria. Uso: py -3 scripts/serve_gallery.py"""
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import threading
import webbrowser

ROOT = Path(__file__).resolve().parents[1]

class GalleryHandler(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map,
                      ".glb": "model/gltf-binary", ".gltf": "model/gltf+json",
                      ".js": "text/javascript; charset=utf-8"}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_head(self):
        raw = unquote(urlsplit(self.path).path)
        parts = Path(raw.lstrip("/")).parts
        if any(p.startswith(".") or p == ".." for p in parts):
            self.send_error(404)
            return None
        target = (ROOT / raw.lstrip("/")).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            self.send_error(404)
            return None
        permitted_root = {"", "index.html", "catalog.json", "README.md"}
        allowed = (raw.lstrip("/") in permitted_root
                   or (parts and parts[0] in {"assets", "characters"}
                       and target.suffix.lower() in {".js", ".css", ".json", ".glb",
                           ".gltf", ".bin", ".png", ".jpg", ".jpeg", ".webp",
                           ".md", ".license"}))
        if not allowed:
            self.send_error(404)
            return None
        return super().send_head()

    def list_directory(self, path):
        self.send_error(404)
        return None

class GalleryServer(ThreadingHTTPServer):
    allow_reuse_address = False

def main():
    parser = argparse.ArgumentParser(description="Abrir a galeria Biblioteca 3D")
    parser.add_argument("--port", type=int, default=8088)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    try:
        server = GalleryServer(("127.0.0.1", args.port), GalleryHandler)
    except OSError as error:
        print(f"Nao foi possivel abrir a porta {args.port}: {error}")
        print("Tente --port 8089 ou feche a outra instancia da galeria.")
        return 1
    url = f"http://127.0.0.1:{server.server_port}/"
    print(f"Biblioteca 3D: {url}", flush=True)
    print("Pressione Ctrl+C para encerrar.", flush=True)
    if not args.no_browser:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
