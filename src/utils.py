import urllib

def parse_elementor_form(form_data: str) -> dict:
    """Parse Elementor form and return field_id: field_value dict"""
    parsed = urllib.parse.parse_qs(form_data)
    fields = {}
    
    for key, value in parsed.items():
        if key.startswith("fields[") and key.endswith("][value]"):
            field_id = key.split("[")[1].split("]")[0]
            fields[field_id] = value[0] if value else ""
    
    return fields


def parse_bland_ai_webhook(webhook_data: dict) -> dict:
    """Parse Bland AI webhook and extract necessary details"""
    
    # Extract basic call info
    call_id = webhook_data.get("call_id", "")
    c_id = webhook_data.get("c_id", "")
    to = webhook_data.get("to", "")
    from_number = webhook_data.get("from", "")
    call_length = webhook_data.get("call_length", 0)
    corrected_duration = webhook_data.get("corrected_duration", "")
    status = webhook_data.get("status", "")
    completed = webhook_data.get("completed", False)
    answered_by = webhook_data.get("answered_by", "")
    call_ended_by = webhook_data.get("call_ended_by", "")
    disposition_tag = webhook_data.get("disposition_tag", "")
    
    # Extract timestamps
    created_at = webhook_data.get("created_at", "")
    started_at = webhook_data.get("started_at", "")
    end_at = webhook_data.get("end_at", "")
    
    # Extract analysis data (not analysis_schema)
    analysis = webhook_data.get("analysis", {})
    is_potential_lead = analysis.get("is_potential_lead", False)
    how_soon_can_he_join = analysis.get("how_soon_can_he_join", None)
    interested_course_name = analysis.get("interested_course_name", "")
    
    # Extract other important fields
    summary = webhook_data.get("summary", "")
    recording_url = webhook_data.get("recording_url", "")
    concatenated_transcript = webhook_data.get("concatenated_transcript", "")
    price = webhook_data.get("price", 0)
    
    # Extract metadata
    metadata = webhook_data.get("metadata", {})
    source = metadata.get("source", "")
    
    # Extract variables if needed
    variables = webhook_data.get("variables", {})
    country = variables.get("country", "")
    language = variables.get("language", "")
    timezone = variables.get("timezone", "")
    
    return {
        "call_id": call_id,
        "c_id": c_id,
        "phone_number": to,
        "from_number": from_number,
        "call_duration": call_length,
        "corrected_duration": corrected_duration,
        "call_status": status,
        "completed": completed,
        "answered_by": answered_by,
        "call_ended_by": call_ended_by,
        "disposition_tag": disposition_tag,
        "created_at": created_at,
        "started_at": started_at,
        "end_at": end_at,
        "is_potential_lead": is_potential_lead,
        "how_soon_can_he_join": how_soon_can_he_join,
        "interested_course_name": interested_course_name,
        "summary": summary,
        "recording_url": recording_url,
        "transcript": concatenated_transcript,
        "call_price": price,
        "source": source,
        "country": country,
        "language": language,
        "timezone": timezone
    }

