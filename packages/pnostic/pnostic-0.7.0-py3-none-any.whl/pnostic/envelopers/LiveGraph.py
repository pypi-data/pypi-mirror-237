import mystring, asyncio, threading

from pnostic.structure import Envelop, RepoResultObject, RepoObject, RepoSifting, Runner
from pnostic.utils import now

class app(Envelop):
    def __init__(self, ipaddress:str="127.0.0.1", port_to_use:int=5000):
        super().__init__()
        self.imports = [
            "pyvibe",
            "flask"
        ]
        self.flask_app = None
        self.flask_runner_thread = None
        self.host = ipaddress
        self.port = port_to_use

    def initialize(self)->bool:
        self.flask_runner_thread = threading.Thread(target=self.flask_runner, args=(), daemon = True)
        self.flask_runner_thread.start()
        return True

    def name(self) -> mystring.string:
        return mystring.string.of("LiveGraph")

    def flask_runner(self):
        from flask import Flask
        import pyvibe as pv
        self.flask_app = Flask(__name__)

        @self.flask_app.route("/")
        def index():
            page = pv.Page('Home')
            page.add_header('Hello World')
            return page.to_html()
        
        self.flask_app.run(host=self.host, port=self.port, debug=True,use_reloader=False)

    def clean(self) -> bool:
        return True

    def per_next_repo_obj(self,repo_object: RepoObject):
        return

    def per_repo_obj_scan(self,repo_object: RepoObject, runner:Runner):
        return

    def per_repo_obj_scan_result(self,repo_object: RepoResultObject, runner:Runner):
        return