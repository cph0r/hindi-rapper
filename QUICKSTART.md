# 🚀 Quick Start Guide - Hindi Rap Generator

Get your Hindi rap track in just 5 minutes!

## Step 1: Install Dependencies (2 minutes)

### On macOS/Linux:

```bash
# Install espeak-ng first
# macOS:
brew install espeak-ng

# Ubuntu/Debian:
sudo apt-get install espeak-ng

# Create Python environment
conda create -n hindi-rap python=3.10
conda activate hindi-rap

# Install packages
pip install -r requirements.txt
```

### On Windows:

1. Download and install [espeak-ng](https://github.com/espeak-ng/espeak-ng/releases)
2. Set environment variables:
   - `PHONEMIZER_ESPEAK_LIBRARY` → `C:\Program Files\eSpeak NG\libespeak-ng.dll`
   - `PHONEMIZER_ESPEAK_PATH` → `C:\Program Files\eSpeak NG`
3. Reboot your PC

```batch
conda create -n hindi-rap python=3.10
conda activate hindi-rap
pip install -r requirements.txt
```

## Step 2: Launch the UI (1 minute)

### Easy Way (Recommended):

**macOS/Linux:**
```bash
./launch_hindi_rap.sh
```

**Windows:**
```batch
launch_hindi_rap.bat
```

### Manual Way:

```bash
python hindi_rap_ui.py
```

For public sharing:
```bash
python hindi_rap_ui.py --share
```

## Step 3: Create Your First Rap (2 minutes)

1. **Open your browser** to http://localhost:7860

2. **Enter your lyrics** in LRC format:
   ```
   [00:00.00]यह है मेरा पहला रैप
   [00:03.00]बनाया AI की मदद से
   [00:06.00]संगीत का जादू है यहां
   [00:09.00]हिंदी रैप का नया सफर
   ```

3. **Choose a style**: Pick "🔥 Hard Trap Beat" (or any other)

4. **Set duration**: 60 seconds (for a quick test)

5. **Click "Generate Hindi Rap!"**

6. **Wait 1-3 minutes** and your rap will be ready!

7. **Download** and share! 🎉

## 📝 Writing LRC Lyrics

LRC format is simple:

```
[MM:SS.MS]Your lyrics here
```

### Example 1: Simple Rap

```lrc
[00:00.00]मैं हूं राजा इस गली का
[00:03.50]मेरा है दम रैप वाली बात का
[00:07.00]सुन मेरी आवाज़ को ध्यान से
[00:10.50]बजेगा ये गाना हर कान में
```

### Example 2: Fast Flow

```lrc
[00:00.00]तेज़ है मेरी रफ़्तार
[00:02.00]नहीं कोई इंतज़ार
[00:04.00]रैप है मेरा हथियार
[00:06.00]दिल से करूं प्यार
```

### Example 3: Hinglish Mix

```lrc
[00:00.00]I'm grinding every day और रात
[00:03.50]Making moves करूं बात की बात
[00:07.00]Dreams are big लक्ष्य है ऊंचा
[00:10.50]Success का सफर is real माचा
```

## 🎨 Style Guide

| Want to create... | Choose this style |
|------------------|------------------|
| Hard aggressive rap | 🔥 Hard Trap Beat |
| Chill storytelling | 💎 Chill Hip-Hop |
| Party track | 🌆 Desi Trap |
| Emotional song | 🎵 Melodic Rap |
| Street rap | ⚡ Drill Beat |
| Commercial hit | 🌟 Pop Rap |
| Classic hip-hop | 🎹 Old School Hip-Hop |
| Late night vibe | 🌙 Lo-Fi Rap |

## ⚡ Pro Tips

1. **First run takes longer** - Models need to download (3-5GB)
2. **GPU is faster** - CPU works but takes 3-4x longer
3. **Short lyrics work better** - Start with 30-60 second tracks
4. **Time your lyrics** - Match rap flow rhythm
5. **Experiment with styles** - Each gives a unique vibe
6. **Custom styles** - Be specific: "aggressive desi trap with dhol drums"

## 🐛 Troubleshooting

### "Models are loading..."
- First time? Models are downloading (wait 5 minutes)
- Check your internet connection

### "Out of memory"
- Reduce audio length
- Close other programs
- Use chunked mode (automatic in UI)

### "espeak-ng not found"
- Install espeak-ng (see Step 1)
- On Windows: Set environment variables and reboot

### Generation is very slow
- Use a GPU if available
- Reduce batch inference quality
- Try shorter audio lengths

## 🎯 Example Workflow

1. **Write lyrics** in a text editor
2. **Add timestamps** using this pattern:
   - First line: `[00:00.00]`
   - Add 3-4 seconds per line
   - Adjust based on your rap flow
3. **Copy-paste** into the UI
4. **Select style** matching your vibe
5. **Generate** and iterate!

## 📱 Next Steps

- Try different styles with same lyrics
- Experiment with custom style descriptions
- Mix Hindi and English (Hinglish)
- Create longer tracks (up to 130 seconds)
- Share your creations! 🎤

## 💡 Need Help?

- Read the full [README.md](Readme.md)
- Check the [examples](infer/example/)
- Open an issue on GitHub

---

**Happy Rap Creating! 🎵🔥**

