
import os
import uuid
import io
from flask import Flask, render_template, request, redirect, send_file
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
from azure.cosmos import CosmosClient

# ------------------ LOAD ENV VARIABLES ------------------
load_dotenv()  # Loads .env from the project root

BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
COSMOS_KEY = os.getenv("COSMOS_KEY")

# DEBUG: check if variables are loaded correctly
print("BLOB_CONNECTION_STRING:", BLOB_CONNECTION_STRING)
print("COSMOS_KEY:", COSMOS_KEY)

BLOB_CONTAINER_NAME = "files"
COSMOS_ENDPOINT = "https://cloudfilecosmos12.documents.azure.com:443/"
DATABASE_NAME = "filedb"
CONTAINER_NAME = "metadata"
# --------------------------------------------------------

# Initialize Flask app
app = Flask(__name__)

# ------------------ AZURE BLOB SETUP ------------------
blob_service = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
blob_container = blob_service.get_container_client(BLOB_CONTAINER_NAME)

# ------------------ COSMOS DB SETUP -------------------
cosmos_client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = cosmos_client.create_database_if_not_exists(DATABASE_NAME)
container = database.create_container_if_not_exists(
    id=CONTAINER_NAME,
    partition_key="/id"
)

# ------------------ ROUTES ----------------------------
@app.route("/")
def index():
    items = list(container.read_all_items())
    return render_template("index.html", files=items)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    description = request.form["description"]

    file_id = str(uuid.uuid4())
    blob_name = f"{file_id}_{file.filename}"

    blob_container.upload_blob(blob_name, file)

    container.create_item({
        "id": file_id,
        "filename": file.filename,
        "blob_name": blob_name,
        "description": description
    })

    return redirect("/")

@app.route("/download/<blob_name>")
def download(blob_name):
    blob = blob_container.download_blob(blob_name)
    return send_file(
        io.BytesIO(blob.readall()),
        download_name=blob_name.split("_", 1)[1],
        as_attachment=True
    )

# ------------------ RUN APP ---------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
