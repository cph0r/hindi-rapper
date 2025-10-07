# 🚀 Deploying to Hugging Face Spaces

This guide will help you deploy your Hinglish Rap Generator to Hugging Face Spaces with automatic GitHub deployment.

## 📋 Prerequisites

- GitHub account
- Hugging Face account ([Sign up here](https://huggingface.co/join))
- Git repository set up (already done! ✅)

## 🎯 Step-by-Step Deployment

### Step 1: Create a Hugging Face Space

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Fill in the details:
   - **Space name**: `hinglish-rap-generator` (or your preferred name)
   - **License**: Apache 2.0
   - **SDK**: Gradio
   - **Hardware**: CPU Basic (free) or GPU (paid, faster)
   - **Visibility**: Public (recommended) or Private

4. Click "Create Space"

### Step 2: Get Your Hugging Face Token

1. Go to [Hugging Face Settings > Access Tokens](https://huggingface.co/settings/tokens)
2. Click "New token"
3. Give it a name: `github-actions-deploy`
4. Role: Select **Write** access
5. Click "Generate token"
6. **COPY the token** - you won't see it again!

### Step 3: Configure GitHub Secrets

1. Go to your GitHub repository: `https://github.com/cph0r/hindi-rapper`
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click "New repository secret"
4. Add two secrets:

   **Secret 1:**
   - Name: `HF_TOKEN`
   - Value: Your Hugging Face token (from Step 2)
   - Click "Add secret"

   **Secret 2:**
   - Name: `HF_SPACE_NAME`
   - Value: `YOUR_HF_USERNAME/hinglish-rap-generator`
     (Replace `YOUR_HF_USERNAME` with your actual Hugging Face username)
   - Click "Add secret"

### Step 4: Add README to Hugging Face Space

The Hugging Face Space needs a special README with metadata. We'll set this up:

1. In your Hugging Face Space, create a file named `README.md`
2. Copy the contents from `README_HF.md` in this repo
3. Make sure it includes the YAML frontmatter at the top:
   ```yaml
   ---
   title: Hinglish Rap Generator
   emoji: 🎤
   colorFrom: orange
   colorTo: red
   sdk: gradio
   sdk_version: 4.0.0
   app_file: app.py
   pinned: false
   license: apache-2.0
   ---
   ```

### Step 5: Initial Push to Hugging Face

Before the GitHub Actions workflow can sync, you need to do an initial push:

```bash
# Add Hugging Face remote
git remote add huggingface https://huggingface.co/spaces/YOUR_HF_USERNAME/hinglish-rap-generator

# Push to Hugging Face
git push huggingface main
```

When prompted for credentials:
- **Username**: Your Hugging Face username
- **Password**: Your Hugging Face token (from Step 2)

### Step 6: Enable GitHub Actions

1. Go to your GitHub repository
2. Click **Actions** tab
3. If disabled, click "I understand my workflows, go ahead and enable them"
4. You should see the workflow: "Deploy to Hugging Face Spaces"

### Step 7: Trigger Deployment

The deployment will happen automatically on every push to `main` branch.

To trigger it manually:
1. Go to **Actions** tab
2. Click "Deploy to Hugging Face Spaces" workflow
3. Click "Run workflow"
4. Select branch: `main`
5. Click "Run workflow"

---

## ✅ Verify Deployment

1. Go to your Hugging Face Space: `https://huggingface.co/spaces/YOUR_HF_USERNAME/hinglish-rap-generator`
2. Wait for the build to complete (check the "Building" status)
3. Once ready, your app will be live! 🎉

---

## 🔧 Configuration Files

The following files are used for Hugging Face deployment:

### `app.py`
Entry point for Hugging Face Spaces. This file is automatically run when the Space starts.

### `requirements.txt`
All Python dependencies needed for the app.

### `README_HF.md`
Special README for Hugging Face Spaces with metadata.

### `.github/workflows/deploy-to-huggingface.yml`
GitHub Actions workflow that auto-deploys on push.

---

## 🎛️ Hardware Settings

### Free Tier (CPU Basic)
- ✅ Free forever
- ⏱️ Slower generation (5-10 minutes per track)
- 💾 Limited to 16GB RAM
- 👥 Good for testing and light use

### Paid Tier (GPU)
- 💰 ~$0.60/hour
- ⚡ Fast generation (1-3 minutes per track)
- 💾 More RAM available
- 👥 Better for production use

To upgrade:
1. Go to your Space settings
2. Click "Hardware"
3. Select desired GPU tier
4. Confirm payment method

---

## 🔄 Automatic Updates

Now whenever you push to GitHub `main` branch:
1. GitHub Actions triggers automatically
2. Code is synced to Hugging Face
3. Space rebuilds with new code
4. Updates go live automatically! 🚀

---

## 🐛 Troubleshooting

### Build Failing?

Check the logs:
1. Go to your Space on Hugging Face
2. Click "Logs" tab
3. Look for error messages

Common issues:
- Missing dependencies → Check `requirements.txt`
- Wrong file paths → Ensure `app.py` exists
- Token expired → Generate new token and update secret

### GitHub Actions Failing?

1. Go to GitHub → Actions tab
2. Click on the failed workflow
3. Check the error logs
4. Common issues:
   - Wrong `HF_SPACE_NAME` format
   - Invalid `HF_TOKEN`
   - Space doesn't exist on Hugging Face

### Space Running but Not Loading?

1. Check if models are downloading (first run takes 10-15 minutes)
2. Look at Space logs for errors
3. Ensure GPU/CPU has enough memory

---

## 📊 Monitoring

### Check Usage
1. Go to Hugging Face Space settings
2. View "Analytics" tab
3. Monitor:
   - Visitor count
   - Generation requests
   - Error rate

### Check Costs (if using GPU)
1. Go to [Hugging Face Billing](https://huggingface.co/settings/billing)
2. Monitor GPU usage hours
3. Set spending limits if needed

---

## 🎨 Customization

### Update Space Appearance

Edit the YAML frontmatter in `README_HF.md`:

```yaml
---
title: Your Custom Title
emoji: 🎵  # Any emoji
colorFrom: blue  # Start color
colorTo: purple  # End color
---
```

### Add Custom Domain

1. Go to Space settings
2. Click "Custom Domain"
3. Follow Hugging Face instructions

---

## 🔐 Security Best Practices

✅ **DO:**
- Use separate tokens for different services
- Rotate tokens regularly
- Use write-only tokens (not admin)
- Keep secrets in GitHub Secrets (never in code)

❌ **DON'T:**
- Commit tokens to repository
- Share tokens publicly
- Use personal access tokens in production
- Give more permissions than needed

---

## 📚 Resources

- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Gradio Documentation](https://gradio.app/docs)

---

## 🎉 You're All Set!

Your Hinglish Rap Generator is now:
- ✅ Live on Hugging Face Spaces
- ✅ Auto-deploying from GitHub
- ✅ Accessible worldwide
- ✅ Ready to create amazing rap tracks!

**Share your Space**: `https://huggingface.co/spaces/YOUR_HF_USERNAME/hinglish-rap-generator`

---

**Need help?** Open an issue on [GitHub](https://github.com/cph0r/hindi-rapper/issues)

🎤 Happy Rap Creating! 🔥

