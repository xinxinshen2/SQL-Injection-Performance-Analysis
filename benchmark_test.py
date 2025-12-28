import requests
import time
import statistics

# Configuration
BASE_URL = "http://localhost/sql_test"  # Adjust if your XAMPP uses a different port
VULN_URL = f"{BASE_URL}/vulnerable.php"
SECURE_URL = f"{BASE_URL}/secure.php"

# Test Payloads
NORMAL_USER = "admin"
INJECTION_PAYLOAD = "' OR '1'='1"

def measure_latency(url, username, iterations=100):
    latencies = []
    print(f"--- Benchmarking {url} ({iterations} requests) ---")
    
    for _ in range(iterations):
        start_time = time.time()
        try:
            requests.get(url, params={'username': username})
            end_time = time.time()
            latencies.append((end_time - start_time) * 1000) # Convert to ms
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    avg_latency = statistics.mean(latencies)
    print(f"Average Latency: {avg_latency:.4f} ms")
    return avg_latency

def test_security(url, payload, description):
    print(f"\nTesting Security on [{description}]...")
    try:
        # Send the injection payload
        response = requests.get(url, params={'username': payload})
        
        # Check if the page indicates a successful login
        if "Login Successful" in response.text:
            print(f"[RESULT] VULNERABLE: Injection succeeded with payload: {payload}")
            print(f"Server Response snippet: {response.text.strip()[:100]}...")
            return False # Failed security test
        else:
            print("[RESULT] SECURE: Injection failed (Login blocked).")
            return True # Passed security test
            
    except Exception as e:
        print(f"Error testing security: {e}")

def main():
    print("=== SQL Injection Research Experiment ===\n")

    # 1. Security Analysis (Integrity)
    test_security(VULN_URL, INJECTION_PAYLOAD, "Vulnerable Page")
    test_security(SECURE_URL, INJECTION_PAYLOAD, "Secure Page")

    print("\n" + "="*40 + "\n")

    # 2. Performance Analysis (Latency)
    # We use a normal username for latency testing to keep it consistent
    measure_latency(VULN_URL, NORMAL_USER)
    measure_latency(SECURE_URL, NORMAL_USER)

if __name__ == "__main__":
    main()