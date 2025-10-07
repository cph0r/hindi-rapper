# 🎤 Hindi Rap Generator (हिंदी रैप जनरेटर)

<p align="center">
   <h2>AI-Powered Hindi Rap Song Generator</h2>
   <h3>Create Professional Hindi Rap Tracks in Minutes! 🔥</h3>
</p>

---

## 🌟 What is Hindi Rap Generator?

**Hindi Rap Generator** is a specialized AI-powered tool for creating Hindi rap songs using cutting-edge **Latent Diffusion** technology. Built on top of the powerful **DiffRhythm** model, this tool makes it incredibly easy to generate professional-quality Hindi rap tracks with just your lyrics and a style preference.

### ✨ Key Features

- 🎵 **Generate Full Hindi Rap Songs** - Create complete rap tracks up to 2+ minutes
- 🎨 **Multiple Rap Styles** - Choose from Trap, Drill, Boom Bap, Lo-Fi, and more
- 🌐 **Multi-language Support** - Hindi, English, Hinglish, and more
- 🎛️ **Easy-to-Use Web Interface** - No coding required!
- ⚡ **Fast Generation** - Get your track in minutes
- 🎧 **Professional Quality** - Studio-grade audio output

### 🎯 Perfect For

- 🎤 Rappers and lyricists
- 🎬 Content creators
- 🎮 Game developers
- 📱 App developers
- 🎓 Music students and educators
- 🎪 Entertainment projects

---

## 🚀 Quick Start

### 🌐 Try it Online (Hugging Face Spaces)

Want to try it without installation? Deploy to Hugging Face Spaces for free!

👉 **[Deploy to Hugging Face Guide](HUGGINGFACE_DEPLOYMENT.md)**

Or try the live demo: *(coming soon)*

### 💻 Local Installation

#### Prerequisites

- Python 3.10+
- 8GB+ GPU VRAM (recommended) or CPU (slower)
- espeak-ng installed

### Installation

```bash 
# Clone the repository
git clone https://github.com/ASLP-lab/DiffRhythm.git
cd DiffRhythm

# Install espeak-ng
# For Debian/Ubuntu
sudo apt-get install espeak-ng

# For macOS
brew install espeak-ng

# For Windows
# Download from: https://github.com/espeak-ng/espeak-ng/releases

# Create Python environment
conda create -n hindi-rap python=3.10
conda activate hindi-rap

# OR use venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install gradio  # For the web UI
```

### 🎵 Launch the Web UI

```bash
python hindi_rap_ui.py
```

Then open your browser to **http://localhost:7860**

For public access (shareable link):
```bash
python hindi_rap_ui.py --share
```

---

## 📝 How to Use

### Step 1: Write Your Lyrics in LRC Format

LRC format is simple - just add timestamps before each line:

```
[00:00.00]This is my rap song यार
[00:03.50]Hinglish में flow करूंगा main
[00:07.00]Music है मेरी जान
[00:10.50]Rap game का king हूं main
```

**Format:** `[MM:SS.MS]Your lyrics here`
- **MM** = Minutes (00, 01, 02...)
- **SS** = Seconds (00-59)
- **MS** = Milliseconds (00-99)

### Step 2: Choose Your Style

Select from our preset rap styles:

- 🔥 **Hard Trap Beat** - Aggressive trap with heavy 808s
- 💎 **Chill Hip-Hop** - Smooth, laid-back boom bap
- 🌆 **Desi Trap** - Fusion of Indian instruments with trap
- 🎵 **Melodic Rap** - Emotional, melodic flow
- ⚡ **Drill Beat** - Dark, hard-hitting drill
- 🌟 **Pop Rap** - Commercial, radio-friendly sound
- 🎹 **Old School Hip-Hop** - Classic boom bap vibes
- 🌙 **Lo-Fi Rap** - Chill, atmospheric beats

Or create your own custom style description!

### Step 3: Generate!

