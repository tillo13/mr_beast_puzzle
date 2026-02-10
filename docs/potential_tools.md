# Andy's Reusable Tools & Code Reference

A catalog of tools, utilities, and patterns I've already built that can be repurposed across projects — especially for test harnesses, QA pipelines, and automated validation.

---

## 1. Vision & Image Analysis

### VisionAnalyzer (Replicate API — Cloud)

**What it does:** Sends any image + any prompt to a vision LLM, gets structured text back. Used for image QA, captioning, content verification.

**Where I built it:** `replicate_utils.py` in Kumori/Pilgrims projects

**Key code:**
```python
from replicate_utils import VisionAnalyzer

va = VisionAnalyzer()  # uses GCP Secret Manager for API key
result = va.analyze(
    image_url="https://...",
    prompt="Does this image contain a full-body character? Answer yes or no.",
    temperature=0.2
)
```

**Model:** `yorickvp/llava-13b` on Replicate ($0.01-0.03/call)

**Test/QA uses:**
- Verify AI-generated images match specs ("is the character orange?", "is background a park?")
- Batch QA on generated assets — flag images that don't meet criteria
- Compare before/after edits ("did the character's appearance change?")
- Validate screenshots of deployed apps match expected layout

**Past projects:** Kumori chat, Pilgrims character creation, Taco & Red episode QA

---

### JoyCaption (Local — LM Studio)

**What it does:** Local vision model that describes images in detail. Free, runs on GPU, no API costs.

**Where I built it:** `lmstudio_utils.py` on ASUS ROG (5060 Ti) and 3060 box

**Key code:**
```python
from lmstudio_utils import LMStudio

lm = LMStudio()
lm.start()
lm.load_model("joycaption")
caption = lm.vision("path/to/image.png", "Describe this scene in detail.")
lm.obliterate()  # free VRAM when done
```

**Model:** `llama-joycaption-beta-one-hf-llava` (Q4_K GGUF, fits in 16GB VRAM)

**Test/QA uses:**
- Automated image quality checks in episode pipeline ("does this show full body?")
- Generate captions for metadata/searchability
- Verify character consistency across generated frames
- Scene continuity checking (feed last frame, compare to expected)

**Past projects:** Episode Maker pipeline (quality gate between scene generation and video render), Flux Kontext iterative editing

---

### Qwen 2.5 Vision (Local — LM Studio)

**What it does:** General-purpose local LLM with vision capabilities. Reads images, answers questions, generates structured output.

**Where I built it:** `lmstudio_utils.py`

**Key code:**
```python
lm = LMStudio()
lm.start()
lm.load_model("qwen")
response = lm.chat("Break this screenplay into 5 scenes with character assignments...")
# or with images:
result = lm.vision("screenshot.png", "List all UI elements visible in this screenshot")
lm.obliterate()
```

**Model:** `Qwen2.5-7B-Instruct.Q4_K_S.gguf`

**Test/QA uses:**
- Parse screenshots of deployed web apps and verify expected content
- Generate test data from descriptions
- Analyze error screenshots automatically
- Convert visual information into structured JSON for comparison

**Past projects:** Episode Maker (screenplay parsing), ComfyUI prompt generation

---

## 2. Audio & Speech Processing

### AssemblyAI (Cloud API — Speaker Diarization)

**What it does:** Transcribes audio with speaker identification, timestamps, confidence scores. Detects who said what and when.

**Where I built it:** `assembly_ai_utils.py` in Digital Empire projects

**Key code:**
```python
import assemblyai as aai

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")
config = aai.TranscriptionConfig(
    speaker_labels=True,
    speakers_expected=2,
    word_boost=["sonic", "shadow"],
    speech_model=aai.SpeechModel.best
)
transcript = aai.Transcriber(config=config).transcribe("audio.mp3")

for utterance in transcript.utterances:
    print(f"Speaker {utterance.speaker}: {utterance.text}")
    print(f"  Start: {utterance.start}ms, End: {utterance.end}ms")
```

**Test/QA uses:**
- Verify TTS output matches expected script (text comparison)
- Validate speaker count in generated dialogue videos
- Check timing accuracy of lip-sync (compare utterance timestamps to video frames)
- Audio QA gate: "does the generated audio contain all expected lines?"

**Past projects:** Digital Empire (dexter_playz, fast_friends, sonic_shadow, red_ninja), speaker detection pipeline

---

### Seed-VC (Local — Voice Conversion)

**What it does:** Converts one voice to another while preserving speech content. Takes audio in voice A, outputs audio in voice B.

**Where I built it:** `D:\apps\seed-vc-gpu\seed-vc\` on ASUS ROG, with `voice_server.py` API wrapper

**Key code:**
```python
import requests

