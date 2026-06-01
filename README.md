# Linux-Based-Keylogger-Live-Monitoring-on-Logs
Advanced keylogger for authorized security testing: captures keystrokes with timestamps, analyzes typed text for sensitive keywords (credentials, financial data, secrets), issues console/GUI/audio alerts, logs incidents and session stats, with configurable thresholds and keyword lists.
# Advanced Keylogger with Data Leakage Detection
## Complete Installation and Usage Guide

### Installation Steps:

1. **Install Python Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Keylogger:**
   ```bash
   python advanced_keylogger_complete.py
   ```

### Features:

✅ **Real-time Keystroke Monitoring**
- Captures all keyboard input with timestamps
- Stores logs in hidden directory (~/.keylogger_data/)

✅ **Advanced Data Leakage Detection**
- Monitors for 50+ sensitive keywords
- Detects company secrets, financial data, passwords, etc.
- Real-time analysis of keystroke patterns

✅ **Multi-layered Alert System**
- Console alerts with visual warnings
- GUI popup notifications
- Audio beep alerts
- Detailed alert logging

✅ **Smart Detection Logic**
- Word-level and phrase-level analysis
- Configurable sensitivity thresholds
- Cooldown periods to prevent spam alerts

✅ **Comprehensive Logging**
- Keystroke logs with timestamps
- Security alert logs
- Session statistics
- JSON configuration files

### Security Keywords Monitored:

**Company Secrets:**
- confidential, secret, classified, internal, proprietary
- restricted, private, sensitive, trade secret, non-disclosure

**Financial Data:**
- password, credit card, ssn, social security, bank account
- routing number, pin, salary, budget, financial

**Technical Secrets:**
- api key, access token, database, server, admin
- root, master key, encryption, certificate, private key

**Business Sensitive:**
- merger, acquisition, layoff, restructure, patent
- client list, customer data, employee records

### How It Works:

1. **Monitoring:** Runs in background, capturing all keystrokes
2. **Analysis:** Real-time analysis of typed content for sensitive patterns
3. **Detection:** Triggers alerts when sensitive keywords are detected
4. **Logging:** All keystrokes and alerts are logged with timestamps
5. **Reporting:** Detailed session statistics and security reports

### Files Created:
- `~/.keylogger_data/keystroke_log.txt` - All keystrokes with timestamps
- `~/.keylogger_data/security_alerts.txt` - Security alert details
- `~/.keylogger_data/session_stats.json` - Session statistics
- `~/.keylogger_data/config.json` - Configuration settings

### Stopping the Keylogger:
- Press `Ctrl+C` to stop monitoring
- Session statistics will be displayed
- All logs are automatically saved

### Legal Notice:
This tool should only be used for legitimate security monitoring purposes
with proper authorization. Unauthorized keylogging may violate privacy laws.

### Customization:
You can modify the `sensitive_keywords` list in the code to add/remove
keywords specific to your organization's security requirements.
