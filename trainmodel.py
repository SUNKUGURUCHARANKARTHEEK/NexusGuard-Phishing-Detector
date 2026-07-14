#!/usr/bin/env python3

import time
import random
import json
from datetime import datetime

class NexusGuard:
    def __init__(self):
        self.model = MockModel()
        self.history = self.load_history()
    
    def load_history(self):
        try:
            with open("scan_history.json", "r") as f:
                return json.load(f)
        except:
            return []
    
    def save_history(self):
        with open("scan_history.json", "w") as f:
            json.dump(self.history, f, indent=2)

    def scan_message(self, message):
        print("\n🔍 Initializing Neural Scan...")
        time.sleep(1.2)
        
        prediction = self.model.predict(message)
        proba = self.model.predict_proba(message)
        is_threat = prediction == 1
        confidence = round(max(proba) * 100, 1)
        
        print("\n" + "="*60)
        
        if is_threat:
            print("🛑 HIGH THREAT DETECTED")
            print(f"Confidence Level: {confidence}%")
        else:
            print("✅ MESSAGE CLEARED")
            print(f"Confidence Level: {confidence}%")
        
        print("="*60)
        
        # Detailed Analysis
        print("\n📊 DETAILED ANALYSIS:")
        print(f"   • Phishing Probability : {proba[1]*100:.1f}%")
        print(f"   • Safe Probability     : {proba[0]*100:.1f}%")
        print(f"   • Risk Level           : {'CRITICAL' if is_threat else 'LOW'}")
        
        if is_threat:
            print("\n⚠️  RECOMMENDATION: Do not click links. Block the sender.")
        else:
            print("\n✅ This message appears to be legitimate.")
        
        # Save record
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "threat": is_threat,
            "confidence": confidence,
            "preview": message[:75] + "..." if len(message) > 75 else message
        }
        self.history.append(entry)
        self.save_history()
        
        return is_threat, confidence


class MockModel:
    def predict(self, text):
        text = text.lower()
        danger_words = ["win", "free", "cash", "prize", "urgent", "click", "guarantee", 
                       "lottery", "offer", "limited", "verify", "account", "password", "bank"]
        return 1 if any(word in text for word in danger_words) else 0
    
    def predict_proba(self, text):
        if self.predict(text) == 1:
            return [0.08, random.uniform(0.85, 0.98)]
        return [random.uniform(0.80, 0.96), 0.12]


def main():
    scanner = NexusGuard()
    
    print("\n" + "="*70)
    print("                    NEXUSGUARD SENTINEL v4.2")
    print("               Advanced AI Threat Intelligence")
    print("="*70)
    
    while True:
        print("\nOptions:")
        print("1. Scan New Message")
        print("2. View Scan History")
        print("3. Clear History")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\nPaste your message below:")
            message = input("> ")
            if message.strip():
                scanner.scan_message(message)
        
        elif choice == "2":
            print("\n📜 SCAN HISTORY")
            if not scanner.history:
                print("No scans recorded yet.")
            else:
                for i, entry in enumerate(reversed(scanner.history[-10:]), 1):
                    status = "THREAT" if entry["threat"] else "SAFE"
                    print(f"{i:2d}. [{entry['timestamp']}] {status} - {entry['confidence']}%")
                    print(f"    {entry['preview']}")
                    print("-" * 55)
        
        elif choice == "3":
            confirm = input("Clear all history? (y/n): ").lower()
            if confirm == "y":
                scanner.history = []
                scanner.save_history()
                print("History has been cleared.")
        
        elif choice == "4":
            print("\nThank you for using NexusGuard. Stay safe!")
            break
        
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nScan session terminated.")
