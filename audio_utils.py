import essentia.standard as es
import mido
import os
import sounddevice as sd
from scipy.io.wavfile import write

def extract_rhythm(file_path: str):
    """
    Extract rhythm features including BPM from an audio file.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        float: Beats per minute (BPM) of the audio.
    """
    print(f"Extracting rhythm for file: {file_path}")
    try:
        # Load the audio file as mono.
        audio = es.MonoLoader(filename=file_path)()
        print("Audio loaded successfully for rhythm extraction.")

        # Use the RhythmExtractor2013 algorithm to detect BPM and beat-related features.
        rhythm_extractor = es.RhythmExtractor2013(method="multifeature")
        bpm, beats, beats_confidence, _, beats_intervals = rhythm_extractor(audio)
        print(f"BPM detected: {bpm:.2f}")
        print(f"Beats confidence: {beats_confidence}")
        return bpm
    except Exception as e:
        print(f"Error extracting rhythm: {e}")
        return None


def extract_melody(file_path: str):
    """
    Extract the melody from an audio file and convert it to a MIDI file.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        mido.MidiFile: Generated MIDI file object.
    """
    print(f"Extracting melody for file: {file_path}")
    try:
        # Load the audio file for melody extraction.
        loader = es.EqloudLoader(filename=file_path, sampleRate=44100)
        audio = loader()
        print("Audio loaded successfully for melody extraction.")

        # Extract predominant pitch using the Melodia algorithm.
        pitch_extractor = es.PredominantPitchMelodia(frameSize=2048, hopSize=128)
        pitch_values, pitch_confidence = pitch_extractor(audio)
        print("Pitch extraction complete.")

        # Segment pitch contours into notes.
        onsets, durations, notes = es.PitchContourSegmentation(hopSize=128)(pitch_values, audio)
        print(f"MIDI notes: {notes}")

        # Convert extracted notes into a MIDI file.
        BPM = extract_rhythm(file_path) or 120  # Default to 120 BPM if rhythm extraction fails.
        PPQ = 96  # Pulses per quarter note.
        tempo = mido.bpm2tempo(BPM)  # Convert BPM to microseconds per beat.

        # Create MIDI object and track.
        mid = mido.MidiFile()
        track = mido.MidiTrack()
        mid.tracks.append(track)
        print("Building MIDI file...")

        offsets = onsets + durations
        silence_durations = list(onsets[1:] - offsets[:-1]) + [0]

        for note, onset, duration, silence_duration in zip(list(notes), list(onsets), list(durations),
                                                           silence_durations):
            track.append(mido.Message('note_on', note=int(note), velocity=64,
                                      time=int(mido.second2tick(duration, PPQ, tempo))))
            track.append(mido.Message('note_off', note=int(note),
                                      time=int(mido.second2tick(silence_duration, PPQ, tempo))))

        # Save the MIDI file.
        midi_file = os.path.join("output", "extracted_melody.mid")
        os.makedirs(os.path.dirname(midi_file), exist_ok=True)
        mid.save(midi_file)
        print(f"MIDI file saved to: {midi_file}")
        return mid
    except Exception as e:
        print(f"Error extracting melody: {e}")
        return None


def record_audio(output_file: str, duration: int = 10, sample_rate: int = 44100, channels: int = 1):
    """
    Record live audio and save it as a .wav file.

    Args:
        output_file (str): Path to save the recorded audio file.
        duration (int): Duration of the recording in seconds.
        sample_rate (int): Sampling rate in Hz.
        channels (int): Number of audio channels.

    Returns:
        None
    """
    print(f"Starting audio recording for {duration} seconds...")
    try:
        # Record audio using sounddevice.
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='int16')
        sd.wait()  # Wait for recording to finish.
        write(output_file, sample_rate, audio_data)  # Save the recorded audio as a .wav file.
        print(f"Audio recording saved to: {output_file}")
    except Exception as e:
        print(f"Error during audio recording: {e}")