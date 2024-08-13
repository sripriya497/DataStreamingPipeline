from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'Airflow',
    'start_date': datetime(2024,8,6,10,00)
}

def get_data():
    import requests
    response = requests.get("https://randomuser.me/api/")
    response_result = response.json()['results'][0]
    return response_result

def format_data(response_result):
    data = {}
    data['first_name'] = response_result['name']['first']
    data['first_name'] = response_result['name']['last']
    data['gender'] = response_result['gender']
    location = response_result['location']
    data['address'] = f"{str(location['street']['number'])}  {location['street']['name']}" \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['postcode'] = location['postcode']
    data['email'] = response_result['email']
    data['username'] = response_result['login']['username']
    data['dob'] = response_result['dob']['date']
    data['registered_date'] = response_result['registered']['date']
    data['phone'] = response_result['phone']
    data['picture'] = response_result['picture']['medium']

    return data

def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging

    producer = KafkaProducer(bootstrap_servers = ['broker:29092'], max_block_ms = 5000)
    current_time = time.time()
    while True:
        if time.time() > current_time + 60:
            break
        try:
            response = get_data()
            response = format_data(response)
            producer.send('users_created', json.dumps(response).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            continue

with DAG('user_automation',
         default_args = default_args,
         schedule = timedelta(days=1),
         catchup= False) as dag:
    stream_task = PythonOperator(
        task_id = 'stream_data_from_api',
        python_callable= stream_data
    )