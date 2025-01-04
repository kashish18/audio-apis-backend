from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from audio_utils import extract_rhythm, extract_melody, record_audio
import shutil
import os

# Initialize the FastAPI app
app = FastAPI()

# Define allowed origins for CORS
origins = [
    "http://localhost:3000",  # Adjust this based on the frontend's origin
]

# Add CORS middleware to allow communication between frontend and backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory to store uploaded audio files
UPLOAD_DIR = "test_audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/analyze/rhythm/")
async def extract_rhythm_endpoint(file: UploadFile = File(...)):
    """
    API endpoint to extract rhythm and BPM from an uploaded audio file.

    Args:
        file (UploadFile): Uploaded audio file.

    Returns:
        dict: Detected BPM.
    """
    print(f"Received file for rhythm analysis: {file.filename}")
    try:
        # Save the uploaded file to the server
        file_path = f"{UPLOAD_DIR}/{file.filename}"
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        print(f"File saved to {file_path}")

        # Extract rhythm and BPM
        print("Starting rhythm analysis...")
        bpm = extract_rhythm(file_path)
        print(f"Rhythm analysis complete. BPM: {bpm}")

        # Return the result
        return {"bpm": bpm}
    except Exception as e:
        print(f"Error extracting rhythm: {e}")
        return {"error": str(e)}

@app.post("/record_and_analyze_melody/")
async def record_and_analyze_melody():
    """
    API endpoint to record live audio and analyze its melody.

    Returns:
        dict: Generated MIDI file information.
    """
    print("Starting live audio recording...")
    try:
        # Record live audio
        output_file = "recorded_audio.wav"
        record_audio(output_file)
        print(f"Audio recording complete. File saved to {output_file}")

        # Extract melody from the recorded audio
        print("Starting melody extraction...")
        melody = extract_melody(output_file)
        print("Melody extraction complete.")

        # Return the result
        return {"melody": "Melody extracted and MIDI file created."}
    except Exception as e:
        print(f"Error during melody recording or extraction: {e}")
        return {"error": str(e)}
