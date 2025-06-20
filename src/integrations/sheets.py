import requests
import time

GOOGLE_SHEETS_WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbwRf988aZd6-Npf2u08jMBZhYcFg73kkD1tnzYrTi8XZTFj4XBOjSlZx5_l6jjA6IyH7w/exec"

def send_to_google_sheets(data: dict):
    """Send parsed data to Google Sheets via Google Apps Script"""
    try:
        response = requests.post(
            GOOGLE_SHEETS_WEBHOOK_URL,
            json=data,
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'Medha-AI-Backend/1.0'
            },
            timeout=30
        )
        
        print(f"Google Sheets response status: {response.status_code}")
        print(f"Google Sheets response: {response.text}")
        
        response.raise_for_status()
        
        # Parse the response
        result = response.json()
        
        if result.get('status') == 'success':
            print("✅ Data successfully sent to Google Sheets")
            return True
        else:
            print(f"❌ Google Sheets error: {result.get('message', 'Unknown error')}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ Timeout error sending to Google Sheets")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error sending to Google Sheets: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Error sending to Google Sheets: {str(e)}")
        return False

def test_google_sheets_connection():
    """Test function to verify Google Sheets integration works"""
    test_data = {
        "call_id": "backend-test-" + str(int(time.time())),
        "phone_number": "+919876543210",
        "from_number": "+17754297771", 
        "call_duration": 2.5,
        "call_status": "completed",
        "is_potential_lead": True,
        "how_soon_can_he_join": "2 weeks",
        "interested_course_name": "Backend Test Course",
        "disposition_tag": "INTERESTED",
        "call_ended_by": "USER",
        "answered_by": "human",
        "summary": "Test call from backend to verify Google Sheets integration",
        "country": "IN",
        "language": "English (India)",
        "source": "backend_test",
        "recording_url": "https://example.com/test-recording",
        "created_at": "2025-06-20T10:05:09.981+00:00",
        "started_at": "2025-06-20T10:05:09.981Z",
        "end_at": "2025-06-20T10:06:41.000Z",
        "call_price": 0.15,
        "transcript": "This is a test call transcript from the backend."
    }
    
    print("🔄 Testing Google Sheets connection...")
    success = send_to_google_sheets(test_data)
    
    if success:
        print("✅ Google Sheets test successful!")
        return {"status": "success", "message": "Test data sent to Google Sheets"}
    else:
        print("❌ Google Sheets test failed!")
        return {"status": "error", "message": "Failed to send test data to Google Sheets"}