# Voice server running on ASUS ROG at 10.0.0.100:8000
response = requests.post("http://10.0.0.100:8000/convert", files={
    "source": open("input.wav", "rb"),
    "target": open("voices/redninja.wav", "rb")
}, data={
    "diffusion_steps": 50,
    "inference_cfg": 0.85
})

with open("converted.wav", "wb") as f:
    f.write(response.content)
```

**Optimal settings:** 50 diffusion steps, CFG 0.85, auto F0 adjust True, FP16 True

**Test/QA uses:**
- Verify converted voice matches target (compare spectrograms)
- Batch test all character voices for consistency
- A/B quality testing across different parameter settings
- Pipeline integration test: TTS → Seed-VC → verify output exists and isn't silent

**Past projects:** Digital Empire voice pipeline (all projects), Taco & Red episode maker

---

### Audio Separation (Demucs / audio-separator)

**What it does:** Splits audio into vocals and background/instrumental tracks.

**Key code:**
```bash
# Using audio-separator
pip install audio-separator[gpu]
audio-separator input_video.mp4 --model_filename UVR-MDX-NET-Voc_FT.onnx

# Using demucs
pip install demucs
demucs input_audio.wav
# outputs to separated/htdemucs/input_audio/vocals.wav
```

**Test/QA uses:**
- Pre-process noisy audio before transcription (cleaner AssemblyAI results)
- Verify vocal isolation quality before voice conversion
- QA gate: "does the separated vocal track contain intelligible speech?"

**Past projects:** LTX-2 video voice fix pipeline (extract vocals → Seed-VC → remix)

---

## 3. Image Generation & Editing

### Flux Kontext Pro (Cloud — Replicate API)

**What it does:** Text-based image editing that preserves character identity. Send image + instruction, get edited image back.

**Where I built it:** `flux_utils.py` in Kumori app

**Key code:**
```python
import replicate

output = replicate.run("black-forest-labs/flux-kontext-pro", input={
    "prompt": "Place this character in a park setting with trees",
    "input_image": "https://url-to-source-image.png",
    "aspect_ratio": "match_input_image"
})
```

**Cost:** $0.04/image

**Test/QA uses:**
- Automated character consistency checks (generate variant, compare to original)
- Test prompt adherence across different instructions
- Batch generate scene variations for A/B visual testing

**Past projects:** Kumori app, Taco & Red episode maker, Ricky Roo memorial

---

### Flux Kontext Dev (Local — ComfyUI)

**What it does:** Same as Kontext Pro but runs locally. Free, unlimited, but slower.

**Where I built it:** ComfyUI workflow JSONs on ASUS ROG

**Key code:**
```python
import requests, json

workflow = json.load(open("flux_kontext_workflow.json"))
# Modify nodes for source image and prompt
workflow["6"]["inputs"]["text"] = "New scene description..."

response = requests.post("http://127.0.0.1:8188/prompt", json={"prompt": workflow})
```

**Models:** `flux1-dev-kontext_fp8_scaled.safetensors` (FP8, fits 16GB VRAM)

**Test/QA uses:**
- Free batch testing of prompts before spending on Replicate
- Parameter sweep testing (different seeds, CFG values)
- Overnight batch generation with automated QA

**Past projects:** ComfyUI stress tests, ceiling tests, episode maker

---

### Qwen Image Edit (Local — ComfyUI)

**What it does:** Precise object-level image editing. Better than Flux for targeted changes, text rendering, and object manipulation.

**Where I built it:** ComfyUI workflows on ASUS ROG

**Models:** `qwen_image_edit_2509_fp8_e4m3fn.safetensors` + Lightning LoRA (4-step)

**Test/QA uses:**
- Fix specific visual defects in generated images
- Add/remove objects for testing variations
- Text overlay testing (Qwen handles text better than Flux)

**Past projects:** Character editing, multi-angle generation

---

### Flux Fill OneReward (Local — ComfyUI)

**What it does:** Mask-based outpainting/inpainting. Extends images beyond their borders or fills in masked regions.

**Where I built it:** ComfyUI workflow with Swirl+Pyramid extension pattern

**Test/QA uses:**
- Extend images to different aspect ratios for testing responsive layouts
- Fill in missing regions for composite testing
- Outpaint character scenes to test different framing

**Past projects:** Episode maker (scene framing), character sheet generation

---

## 4. Video Processing

### FFmpeg (Direct CLI + Python wrapper)

**What it does:** Everything video — trim, concatenate, overlay, scale, encode, extract frames, remix audio.

**Key patterns I use:**

```python
import subprocess

# Extract frames at exact timestamps
subprocess.run([
    "ffmpeg", "-i", "input.mp4",
    "-ss", "00:11:00", "-to", "00:11:05",
    "-vf", f"fps={fps}",
    "frames/%05d.png"
])

