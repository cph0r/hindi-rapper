# Copyright (c) 2025 ASLP-LAB
# Modified for Hindi Rap Generation UI

import gradio as gr
import argparse
import os
import torch
import torchaudio
from einops import rearrange
import tempfile

from infer.infer_utils import (
    decode_audio,
    get_lrc_token,
    get_negative_style_prompt,
    get_reference_latent,
    get_style_prompt,
    prepare_model,
)

# Hindi Rap Style Presets
RAP_STYLE_PRESETS = {
    "🔥 Hard Trap Beat": "aggressive trap beat, heavy 808 bass, fast hi-hats, dark synths, energetic rap flow",
    "💎 Chill Hip-Hop": "chill hip-hop beat, smooth bass, jazz samples, laid-back rap flow, boom bap drums",
    "🌆 Desi Trap": "desi trap, tabla mixed with trap drums, indian instruments, modern bass, energetic rap",
    "🎵 Melodic Rap": "melodic rap, emotional piano, soft 808s, smooth flow, atmospheric pads",
    "⚡ Drill Beat": "drill beat, sliding 808s, dark piano, aggressive hi-hats, hard-hitting drums",
    "🌟 Pop Rap": "pop rap beat, catchy melody, upbeat drums, commercial sound, radio-friendly",
    "🎹 Old School Hip-Hop": "old school hip-hop, classic boom bap, vinyl scratches, funky bass, retro vibe",
    "🌙 Lo-Fi Rap": "lo-fi rap beat, dusty drums, warm bass, vinyl crackle, chill atmosphere",
}

# Global model variables
cfm_model = None
vae_model = None
tokenizer = None
muq_model = None
device = None

def initialize_models(max_frames=2048):
    """Initialize all models on startup"""
    global cfm_model, vae_model, tokenizer, muq_model, device
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"🎵 Loading models on {device}...")
    
    cfm_model, tokenizer, muq_model, vae_model = prepare_model(
        max_frames=max_frames,
        device=device
    )
    
    print("✅ Models loaded successfully!")
    return f"Models loaded on {device}"

def inference(
    cfm,
    vae,
    cond,
    text,
    duration,
    style_prompt,
    negative_style_prompt,
    start_time,
    pred_frames,
    batch_infer_num,
    song_duration,
    chunked=True,
):
    """Run inference to generate audio"""
    with torch.inference_mode():
        latents, _ = cfm.sample(
            cond=cond,
            text=text,
            duration=duration,
            style_prompt=style_prompt,
            max_duration=duration,
            song_duration=song_duration,
            negative_style_prompt=negative_style_prompt,
            steps=32,
            cfg_strength=4.0,
            start_time=start_time,
            latent_pred_segments=pred_frames,
            batch_infer_num=batch_infer_num
        )

        outputs = []
        for latent in latents:
            latent = latent.to(torch.float32)
            latent = latent.transpose(1, 2)

            output = decode_audio(latent, vae, chunked=chunked)

            output = rearrange(output, "b d n -> d (b n)")
            output = (
                output.to(torch.float32)
                .div(torch.max(torch.abs(output)))
                .clamp(-1, 1)
                .mul(32767)
                .to(torch.int16)
                .cpu()
            )
            outputs.append(output)

        return outputs

def generate_rap(lyrics, style_preset, custom_style, audio_length, use_custom_style, batch_infer_num=5):
    """
    Generate Hindi rap song
    
    Args:
        lyrics: LRC format lyrics
        style_preset: Preset style selection
        custom_style: Custom style description
        audio_length: Duration in seconds
        use_custom_style: Whether to use custom style
        batch_infer_num: Number of batch inferences
    """
    global cfm_model, vae_model, tokenizer, muq_model, device
    
    if cfm_model is None:
        return None, "❌ Please wait for models to load..."
    
    try:
        # Determine style prompt
        if use_custom_style and custom_style.strip():
            style_prompt = custom_style
        else:
            style_prompt = RAP_STYLE_PRESETS[style_preset]
        
        # Validate lyrics
        if not lyrics.strip():
            return None, "❌ Please enter lyrics in LRC format"
        
        # Calculate max frames
        max_frames = 2048 if audio_length <= 95 else 13000
        
        # Prepare inputs
        max_secs = audio_length
        
        # Get lyrics tokens
        lrc_emb, normalized_start_time, end_frame, normalized_duration = get_lrc_token(
            max_frames, lyrics, tokenizer, max_secs, device
        )
        
        # Get style embeddings
        style_emb = get_style_prompt(muq_model, prompt=style_prompt)
        negative_style_emb = get_negative_style_prompt(device)
        
        # Get reference latent (no editing)
        cond, pred_frames = get_reference_latent(
            device, max_frames, False, None, None, vae_model
        )
        
        # Generate audio
        outputs = inference(
            cfm_model,
            vae_model,
            cond,
            lrc_emb,
            normalized_duration,
            style_emb,
            negative_style_emb,
            normalized_start_time,
            pred_frames,
            batch_infer_num,
            max_secs,
            chunked=True,
        )
        
        # Save to temporary file
        output = outputs[0]
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        torchaudio.save(temp_file.name, output, 44100)
        
        return temp_file.name, f"✅ Successfully generated {audio_length}s Hindi rap!"
        
    except Exception as e:
        return None, f"❌ Error: {str(e)}"

