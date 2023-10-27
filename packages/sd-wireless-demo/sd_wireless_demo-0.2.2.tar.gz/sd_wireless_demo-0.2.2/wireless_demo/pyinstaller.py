import PyInstaller.__main__
from pathlib import Path

this_dir = Path(__file__).parent.absolute()
path_to_main = str(this_dir / "main.py")

def make_exe():
    PyInstaller.__main__.run([
        path_to_main,
        '--onefile',
        '--clean',
        '--console',
        '--name', 'wireless_demo',
        '--add-data', f'{str(this_dir / "demo_ui.css")}:wireless_demo',
        '--paths', str(this_dir / ".."),
    ])
