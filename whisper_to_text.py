# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 14:45:41 2025

@author: yusuk
"""

#起動前に音声をアップロードすること
#for google colab google colabで起動しないと上手く動作しません

!pip install git+https://github.com/openai/whisper.git

import whisper

# Load the Whisper model
model = whisper.load_model("medium") # You can choose other models like "small", "medium", "large"

# Transcribe the audio file
result = model.transcribe(R"/content/Tue_2_L2.mp3") # Replace "audio.mp3" with your audio file

# Print the transcribed text
print(result["text"])