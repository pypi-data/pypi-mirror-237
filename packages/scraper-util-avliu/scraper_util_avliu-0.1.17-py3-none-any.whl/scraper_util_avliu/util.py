import json
import os
import re
import time

from selenium import webdriver
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.error

import mysql.connector

import boto3
import datetime


def get_selenium_driver(undetected=False):
    # adblock_filepath = '../lib/adblock.crx'

    if undetected:
        driver_executable_path = os.environ.get('DRIVER_EXECUTABLE_PATH')
        if not driver_executable_path:
            driver_executable_path = '/usr/bin/chromedriver'
        print(f'path={driver_executable_path}')
        # See if we actually need this in cloud
        # use_subprocess = True

        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--remote-debugging-port=9222")
        # chrome_options.add_extension(adblock_filepath)
        driver = uc.Chrome(options=chrome_options,
                           use_subprocess=True,
                           driver_executable_path=driver_executable_path)

    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_extension(adblock_filepath)
        driver = webdriver.Chrome(options=chrome_options)

    return driver


def get_soup(url_or_driver):
    if type(url_or_driver) == uc.Chrome or type(url_or_driver) == webdriver.Chrome:
        return BeautifulSoup(url_or_driver.page_source, "html.parser")

    success = False
    sleep_time = 1
    max_sleep_time = 60 * 5

    req, html_page = None, None
    while not success:
        try:
            req = Request(url_or_driver)
            html_page = urlopen(req)
            success = True
        except urllib.error.HTTPError as e:
            print(f'error {e.code}')
            if 500 <= e.code <= 599 and sleep_time < max_sleep_time:
                print(f'server error; sleep {sleep_time} seconds')
                time.sleep(sleep_time)
                sleep_time *= 2
            else:
                raise e

    soup = BeautifulSoup(html_page, 'html.parser')
    return soup


# Get all the text within elements found using search_str
def get_soup_text(soup: BeautifulSoup, search_str: str, one=False):
    if one:
        return format_str(soup.select_one(search_str).text)
    else:
        return list(map(lambda x: format_str(x.text), soup.select(search_str)))


def append_to_json(json_file, new_data):
    if os.path.isfile(json_file):
        with open(json_file, 'r') as fp:
            all_data = json.load(fp)
    else:
        all_data = []

    all_data.append(new_data)

    with open(json_file, 'w') as fp:
        json.dump(all_data, fp, indent=4, separators=(',', ': '))


def append_to_file(file_name, new_data):
    with open(file_name, 'a') as f:
        for data in new_data:
            f.write(f'{data}\n')


def find_in_dict(my_dict: dict, key: str):
    # print(f'keys considered: {list(my_dict.keys())}')
    if key in my_dict.keys():
        return my_dict[key]
    ans = False
    for v in my_dict.values():
        if type(v) == dict:
            temp = find_in_dict(v, key)
            if temp != False:
                ans = temp
    return ans


# Replace newlines/tabs with the symbol |
def format_str(s):
    return re.sub("[\n\t\r]+", '|', s)


# Remove unnecessary symbols from a string
def remove_symbols_str(s):
    return re.sub("[|+:,.]", '', s)


def write_to_rds(table_name: str, schema: list, data_dict: dict):
    # Make a mysql connection and create a table if it exists
    mydb = mysql.connector.connect(
        host=os.environ.get('rds_endpoint'),
        # TODO
        user="admin",
        password="12345678",
        database="ev-database-test"
    )

    # TODO: Move
    mycursor = mydb.cursor()
    mycursor.execute(
        f"CREATE TABLE IF NOT EXISTS {table_name} "
        f"("
        f"vin VARCHAR(255), "
        f"date_accessed date, "
        f"make VARCHAR(255), "
        f"model VARCHAR(255), "
        f"price VARCHAR(255), "
        f"location VARCHAR(255), "
        f"fuel VARCHAR(255),"
        f"ebay_item_id VARCHAR(255),"
        f"PRIMARY KEY (vin, date_accessed)"
        f")"
    )

    sql = f"INSERT IGNORE INTO {table_name} VALUES (%s, now(), %s, %s, %s, %s, %s, %s)"
    val_list = []
    for col in schema:
        filt_keys = list(filter(lambda x: col in x.lower(), data_dict.keys()))
        if len(filt_keys) == 0:
            val_list.append('')
        else:
            val_list.append(data_dict[filt_keys[0]])
    val = tuple(val_list)
    mycursor.execute(sql, val)
    mydb.commit()


def batch_submit_job(job_name, job_def, job_queue):
    client = boto3.client('batch')
    response = client.submit_job(
        jobName=job_name,
        jobQueue=job_queue,
        jobDefinition=job_def,
        shareIdentifier='high',
        schedulingPriorityOverride=9999
    )
    print(f'batch submit job repsonse: {response}')


def get_log_time():
    dt = datetime.datetime.now()
    epoch = datetime.datetime.utcfromtimestamp(0)
    time = int((dt - epoch).total_seconds() * 1000.0)
    return time


def write_cloudwatch_log(log_group, log_stream, message):
    client = boto3.client('logs')
    response = client.put_log_events(
        logGroupName=log_group,
        logStreamName=log_stream,
        logEvents=[
            {
                'timestamp': get_log_time(),
                'message': message
            },
        ]
    )
    print(f'response: {response}')


def write_to_s3(aws_bucket, source, dest):
    # Make sure to configure ~/.aws/configure file
    s3 = boto3.resource('s3')
    s3.Bucket(aws_bucket).upload_file(source, dest)


# Write a list of messages to SQS queue
def write_to_sqs(sqs_queue_id: str, messages_list: list):
    sqs = boto3.client('sqs')
    # Convert dictionary to json
    entries = [{'Id': str(i), 'MessageBody': json.dumps(message)} for i, message in enumerate(messages_list)]

    # Splitting into chunks of 10
    chunks = [entries[i:i + 10] for i in range(0, len(entries), 10)]

    # Send message to SQS queue
    for chunk in chunks:
        entries = [{'Id': str(i), 'MessageBody': json.dumps(message)} for i, message in enumerate(chunk)]
        response = sqs.send_message_batch(
            QueueUrl=sqs_queue_id,
            Entries=entries
        )
        print(f'write to sqs response: {response}')


# Read one message from SQS queue
def read_from_sqs(sqs_queue_id: str):
    # Borrowed from: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs-example-sending-receiving-msgs.html
    # Create SQS client
    sqs = boto3.client('sqs')

    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=sqs_queue_id,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']

    # Delete received message from queue
    # TODO: Move out
    sqs.delete_message(
        QueueUrl=sqs_queue_id,
        ReceiptHandle=receipt_handle
    )

    message_id = message['MessageId'] if 'MessageId' in message.keys() else 'UnknownId'
    message_body = message['Body']
    message_body = json.loads(message_body)
    message_content = json.loads(message_body['MessageBody']) if 'MessageBody' in message_body.keys() else message_body

    return message_id, message_content


def get_today():
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    return today


def main():
    bucket = 'test-youtube-audit-bucket'
    f = open("test_result_file.txt", "a")
    f.write("File content!")
    f.close()
    destination = 'test_folder/test_results_file.txt'

    write_to_s3(bucket, "./test_result_file.txt", destination)


if __name__ == '__main__':
    main()
