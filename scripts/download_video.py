import os
import subprocess
import yt_dlp as youtube_dl
import time
import glob
from datetime import datetime

VIDEO_TO_DOWNLOAD = """
https://www.youtube.com/watch?v=JBy1T5IykkU
"""

def get_video_info(file_path):
    """Get video information using ffprobe."""
    try:
        cmd = [
            'ffprobe', '-v', 'quiet', '-print_format', 'json', '-show_format', '-show_streams', file_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        import json
        data = json.loads(result.stdout)

        video_stream = next((s for s in data['streams'] if s['codec_type'] == 'video'), None)
        audio_stream = next((s for s in data['streams'] if s['codec_type'] == 'audio'), None)

        info = {
            'duration': float(data['format'].get('duration', 0)),
            'size_mb': round(float(data['format'].get('size', 0)) / (1024 * 1024), 2),
            'video_codec': video_stream.get('codec_name', 'unknown') if video_stream else 'none',
            'audio_codec': audio_stream.get('codec_name', 'unknown') if audio_stream else 'none',
            'resolution': f"{video_stream.get('width', 0)}x{video_stream.get('height', 0)}" if video_stream else 'unknown',
            'fps': video_stream.get('r_frame_rate', 'unknown') if video_stream else 'unknown',
            'video_bitrate': video_stream.get('bit_rate', 'unknown') if video_stream else 'unknown',
            'audio_bitrate': audio_stream.get('bit_rate', 'unknown') if audio_stream else 'unknown',
            'format_name': data['format'].get('format_name', 'unknown'),
            'total_bitrate': round(float(data['format'].get('bit_rate', 0)) / 1000) if data['format'].get('bit_rate') else 0
        }
        return info
    except:
        return None

def validate_mp4_file(file_path):
    """Validate that the MP4 file is playable."""
    try:
        # Check if ffmpeg can read and process the file
        cmd = [
            'ffmpeg', '-v', 'quiet', '-i', file_path, '-t', '1', '-f', 'null', '-'
        ]
        result = subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def format_duration(seconds):
    """Format duration in a readable way."""
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        return f"{int(seconds//60)}m {int(seconds%60)}s"
    else:
        return f"{int(seconds//3600)}h {int((seconds%3600)//60)}m {int(seconds%60)}s"

def format_bitrate(bitrate_str):
    """Format bitrate for display."""
    if bitrate_str == 'unknown' or not bitrate_str:
        return 'unknown'
    try:
        bitrate = int(bitrate_str) // 1000
        return f"{bitrate} kbps"
    except:
        return str(bitrate_str)

def get_next_sample_number(directory):
    """
    Returns the next available sample number such that a file named sampleXX.mp4
    does not already exist in the directory.
    """
    num = 1
    while True:
        file_path = os.path.join(directory, f"sample{num:02d}.mp4")
        if not os.path.exists(file_path):
            return num
        num += 1

def cleanup_extra_files(base_path):
    """Remove all files except the final MP4."""
    base_name = os.path.splitext(base_path)[0]

    # Find all files that start with the base name
    pattern = base_name + "*"
    all_files = glob.glob(pattern)

    # Keep only the .mp4 file, remove everything else
    for file_path in all_files:
        if not file_path.endswith('.mp4'):
            try:
                os.remove(file_path)
                print(f"  Cleaned up: {os.path.basename(file_path)}")
            except Exception as e:
                print(f"  Could not remove {os.path.basename(file_path)}: {e}")

def re_encode_for_compatibility(input_file, output_file):
    """Re-encode video to ensure maximum compatibility."""
    try:
        print("Re-encoding for maximum compatibility...")
        cmd = [
            'ffmpeg', '-i', input_file,
            '-c:v', 'libx264',  # Force H.264
            '-profile:v', 'high',  # High profile for better compression
            '-level:v', '4.0',  # Level 4.0 for wide compatibility
            '-c:a', 'aac',  # Force AAC audio
            '-b:a', '128k',  # Standard audio bitrate
            '-movflags', '+faststart',  # Optimize for streaming/quick playback
            '-pix_fmt', 'yuv420p',  # Standard pixel format
            '-y',  # Overwrite output file
            output_file
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        # Remove original file if re-encoding succeeded
        if os.path.exists(output_file):
            os.remove(input_file)
            return True
        return False
    except Exception as e:
        print(f"  Re-encoding failed: {e}")
        return False

def download_video(video_url, output_path):
    """
    Downloads the video as universally compatible MP4 with validation and re-encoding if needed.
    """
    download_start = time.time()

    # Simple format selection - get the best available, we'll re-encode if needed
    ydl_opts = {
        'format': 'best[ext=mp4]/best',  # Simplified format selection
        'restrictfilenames': True,
        'no_warnings': False,
        'writesubtitles': False,
        'writeautomaticsub': False,
        'ignoreerrors': False,
        'outtmpl': output_path,
        'postprocessors': [],
        'keepvideo': False,
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading video...")
            info_dict = ydl.extract_info(video_url, download=True)
            download_time = time.time() - download_start

            # Find the actual downloaded file
            base_path = os.path.splitext(output_path)[0]

            # Look for downloaded file with various extensions
            possible_files = [
                base_path + '.mp4',
                base_path + '.webm',
                base_path + '.mkv',
                base_path + '.m4a'
            ]

            downloaded_file = None
            for file_path in possible_files:
                if os.path.exists(file_path):
                    downloaded_file = file_path
                    break

            if not downloaded_file:
                return False, "No downloaded file found"

            final_mp4 = base_path + '.mp4'

            # If it's not MP4, needs conversion. If it's MP4 but has compatibility issues, re-encode
            if downloaded_file != final_mp4:
                print(f"Converting {os.path.splitext(downloaded_file)[1]} to MP4...")
                success = re_encode_for_compatibility(downloaded_file, final_mp4)
                if not success:
                    return False, "Conversion failed"
            elif not validate_mp4_file(downloaded_file):
                print("Video has compatibility issues, re-encoding...")
                # Create temp file for re-encoding
                temp_file = base_path + '_temp.mp4'
                os.rename(downloaded_file, temp_file)
                success = re_encode_for_compatibility(temp_file, final_mp4)
                if not success:
                    # Restore original if re-encoding fails
                    os.rename(temp_file, final_mp4)
                    print("Re-encoding failed, keeping original")
            else:
                print("Video passed compatibility check!")

            # Final validation
            if not validate_mp4_file(final_mp4):
                return False, "Final validation failed"

            # Clean up any extra files
            cleanup_extra_files(output_path)

            file_info = get_video_info(final_mp4)
            final_info = {
                'download_time': download_time,
                'file_path': final_mp4,
                'file_info': file_info,
                'metadata': info_dict
            }
            return True, final_info

    except Exception as e:
        return False, str(e)

def print_quality_summary(final_info):
    """Print a focused summary of the quality achieved."""
    print("\n" + "="*60)
    print("         UNIVERSALLY COMPATIBLE MP4 DOWNLOAD")
    print("="*60)

    metadata = final_info['metadata']
    file_info = final_info['file_info']

    # Basic info
    title = metadata.get('title', 'Unknown')
    print(f"Title: {title}")
    print(f"File: {os.path.basename(final_info['file_path'])}")

    # Quality metrics
    if file_info:
        print(f"\nVIDEO:")
        print(f"  Resolution: {file_info['resolution']}")
        print(f"  Codec:      {file_info['video_codec']}")
        print(f"  Bitrate:    {format_bitrate(file_info['video_bitrate'])}")
        print(f"  FPS:        {file_info['fps']}")

        print(f"\nAUDIO:")
        print(f"  Codec:      {file_info['audio_codec']}")
        print(f"  Bitrate:    {format_bitrate(file_info['audio_bitrate'])}")

        print(f"\nFILE:")
        print(f"  Size:       {file_info['size_mb']} MB")
        print(f"  Duration:   {format_duration(file_info['duration'])}")
        print(f"  Format:     MP4")

        # Quality assessment
        print(f"\nQUALITY:")
        width = int(file_info['resolution'].split('x')[0]) if 'x' in file_info['resolution'] else 0
        if width >= 3840:
            print(f"  * 4K+ Quality")
        elif width >= 1920:
            print(f"  * Full HD Quality")
        elif width >= 1280:
            print(f"  * HD Quality")

        # Compatibility indicators
        codec = file_info['video_codec'].lower()
        if 'h264' in codec or 'avc' in codec:
            print(f"  H.264 - Universal Compatibility")

        if 'aac' in file_info['audio_codec'].lower():
            print(f"  AAC Audio - Universal Compatibility")

    print(f"\nDownload Time: {format_duration(final_info['download_time'])}")
    print(f"\nCOMPATIBILITY: Validated for universal playback")
    print("="*60)

def main():
    video_url = VIDEO_TO_DOWNLOAD.strip()
    if not video_url or "video link here" in video_url:
        print("Please set a valid video URL in VIDEO_TO_DOWNLOAD")
        return

    output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "clues", "super_bowl_ad")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "ad_hires.%(ext)s")

    print(f"UNIVERSALLY COMPATIBLE MP4 DOWNLOAD")
    print(f"Target: {output_dir}/ad_hires.mp4")
    print(f"Started: {datetime.now().strftime('%H:%M:%S')}")
    print(f"Strategy: Download best quality + validate + re-encode if needed")

    success, result = download_video(video_url, output_path)

    if success:
        print_quality_summary(result)
        print(f"\nSUCCESS - Universally compatible MP4 ready!")
        print(f"Location: {result['file_path']}")
    else:
        print(f"\nDOWNLOAD FAILED: {result}")

if __name__ == "__main__":
    main()
