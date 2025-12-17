import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

sb_url = os.getenv("SUPABASE_API_URL")
sb_key = os.getenv("SUPABASE_SERVICE_KEY")

if not sb_url or not sb_key:
    raise ValueError("Missing Supabase Details")

supabase: Client = create_client(supabase_url=sb_url,supabase_key=sb_key)