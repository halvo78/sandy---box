# 🚀 QUICK SETUP INSTRUCTIONS

## ✅ YOUR SYSTEM IS RUNNING!

But the AI models need API keys to work. Here's how to fix it:

---

## 🔑 STEP 1: GET YOUR OPENROUTER API KEYS

1. Go to **https://openrouter.ai/**
2. Sign up or log in
3. Click on **"Keys"** in the menu
4. Click **"Create Key"**
5. Copy the key (starts with `sk-or-v1-...`)
6. **Repeat 4-8 times** for better performance (optional)

---

## ⚡ STEP 2: CONFIGURE THE SYSTEM

### **Option A: Interactive Setup (EASIEST)**

```bash
cd ~/ultimate_lyra_systems
./SETUP_API_KEYS.sh
```

This will ask you to paste your API keys one by one.

### **Option B: Manual Setup**

1. Edit `config_template.json`:
   ```bash
   nano config_template.json
   ```

2. Replace `YOUR_OPENROUTER_API_KEY_X_HERE` with your actual keys

3. Save as `config.json`:
   ```bash
   cp config_template.json config.json
   ```

---

## 🚀 STEP 3: RESTART THE SYSTEM

```bash
cd ~/ultimate_lyra_systems
source venv/bin/activate
python3 ULTIMATE_TURBO_CHARGED_PRODUCTION_SYSTEM.py
```

---

## 📊 WHAT YOU'LL SEE

Once configured, you'll see:

```
✅ AI Team initialized (14 models)
✅ Market Analyst: google/gemini-pro-1.5
✅ Technical Analyst: anthropic/claude-3.5-sonnet
✅ Risk Manager: openai/gpt-4-turbo
... (and 11 more AIs)

🤖 AI CONSENSUS: Analyzing BTC/USDT...
📊 Confidence: 92.5%
💡 Decision: BUY
📈 Position Size: $50,000
```

---

## 🎯 SYSTEM FEATURES

Once running with API keys:

- 💰 **$1,000,000 capital** (paper trading)
- 🪙 **8 coins trading** simultaneously
- ⏱️  **6 timeframes** analyzed in parallel
- 🤖 **14 AI professionals** making decisions
- 📊 **18 trading strategies** active
- 📈 **330+ indicators** calculated
- 🚀 **Unlimited positions**
- ⚡ **Turbo mode** enabled

---

## 🔧 TROUBLESHOOTING

### **Still getting 401 errors?**

1. Check your API keys are valid
2. Make sure `config.json` exists (not `config_template.json`)
3. Verify keys start with `sk-or-v1-`
4. Check OpenRouter account has credits

### **Want to test without AI first?**

Edit `config.json` and set:
```json
"min_confidence": 0.0
```

This will allow trading without AI consensus (not recommended for production).

---

## 📞 NEED HELP?

The system is running in **paper trading mode** - it's completely safe!

You can:
- Stop it anytime with `Ctrl+C`
- Check logs in `logs/turbo/`
- View data in `data/turbo/`
- Modify `config.json` for any settings

---

## 🎉 READY TO GO!

Once you add your API keys and restart, the ULTIMATE TURBO-CHARGED SYSTEM will:

1. ✅ Query all 14 AI models
2. ✅ Get weighted consensus
3. ✅ Execute trades based on AI decisions
4. ✅ Track performance
5. ✅ Learn and optimize
6. ✅ Generate reports

**Add your API keys and watch the AI trade! 🚀**