# Create Gradio Interface
def create_ui():
    with gr.Blocks(
        title="Hinglish Rap Generator 🎤",
        theme=gr.themes.Soft(
            primary_hue="orange",
            secondary_hue="red",
        )
    ) as demo:
        
        gr.Markdown("""
        # 🎤 Hinglish Rap Generator (हिंग्लिश रैप जनरेटर)
        
        Generate Hinglish rap songs using AI! Mix Hindi + English for modern rap vibes 🔥
        
        ### How to use:
        1. **Enter your Hinglish lyrics** in LRC format (time-aligned)
        2. **Choose a rap style** preset or create your own
        3. **Set audio length** and hit Generate!
        4. **Download** your generated rap track
        
        ---
        """)
        
        with gr.Row():
            with gr.Column(scale=2):
                # Lyrics Input
                lyrics_input = gr.TextArea(
                    label="📝 Hinglish Lyrics (LRC Format)",
                    placeholder="""[00:00.00]Let's start करते हैं ये journey यार
[00:03.50]Hinglish में rap करूंगा main
[00:07.00]Music का जलवा है worldwide में
[00:10.50]This is my identity अब मेरी पहचान

Example format:
[MM:SS.MS]Your Hinglish lyrics here (mix Hindi + English)
""",
                    lines=10,
                    value="""[00:00.00]This is my rap song यार
[00:03.50]Hinglish में flow करूंगा main
[00:07.00]Music है मेरी जान
[00:10.50]Rap game का king हूं main""",
                )
                
                # Style Selection
                with gr.Row():
                    style_preset = gr.Dropdown(
                        label="🎵 Rap Style Preset",
                        choices=list(RAP_STYLE_PRESETS.keys()),
                        value=list(RAP_STYLE_PRESETS.keys())[0],
                    )
                
                use_custom_style = gr.Checkbox(
                    label="Use Custom Style Description",
                    value=False
                )
                
                custom_style = gr.TextArea(
                    label="✍️ Custom Style Description (Optional)",
                    placeholder="e.g., 'aggressive desi hip-hop with dhol drums, heavy bass, fast rap flow'",
                    lines=3,
                    visible=False,
                )
                
                use_custom_style.change(
                    lambda x: gr.update(visible=x),
                    inputs=[use_custom_style],
                    outputs=[custom_style]
                )
                
            with gr.Column(scale=1):
                # Parameters
                audio_length = gr.Slider(
                    label="⏱️ Audio Length (seconds)",
                    minimum=10,
                    maximum=130,
                    value=60,
                    step=5,
                )
                
                batch_infer_num = gr.Slider(
                    label="🎛️ Quality (Batch Inference)",
                    minimum=1,
                    maximum=10,
                    value=5,
                    step=1,
                    info="Higher = better quality but slower"
                )
                
                # Generate Button
                generate_btn = gr.Button(
                    "🎵 Generate Hindi Rap!",
                    variant="primary",
                    size="lg"
                )
                
                # Status
                status_output = gr.Textbox(
                    label="📊 Status",
                    interactive=False,
                )
        
        # Audio Output
        with gr.Row():
            audio_output = gr.Audio(
                label="🎧 Generated Rap Track",
                type="filepath",
            )
        
        # Examples
        gr.Markdown("""
        ### 📚 LRC Format Guide:
        ```
        [MM:SS.MS]Lyrics line here
        ```
        - **MM** = Minutes (e.g., 00, 01, 02)
        - **SS** = Seconds (e.g., 00-59)
        - **MS** = Milliseconds (e.g., 00-99)
        
        ### 💡 Tips:
        - Keep lyrics short and punchy for rap
        - Use appropriate timing for rap flow
        - Experiment with different style presets
        - Try mixing Hindi with English (Hinglish) for modern rap
        """)
        
        # Generate button action
        generate_btn.click(
            fn=generate_rap,
            inputs=[
                lyrics_input,
                style_preset,
                custom_style,
                audio_length,
                use_custom_style,
                batch_infer_num,
            ],
            outputs=[audio_output, status_output],
        )
        
        gr.Markdown("""
        ---
        ### ⚠️ Note:
        - First generation may take longer as models are loading
        - Supported languages: Hindi, English, Chinese, French, Korean, German
        - For best results, use clear, time-aligned lyrics
        
        **Made with ❤️ using DiffRhythm**
        """)
    
    return demo

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--share", action="store_true", help="Create public link")
    parser.add_argument("--port", type=int, default=7860, help="Port number")
    parser.add_argument("--max-frames", type=int, default=2048, help="Max frames for model")
    args = parser.parse_args()
    
    # Initialize models on startup
    print("🎵 Hinglish Rap Generator Starting...")
    print("📦 Loading AI models (this may take a minute)...")
    print("⏳ First-time setup will download ~3-5GB of models...")
    print("")
    
    # Load models before creating UI
    status = initialize_models(args.max_frames)
    print(status)
    print("")
    
    # Create UI
    demo = create_ui()
    
    # Launch
    print("🚀 Launching web interface...")
    demo.launch(
        share=args.share,
        server_port=args.port,
        server_name="0.0.0.0"
    )

