from fastapi import APIRouter, Request
import urllib.parse
from src.integrations.bland import bland_trigger_demo_call
from src.integrations.sheets import send_to_google_sheets
from src.utils import parse_bland_ai_webhook, parse_elementor_form

import json

router = APIRouter()



@router.post("/webhook/trigger_demo_call")
async def wp_homepage_trigger_demo_call(request: Request):
    body = await request.body()
    form_data = body.decode('utf-8')
    fields = parse_elementor_form(form_data)
    bland_trigger_demo_call(fields["user_name"], fields["user_phone"])

@router.post("/webhook/bland_ai_callback")
async def bland_ai_webhook_handler(request: Request):
    """Handle Bland AI webhook after call completion"""
    
    body = await request.body()
    webhook_data = json.loads(body.decode('utf-8'))
    
    # Parse the webhook data
    call_details = parse_bland_ai_webhook(webhook_data)
    
    # Send to Google Sheets
    sheets_success = send_to_google_sheets(call_details)
    
    # Your other business logic here:
    # - Save to database
    # - Send notifications
    # - Update user records
    
    return {
        "status": "success", 
        "message": "Bland AI webhook processed",
        "call_details": call_details,
        "google_sheets_updated": sheets_success
    }