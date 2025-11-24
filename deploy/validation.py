
sample_payload ={
  "income": 0.10000000149011612,
  "name_email_similarity": 0.5249947309494019,
  "customer_age": 20.0,
  "days_since_request": 0.0014186592306941748,
  "intended_balcon_amount": -0.7624531388282776,

  "payment_type": "AC",
  "velocity_6h": 6869.3974609375,
  "velocity_24h": 6826.61376953125,
  "velocity_4w": 5483.5908203125,
  "bank_branch_count_8w": 0.0,
  "date_of_birth_distinct_emails_4w": 6.0,

  "employment_status": "CA",
  "credit_risk_score": 55.0,
  "email_is_free": 0,
  "housing_status": "BE",
  "phone_home_valid": 0,
  "phone_mobile_valid": 1,
  "has_other_cards": 0,
  "proposed_credit_limit": 200.0,
  "foreign_request": 0,
  "source": 0,
  "session_length_in_minutes": 12.901134490966797,
  "device_os": "other",
  "keep_alive_session": 1,
  "device_distinct_emails_8w": 1.0,
  "month_sin": 0.0,
  "month_cos": 1.0
}

bad_payload = sample_payload.copy()
bad_payload['email_is_free'] = 3.0