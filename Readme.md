# StockBot

StockBot is a WhatsApp-based chatbot for managing inventory. It allows users to check the current stock of a product, add or reduce stock using simple commands, and logs all transactions in MongoDB. It is designed to work in Portuguese and can be deployed on AWS Lambda.

## Features

* **Check Stock** : Users can check the current stock level using the command `Quantas unidades em estoque?`.
* **Add Stock** : Users can increase stock using the command `Adicionar <number>`.
* **Reduce Stock** : Users can decrease stock using the command `Reduzir <number>`.
* **Error Handling** : Handles invalid inputs and ensures stock doesn't go negative.
* **Database** : Logs all stock transactions in a MongoDB database.
* **WhatsApp Integration** : Interacts with users via WhatsApp using the Twilio API.

---

## Prerequisites

Before running the project, make sure you have:

* **Python 3.x** installed on your machine.
* **MongoDB** : A MongoDB cloud database (e.g., MongoDB Atlas).
* **Twilio Account** : A Twilio account with WhatsApp sandbox set up.
* **AWS Account** : AWS account with access to Lambda, API Gateway, and S3 for deployment using Zappa.

---

## Setup Instructions


### 3. **Install Dependencies**

Install the required Python libraries using  **pip** :

`pip install -r requirements.txt
`


This will install:

* Flask: For the web framework.
* Twilio: For WhatsApp messaging integration.
* PyMongo: For interacting with MongoDB.
* Zappa: For deploying the application to AWS Lambda.

### 4. **Configure MongoDB**

In  **app.py** , update the connection string for MongoDB:

`client = pymongo.MongoClient("YOUR_MONGODB_CONNECTION_STRING")
`


Here's the **`README.md`** documentation for your **StockBot** project. It includes all the necessary information for setting up, running, and deploying the WhatsApp chatbot.

---

# StockBot

StockBot is a WhatsApp-based chatbot for managing inventory. It allows users to check the current stock of a product, add or reduce stock using simple commands, and logs all transactions in MongoDB. It is designed to work in Portuguese and can be deployed on AWS Lambda.

## Features

* **Check Stock** : Users can check the current stock level using the command `Quantas unidades em estoque?`.
* **Add Stock** : Users can increase stock using the command `Adicionar <number>`.
* **Reduce Stock** : Users can decrease stock using the command `Reduzir <number>`.
* **Error Handling** : Handles invalid inputs and ensures stock doesn't go negative.
* **Database** : Logs all stock transactions in a MongoDB database.
* **WhatsApp Integration** : Interacts with users via WhatsApp using the Twilio API.

---

## Prerequisites

Before running the project, make sure you have:

* **Python 3.x** installed on your machine.
* **MongoDB** : A MongoDB cloud database (e.g., MongoDB Atlas).
* **Twilio Account** : A Twilio account with WhatsApp sandbox set up.
* **AWS Account** : AWS account with access to Lambda, API Gateway, and S3 for deployment using Zappa.

---

## Setup Instructions

### 1. **Clone the Repository**

First, clone the repository to your local machine:

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git clone https://github.com/yourusername/stockbot.git
cd stockbot
</code></div></div></pre>

### 2. **Create a Virtual Environment**

It is recommended to use a virtual environment to manage dependencies:

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python3 -m venv venv
source venv/bin/activate  # For Linux/MacOS
# For Windows: venv\Scripts\activate
</code></div></div></pre>

### 3. **Install Dependencies**

Install the required Python libraries using  **pip** :

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
</code></div></div></pre>

This will install:

* Flask: For the web framework.
* Twilio: For WhatsApp messaging integration.
* PyMongo: For interacting with MongoDB.
* Zappa: For deploying the application to AWS Lambda.

### 4. **Configure MongoDB**

In  **app.py** , update the connection string for MongoDB:

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python">client = pymongo.MongoClient("YOUR_MONGODB_CONNECTION_STRING")
</code></div></div></pre>

If you’re using MongoDB Atlas, you can find the connection string in your MongoDB Atlas dashboard. Ensure the database and collection are properly configured.

