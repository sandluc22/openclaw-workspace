import json, os, sys
from google_auth_oauthlib.flow import InstalledAppFlow

with open('.creds/oauth_client.json') as f:
    client_config = json.load(f)

SCOPES = ['https://www.googleapis.com/auth/youtube.upload',
          'https://www.googleapis.com/auth/youtube']

CODE_VERIFIER = "b105jqROFNwEUAPvQcgtFeVPbrPrrAmW4n7USoZBTr8"

flow = InstalledAppFlow.from_client_config(
    client_config, SCOPES,
    redirect_uri='http://localhost:8080/'
)

code = sys.argv[sys.argv.index('--code') + 1]
flow.code_verifier = CODE_VERIFIER
flow.fetch_token(code=code)
creds = flow.credentials
print("✅ AUTENTICACIÓN COMPLETA!")

token_data = {
    "token": creds.token,
    "refresh_token": creds.refresh_token,
    "token_uri": creds.token_uri,
    "client_id": creds.client_id,
    "client_secret": creds.client_secret,
    "scopes": creds.scopes,
    "expiry": creds.expiry.isoformat() if creds.expiry else None
}
with open('.creds/youtube_token.json', 'w') as f:
    json.dump(token_data, f)
os.chmod('.creds/youtube_token.json', 0o600)
print("✅ Token guardado!")

# SUBIR
from googleapiclient.discovery import build
youtube = build('youtube', 'v3', credentials=creds)
ch = youtube.channels().list(part='snippet', mine=True).execute()
for c in ch.get('items', []):
    print(f"📺 {c['snippet']['title']}")

video_path = 'clubcontable/videos/habitos_video_01_ok.mp4'
print(f"🚀 Subiendo ({os.path.getsize(video_path)/1024/1024:.1f} MB)...")
r = youtube.videos().insert(
    part='snippet,status',
    body={
        'snippet': {
            'title': 'El BUCLE del HÁBITO 🧠 | El Poder de los Hábitos #1',
            'description': 'Aprende el bucle del hábito aplicado a tu vida. De "El poder de los hábitos" de Charles Duhigg.\n\n📌 Parte 1 de 5. Suscríbete.\n\n🎯 Déjanos tus comentarios, los leo todos.\n\n#Productividad #Hábitos #DesarrolloPersonal',
            'categoryId': '27',
            'tags': ['productividad', 'hábitos', 'desarrollo personal']
        },
        'status': {'privacyStatus': 'private', 'selfDeclaredMadeForKids': False}
    },
    media_body=video_path
).execute()
print(f"🎉 SUBIDO! https://youtube.com/watch?v={r['id']}")
