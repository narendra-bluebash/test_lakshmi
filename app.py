import random
from pydantic import BaseModel
from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if token != "1234":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
        )
    return token

valid_emails = [
    "userone@gmail.com",
    "usertwo@gmail.com",
    "userthree@gmail.com",
    "userfour@gmail.com",
    "user@gmail.com",
]

@app.get('/email')
async def check_email(request: Request, token: str = Depends(verify_token)):
    email = request.query_params.get("email")

    if not email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email query parameter is required"
        )

    if email in valid_emails:
        return {
            "status": "success",
            "message": f"The email '{email}' is valid and present in the list."
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The email '{email}' is not found in the valid list."
        )

valid_phones = ["+917389058485", "+12363269419", "+911234567890"]
@app.get('/phone')
async def check_phone(request: Request, token: str = Depends(verify_token)):
    phone = request.query_params.get("phone")

    if not phone:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Phone query parameter is required"
        )

    phone = phone.replace(' ', '+')
    if phone in valid_phones:
        return {
            "status": "success",
            "message": f"The phone number '{phone}' is valid and present in the list."
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The phone number '{phone}' is not found in the valid list."
        )


@app.get('/get_status')
async def get_order_status(request: Request):
    phone_number = request.query_params.get("phone_number")
    dob = request.query_params.get("dob")

    return {
        "status": "success",
        "order_status": f"Your order is confirmed and is being processed. Phone number: {phone_number}, DOB: {dob}"
    }

@app.post('/book_ticket')
async def book_ticket(request: Request):
    body = await request.json()
    movie_name = request.query_params.get("movie_name")
    username = body.get("username")
    time = body.get("time")
    price = body.get("price")

    return {
        "status": "success",
        "data":[
            {
                "order_status": "Pending",
                "dispatched_at": None,
                "order_id": 12346,
                "customer_name": "Alice Smith",
                "email": "alice@example.com",
                "phone": "+1-555-5678",
                "address": "456 Oak St, Anytown, USA",
                "payment_status": "Pending",
                "payment_method": "PayPal",
                "total_amount": 250.50,
                "currency": "USD",
                "items_purchased": 5,
                "delivery_partner": "EcoDelivery",
                "estimated_delivery": None,
                "priority": "Normal",
                "movie_name": movie_name,
                "username": username,
                "time": time,
                "price": price,
                "notes": "Contact upon arrival",
                "created_at": "2024-12-30T09:00:00Z",
                "last_updated": "2024-12-30T09:05:00Z"
            },
            {
                "order_status": "Dispatched",
                "dispatched_at": "2024-12-30T10:00:00Z",
                "order_id": 12347,
                "customer_name": "Bob Johnson",
                "email": "bob@example.com",
                "phone": "+1-555-8910",
                "address": "789 Pine St, Anytown, USA",
                "payment_status": "Paid",
                "payment_method": "Debit Card",
                "total_amount": 75.25,
                "currency": "USD",
                "items_purchased": 1,
                "delivery_partner": "QuickShip",
                "estimated_delivery": "2024-12-31T16:00:00Z",
                "priority": "Normal",
                "movie_name": movie_name,
                "username": username,
                "time": time,
                "price": price,
                "notes": "N/A",
                "created_at": "2024-12-29T14:00:00Z",
                "last_updated": "2024-12-30T10:00:00Z"
            },
            {
                "order_status": "Delivered",
                "dispatched_at": "2024-12-29T14:20:00Z",
                "order_id": 12348,
                "customer_name": "Charlie Brown",
                "email": "charlie@example.com",
                "phone": "+1-555-1122",
                "address": "101 Birch St, Anytown, USA",
                "payment_status": "Paid",
                "payment_method": "Cash on Delivery",
                "total_amount": 99.99,
                "currency": "USD",
                "movie_name": movie_name,
                "username": username,
                "time": time,
                "price": price,
                "items_purchased": 2,
                "delivery_partner": "SwiftMove",
                "estimated_delivery": "2024-12-30T12:00:00Z",
                "priority": "High",
                "notes": "Call before delivery",
                "created_at": "2024-12-28T11:30:00Z",
                "last_updated": "2024-12-30T12:00:00Z"
            }
        ]
    }


@app.post('/book_ticket2')
async def book_ticket(request: Request):
    body = await request.json()
    movie_name = request.query_params.get("movie_name")
    username = body.get("username")
    time = body.get("time")
    price = body.get("price")

    return {
        "status": "success",
        "order_status": "Pending",
        "dispatched_at": None,
        "order_id": 12346,
        "customer_name": "Alice Smith",
        "email": "alice@example.com",
        "phone": "+1-555-5678",
        "address": "456 Oak St, Anytown, USA",
        "payment_status": "Pending",
        "payment_method": "PayPal",
        "total_amount": 250.50,
        "currency": "USD",
        "items_purchased": 5,
        "delivery_partner": "EcoDelivery",
        "estimated_delivery": None,
        "priority": "Normal",
        "movie_name": movie_name,
        "username": username,
        "time": time,
        "price": price,
        "notes": "Contact upon arrival",
        "created_at": "2024-12-30T09:00:00Z",
        "last_updated": "2024-12-30T09:05:00Z"
    }

class AgentAction(BaseModel):
    name: str
    email: str = None
    from_number: str = None
    to_number: str = None

class Payload(BaseModel):
    agent_action_id: int
    agent_action: AgentAction

@app.post('/generate_otp')
async def generate_otp(payload: Payload, token: str = Depends(verify_token)):
    otp = random.randint(10000, 99999)

    if payload.agent_action.from_number is None:
        print(f"[AMSService][generate_otp] Generating OTP for email: {payload.agent_action.email}")
        result = {
            "status": "success",
            "verification_code": otp,
            "message": f"OTP generated for email: {payload.agent_action.email}"
        }
    else:
        print(f"[AMSService][generate_otp] Generating OTP for phone number: {payload.agent_action.from_number}")
        result = {
            "status": "success",
            "verification_code": otp,
            "message": f"OTP generated for phone number: {payload.agent_action.from_number}"
        }

    return result