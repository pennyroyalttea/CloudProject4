{"filter":false,"title":"lambda_function.py","tooltip":"/producer2021New/lambda_function.py","undoManager":{"mark":24,"position":24,"stack":[[{"start":{"row":0,"column":0},"end":{"row":8,"column":0},"action":"remove","lines":["import json","","def lambda_handler(event, context):","    # TODO implement","    return {","        'statusCode': 200,","        'body': json.dumps('Hello from Lambda!')","    }",""],"id":1},{"start":{"row":0,"column":0},"end":{"row":72,"column":49},"action":"insert","lines":["\"\"\"","Dynamo to SQS","\"\"\"","","import boto3","import json","import sys","import os","","DYNAMODB = boto3.resource('dynamodb')","TABLE = \"fang\"","QUEUE = \"producer\"","SQS = boto3.client(\"sqs\")","","#SETUP LOGGING","import logging","from pythonjsonlogger import jsonlogger","","LOG = logging.getLogger()","LOG.setLevel(logging.INFO)","logHandler = logging.StreamHandler()","formatter = jsonlogger.JsonFormatter()","logHandler.setFormatter(formatter)","LOG.addHandler(logHandler)","","def scan_table(table):","    \"\"\"Scans table and return results\"\"\"","","    LOG.info(f\"Scanning Table {table}\")","    producer_table = DYNAMODB.Table(table)","    response = producer_table.scan()","    items = response['Items']","    LOG.info(f\"Found {len(items)} Items\")","    return items","","def send_sqs_msg(msg, queue_name, delay=0):","    \"\"\"Send SQS Message","","    Expects an SQS queue_name and msg in a dictionary format.","    Returns a response dictionary. ","    \"\"\"","","    queue_url = SQS.get_queue_url(QueueName=queue_name)[\"QueueUrl\"]","    queue_send_log_msg = \"Send message to queue url: %s, with body: %s\" %\\","        (queue_url, msg)","    LOG.info(queue_send_log_msg)","    json_msg = json.dumps(msg)","    response = SQS.send_message(","        QueueUrl=queue_url,","        MessageBody=json_msg,","        DelaySeconds=delay)","    queue_send_log_msg_resp = \"Message Response: %s for queue url: %s\" %\\","        (response, queue_url) ","    LOG.info(queue_send_log_msg_resp)","    return response","","def send_emissions(table, queue_name):","    \"\"\"Send Emissions\"\"\"","","    items = scan_table(table=table)","    for item in items:","        LOG.info(f\"Sending item {item} to queue: {queue_name}\")","        response = send_sqs_msg(item, queue_name=queue_name)","        LOG.debug(response)","","def lambda_handler(event, context):","    \"\"\"","    Lambda entrypoint","    \"\"\"","","    extra_logging = {\"table\": TABLE, \"queue\": QUEUE}","    LOG.info(f\"event {event}, context {context}\", extra=extra_logging)","    send_emissions(table=TABLE, queue_name=QUEUE)"]}],[{"start":{"row":60,"column":22},"end":{"row":61,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":61,"column":0},"end":{"row":61,"column":8},"action":"insert","lines":["        "]},{"start":{"row":61,"column":8},"end":{"row":61,"column":9},"action":"insert","lines":["s"]},{"start":{"row":61,"column":9},"end":{"row":61,"column":10},"action":"insert","lines":["e"]},{"start":{"row":61,"column":10},"end":{"row":61,"column":11},"action":"insert","lines":["n"]},{"start":{"row":61,"column":11},"end":{"row":61,"column":12},"action":"insert","lines":["d"]},{"start":{"row":61,"column":12},"end":{"row":61,"column":13},"action":"insert","lines":["i"]},{"start":{"row":61,"column":13},"end":{"row":61,"column":14},"action":"insert","lines":["n"]},{"start":{"row":61,"column":14},"end":{"row":61,"column":15},"action":"insert","lines":["g"]}],[{"start":{"row":61,"column":15},"end":{"row":61,"column":17},"action":"insert","lines":["()"],"id":3}],[{"start":{"row":61,"column":16},"end":{"row":61,"column":17},"action":"insert","lines":["i"],"id":4},{"start":{"row":61,"column":17},"end":{"row":61,"column":18},"action":"insert","lines":["t"]},{"start":{"row":61,"column":18},"end":{"row":61,"column":19},"action":"insert","lines":["e"]},{"start":{"row":61,"column":19},"end":{"row":61,"column":20},"action":"insert","lines":["m"]}],[{"start":{"row":61,"column":19},"end":{"row":61,"column":20},"action":"remove","lines":["m"],"id":5},{"start":{"row":61,"column":18},"end":{"row":61,"column":19},"action":"remove","lines":["e"]},{"start":{"row":61,"column":17},"end":{"row":61,"column":18},"action":"remove","lines":["t"]},{"start":{"row":61,"column":16},"end":{"row":61,"column":17},"action":"remove","lines":["i"]},{"start":{"row":61,"column":15},"end":{"row":61,"column":17},"action":"remove","lines":["()"]},{"start":{"row":61,"column":14},"end":{"row":61,"column":15},"action":"remove","lines":["g"]},{"start":{"row":61,"column":13},"end":{"row":61,"column":14},"action":"remove","lines":["n"]},{"start":{"row":61,"column":12},"end":{"row":61,"column":13},"action":"remove","lines":["i"]},{"start":{"row":61,"column":11},"end":{"row":61,"column":12},"action":"remove","lines":["d"]},{"start":{"row":61,"column":10},"end":{"row":61,"column":11},"action":"remove","lines":["n"]},{"start":{"row":61,"column":9},"end":{"row":61,"column":10},"action":"remove","lines":["e"]},{"start":{"row":61,"column":8},"end":{"row":61,"column":9},"action":"remove","lines":["s"]}],[{"start":{"row":61,"column":8},"end":{"row":61,"column":9},"action":"insert","lines":["p"],"id":6},{"start":{"row":61,"column":9},"end":{"row":61,"column":10},"action":"insert","lines":["r"]},{"start":{"row":61,"column":10},"end":{"row":61,"column":11},"action":"insert","lines":["i"]},{"start":{"row":61,"column":11},"end":{"row":61,"column":12},"action":"insert","lines":["n"]},{"start":{"row":61,"column":12},"end":{"row":61,"column":13},"action":"insert","lines":["t"]}],[{"start":{"row":61,"column":13},"end":{"row":61,"column":15},"action":"insert","lines":["()"],"id":7}],[{"start":{"row":61,"column":14},"end":{"row":61,"column":15},"action":"insert","lines":["i"],"id":8},{"start":{"row":61,"column":15},"end":{"row":61,"column":16},"action":"insert","lines":["t"]},{"start":{"row":61,"column":16},"end":{"row":61,"column":17},"action":"insert","lines":["e"]},{"start":{"row":61,"column":17},"end":{"row":61,"column":18},"action":"insert","lines":["m"]}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "],"id":9}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["p"],"id":10},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["r"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["i"]},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["n"]},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":9},"end":{"row":27,"column":11},"action":"insert","lines":["()"],"id":11}],[{"start":{"row":27,"column":10},"end":{"row":27,"column":12},"action":"insert","lines":["\"\""],"id":12}],[{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["s"],"id":13},{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":["c"]},{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"insert","lines":["a"]},{"start":{"row":27,"column":14},"end":{"row":27,"column":15},"action":"insert","lines":["n"]},{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":["n"]},{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"insert","lines":["i"]},{"start":{"row":27,"column":17},"end":{"row":27,"column":18},"action":"insert","lines":["n"]},{"start":{"row":27,"column":18},"end":{"row":27,"column":19},"action":"insert","lines":["g"]}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":18,"column":0},"end":{"row":18,"column":1},"action":"insert","lines":["p"]},{"start":{"row":18,"column":1},"end":{"row":18,"column":2},"action":"insert","lines":["r"]},{"start":{"row":18,"column":2},"end":{"row":18,"column":3},"action":"insert","lines":["i"]},{"start":{"row":18,"column":3},"end":{"row":18,"column":4},"action":"insert","lines":["n"]},{"start":{"row":18,"column":4},"end":{"row":18,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":18,"column":5},"end":{"row":18,"column":7},"action":"insert","lines":["()"],"id":15}],[{"start":{"row":18,"column":6},"end":{"row":18,"column":8},"action":"insert","lines":["\"\""],"id":16}],[{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["s"],"id":17},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["c"]},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["a"]},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["n"]},{"start":{"row":18,"column":11},"end":{"row":18,"column":12},"action":"insert","lines":["n"]},{"start":{"row":18,"column":12},"end":{"row":18,"column":13},"action":"insert","lines":["i"]},{"start":{"row":18,"column":13},"end":{"row":18,"column":14},"action":"insert","lines":["n"]},{"start":{"row":18,"column":14},"end":{"row":18,"column":15},"action":"insert","lines":["g"]}],[{"start":{"row":59,"column":0},"end":{"row":60,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":60,"column":0},"end":{"row":60,"column":1},"action":"insert","lines":[" "]},{"start":{"row":60,"column":1},"end":{"row":60,"column":2},"action":"insert","lines":[" "]},{"start":{"row":60,"column":2},"end":{"row":60,"column":3},"action":"insert","lines":[" "]},{"start":{"row":60,"column":3},"end":{"row":60,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":60,"column":4},"end":{"row":60,"column":6},"action":"insert","lines":["[]"],"id":19}],[{"start":{"row":60,"column":5},"end":{"row":60,"column":6},"action":"insert","lines":["r"],"id":20}],[{"start":{"row":60,"column":5},"end":{"row":60,"column":6},"action":"remove","lines":["r"],"id":21},{"start":{"row":60,"column":4},"end":{"row":60,"column":6},"action":"remove","lines":["[]"]}],[{"start":{"row":60,"column":4},"end":{"row":60,"column":5},"action":"insert","lines":["p"],"id":22},{"start":{"row":60,"column":5},"end":{"row":60,"column":6},"action":"insert","lines":["r"]},{"start":{"row":60,"column":6},"end":{"row":60,"column":7},"action":"insert","lines":["i"]},{"start":{"row":60,"column":7},"end":{"row":60,"column":8},"action":"insert","lines":["n"]},{"start":{"row":60,"column":8},"end":{"row":60,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":60,"column":9},"end":{"row":60,"column":11},"action":"insert","lines":["()"],"id":23}],[{"start":{"row":60,"column":10},"end":{"row":60,"column":12},"action":"insert","lines":["\"\""],"id":24}],[{"start":{"row":60,"column":11},"end":{"row":60,"column":12},"action":"insert","lines":["s"],"id":25},{"start":{"row":60,"column":12},"end":{"row":60,"column":13},"action":"insert","lines":["e"]},{"start":{"row":60,"column":13},"end":{"row":60,"column":14},"action":"insert","lines":["n"]},{"start":{"row":60,"column":14},"end":{"row":60,"column":15},"action":"insert","lines":["d"]},{"start":{"row":60,"column":15},"end":{"row":60,"column":16},"action":"insert","lines":["i"]},{"start":{"row":60,"column":16},"end":{"row":60,"column":17},"action":"insert","lines":["n"]},{"start":{"row":60,"column":17},"end":{"row":60,"column":18},"action":"insert","lines":["g"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":60,"column":4},"end":{"row":60,"column":20},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1617683955487,"hash":"47e40976bfad3fe578d54990072cd605922058c0"}