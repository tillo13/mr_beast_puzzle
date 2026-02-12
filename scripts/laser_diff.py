#!/usr/bin/env python3
"""Generate frame-difference images to track laser beam activation sequence.

Subtracts frame N-1 from frame N so only NEW beams (bright additions) are visible.
Also generates a composite showing beam count progression.
"""

import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageEnhance
import numpy as np

FRAMES_DIR = Path("clues/super_bowl_ad/frames_4k")
OUTPUT_DIR = Path("clues/super_bowl_ad/grids/scene_1_laser_hallway/laser_diffs")


def load_frame(n: int) -> Image.Image:
    path = FRAMES_DIR / f"frame_{n:04d}.jpg"
    if not path.exists():
        raise FileNotFoundError(f"Frame not found: {path}")
    return Image.open(path)


def frame_diff(a: Image.Image, b: Image.Image, boost: float = 3.0) -> Image.Image:
    """Return (b - a), clamped to 0, with brightness boost.
    Shows only pixels that got BRIGHTER (new beams appearing).
    """
    arr_a = np.array(a, dtype=np.int16)
    arr_b = np.array(b, dtype=np.int16)
    diff = arr_b - arr_a
    diff = np.clip(diff * boost, 0, 255).astype(np.uint8)
    return Image.fromarray(diff)


def red_channel_diff(a: Image.Image, b: Image.Image, boost: float = 5.0) -> Image.Image:
    """Diff on red channel only (lasers are red), boosted for visibility."""
    arr_a = np.array(a, dtype=np.int16)[:, :, 0]  # red channel
    arr_b = np.array(b, dtype=np.int16)[:, :, 0]
    diff = arr_b - arr_a
    diff = np.clip(diff * boost, 0, 255).astype(np.uint8)
    # Make output red-tinted
    out = np.zeros((*diff.shape, 3), dtype=np.uint8)
    out[:, :, 0] = diff
    out[:, :, 1] = diff // 4
    out[:, :, 2] = diff // 8
    return Image.fromarray(out)


def annotate(img: Image.Image, text: str) -> Image.Image:
    """Add text label to top-left of image."""
    draw = ImageDraw.Draw(img)
    draw.rectangle([(0, 0), (len(text) * 20 + 20, 40)], fill="black")
    draw.text((10, 5), text, fill="white")
    return img


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Key frame range: 97 (no lasers) through 135 (peak)
    start, end = 97, 135
    frames = list(range(start, end + 1))

    print(f"Processing frames {start}-{end} ({len(frames)} frames)")

    # Load all frames
    loaded = {}
    for n in frames:
        try:
            loaded[n] = load_frame(n)
            print(f"  Loaded frame {n}")
        except FileNotFoundError:
            print(f"  MISSING frame {n}")

    available = sorted(loaded.keys())
    print(f"\n{len(available)} frames available")

    # Generate diffs between consecutive available frames
    print("\nGenerating difference images...")
    for i in range(1, len(available)):
        prev_n = available[i - 1]
        curr_n = available[i]

        prev_img = loaded[prev_n]
        curr_img = loaded[curr_n]

        # Full color diff
        diff_color = frame_diff(prev_img, curr_img, boost=3.0)
        diff_color = annotate(diff_color, f"DIFF: f{prev_n:04d} -> f{curr_n:04d}")

        # Red channel diff (laser-specific)
        diff_red = red_channel_diff(prev_img, curr_img, boost=5.0)
        diff_red = annotate(diff_red, f"RED DIFF: f{prev_n:04d} -> f{curr_n:04d}")

        # Save both
        diff_color.save(OUTPUT_DIR / f"diff_{prev_n:04d}_{curr_n:04d}_color.jpg", quality=90)
        diff_red.save(OUTPUT_DIR / f"diff_{prev_n:04d}_{curr_n:04d}_red.jpg", quality=90)

        print(f"  diff {prev_n}->{curr_n}")

    # Generate cumulative overlay: show ALL beams added since frame 97
    print("\nGenerating cumulative beam maps...")
    base = loaded[available[0]]
    for n in available[1:]:
        cumul = red_channel_diff(base, loaded[n], boost=4.0)
        cumul = annotate(cumul, f"CUMULATIVE f{available[0]:04d}->f{n:04d}")
        cumul.save(OUTPUT_DIR / f"cumul_{n:04d}.jpg", quality=90)

    # Generate a contact sheet of key transition frames
    print("\nGenerating contact sheet...")
    key_frames = [97, 100, 102, 104, 105, 106, 107, 108, 110, 112, 115, 118, 120, 125, 130]
    key_available = [n for n in key_frames if n in loaded]

    if key_available:
        thumb_w, thumb_h = 640, 360
        cols = 5
        rows = (len(key_available) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * thumb_w, rows * thumb_h), "black")
        draw = ImageDraw.Draw(sheet)

        for idx, n in enumerate(key_available):
            col = idx % cols
            row = idx // cols
            thumb = loaded[n].resize((thumb_w, thumb_h), Image.LANCZOS)
            sheet.paste(thumb, (col * thumb_w, row * thumb_h))
            draw.rectangle(
                [(col * thumb_w, row * thumb_h), (col * thumb_w + 120, row * thumb_h + 25)],
                fill="black",
            )
            draw.text((col * thumb_w + 5, row * thumb_h + 3), f"F{n:04d}", fill="yellow")

        sheet.save(OUTPUT_DIR / "contact_sheet.jpg", quality=90)
        print(f"  Contact sheet: {len(key_available)} frames in {rows}x{cols} grid")

    print(f"\nDone! Output in {OUTPUT_DIR}")
    print(f"Total files: {len(list(OUTPUT_DIR.glob('*.jpg')))}")


if __name__ == "__main__":
    main()
