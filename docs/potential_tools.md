# Puzzle-Relevant Tools Reference

Tools from Andy's existing toolkit that are useful for this puzzle hunt.

---

## Vision & Image Analysis

### VisionAnalyzer (Replicate API)
Sends image + prompt to a vision LLM, gets structured text back.
```python
from replicate_utils import VisionAnalyzer
va = VisionAnalyzer()
result = va.analyze(image_url="https://...", prompt="List all text visible in this image.", temperature=0.2)
```
**Model:** `yorickvp/llava-13b` (~$0.02/call)
**Use for:** OCR on ad frames, reading puzzle images, identifying symbols

### JoyCaption (Local — LM Studio)
Free local vision model for detailed image descriptions.
```python
from lmstudio_utils import LMStudio
lm = LMStudio()
lm.start()
lm.load_model("joycaption")
caption = lm.vision("frame_042.png", "Describe every symbol, number, and text visible.")
lm.obliterate()
```
**Use for:** Batch frame analysis (64 ad frames, 82 rewatch frames) without API costs

### Qwen 2.5 Vision (Local — LM Studio)
General-purpose local LLM with vision. Better at structured output than JoyCaption.
```python
lm.load_model("qwen")
result = lm.vision("puzzle_image.png", "Extract the grid layout as a 9x9 matrix of letters.")
```
**Use for:** Structured extraction from puzzle images, grid parsing

---

## Audio Analysis

### AssemblyAI (Cloud API)
Transcription with speaker identification and timestamps.
```python
import assemblyai as aai
config = aai.TranscriptionConfig(speaker_labels=True, speech_model=aai.SpeechModel.best)
transcript = aai.Transcriber(config=config).transcribe("video_audio.mp3")
```
**Use for:** Transcribing teaser videos, detecting hidden spoken clues

### Audio Separation (Demucs)
Splits audio into vocals and background tracks.
```bash
pip install demucs
demucs input_audio.wav  # outputs to separated/htdemucs/*/vocals.wav
```
**Use for:** Isolating audio layers that might contain hidden messages

---

## Video Processing

### FFmpeg
Extract frames, analyze video metadata, isolate audio tracks.
```bash
# Extract all frames at 2fps
ffmpeg -i super_bowl_ad.mp4 -vf "fps=2" frames/%04d.png

# Extract audio only
ffmpeg -i video.mp4 -vn -acodec pcm_s16le audio.wav

# Get video metadata
ffprobe -v quiet -print_format json -show_format -show_streams video.mp4
```
**Use for:** Frame extraction from all videos, audio isolation for spectrogram analysis

---

## Steganography & Data Hiding

### Python tools for hidden data detection
```bash
pip install stegano pillow
```
```python
from stegano import lsb
# Check if image has LSB-encoded hidden message
secret = lsb.reveal("suspicious_image.png")

# Check EXIF metadata
from PIL import Image
img = Image.open("photo.jpg")
exif = img._getexif()  # GPS coords, comments, camera info
```
**Use for:** Checking MrBeast's Super Bowl photos, puzzle images from all 9 platforms

### zsteg (for PNG steganography)
```bash
gem install zsteg
zsteg puzzle_image.png  # checks all common hiding methods
```

---

## Quick Reference

| Need | Tool | Local/Cloud | Cost |
|------|------|-------------|------|
| OCR on video frames | VisionAnalyzer | Cloud | ~$0.02/frame |
| Batch frame analysis | JoyCaption | Local | Free |
| Grid extraction from images | Qwen Vision | Local | Free |
| Audio transcription | AssemblyAI | Cloud | ~$0.01/min |
| Frame extraction | FFmpeg | Local | Free |
| Audio separation | Demucs | Local | Free |
| Steganography check | stegano/zsteg | Local | Free |
| Image metadata | PIL/EXIF | Local | Free |
