"""
Hierarchical Grid System — Progressive quadrant-based image analysis.

Works with any image: Super Bowl ad frames (by number) or puzzle images (by path).
Generates quadrants on demand; only zooms where clues exist.

Usage:
  python3 frame_grid.py init                                  # Create scene dirs from scenes.json
  python3 frame_grid.py quad <frame_or_path> [--scene NAME]   # Overview + 4 quadrants
  python3 frame_grid.py zoom <frame_or_path> <Q>              # Sub-quadrants (Q1 → Q1_1..Q1_4)
  python3 frame_grid.py crop <frame_or_path> <name> <x1,y1,x2,y2> [--scale N]
  python3 frame_grid.py batch [--all | --scene NAME]          # Quadrants for key frames
  python3 frame_grid.py status                                # Show what's generated

Examples:
  python3 frame_grid.py quad 360                              # Ad frame 360
  python3 frame_grid.py quad puzzles/02_lifechange/puzzle.png # Any image
  python3 frame_grid.py zoom 360 Q1                           # Sub-quadrants of Q1
  python3 frame_grid.py zoom 360 Q1_2                         # Sub-sub-quadrants
  python3 frame_grid.py crop 360 braille_left 1050,180,1650,530 --scale 3
  python3 frame_grid.py batch --all                           # All 17 key frames
  python3 frame_grid.py batch --scene blast_door              # Just blast door frames

Citation format: f0360:Q1, f0360:Q1_2, f0360:crop_braille_left, p02:Q3

Output:
  grids/scene_4_blast_door/f0360/
    overview.jpg    Q1.jpg Q2.jpg Q3.jpg Q4.jpg    notes.md
    Q1_1.jpg ...    (on demand)
    crop_braille_left.jpg    (on demand)
"""
import sys
import os
import json
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRAMES_DIR = os.path.join(BASE_DIR, "clues", "super_bowl_ad", "frames_4k")
GRIDS_DIR = os.path.join(BASE_DIR, "clues", "super_bowl_ad", "grids")
SCENES_JSON = os.path.join(GRIDS_DIR, "scenes.json")

# Quadrant layout (Z-order: TL, TR, BL, BR)
Q_NAMES = {"Q1": "Top-Left", "Q2": "Top-Right", "Q3": "Bottom-Left", "Q4": "Bottom-Right"}


def get_font(size=48):
    for path in [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSMono.ttf",
        "/System/Library/Fonts/Menlo.ttc",
    ]:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()


def load_scenes():
    if not os.path.exists(SCENES_JSON):
        print(f"ERROR: {SCENES_JSON} not found. Run 'init' first.")
        return None
    with open(SCENES_JSON) as f:
        return json.load(f)["scenes"]


def find_scene_for_frame(scenes, frame_num):
    for scene_id, info in scenes.items():
        lo, hi = info["frame_range"]
        if lo <= frame_num <= hi:
            return scene_id
    return None


def resolve_input(frame_or_path):
    """Resolve input to (image_path, output_dir, label).

    Accepts:
      - Frame number (int or string of digits): looks up in frames_4k/
      - Image file path: uses grids/ subdir next to image
    """
    # Frame number?
    if frame_or_path.isdigit():
        frame_num = int(frame_or_path)
        img_path = os.path.join(FRAMES_DIR, f"frame_{frame_num:04d}.jpg")
        if not os.path.exists(img_path):
            print(f"ERROR: Frame not found: {img_path}")
            return None, None, None

        scenes = load_scenes()
        if scenes:
            scene_id = find_scene_for_frame(scenes, frame_num)
            if scene_id:
                out_dir = os.path.join(GRIDS_DIR, scene_id, f"f{frame_num:04d}")
                return img_path, out_dir, f"f{frame_num:04d}"

        # Fallback: flat directory
        out_dir = os.path.join(GRIDS_DIR, f"f{frame_num:04d}")
        return img_path, out_dir, f"f{frame_num:04d}"

    # Image path
    img_path = os.path.join(BASE_DIR, frame_or_path) if not os.path.isabs(frame_or_path) else frame_or_path
    if not os.path.exists(img_path):
        print(f"ERROR: Image not found: {img_path}")
        return None, None, None

    img_dir = os.path.dirname(img_path)
    img_name = os.path.splitext(os.path.basename(img_path))[0]
    out_dir = os.path.join(img_dir, "grids", img_name)
    return img_path, out_dir, img_name


def quadrant_box(w, h, q_path):
    """Compute crop box for a quadrant path like 'Q1', 'Q1_2', 'Q1_2_3'.

    Returns (x1, y1, x2, y2) in original image coordinates.
    """
    x1, y1, x2, y2 = 0, 0, w, h

    parts = q_path.upper().replace("Q", "").split("_")
    for part in parts:
        n = int(part)
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2
        if n == 1:    # TL
            x2, y2 = mx, my
        elif n == 2:  # TR
            x1, y2 = mx, my
        elif n == 3:  # BL
            x2, y1 = mx, my
        elif n == 4:  # BR
            x1, y1 = mx, my
        else:
            print(f"ERROR: Invalid quadrant number {n} in {q_path}")
            return None
    return x1, y1, x2, y2