# Concatenate videos (same codec)
with open("list.txt", "w") as f:
    for v in videos:
        f.write(f"file '{v}'\n")
subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "list.txt", "-c", "copy", "output.mp4"])

# Get frame count/duration
result = subprocess.run(
    ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", "input.mp4"],
    capture_output=True, text=True
)
info = json.loads(result.stdout)
duration = float(info["format"]["duration"])
fps = eval(info["streams"][0]["r_frame_rate"])  # e.g., "30000/1001"
total_frames = int(duration * fps)
```

**Test/QA uses:**
- Verify output video duration matches expected
- Check frame count (fps × duration)
- Validate resolution after processing
- Compare file sizes (detect corrupted outputs)
- Extract specific frames for visual QA with vision models

**Past projects:** Every video project (Digital Empire, episode maker, stress tests, face swapping)

---

### WAN 2.2 / InfiniteTalk (Local — ComfyUI)

**What it does:** Image-to-video generation with lip sync. Takes a still image and animates it.

**Where I built it:** ComfyUI on ASUS ROG with optimized 5060 Ti settings

**Optimized settings:**
- CFG 3.0 HIGH / 1.0 LOW
- `--lowvram --use-sage-attention --disable-xformers`
- Duration presets: "Quick take (~7s)" through "Epic dialogue (~40s)"
- FP8 model for VRAM efficiency

**Test/QA uses:**
- Verify generated video isn't corrupted (check frame count vs expected)
- Check that lip sync timing matches audio (compare with AssemblyAI timestamps)
- Quality gate: run JoyCaption on first/last frame to verify character consistency

**Past projects:** Taco & Red episodes, self-realization loop, stress tests

---

## 5. File & Data Management

### MD5 Golden Catalog (SQLite + Parallel Hashing)

**What it does:** Catalogs files by MD5 hash, detects duplicates across drives, tracks metadata.

**Where I built it:** `C:\local\md5_cataloging\` on ASUS ROG

**Key scripts:**
- `1_setup_golden_directory.py` — Scan golden directory, build SQLite DB (16 parallel threads)
- `check_if_golden.py` — Scan other folders, find duplicates against golden DB
- `check_if_golden_PARALLEL.py` — 16-thread version (50-150 files/sec vs 3-4/sec)

**Stats from last run:** 269,357 files scanned, 72,437 duplicates found, 671.93 GB savings

**Test/QA uses:**
- Verify no duplicate files crept into project directories
- Validate backup integrity (compare MD5s between source and backup)
- Pre-deploy check: ensure no large media files accidentally included
- Asset pipeline QA: verify all expected output files are unique

**Past projects:** Golden catalog system, F: drive cleanup, image deduplication

---

### Image Deduplication & Anonymization

**What it does:** Scans a directory, removes duplicate files by MD5, renames survivors to clean sequential names.

**Where I built it:** `dedupe_and_anonymize.py`

**Key code:**
```bash
# See what it would do
python dedupe_and_anonymize.py --dry-run --dir "Q:\comfy\ComfyUI\input"

# Actually run it
python dedupe_and_anonymize.py

# Just one step
python dedupe_and_anonymize.py --dedupe-only
python dedupe_and_anonymize.py --rename-only
```

**Test/QA uses:**
- Clean up ComfyUI input folders before batch runs
- Prepare test image sets (no duplicates, clean names)
- Post-generation cleanup (remove identical outputs from different seeds)

**Past projects:** ComfyUI input folder maintenance

---

## 6. Image Comparison & Mosaics

### FaceFusion Mosaic Comparison

**What it does:** Creates side-by-side comparison images from multiple test runs. Generates per-input-image comparison grids with labels.

**Where I built it:** `create_mosaic.py` in FaceFusion testing

**Test/QA uses:**
- Visual A/B testing of any image pipeline (different settings side by side)
- Before/after comparison grids
- Parameter sweep visualization (CFG 2.0 vs 2.5 vs 3.0 in one image)
- Character consistency comparison across multiple generations

**Past projects:** FaceFusion occlusion testing (234 test combinations)

---

## 7. Deployment & Infrastructure

### GCP Deploy Pattern

**What it does:** Standardized deployment to Google App Engine with version management and log tailing.

**Where I built it:** Every Flask project — `gcloud_deploy.py` + `git_push.sh` pattern

**Key code:**
```python
# gcloud_deploy.py pattern (used across all projects)
PROJECT_NAME = "your-project-id"
subprocess.run([
    "gcloud", "app", "deploy", "app.yaml",
    "--project", PROJECT_NAME, "--quiet"
])
```

**Projects using this pattern:**
- Kumori (`kumori-404602`)
- Pilgrims (`galactica-character-game`)
- Wattson (`wattson-gym-monitor`)
- Stealth (`stealth-connections`)
- Digital Empire
- Dandy (`dandy-chat`)

**Test/QA uses:** The `test_deploy_gate.sh` from the test methodology doc validates all of these pre-deploy

---

### LMStudio Lifecycle Management

**What it does:** Programmatically start, stop, load models, and free VRAM for LM Studio.

**Where I built it:** `lmstudio_utils.py`

**Key code:**
```python
from lmstudio_utils import LMStudio

