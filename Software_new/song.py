import os
import random
import pygame

playlist_directory = "Playlist"

pygame.init()

playlist = []

song_files = os.listdir(playlist_directory)

for song_file in song_files:
    # Create the full path to the song file
    song_path = os.path.join(playlist_directory, song_file)
    playlist.append(song_path)

# Randomly shuffle the playlist
random.shuffle(playlist)

# Play the first song in the shuffled playlist
current_song_index = 0
pygame.mixer.music.load(playlist[current_song_index])
pygame.mixer.music.play()

# Print the current song name
print("Now playing:", os.path.basename(playlist[current_song_index]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Pause on 'p' key press
                pygame.mixer.music.pause()
                print("Paused")
            elif event.key == pygame.K_r:  # Resume on 'r' key press
                pygame.mixer.music.unpause()
                print("Resumed")
            elif event.key == pygame.K_q:  # Exit on 'q' key press
                # Stop the current song
                pygame.mixer.music.stop()

                # Quit pygame and exit the program
                pygame.quit()
                exit()

    # Check for user input in the terminal
    user_input = input("Enter command (n to skip to next song, p to pause, r to resume, q to quit): ")
    if user_input.lower() == "n":
        # Stop the current song
        pygame.mixer.music.stop()

        # Increment the current song index
        current_song_index += 1

        # Check if reached the end of the playlist
        if current_song_index >= len(playlist):
            # Restart the playlist from the beginning
            current_song_index = 0

        # Load and play the next song
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play()

        # Print the current song name
        print("Now playing:", os.path.basename(playlist[current_song_index]))

    elif user_input.lower() == "p":
        # Pause the current song
        pygame.mixer.music.pause()
        print("Paused")

    elif user_input.lower() == "r":
        # Resume the current song
        pygame.mixer.music.unpause()
        print("Resumed")

    elif user_input.lower() == "q":
        # Stop the current song
        pygame.mixer.music.stop()

        # Quit pygame and exit the program
        pygame.quit()
        exit()

