# **Audio Backend with FastAPI**

A backend application for audio processing and analysis, leveraging FastAPI, Essentia, and other Python libraries. This application includes APIs for rhythm analysis, melody extraction, and live audio recording. It generates insights such as BPM and MIDI files from uploaded or recorded audio.

---

## **Features**

- **Rhythm Analysis**: Detect beats per minute (BPM) and rhythm-related features from audio files.
- **Melody Extraction**: Extract predominant melody from audio and convert it to a MIDI file.
- **Live Audio Recording**: Record live audio and analyze its melody.
- **MIDI File Generation**: Convert extracted melody into a MIDI file for further use.

---

## **Technologies Used**

- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework for building APIs.
- **[Essentia](https://essentia.upf.edu/)**: Library for audio analysis and processing.
- **[Sounddevice](https://python-sounddevice.readthedocs.io/)**: Library for audio recording.
- **[Scipy](https://scipy.org/)**: Used for saving audio files.
- **[Mido](https://mido.readthedocs.io/)**: Library for working with MIDI files.

---

## **Getting Started**

### **Prerequisites**

Ensure you have the following installed:

- Python 3.9+
- Virtual environment (optional but recommended)
- Essentia dependencies (see their [installation guide](https://essentia.upf.edu/installing.html))

---

### **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kashish18/audio-apis-backend.git
   cd audio-apis-backend
   ```

2. **Set up the virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Essentia (if not already installed):**

   Follow [Essentia's installation instructions](https://essentia.upf.edu/installing.html).

---

### **Run the Application**

1. **Start the FastAPI server:**

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API documentation:**

   Open your browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive Swagger UI.



[//]: # (## **API Endpoints**)

[//]: # ()
[//]: # (### **1. Analyze Rhythm**)

[//]: # (   - **Endpoint**: `/analyze/rhythm/`)

[//]: # (   - **Method**: `POST`)

[//]: # (   - **Description**: Upload an audio file to detect BPM.)

[//]: # (   - **Request**: File upload.)

[//]: # (   - **Response**: JSON with detected BPM.)

[//]: # ()
[//]: # (### **2. Record and Analyze Melody**)

[//]: # (   - **Endpoint**: `/record_and_analyze_melody/`)

[//]: # (   - **Method**: `POST`)

[//]: # (   - **Description**: Record live audio and analyze its melody, generating a MIDI file.)

[//]: # (   - **Response**: JSON indicating melody extraction and MIDI file generation.)

---

## **Contributing**

Contributions are welcome! Feel free to submit issues, fork the repository, or create pull requests.

---

## **License**

This project is licensed under the [MIT License](LICENSE).

---

## **Acknowledgements**

- [Essentia](https://essentia.upf.edu/) for advanced audio analysis tools.
- [FastAPI](https://fastapi.tiangolo.com/) for building modern APIs effortlessly.

---