# Info Assurance Lab — Spring 2022 (Prof. Dnayak)

## Tools Used
- Wireshark (traffic analysis)  
- Nmap (host discovery, service scan)  
- Metasploit (only in controlled VM — focused on *defensive* logging)

## What I Did
- Captured HTTP vs. HTTPS traffic → saw cleartext passwords in HTTP  
- Simulated phishing email → observed how users click → discussed mitigation (training, email filters)  
- Ran `nmap -sS -sV 192.168.1.0/24` → documented open ports → matched to asset inventory

## Support Relevance
When a user says “my account got hacked,” check:
1. Did they use HTTP on public Wi-Fi?  
2. Was MFA enabled?  
3. Any recent suspicious emails?

> Original PCAP files not retained. Notes based on lab write-ups.
