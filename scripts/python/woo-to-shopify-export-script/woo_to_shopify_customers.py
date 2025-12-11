from dotenv import load_dotenv
load_dotenv()

import requests
import csv
import time
import os

API_BASE = os.getenv("WC_API_BASE", "https://example.com/wp-json/wc/v3")
CONSUMER_KEY = os.getenv("WC_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("WC_CONSUMER_SECRET")

MAX_RETRIES = 5

def get_with_retries(url, params):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = requests.get(url, auth=(CONSUMER_KEY, CONSUMER_SECRET), params=params, timeout=15)
            if r.status_code == 429:
                wait_time = int(r.headers.get("Retry-After", 5))
                print(f"⚠️ Rate-Limit – Warte {wait_time}s ...")
                time.sleep(wait_time)
                continue
            r.raise_for_status()
            return r
        except requests.exceptions.RequestException as e:
            print(f"❌ Fehler bei Versuch {attempt}: {e}")
            if attempt < MAX_RETRIES:
                wait_time = attempt * 3
                print(f"⏳ Warte {wait_time}s und versuche erneut ...")
                time.sleep(wait_time)
            else:
                print("🚨 Maximale Versuche erreicht – Anfrage übersprungen.")
                return None

def fetch_all(endpoint):
    data = []
    page = 1
    per_page = 100
    url = f"{API_BASE}/{endpoint}"

    print(f"🔄 Lade Daten von {endpoint} ...")
    first = get_with_retries(url, {"per_page": per_page, "page": 1})
    if not first:
        return data

    total_pages = int(first.headers.get("X-WP-TotalPages", 1))
    print(f"📊 {total_pages} Seiten gefunden für {endpoint}.")

    data.extend(first.json())

    for page in range(2, total_pages + 1):
        print(f"➡️ Lade Seite {page}/{total_pages} von {endpoint} ...")
        r = get_with_retries(url, {"per_page": per_page, "page": page})
        if not r:
            continue
        data.extend(r.json())
        time.sleep(0.5)

    print(f"✅ Insgesamt {len(data)} Datensätze aus {endpoint}.")
    return data

def extract_customers_from_orders(orders):
    customers = {}
    for order in orders:
        billing = order.get("billing", {})
        email = billing.get("email", "")
        if not email:
            continue
        customers[email] = {
            "first_name": billing.get("first_name", ""),
            "last_name": billing.get("last_name", ""),
            "email": email,
            "phone": billing.get("phone", ""),
            "username": order.get("customer_id", "guest"),
            "date_created": order.get("date_created", ""),
            "billing_address_1": billing.get("address_1", ""),
            "billing_city": billing.get("city", ""),
            "billing_postcode": billing.get("postcode", ""),
            "billing_country": billing.get("country", "")
        }
    return list(customers.values())

def sanitize_customer(c, allowed_fields):
    """Filtert nur erlaubte Felder heraus"""
    return {k: c.get(k, "") for k in allowed_fields}

def save_to_csv(customers):
    filename = "customers_shopify.csv"
    fieldnames = [
        "first_name", "last_name", "email", "phone", "username",
        "date_created", "billing_address_1", "billing_city",
        "billing_postcode", "billing_country"
    ]
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for c in customers:
            clean_row = sanitize_customer(c, fieldnames)
            writer.writerow(clean_row)
    print(f"💾 CSV-Datei erstellt: {filename}")

if __name__ == "__main__":
    customers_direct = fetch_all("customers")
    orders = fetch_all("orders")

    customers_from_orders = extract_customers_from_orders(orders)

    # Kombinieren & Duplikate vermeiden (nach Email)
    all_customers = {c["email"]: c for c in customers_direct if c.get("email")}
    for c in customers_from_orders:
        if c["email"] not in all_customers:
            all_customers[c["email"]] = c

    combined_list = list(all_customers.values())

    print(f"🧩 Kombiniert: {len(combined_list)} eindeutige Kunden insgesamt.")
    save_to_csv(combined_list)
