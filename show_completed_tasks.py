
import requests
import datetime as dt
import pandas as pd
import yaml

def get_token():
    with open("token", "r") as f:
        return f.readline()
    
def get_data():
    uri = "https://api.todoist.com/sync/v8/completed/get_all"
    auth = {"Authorization": f"Bearer {get_token()}"}
    resp = requests.get(uri, headers=auth)
    return resp.json()

def update_data(json_data, file="data.csv"):
    try:
        existing_data = pd.read_csv(file)
    except Exception:
        existing_data = pd.DataFrame()
    data = pd.concat([existing_data, pd.DataFrame(json_data["items"])])
    data = data.drop_duplicates("id")
    data.to_csv(file, index=False)
    return data

def print_items(data):
    date_old = dt.date.today()
    print("Today:")
    for _, t in data.sort_values("completed_date", ascending=False).iterrows():
        date = dt.datetime.strptime(t["completed_date"], "%Y-%m-%dT%H:%M:%SZ")
        if date_old != date.date():
            print()
            date_old = date.date()
            print(date_old)
        print(f"✅ {date.time()} | {t['content']}")
        
if __name__ == "__main__":
    json_data = get_data()
    data = update_data(json_data)
    print_items(data)
