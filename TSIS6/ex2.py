import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Sample music files (replace with your own music files)
music_files = [r"C:\Users\user\Desktop\Pygame\TSIS6\Music1.mp3",
               r"C:\Users\user\Desktop\Pygame\TSIS6\Music2.mp3",
               r"C:\Users\user\Desktop\Pygame\TSIS6\Music3.mp3"]

current_track_index = 0
pygame.mixer.music.load(music_files[current_track_index])

# Create a basic GUI window
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Keyboard Music Player")

def play_music():
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    play_music()

def prev_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Check for keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # play/pause
                if pygame.mixer.music.get_busy():
                    pause_music()
                else:
                    play_music()
            elif event.key == pygame.K_n:  # 'N' next track
                next_track()
            elif event.key == pygame.K_b:  # 'B' previous track
                prev_track()
            elif event.key == pygame.K_q:  # 'Q' quit
                pygame.quit()
    pygame.display.flip()

pygame.quit()
