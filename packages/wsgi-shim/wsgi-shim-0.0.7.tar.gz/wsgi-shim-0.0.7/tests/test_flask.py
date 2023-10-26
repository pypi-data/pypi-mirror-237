import re

from wsgi_shim.wsgi_shim import cli_backend

from tests.conftest import run_passenger_wsgi_py


def test_install_passenger_wsgi_py_normal_flask(
        tmp_path_world_readable,
        monkeypatch,
        passenger_block,
):
    site_dir_path = tmp_path_world_readable
    monkeypatch.setattr(
        'sys.argv',
        [
            'wsgi-shim',
            'install',
            str(site_dir_path),
        ],
    )
    cli_backend()
    log_file_path = site_dir_path / 'logfile'
    passenger_app_root_path = site_dir_path / 'www-approot'
    config_toml_path = passenger_app_root_path / 'config.toml'
    config_toml_path.write_text(f"""
    [passenger]
    {passenger_block}
    [wsgi]
    module = "tests.flask_example"
    app = "app"
    [environment]
    LOG_FILENAME = "{log_file_path}"
    """)
    restart_dir_path = passenger_app_root_path / 'tmp'
    maint_txt_path = restart_dir_path / 'maint.txt'
    maint_txt_path.unlink()
    monkeypatch.setenv('PWD', str(passenger_app_root_path))
    html, status, headers = run_passenger_wsgi_py(passenger_app_root_path)
    assert re.search(r'Hello, World', html)
    assert status == '200 OK'
    assert len(headers) == 2
    log = log_file_path.read_text()
    assert "INFO tests.flask_example MainThread : Request: /" in log
