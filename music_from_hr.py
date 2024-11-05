#%%
import pickle
import librosa
import soundfile as sf

#%% Read the healthy controls pickle file
# Replace 'your_pickle_file.pkl' with the path to your pickle file
pickle_file_path = 'datasets/healthy controls/5f4888a8-4063-4044-bf39-b5b50b8111bb_heart_rate.pickle'

# Open the pickle file in binary read mode
with open(pickle_file_path, 'rb') as file:
    data = pickle.load(file)

# Print the content of the pickle file
print(data)

hr = data['value'].mean()

# Print the hr value as a whole number
print(f"Average Heart rate (hr): {hr:.2f}")

#%%
# Detect tempo of a music file
music_file_path = 'test/test-music.mp3'  # Replace with your music file path
y, sr = librosa.load(music_file_path)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

print(f"Detected tempo of the music: {tempo} BPM")

# Change the tempo of the music
new_tempo = hr  # Use heart rate as the new tempo
rate = new_tempo / tempo
y_changed = librosa.effects.time_stretch(y, rate)

# Save the modified music file
output_file_path = 'test/test-music-changed.mp3'
sf.write(output_file_path, y_changed, sr)

print(f"Changed the tempo of the music to {new_tempo} BPM and saved as '{output_file_path}'")

#%%

