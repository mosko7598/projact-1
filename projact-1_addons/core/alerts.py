import json

def check_alerts(portfolio):
    with open("alerts_config.json", "r", encoding="utf-8") as f:
        alerts = json.load(f)

    for asset, limits in alerts.items():
        if asset in portfolio:
            current_value = portfolio[asset]
            if "min" in limits and current_value < limits["min"]:
                print(f"⚠️ {asset} ירד מתחת ל-{limits['min']}!")
            if "max" in limits and current_value > limits["max"]:
                print(f"📈 {asset} עבר את הגבול העליון ({limits['max']})!")
