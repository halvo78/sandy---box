
#!/bin/bash
BACKUP_DIR="/home/ubuntu/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# Backup system files
cp -r /home/ubuntu/ultimate_lyra_v5 "$BACKUP_DIR/"
cp -r /home/ubuntu/ultimate_lyra_systems "$BACKUP_DIR/" 2>/dev/null || true

# Backup logs
mkdir -p "$BACKUP_DIR/logs"
cp /home/ubuntu/ultimate_lyra_v5/logs/* "$BACKUP_DIR/logs/" 2>/dev/null || true

# Create backup manifest
echo "Backup created: $(date)" > "$BACKUP_DIR/backup_manifest.txt"
echo "System: $(uname -a)" >> "$BACKUP_DIR/backup_manifest.txt"
echo "Files backed up: $(find $BACKUP_DIR -type f | wc -l)" >> "$BACKUP_DIR/backup_manifest.txt"

echo "Backup completed: $BACKUP_DIR"