lm = LMStudio()
lm.start()           # Open app, start server, wait for ready
lm.load_model("qwen")  # Load specific model
lm.chat("prompt")     # Text interaction
lm.vision("img.png", "describe")  # Vision interaction
lm.unload_model()    # Free VRAM, keep app open
lm.obliterate()      # Kill everything, full VRAM recovery
```

**Test/QA uses:**
- Automated test pipelines that need LLM calls between GPU-heavy tasks
- Context manager pattern ensures cleanup even on crash
- Health checks: `lm.is_running()`, `lm.is_server_ready()`

---

### ComfyUI API Interaction

**What it does:** Submit workflows, monitor progress, retrieve outputs from ComfyUI programmatically.

**Where I built it:** `comfy_utils.py` in episode maker + stress test scripts

**Key code:**
```python
import requests, json

# Submit workflow
workflow = json.load(open("workflow.json"))
resp = requests.post("http://127.0.0.1:8188/prompt", json={"prompt": workflow})
prompt_id = resp.json()["prompt_id"]

# Poll for completion
while True:
    history = requests.get(f"http://127.0.0.1:8188/history/{prompt_id}").json()
    if prompt_id in history:
        break
    time.sleep(2)

# Get output file
outputs = history[prompt_id]["outputs"]
```

**Test/QA uses:**
- Automated workflow testing (submit → wait → verify output)
- Parameter sweep automation
- Health check: verify ComfyUI is running before test suite starts
- Output validation: check file exists, isn't zero bytes, has expected dimensions

---

## 8. Process & System Management

### Mac Cleaner Scripts

**What it does:** Kills non-essential processes to free resources. Two variants — nuclear (aggressive) and smart (CPU-aware).

**Where I built it:** `nuclear_cleaner.py`, `smart_mac_cleaner.py`

**Test/QA uses:**
- Pre-test cleanup: ensure clean resource state before benchmarks
- Post-test: free resources for other work

---

### WiFi Watchdog

**What it does:** Monitors connectivity, resets adapter on failure, logs to CSV.

**Where I built it:** `C:\local\wifi_watchdog\wifi_watchdog.ps1`

**Test/QA uses:**
- Validate network stability during long-running API test suites
- Log connectivity issues that might explain flaky test results

---

## Quick Reference: Which Tool for Which QA Task

| QA Need | Tool | Cloud/Local | Cost |
|---------|------|-------------|------|
| "Does this image look right?" | VisionAnalyzer (Replicate) | Cloud | ~$0.02/check |
| "Does this image look right?" (free) | JoyCaption (LM Studio) | Local | Free |
| "Is the audio correct?" | AssemblyAI | Cloud | ~$0.01/min |
| "Does the video play?" | FFprobe | Local | Free |
| "Are there duplicate files?" | MD5 Golden Catalog | Local | Free |
| "Did deployment succeed?" | gcloud_deploy + smoke test | Cloud | Free |
| "Is ComfyUI healthy?" | comfy_utils health check | Local | Free |
| "Do all character images match?" | Mosaic comparison + JoyCaption | Local | Free |
| "Does the voice sound right?" | Seed-VC + spectrogram compare | Local | Free |
| "Is the LLM responding?" | lmstudio_utils status check | Local | Free |

---

## Integration Pattern: Chaining Tools for Automated QA

The most powerful use is chaining these together in a test gate:

```python
# Example: Episode Maker QA Gate
def qa_gate_episode_scene(scene_image_path, expected_character, expected_setting):
    """Gate between scene generation and video rendering"""
    
    lm = LMStudio()
    lm.start()
    lm.load_model("joycaption")
    
    # 1. Caption the generated image
    caption = lm.vision(scene_image_path, 
        "Describe the main character and setting in this image. "
        "Include: character color, clothing, number of fingers, background setting.")
    
    # 2. Check character identity
    char_check = lm.vision(scene_image_path,
        f"Is the main character {expected_character}? Answer only YES or NO.")
    
    # 3. Check setting
    setting_check = lm.vision(scene_image_path,
        f"Is this scene set in a {expected_setting}? Answer only YES or NO.")
    
    lm.obliterate()
    
    # 4. Gate decision
    passed = "YES" in char_check.upper() and "YES" in setting_check.upper()
    
    return {
        "passed": passed,
        "caption": caption,
        "character_match": "YES" in char_check.upper(),
        "setting_match": "YES" in setting_check.upper()
    }
```

---

*Last updated: February 2026*
