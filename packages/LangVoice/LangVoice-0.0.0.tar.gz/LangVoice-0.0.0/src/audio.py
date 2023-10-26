"""LangSpeak
"""

 # Example filename: deepgram_test.py
from deepgram import Deepgram
import asyncio
import aiohttp
import sounddevice as sd
from scipy.io.wavfile import write

# Your Deepgram API Key
DEEPGRAM_API_KEY = "937daf2b07523b58979ff495b9aaa17bfbf5f4f2"

# Record audio from the browser's microphone
filename = 'output.wav'

print("Recording")
# Use the MediaRecorder API to record audio from the browser's microphone
"""
<script>
navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    const audioChunks = [];
    mediaRecorder.addEventListener("dataavailable", event => {
      audioChunks.push(event.data);
    });

    mediaRecorder.addEventListener("stop", () => {
      const audioBlob = new Blob(audioChunks);
      const audioUrl = URL.createObjectURL(audioBlob);
      const audio = new Audio(audioUrl);
      const link = document.createElement('a');
      link.href = audioUrl;
      link.download = 'output.wav';
      link.click();
    });

    setTimeout(() => {
      mediaRecorder.stop();
    }, 3000);
  });
</script>
"""
print("Recording saved in output.wav")

async def main():
  # Initialize the Deepgram SDK
  deepgram = Deepgram(DEEPGRAM_API_KEY)

  # Create a websocket connection to Deepgram
  # In this example, punctuation is turned on, interim results are turned off, and language is set to UK English.
  try:
    deepgramLive = await deepgram.transcription.live({
      'smart_format': True,
      'interim_results': False,
      'language': 'en-US',
      'model': 'nova',
    })
  except Exception as e:
    print(f'Could not open socket: {e}')
    return

  # Listen for the connection to close
  deepgramLive.registerHandler(deepgramLive.event.CLOSE, lambda c: print(f'Connection closed with code {c}.'))

  # Listen for any transcripts received from Deepgram and write them to the console
  deepgramLive.registerHandler(deepgramLive.event.TRANSCRIPT_RECEIVED, print)

  # Send the recorded audio to Deepgram
  with open(filename, 'rb') as audio:
    while True:
      data = audio.read(1024)
      deepgramLive.send(data)

      # If no data is being sent from the live stream, then break out of the loop.
      if not data:
          break

  # Indicate that we've finished sending data by sending the customary zero-byte message to the Deepgram streaming endpoint, and wait until we get back the final summary metadata object
  await deepgramLive.finish()

# If running in a Jupyter notebook, Jupyter is already running an event loop, so run main with this line instead:
#await main()
asyncio.run(main())
