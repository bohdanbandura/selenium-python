import sounddevice as sd
import numpy as np
import wavio

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options as chrome_options

# options = chrome_options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)

# driver.get("https://ukrmuz.net/239-dorofeeva-a-ia-vse-plakala.html")
# driver.get("https://soundcloud.com/balthazarband/bunker-vuurwerk-endless-summer-remix")

# driver.find_element(By.CSS_SELECTOR, 'button#onetrust-accept-btn-handler').click()
# driver.find_element(By.CSS_SELECTOR, 'span[title="Слухати музику онлайн"]').click()

# driver.find_element(By.CSS_SELECTOR, '.fullHero__title .playButton').click()

# Get the default system playback device (15 Stereo Mix (Realtek HD Audio Stereo input), Windows WDM-KS (2 in, 0 out))
# default_device = 21

# Print the list of available devices
print(sd.query_devices()) 

# Define the duration of the recording in seconds
# duration = 20 

# Define the sampling frequency and number of channels
# fs = 44100
# fs = 48000
# channels = 2

# Record audio from the default system playback device
# print("Recording audio from system playback device...")
# recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype=np.int16, device=default_device)
# sd.wait()  # Wait until recording is finished

# # Save the recording to a wav/mp3 file
# filename = "recorded_audio.mp3" 
# print(f"Saving recording to {filename}...")
# wavio.write(filename, recording, fs, sampwidth=2)

# print("Recording saved successfully.")

# driver.quit()