### 5. **Configure Twilio WhatsApp Sandbox**

1. Sign up at [Twilio](https://www.twilio.com/).
2. Go to your Twilio Console and find **WhatsApp Sandbox** under the Messaging section.
3. Set the **Webhook URL** for incoming messages to your deployed Lambda endpoint. For example:

`https://xyz.execute-api.us-east-1.amazonaws.com/production/webhook
`


1. You will get this URL after deploying the application with Zappa (explained below).

---

## Running the Application Locally

You can run the Flask app locally to test it before deploying:

1. Start the local development server:

`python app.py
`


1. The app will be available at `http://localhost:5000`.
   **Note** : Since the Twilio webhook requires an online endpoint, running the app locally may not fully test the WhatsApp integration. However, you can simulate other interactions by sending HTTP requests to `localhost:5000/webhook`.

---

## Deployment with Zappa (AWS Lambda)

1. **Initialize Zappa**
   Zappa simplifies the process of deploying Python web apps to AWS Lambda. Run the following command:

`zappa init
`


* Follow the prompts to set up the deployment. Choose:
  * **AWS region** : Select your preferred AWS region (e.g., `us-east-1`).
  * **Profile name** : Leave as `default`.
  * **Runtime** : Choose `python3.8`.
  * **S3 Bucket** : Select or create an S3 bucket for Zappa to use.
* **Deploy the Flask Application to Lambda**
  After the Zappa initialization is complete, deploy the application to AWS Lambda:

`zappa deploy production
`


1. This command will upload your Flask app to AWS Lambda, configure API Gateway, and provide you with a deployment URL.
2. **Update Twilio Webhook URL**
   After deployment, you will receive an API URL from Zappa (e.g., `https://xyz.execute-api.us-east-1.amazonaws.com/production/webhook`). Set this URL as the webhook for your  **Twilio WhatsApp Sandbox** .

---

## Commands and Usage

### 1. **Check Stock**

To check the current stock of the product, users can send the message:

`Quantas unidades em estoque?
`


The bot will respond with the current stock level.

### 2. **Add Stock**

To add stock, users can send the message:

`Adicionar <number>
`

`Adicionar 10
`


The bot will increase the stock by the specified number and log the transaction in MongoDB.

### 3. **Reduce Stock**

To reduce stock, users can send the message:

`Reduzir <number>
`


Example:

`Reduzir 5
`


The bot will decrease the stock by the specified number and log the transaction in MongoDB. If the stock is insufficient, it will return an error.

### 4. **Error Handling**

If the user enters an invalid command or non-numeric value, the bot will respond with an error message.

---

## MongoDB Transaction Schema

All stock transactions are logged in MongoDB in the **transactions** collection. The schema is as follows:

`{
  "transaction_id": "UUID",
  "action": "Add" or "Reduce",
  "product_id": "String",
  "count": "Integer (positive for Add, negative for Reduce)",
  "timestamp": "ISO-8601 formatted date"
}
`

Example of a logged transaction:

`{
  "transaction_id": "b74d89c7-c36e-4b7d-bcf9-3d41cf83320c",
  "action": "Add",
  "product_id": "product_1",
  "count": 10,
  "timestamp": "2024-11-14T14:10:00Z"
}
`


## Logo Design

You can design a minimalist logo for **StockBot** using tools like **Canva** or  **Figma** . Here's a suggestion for the logo:

* **Symbol** : Use an inventory box, stock icon, or related symbol.
* **Text** : Include the name **StockBot** in a simple, clear font.

Once the logo is designed, you can use it for branding purposes.

---

## Troubleshooting

### 1. **MongoDB Connection Issues**

Make sure your MongoDB URI is correctly configured in `app.py`. If you are using MongoDB Atlas, ensure your connection string includes the correct username, password, and database name.

### 2. **Twilio Webhook Not Working**

Ensure the Twilio webhook is correctly set to the deployed Lambda URL. Check that AWS API Gateway is accessible and the webhook path is correct.
