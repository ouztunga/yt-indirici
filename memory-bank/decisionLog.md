# Decision Log: YT İndirici

## 2026-05-14: Forced Downgrade to Python 3.12
- **Decision**: Remove Python 3.14 (Alpha) and install Python 3.12.9.
- **Rationale**: Python 3.14 had no pre-built wheels for `pythonnet` and `pywin32`, causing `pywebview` to fail entirely. 3.12 is the current stable standard.

## 2026-05-14: Global Window Reference (Anti-Recursion)
- **Decision**: Move from `self.window` to a global `MAIN_WINDOW`.
- **Rationale**: Storing the window object inside the API class (which is passed to the window) created a circular reference. `pywebview`'s JSON serializer entered infinite recursion trying to serialize this loop.

## 2026-05-14: Forced Edge Chromium (WebView2)
- **Decision**: Set `gui='edgechromium'` and `os.environ['PYWEBVIEW_GUI'] = 'edgechromium'`.
- **Rationale**: Default WinForms renderer was triggering Windows 11 accessibility loops. Edge Chromium is natively stable on Windows 11.

## 2026-05-14: Naming Convention Standard
- **Decision**: All project artifacts and executables will be named `indirici` (lowercase).
- **Rationale**: User preference for consistency and simplicity.

## 2026-05-20: Postponed EXE packaging, Development via .bat
- **Decision**: Temporarily suspend PyInstaller/EXE builds during feature development. Run and test the app using `baslat.bat` (`indirici.py` + `index.html`) directly.
- **Rationale**: Accelerate development speed and feedback loop by skipping PyInstaller build overhead until final features are complete and stable.
