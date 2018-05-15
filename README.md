# noxchange-khipu (POC)

## Intro

App Flask, que corre en AWS Lambda usando Zappa. Para correr local:

`./noxchange_khipu.py`

##TODO
- OK Generar una pseudoapi con requests en vez de la opensource, esto por la incompatibilidad de la version 1.3
- Generar pequeño formulario de prueba con callback usando return_url


##Test

Ver tests.py

## Cifrado de mensajes

Khipu utiliza un cifrado bastante particular. Requiere una autorización en el header que utiliza el `subscriber_id` y el `secret` que provee Khipu. El problema es que además te pide codificar el payload de cada mensaje.

Ejemplo de llamada vía cURL.

curl -i -H "Authorization: 178671:b4d39fecbf60a4633d371670eb4aa5b02771a3071ad72a1f7f247395a3db13dc" https://khipu.com/api/2.0/payments\?notification_token\=e2378adb7a79f8c7bc2690981bc4e816cbef9751f10612a41bcaab1ba8912601

{
  "payment_id": "d92mdt3vgeet",
  "payment_url": "https://khipu.com/payment/info/d92mdt3vgeet",
  "app_url": "khipu:///pos/d92mdt3vgeet",
  "ready_for_terminal": true,
  "transfer_url": "https://khipu.com/payment/manual/d92mdt3vgeet",
  "simplified_transfer_url": "https://app.khipu.com/payment/simplified/d92mdt3vgeet",
  "receiver_id": 178671,
  "notification_token": "e2378adb7a79f8c7bc2690981bc4e816cbef9751f10612a41bcaab1ba8912601",
  "subject": "El asunto del cobro",
  "amount": "200.0000",
  "discount": "0.0000",
  "currency": "CLP",
  "status": "done",
  "status_detail": "normal",
  "body": "Descripcion del cobro",
  "picture_url": "",
  "receipt_url": "https://s3.amazonaws.com/notifications.khipu.com/CPKH-0505181713-d92mdt3vgeet.pdf",
  "return_url": "https://qwfm42whze.execute-api.us-east-1.amazonaws.com/dev/testreturn",
  "cancel_url": "",
  "notify_url": "https://qwfm42whze.execute-api.us-east-1.amazonaws.com/dev/testnotify",
  "notify_api_version": "",
  "expires_date": "2018-05-05T20:40:48.000Z",
  "attachment_urls":
  [
  ],
  "bank": "Banco BIC",
  "bank_id": "Evdfk",
  "payer_name": "John Doe",
  "payer_email": "XXXXX@gmail.com",
  "personal_identifier": "XXX",
  "bank_account_number": "XXXXX7",
  "out_of_date_conciliation": false,
  "transaction_id": "T-1000",
  "custom": "some url",
  "responsible_user_email": "XXXX@gmail.com",
  "send_reminders": false,
  "send_email": false,
  "payment_method": "simplified_transfer",
  "conciliation_date": "2018-05-05T20:13:05.203Z"
}
