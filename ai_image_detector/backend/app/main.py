from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
import torch

from fastapi.middleware.cors import CORSMiddleware

from app.model.preprocess import preprocess_image
from app.model.model import HybridModel
from app.schemas.prediction import PredictionResponse

# Initializes the FastAPI web server
app = FastAPI()

# Configures Cross-Origin Resource Sharing (CORS) to allow 
# your React frontend to communicate with this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Device
# -----------------------------
# Checks if a high-performance GPU (CUDA) is available, 
# otherwise defaults to using the computer's CPU.
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -----------------------------
# Global model variable
# -----------------------------
model = None


# -----------------------------
# Load model at startup
# -----------------------------
# Automatically loads the pre-trained AI weights into memory 
# when the server first starts up so it's ready for requests.
@app.on_event("startup")
def load_model():
    global model

    model = HybridModel().to(DEVICE)

    model.load_state_dict(
        torch.load(
            "app/model/best_model_dm_detect.pth",
            map_location=DEVICE
        )
    )

    model.eval()

    print("✅ Model loaded successfully")


# A simple health-check route to confirm the server is running.
@app.get("/")
def root():
    return {"message": "FastAPI is working"}

# The main API endpoint that receives an image file, processes it, 
# runs the AI prediction, and returns the final verdict.
@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    # Read the file sent from the browser and open it as an image
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # Pass the image to the preprocessing logic (File 2)
    spatial, freq = preprocess_image(image)

    spatial = spatial.to(DEVICE)
    freq = freq.to(DEVICE)

    # Perform the AI inference without calculating gradients (saves memory)
    with torch.no_grad():
        # sigmoid turns the raw model output into a probability (0 to 1)
        output = torch.sigmoid(model(spatial, freq))
        score = output.item()

    # Determine label based on a 50% confidence threshold
    label = "AI-generated" if score > 0.5 else "Real"
    print("Raw score:", score)
    return {
        "filename": file.filename,
        "score": round(score, 4),
        "label": label
    }