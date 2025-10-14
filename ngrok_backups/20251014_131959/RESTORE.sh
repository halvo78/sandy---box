#!/bin/bash
# Restore Ngrok from this backup

echo "🔄 Restoring Ngrok from backup..."

# Restore config
mkdir -p "$HOME/.config/ngrok"
cp ngrok.yml "$HOME/.config/ngrok/" 2>/dev/null || echo "No config to restore"

# Restore systemd service
if [ -f "ngrok-permanent.service" ]; then
    sudo cp ngrok-permanent.service /etc/systemd/system/
    sudo systemctl daemon-reload
    sudo systemctl enable ngrok-permanent
    echo "✅ Systemd service restored"
fi

# Show tunnel URLs from backup
if [ -f "tunnels.txt" ]; then
    echo ""
    echo "Previous tunnel URLs:"
    cat tunnels.txt
fi

echo ""
echo "✅ Restore complete!"
echo "Run: sudo systemctl start ngrok-permanent"