1. Set your desired audio length (10-130 seconds)
2. Click "Generate Hindi Rap!"
3. Wait for the magic to happen ✨
4. Download your track!

---

## 💡 Tips for Best Results

### Writing Lyrics

- ✅ Keep lines short and punchy
- ✅ Time your lyrics to match rap flow
- ✅ Leave gaps for instrumental breaks
- ✅ Mix Hindi with English (Hinglish) for modern style
- ✅ Use repetition for hooks/choruses

### Choosing Styles

- For **aggressive rap**: Try Hard Trap or Drill
- For **storytelling**: Try Chill Hip-Hop or Melodic Rap
- For **party tracks**: Try Desi Trap or Pop Rap
- For **conscious rap**: Try Old School Hip-Hop
- For **experimental**: Create custom style descriptions

### Custom Style Descriptions

Be specific! Examples:

```
"aggressive desi hip-hop with dhol drums, heavy bass, fast rap flow"
"emotional melodic rap with sitar, soft 808s, introspective vibe"
"upbeat bollywood trap fusion, tabla, modern synths, energetic"
```

---

## 🎯 Advanced Usage

### Command Line Inference

For advanced users, you can use the original inference scripts:

```bash
# Using text prompt style
bash scripts/infer_prompt_ref.sh

# Using reference audio
bash scripts/infer_wav_ref.sh
```

Edit the scripts to customize:
- LRC file path
- Style prompt
- Audio length
- Output directory

### Docker Installation

```bash
cd docker
docker-compose up -d
docker exec -it DiffRhythm bash
cd /home/app/scripts
bash infer_prompt_ref.sh
```

---

## 🎨 Style Preset Details

| Style | Tempo | Vibe | Best For |
|-------|-------|------|----------|
| Hard Trap | Fast | Aggressive | Diss tracks, hard rap |
| Chill Hip-Hop | Medium | Laid-back | Storytelling, conscious rap |
| Desi Trap | Fast | Energetic | Party tracks, fusion |
| Melodic Rap | Medium | Emotional | Love songs, introspection |
| Drill | Medium-Fast | Dark | Street rap, hard lyrics |
| Pop Rap | Medium | Upbeat | Commercial, radio hits |
| Old School | Medium | Classic | Traditional hip-hop |
| Lo-Fi | Slow | Chill | Late night, relaxed vibe |

---

## 🛠️ Technical Details

### Model Architecture

- **Base Model**: DiffRhythm (Latent Diffusion Transformer)
- **VAE**: DiffRhythm-VAE for audio encoding/decoding
- **Style Encoder**: MuQ-MuLan for style embeddings
- **Language Support**: Multi-language G2P (Grapheme-to-Phoneme)

### System Requirements

**Minimum:**
- 8GB GPU VRAM (with `--chunked` mode)
- 16GB RAM
- 10GB disk space

**Recommended:**
- 16GB+ GPU VRAM
- 32GB RAM
- 20GB disk space

### Audio Specifications

- **Sample Rate**: 44100 Hz
- **Channels**: Stereo (2)
- **Format**: WAV/MP3
- **Quality**: 16-bit

---

## 📚 Examples

### Example 1: Motivational Rap

```lrc
[00:00.00]Wake up और चलो आगे बढ़ो
[00:03.50]Chase your dreams अपने goals को पकड़ो
[00:07.00]Every struggle को पार करो
[00:10.50]Success का wait करो never give up यारो
```

**Style**: Hard Trap Beat  
**Length**: 60 seconds

### Example 2: Love Rap

```lrc
[00:00.00]Lost in your memories तेरी यादों में
[00:04.00]Incomplete without you बिना तेरे अधूरा हूं main
[00:08.00]Heart की बातें कह रहा हूं
[00:12.00]Falling for you तुझसे pyaar करता हूं
```

**Style**: Melodic Rap  
**Length**: 90 seconds

### Example 3: Party Track