def draw_overview(img, out_path):
    """Draw quadrant overlay on half-res image and save."""
    w, h = img.size
    overview = img.resize((w // 2, h // 2), Image.LANCZOS)
    draw = ImageDraw.Draw(overview)
    ow, oh = overview.size
    font = get_font(48)
    font_sm = get_font(32)

    # Draw cross
    draw.line([(ow // 2, 0), (ow // 2, oh)], fill=(255, 255, 0), width=4)
    draw.line([(0, oh // 2), (ow, oh // 2)], fill=(255, 255, 0), width=4)

    # Label quadrants
    labels = [("Q1", 12, 8), ("Q2", ow // 2 + 12, 8),
              ("Q3", 12, oh // 2 + 8), ("Q4", ow // 2 + 12, oh // 2 + 8)]
    for text, x, y in labels:
        draw.rectangle([x, y, x + 70, y + 48], fill=(0, 0, 0, 180))
        draw.text((x + 6, y + 4), text, fill=(255, 255, 0), font=font)

    overview.save(out_path, quality=90)


def write_notes_template(out_dir, label, frame_num=None):
    """Write notes.md template if it doesn't exist."""
    notes_path = os.path.join(out_dir, "notes.md")
    if os.path.exists(notes_path):
        return  # Don't clobber

    time_str = f" ({frame_num / 24.0:.1f}s)" if frame_num else ""
    scenes = load_scenes()
    scene_label = ""
    if frame_num and scenes:
        scene_id = find_scene_for_frame(scenes, frame_num)
        if scene_id:
            scene_label = f" -- {scenes[scene_id]['label']}"

    with open(notes_path, "w") as f:
        f.write(f"# {label}{time_str}{scene_label}\n\n")
        f.write("## Quadrant Observations\n\n")
        for q, desc in Q_NAMES.items():
            f.write(f"### {q} ({desc})\n- \n\n")
        f.write("## Zoom Areas\n\n\n")
        f.write("## Custom Crops\n\n\n")
        f.write("## Clues Found\n\n")


# ──────────────────────────────────────────────
# Commands
# ──────────────────────────────────────────────

def cmd_init():
    """Create scene directories from scenes.json."""
    scenes = load_scenes()
    if not scenes:
        return
    for scene_id in scenes:
        scene_dir = os.path.join(GRIDS_DIR, scene_id)
        os.makedirs(scene_dir, exist_ok=True)
        print(f"  {scene_id}/")
    print(f"\n{len(scenes)} scene directories created in {GRIDS_DIR}/")


def cmd_quad(frame_or_path, scene_override=None):
    """Generate overview + 4 quadrants for an image."""
    img_path, out_dir, label = resolve_input(frame_or_path)
    if not img_path:
        return

    os.makedirs(out_dir, exist_ok=True)
    img = Image.open(img_path)
    w, h = img.size

    # Overview
    overview_path = os.path.join(out_dir, "overview.jpg")
    draw_overview(img, overview_path)

    # 4 quadrants at native resolution
    for q_name in ["Q1", "Q2", "Q3", "Q4"]:
        box = quadrant_box(w, h, q_name)
        crop = img.crop(box)
        crop.save(os.path.join(out_dir, f"{q_name}.jpg"), quality=95)

    # Notes template
    frame_num = int(frame_or_path) if frame_or_path.isdigit() else None
    write_notes_template(out_dir, label, frame_num)

    print(f"  {label}: overview + Q1-Q4 → {out_dir}/")
    return out_dir


def cmd_zoom(frame_or_path, q_path):
    """Generate 4 sub-quadrants of the given quadrant."""
    img_path, out_dir, label = resolve_input(frame_or_path)
    if not img_path:
        return

    os.makedirs(out_dir, exist_ok=True)
    img = Image.open(img_path)
    w, h = img.size

    # Validate parent quadrant exists
    parent_box = quadrant_box(w, h, q_path)
    if not parent_box:
        return

    # Generate 4 children
    for sub in [1, 2, 3, 4]:
        child_path = f"{q_path}_{sub}"
        box = quadrant_box(w, h, child_path)
        if not box:
            continue
        crop = img.crop(box)
        crop.save(os.path.join(out_dir, f"{child_path}.jpg"), quality=95)

    print(f"  {label}: {q_path}_1..{q_path}_4 → {out_dir}/")


def cmd_crop(frame_or_path, name, coords_str, scale=1):
    """Create a named custom crop."""
    img_path, out_dir, label = resolve_input(frame_or_path)
    if not img_path:
        return

    os.makedirs(out_dir, exist_ok=True)
    img = Image.open(img_path)

    parts = [int(c.strip()) for c in coords_str.split(",")]
    if len(parts) != 4:
        print("ERROR: Coords must be x1,y1,x2,y2 (4 values)")
        return
    x1, y1, x2, y2 = parts

    crop = img.crop((x1, y1, x2, y2))
    if scale > 1:
        crop = crop.resize((crop.width * scale, crop.height * scale), Image.LANCZOS)

    out_path = os.path.join(out_dir, f"crop_{name}.jpg")
    crop.save(out_path, quality=95)
    size_str = f"{crop.width}x{crop.height}"
    scale_str = f" (scale {scale}x)" if scale > 1 else ""
    print(f"  {label}: crop_{name} [{x1},{y1},{x2},{y2}]{scale_str} {size_str} → {out_path}")


def cmd_batch(target="--all"):
    """Generate quadrants for key frames."""
    scenes = load_scenes()
    if not scenes:
        return

    if target == "--all":
        frames = []
        for info in scenes.values():
            frames.extend(info["key_frames"])
    elif target.startswith("--scene"):
        scene_name = target.split(None, 1)[1] if " " in target else ""
        # Match partial scene name
        matched = [sid for sid in scenes if scene_name.lower() in sid.lower()]
        if not matched:
            print(f"ERROR: No scene matching '{scene_name}'. Available: {list(scenes.keys())}")
            return
        frames = []
        for sid in matched:
            frames.extend(scenes[sid]["key_frames"])
            print(f"  Scene: {sid}")
    else:
        print(f"ERROR: Unknown target '{target}'. Use --all or --scene <name>")
        return

    print(f"\nProcessing {len(frames)} frames...\n")
    for f in sorted(frames):
        cmd_quad(str(f))
    print(f"\nDone! {len(frames)} frames processed.")


def cmd_status():
    """Show what's been generated."""
    scenes = load_scenes()
    if not scenes:
        return

    total_files = 0
    total_frames = 0

    for scene_id, info in scenes.items():
        scene_dir = os.path.join(GRIDS_DIR, scene_id)
        if not os.path.isdir(scene_dir):
            continue
        print(f"\n{info['label']} ({scene_id}):")
        for frame_num in info["key_frames"]:
            frame_dir = os.path.join(scene_dir, f"f{frame_num:04d}")
            if not os.path.isdir(frame_dir):
                print(f"  f{frame_num:04d}: (not generated)")
                continue
            files = os.listdir(frame_dir)
            jpgs = [f for f in files if f.endswith(".jpg")]
            quads = [f for f in jpgs if f.startswith("Q") and "_" not in f]
            subs = [f for f in jpgs if f.startswith("Q") and "_" in f]
            crops = [f for f in jpgs if f.startswith("crop_")]
            has_notes = "notes.md" in files

            parts = []
            if quads:
                parts.append(f"Q1-Q4")
            if subs:
                parts.append(f"{len(subs)} sub-quads")
            if crops:
                parts.append(f"{len(crops)} crops")
            if has_notes:
                parts.append("notes")

            print(f"  f{frame_num:04d}: {', '.join(parts)}")
            total_files += len(files)
            total_frames += 1

    print(f"\n{'─' * 40}")
    print(f"Total: {total_frames} frames, {total_files} files")


# ──────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == "init":
        cmd_init()

    elif cmd == "quad":
        if len(sys.argv) < 3:
            print("Usage: frame_grid.py quad <frame_or_path>")
            return
        scene = None
        if "--scene" in sys.argv:
            idx = sys.argv.index("--scene")
            scene = sys.argv[idx + 1]
        cmd_quad(sys.argv[2], scene)

    elif cmd == "zoom":
        if len(sys.argv) < 4:
            print("Usage: frame_grid.py zoom <frame_or_path> <Q1|Q1_2|...>")
            return
        cmd_zoom(sys.argv[2], sys.argv[3])

    elif cmd == "crop":
        if len(sys.argv) < 5:
            print("Usage: frame_grid.py crop <frame_or_path> <name> <x1,y1,x2,y2> [--scale N]")
            return
        scale = 1
        if "--scale" in sys.argv:
            idx = sys.argv.index("--scale")
            scale = int(sys.argv[idx + 1])
        cmd_crop(sys.argv[2], sys.argv[3], sys.argv[4], scale)

    elif cmd == "batch":
        if len(sys.argv) < 3:
            target = "--all"
        elif sys.argv[2] == "--all":
            target = "--all"
        elif sys.argv[2] == "--scene":
            if len(sys.argv) < 4:
                print("Usage: frame_grid.py batch --scene <name>")
                return
            target = f"--scene {sys.argv[3]}"
        else:
            target = sys.argv[2]
        cmd_batch(target)

    elif cmd == "status":
        cmd_status()

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)


if __name__ == "__main__":
    main()
