import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import threading
import time
import os
import whisper  

# Google credentials
EMAIL = "abc@gmail.com"
PASSWORD = "abcd"
MEET_LINK = "https://meet.google.com/abc"  

# Audio file path
OUTPUT_FILE = os.path.join(os.getcwd(), "meeting_audio5.wav")

# FFmpeg command for recording system audio
ffmpeg_command = [
    "ffmpeg",
    "-y",
    "-f", "dshow",
    "-i", "audio=CABLE Output (VB-Audio Virtual Cable)",  # Uses VB-Cable
    "-acodec", "pcm_s16le",
    "-ar", "44100",
    "-ac", "2",
    OUTPUT_FILE
]

def record_audio():
    print(" Starting system audio recording...")
    process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

# Chrome options
options = uc.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--use-fake-ui-for-media-stream")  # Auto-allow mic/cam

# Initialize driver
driver = uc.Chrome(options=options, headless=False)

try:
    # Login to Google
    print(" Logging in to Google...")
    driver.get("https://accounts.google.com/")

    wait = WebDriverWait(driver, 20)

    # Enter email
    email_field = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
    email_field.send_keys(EMAIL)
    email_field.send_keys(Keys.ENTER)
    print(" Email entered")
    time.sleep(3)

    # Enter password
    try:
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)
        print(" Password entered")
    except:
        print(" CAPTCHA or 2FA detected. Please solve manually.")
        input(" Press Enter after solving...")

    time.sleep(5)

    # Join Google Meet
    print(" Joining Google Meet...")
    driver.get(MEET_LINK)
    time.sleep(10)

    # Check if a name field is present (join as guest)
    try:
        name_field = driver.find_element(By.XPATH, '//input[@aria-label="Your name"]')
        name_field.clear()
        name_field.send_keys("Bot Recorder")
        print(" Entered name as guest")
        time.sleep(2)
    except:
        print(" No name field found (logged in user)")

    # Turn off mic and camera
    try:
        mic_button = driver.find_element(By.XPATH, '//div[@role="button" and @aria-label="Turn off microphone (CTRL + D)"]')
        mic_button.click()
        camera_button = driver.find_element(By.XPATH, '//div[@role="button" and @aria-label="Turn off camera (CTRL + E)"]')
        camera_button.click()
        print(" Mic and camera turned off")
    except:
        print(" Could not turn off mic/camera automatically")

    # Click "Join now" or "Ask to join"
    try:
        join_button = driver.find_element(By.XPATH, '//span[text()="Join now" or text()="Ask to join"]')
        join_button.click()
        print(" Successfully joined (or requested to join)!")
    except:
        print(" Could not find Join button")

    print(" Bot is in the meeting. Recording system audio...")
    recorder_process = record_audio()

    # Stay in the meeting for X minutes
    MEETING_DURATION_MINUTES = 5  
    time.sleep(MEETING_DURATION_MINUTES * 60)

finally:
    # Leave the meeting and stop recording
    print(" Exiting meeting and stopping recording...")
    driver.quit()
    recorder_process.terminate()
    print(f" Audio saved as {OUTPUT_FILE}")

    # Transcribe the saved audio
    print(" Transcribing audio...")
    model = whisper.load_model("base")  
    result = model.transcribe(OUTPUT_FILE)
    print(" Transcription:")
    print(result["text"])
