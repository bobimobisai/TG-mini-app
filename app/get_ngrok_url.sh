ngrok http 8000 &

sleep 10

ngrok_url=$(curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')

echo "NGROK_URL=${ngrok_url}" > /ngrok_url.txt

wait