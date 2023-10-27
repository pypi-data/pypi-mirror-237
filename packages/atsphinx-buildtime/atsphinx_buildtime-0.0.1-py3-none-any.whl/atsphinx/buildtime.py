from datetime import datetime

__version__ = "0.0.1"

times = {}


def log_config_inited(app, config):
    global times
    times["config-inited"] = datetime.now()


def log_build_finished(app, exc=None):
    global times
    times["build-finished"] = datetime.now()


def report_times(app, exc=None):
    global times
    delta = times["build-finished"] - times["config-inited"]
    print(f"Build time is {delta} secs")


def setup(app):
    app.connect("config-inited", log_config_inited, 1)
    app.connect("build-finished", log_build_finished, 1)
    app.connect("build-finished", report_times, 100000)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
