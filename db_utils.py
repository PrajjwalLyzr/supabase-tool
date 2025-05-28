from supabase import Client, create_client
import os
from dotenv import load_dotenv; load_dotenv()



supabase: Client = create_client(supabase_url=os.getenv("SUPABASE_URL"), supabase_key=os.getenv("SUPABASE_KEY"))

def insert_ticket(ticket_text: str):
    """
    Inserts a new ticket into the 'tickets_demo' table.
    
    :param ticket_text: The content to insert into the 'tickets' column.
    :return: Response from Supabase insert operation.
    """
    if not ticket_text.strip():
        raise ValueError("Ticket text cannot be empty.")

    response = supabase.table("tickets_demo").insert({
        "tickets": ticket_text
    }).execute()

    return response.data