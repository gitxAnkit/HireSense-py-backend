import urllib.request
import json
import time

base_url = "http://127.0.0.1:8000/job/"

def create_job():
    data = {
        "title": "Backend Developer",
        "company": "Startup Inc",
        "skills": "Python, Django, PostgreSQL",
        "location": "New York",
        "salary": "140000"
    }
    headers = {'Content-Type': 'application/json'}
    req = urllib.request.Request(base_url, data=json.dumps(data).encode('utf-8'), headers=headers, method='POST')
    print(f"Sending POST request to {base_url} with data: {data}")
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print("Create Job Success! Response:")
                print(response.read().decode('utf-8'))
            else:
                print(f"Create Failed with status: {response.status}")
                print(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Create Error: {e}")

def get_jobs():
    req = urllib.request.Request(base_url, method='GET')
    print(f"Sending GET request to {base_url}")
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print("Get Jobs Success! Response:")
                print(response.read().decode('utf-8'))
            else:
                print(f"Get Failed with status: {response.status}")
                print(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Get Error: {e}")

if __name__ == "__main__":
    create_job()
    time.sleep(1)
    get_jobs()
