# Azure Key Vault — LYRA Integration Pack
This pack moves **all sensitive secrets** (exchange keys, AI keys, webhooks, DB URLs) out of files and into **Azure Key Vault (AKV)**, with **RBAC**, **private access**, and **automation**.

## Quickstart
1. **Create vault (RBAC + private-by-default + purge protection)**
```bash
export RG="lyra-rg"; export LOC="australiaeast"; export KV_NAME="lyra-kv-prod"
az group create -n "$RG" -l "$LOC"
az keyvault create -n "$KV_NAME" -g "$RG" -l "$LOC"   --enable-rbac-authorization true   --enable-purge-protection true --retention-days 90   --public-network-access Disabled
```

2. **Grant access (RBAC)**
```bash
export PRINCIPAL_ID="<managed-identity-or-sp-objectId>"
export KV_ID="$(az keyvault show -n "$KV_NAME" -g "$RG" --query id -o tsv)"
az role assignment create --assignee "$PRINCIPAL_ID"   --role "Key Vault Secrets User" --scope "$KV_ID"
```

3. **Migrate `.env.local` → Key Vault**
```bash
python3 kv_env_migrator.py .env.local "https://$KV_NAME.vault.azure.net/"
```

4. **Use at runtime**
- Python: `kv_fetcher_python.py`
- Node: `kv_fetcher_node.js`

See full runbook inside for naming, rotation, private endpoints, and troubleshooting.