```lrc
[00:00.00]Party शुरू करो right now यार
[00:02.50]Dance करो साथ में all my people gather
[00:05.00]All night long चलेगा ये show
[00:07.50]Let's go crazy मजे करो यारों को
```

**Style**: Desi Trap  
**Length**: 60 seconds

---

## ❓ FAQ

**Q: Can I use other languages besides Hindi?**  
A: Yes! The model supports English, Chinese, French, Korean, and German. You can also mix languages (Hinglish).

**Q: How long does generation take?**  
A: Typically 1-3 minutes on a GPU, 5-10 minutes on CPU for a 60-second track.

**Q: Can I use generated tracks commercially?**  
A: Yes! The model is under Apache 2.0 license. However, ensure you review the license terms and use responsibly.

**Q: What if my lyrics don't have timestamps?**  
A: You need to add them manually in LRC format. There are online LRC editors that can help.

**Q: Can I upload my own beat/instrumental?**  
A: Currently, the model generates both vocals and instrumentals. Reference audio support may be added in future versions.

**Q: Why is my output quality low?**  
A: Try increasing the "Quality" slider or ensure your GPU has enough VRAM. Use `--chunked` mode for lower VRAM.

---

## 🤝 Contributing

We welcome contributions! Whether it's:

- 🐛 Bug reports
- 💡 Feature requests  
- 📝 Documentation improvements
- 🎨 New style presets
- 🌐 Language support

Feel free to open issues or pull requests!

---

## 📜 License & Credits

This project is based on **DiffRhythm** by ASLP-LAB and is released under the **Apache License 2.0**.

### Original DiffRhythm Credits

**Research Paper**: [DiffRhythm: Latent Diffusion for Full-Length Song Generation](https://arxiv.org/abs/2503.01183)

**Authors**: Ziqian Ning, Huakang Chen, Yuepeng Jiang, Chunbo Hao, Guobin Ma, Shuai Wang, Jixun Yao, Lei Xie†

**Organization**: ASLP Lab, Northwestern Polytechnical University

### Citation

If you use this tool in your research or project, please cite:

```bibtex
@article{ning2025diffrhythm,
  title={{DiffRhythm}: Blazingly Fast and Embarrassingly Simple End-to-End Full-Length Song Generation with Latent Diffusion},
  author={Ziqian, Ning and Huakang, Chen and Yuepeng, Jiang and Chunbo, Hao and Guobin, Ma and Shuai, Wang and Jixun, Yao and Lei, Xie},
  journal={arXiv preprint arXiv:2503.01183},
  year={2025}
}
```

---

## 🔗 Links

- 🏠 **Original DiffRhythm**: [GitHub](https://github.com/ASLP-lab/DiffRhythm)
- 📑 **Research Paper**: [arXiv](https://arxiv.org/abs/2503.01183)
- 🎵 **Demo**: [DiffRhythm Demo](https://aslp-lab.github.io/DiffRhythm.github.io/)
- 🤗 **Models**: [HuggingFace](https://huggingface.co/ASLP-lab)

---

## ⚠️ Disclaimer

This tool enables AI-generated music creation. Please use responsibly:

- ✅ Create original content
- ✅ Respect copyright and intellectual property
- ✅ Disclose AI-generated content when appropriate
- ❌ Don't use for harmful, illegal, or unethical purposes
- ❌ Don't plagiarize or copy existing artists' styles without permission

---

## 🎉 Get Started Now!

```bash
# Install and launch
conda create -n hindi-rap python=3.10
conda activate hindi-rap
pip install -r requirements.txt
pip install gradio
python hindi_rap_ui.py
```

**Create your first Hindi rap in minutes! 🎤🔥**

---

<p align="center">
    Made with ❤️ for the Hindi Hip-Hop Community
</p>

<p align="center">
    <a href="http://www.nwpu-aslp.org/">
        <img src="src/ASLP.jpg" width="300"/>
    </a>
</p>
