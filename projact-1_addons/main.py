from fastapi import FastAPI
from core.portfolio import get_portfolio_value
from core.alerts import check_alerts
from core.history import save_value, get_history

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ברוך הבא למערכת ניהול תיק ההשקעות שלך"}

@app.get("/portfolio-value")
def get_value():
    value = get_portfolio_value()
    save_value(value["total_usd"])
    check_alerts(value)
    return {"portfolio_value": value}

@app.get("/portfolio-history")
def get_portfolio_history():
    return {"history": get_history()}
