# Troubleshooting Log: YT İndirici

## Issue: `create_window() got an unexpected keyword argument 'html'`
- **Root Cause**: An old version of `pywebview` (2.x) was installed via Python 3.14 compatibility fallback.
- **Resolution**: Upgraded to Python 3.12 and installed `pywebview 6.x`.

## Issue: `maximum recursion depth exceeded` (Windows 11 Accessibility)
- **Root Cause**: Edge/WebView2 renderer enters an infinite loop when accessibility tools are active.
- **Resolution**: Moved window reference to global scope and added `os.environ['WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS'] = '--disable-renderer-accessibility'` to prevent the loop.

## Issue: `create_window() got an unexpected keyword argument 'icon'`
- **Root Cause**: `pywebview` 3.x+ does not support an `icon` parameter in `create_window()`.
- **Resolution**: Removed the `icon` argument. Icons should be set via PyInstaller during build.

## Issue: EXE not starting after "clean rewrite"
- **Root Cause**: Indentation error and undefined variable `format_type` in the rewritten `_download_thread`.
- **Resolution**: Performed a final clean rewrite of `indirici.py`.

## Issue: Playlist items resetting UI / Controls disappearing
- **Root Cause**: `updateProgress` called `resetUI` when any single item reached 100%, even if more items remained in the playlist.
- **Resolution**: Updated `updateProgress` to track global playlist progress and only call `resetUI` when the entire playlist is finished.

## Issue: Playlist items cluttering download folder
- **Root Cause**: All items were downloaded directly into the selected path.
- **Resolution**: Added logic to detect playlists and create a subfolder with the playlist title.

## Issue: Stop (Durdur) button not working during download
- **Root Cause**: Raising generic `Exception` inside the progress hook is ignored by `yt-dlp` error handler. Also, stopping a playlist required aborting the loop.
- **Resolution**: Replaced `Exception` with `yt_dlp.utils.DownloadCancelled` in the progress hook. Added a `match_filter` parameter to `ydl_opts` to abort playlist fetching. Handled exceptions properly on the backend.
