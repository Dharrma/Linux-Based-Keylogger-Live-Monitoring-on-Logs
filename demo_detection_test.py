
"""
Demo script to test the keylogger's sensitive data detection
Run this after starting the keylogger to see alerts in action
"""

import time
import sys

def demo_typing_simulation():
    """Simulate typing sensitive data to trigger alerts"""

    print("="*60)
    print("KEYLOGGER DETECTION DEMO")
    print("="*60)
    print("This script will help you test the keylogger's detection capabilities.")
    print("Start the keylogger first, then run this demo.")
    print()

    test_phrases = [
        "This is a confidential document",
        "My password is 123456",
        "The secret project alpha details",
        "Company database server credentials",
        "Internal salary information",
        "Trade secret formulation",
        "Customer credit card data",
        "API key authentication token"
    ]

    print("Test phrases that should trigger alerts:")
    print("-" * 40)

    for i, phrase in enumerate(test_phrases, 1):
        print(f"{i}. {phrase}")
        if input("Press Enter to continue (or 'q' to quit): ").lower() == 'q':
            break
        print()

    print("Demo completed! Check your keylogger for security alerts.")

if __name__ == "__main__":
    demo_typing_simulation()
