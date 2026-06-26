# MamaBaohe-ERP-SQLi
The `ERPBillHandler.ashx` endpoint in the MamaBaohe ERP Management Cloud Platform contains a SQL injection vulnerability. The `billdate` parameter in `action=search` requests does not properly sanitize user input, allowing unauthenticated remote attackers to execute arbitrary SQL queries.
