#%%
import pickle
import numpy as np
from mido import Message, MidiFile, MidiTrack, MetaMessage
import pygame
import threading
import random

#%% Read the healthy controls pickle file
# Replace 'your_pickle_file.pkl' with the path to your pickle file
pickle_file_path = 'datasets/healthy controls/3254439c-d1f0-4866-b20f-eb19bc9d5d69_heart_rate.pickle'

# Open the pickle file in binary read mode
with open(pickle_file_path, 'rb') as file:
    data = pickle.load(file)

# Print the content of the pickle file
print(data)

hr = data['value'].mean()

# Print the hr value as a whole number
print(f"Average Heart rate (hr): {hr:.2f}")

#%% Generate MIDI music based on hr as tempo
# Create a new MIDI file and track
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Set the tempo based on hr (microseconds per beat)
tempo = int(60_000_000 / hr)

# Add tempo meta message
track.append(MetaMessage('set_tempo', tempo=tempo))

# Define the notes for "Jingle Bells"
jingle_bells_notes = [
    (64, 240), (64, 240), (64, 480), (64, 240), (64, 240), (64, 480), (64, 240), (67, 240), (60, 240), (62, 240), (64, 960),  # Jingle bells, jingle bells, jingle all the way
    (65, 240), (65, 240), (65, 240), (65, 240), (65, 240), (64, 240), (64, 240), (64, 240), (64, 240), (64, 240), (62, 240), (62, 240), (64, 240), (62, 480), (67, 480)  # Oh what fun it is to ride in a one-horse open sleigh
]

# Define random major scale piano notes (C major scale) using only crotchets (quarter notes)
major_scale_notes = [(random.choice([60, 62, 64, 65, 67, 69, 71, 72]), 480) for _ in range(50)]

# Define "Twinkle Twinkle Little Star" notes
twinkle_twinkle_notes = [
    (60, 480), (60, 480), (67, 480), (67, 480), (69, 480), (69, 480), (67, 960),  # C C G G A A G
    (65, 480), (65, 480), (64, 480), (64, 480), (62, 480), (62, 480), (60, 960),  # F F E E D D C
    (67, 480), (67, 480), (65, 480), (65, 480), (64, 480), (64, 480), (62, 960),  # G G F F E E D
    (67, 480), (67, 480), (65, 480), (65, 480), (64, 480), (64, 480), (62, 960),  # G G F F E E D
    (60, 480), (60, 480), (67, 480), (67, 480), (69, 480), (69, 480), (67, 960),  # C C G G A A G
    (65, 480), (65, 480), (64, 480), (64, 480), (62, 480), (62, 480), (60, 960)   # F F E E D D C
]

# Ask the user to choose the music
music_choice = input("Choose the music (1 for 'Jingle Bells', 2 for 'Twinkle Twinkle Little Star', 3 for 'Random Major Scale Piano Notes'): ").strip()

if music_choice == '1':
    notes = jingle_bells_notes
elif music_choice == '2':
    notes = twinkle_twinkle_notes
elif music_choice == '3':
    notes = major_scale_notes
else:
    print("Invalid choice. Defaulting to 'Jingle Bells'.")
    notes = jingle_bells_notes

# Add notes to the track
for note, duration in notes:
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=duration))

# Save the MIDI file
output_file_path = 'output_music.mid'
midi.save(output_file_path)

print(f"MIDI music generated and saved to {output_file_path}")

#%% Play the generated MIDI file
# Initialize pygame mixer
pygame.mixer.init()

# Load the MIDI file
pygame.mixer.music.load(output_file_path)

# Play the MIDI file in a loop indefinitely
pygame.mixer.music.play(loops=-1)  # -1 means the music will loop indefinitely

running = True
try:
    while running:
        # Check for user input
        if input("Type 'stop' to stop the music: ").strip().lower() == 'stop':
            running = False
except KeyboardInterrupt:
    print("Playback interrupted by user")

# Stop the music if interrupted
pygame.mixer.music.stop()

print("MIDI music playback finished")
#%%
