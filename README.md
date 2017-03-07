# alexa-sqs-home-manager
Controll local server through alexa using AWS SQS

client.py should run in Raspberry Pi, and lambda_function.py should run in AWS Lambda

## Lambda Function

### YeelightOn

  Send 'turn of Yeelight' message to SQS

### YeelightOff
  Send 'turn off Yeelight' message to SQS
