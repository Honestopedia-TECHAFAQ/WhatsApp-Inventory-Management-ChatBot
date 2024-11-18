from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import pymongo
from uuid import uuid4
from datetime import datetime

app = Flask(__name__)

client = pymongo.MongoClient("YOUR_MONGODB_CONNECTION_STRING")
db = client['inventory']
transactions = db['transactions']

stock = {'product_1': 100}

@app.route("/webhook", methods=["POST"])
def webhook():
    message = request.form['Body']
    from_number = request.form['From']
    
    resp = MessagingResponse()

    if message.lower() == "quantas unidades em estoque?":
        stock_level = stock.get('product_1', 0)
        resp.message(f"Estoque atual: {stock_level} unidades.")
    
    elif message.lower().startswith("adicionar"):
        try:
            count = int(message.split()[1])
            stock['product_1'] += count
            transaction = {
                'transaction_id': str(uuid4()),
                'action': 'Add',
                'product_id': 'product_1',
                'count': count,
                'timestamp': datetime.utcnow().isoformat()
            }
            transactions.insert_one(transaction)
            resp.message(f"Estoque aumentado em {count} unidades.")
        except ValueError:
            resp.message("Erro: Por favor, forneça um número válido.")
    
    elif message.lower().startswith("reduzir"):

        try:
            count = int(message.split()[1])
            if stock['product_1'] - count < 0:
                resp.message("Erro: Não há estoque suficiente.")
            else:
                stock['product_1'] -= count
                transaction = {
                    'transaction_id': str(uuid4()),
                    'action': 'Reduce',
                    'product_id': 'product_1',
                    'count': -count,
                    'timestamp': datetime.utcnow().isoformat()
                }
                transactions.insert_one(transaction)
                resp.message(f"Estoque reduzido em {count} unidades.")
        except ValueError:
            resp.message("Erro: Por favor, forneça um número válido.")
    
    else:
        resp.message("Comando não reconhecido. Tente: 'Quantas unidades em estoque?' ou 'Adicionar 10'.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
