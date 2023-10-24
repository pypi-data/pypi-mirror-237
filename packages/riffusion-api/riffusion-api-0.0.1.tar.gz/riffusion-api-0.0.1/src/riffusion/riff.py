import requests
import json
import base64
import os
from moviepy.editor import AudioFileClip, ImageClip
def sing(lyrics, style):
  url = "https://www.riffusion.com/api/trpc/openai.generateTextVariations"
  lyrics = lyrics
  style = style
  payload = json.dumps({
    "json": {
      "text": style,
      "user_id": "9af56c0b-4690-4136-9d92-dae8e5a9f5c5",
      "is_augment_prompt": True,
      "lyrics": lyrics,
      "is_public": True
    }
  })
  headers = {
    'authority': 'www.riffusion.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': '_ga=GA1.1.1674763534.1697854360; supabase-auth-token=%5B%22eyJhbGciOiJIUzI1NiIsImtpZCI6Ikw0RGdDdUNuOHEvNXFMYm4iLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjk4NDU5MTYxLCJpYXQiOjE2OTc4NTQzNjEsImlzcyI6Imh0dHBzOi8vaGd0cHp1a2V6b2R4cmdtZmhsdnkuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6IjlhZjU2YzBiLTQ2OTAtNDEzNi05ZDkyLWRhZThlNWE5ZjVjNSIsImVtYWlsIjoidGhlbWFnaWNtYW4xMTJAZ21haWwuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJnb29nbGUiLCJwcm92aWRlcnMiOlsiZ29vZ2xlIl19LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NKME1HV2ZoMTlqVHVsOGhNQnVGUmZEMmVvRlpuQ0hfekppSEVZMHdYZmI3Zz1zOTYtYyIsImVtYWlsIjoidGhlbWFnaWNtYW4xMTJAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZ1bGxfbmFtZSI6IkplZmZtYW4xMTIiLCJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYW1lIjoiSmVmZm1hbjExMiIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NKME1HV2ZoMTlqVHVsOGhNQnVGUmZEMmVvRlpuQ0hfekppSEVZMHdYZmI3Zz1zOTYtYyIsInByb3ZpZGVyX2lkIjoiMTE2NTc0MjExNTk5NzE2MzQyMTQyIiwic3ViIjoiMTE2NTc0MjExNTk5NzE2MzQyMTQyIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib2F1dGgiLCJ0aW1lc3RhbXAiOjE2OTc4NTQzNjF9XSwic2Vzc2lvbl9pZCI6IjMzYjU2MjNmLTNiYzEtNGRmMy04YTZiLTkxZTgzOGVlZDg1NSJ9.yM-Q6oc5HR7I-1nUWjJmC1CrCA-iOI2za-r1yQLmo-E%22%2C%22-RGdsFa4_x0gKxDAawdxsQ%22%2C%22ya29.a0AfB_byC7S3simIgLV6QDUMJbaTD6lV7xRENgh_givybTsZQNrPrE03O95VXAc-_wThTvl4bYlJQmZVd72yTUDQTdK0iNn8efW7kpH4899s1IsLqBItZQqbs8GpyqqHNGWEigYyWcd3pPJyi-gmM0MHN3XWgw8PYI5XoaCgYKARgSARESFQGOcNnCh9ydUhgf4yP75Ps82qRV7w0170%22%2Cnull%2Cnull%5D; _ga_19PFVFCT8N=GS1.1.1697854359.1.1.1697854364.0.0.0; _dd_s=rum=0&expire=1697855282928',
    'origin': 'https://www.riffusion.com',
    'referer': 'https://www.riffusion.com/create',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  if response.status_code == 200:
      parsed_data = json.loads(response.text)

      group_id = parsed_data["result"]["data"]["json"]["group_id"]

      outputs = parsed_data["result"]["data"]["json"]["outputs"]
      ids = [item["id"] for item in outputs]
      visuals = [item["visual"] for item in outputs]
      audio_variations = [item["variation"] for item in outputs]

  else:
      print(f"Request failed with status code: {response.status_code}")


  url = "https://www.riffusion.com/api/trpc/inference.textToAudioBatch"

  payload = json.dumps({
    "json": {
      "group_id": group_id,
      "prompts": [
        style,
        style,
        style
      ],
      "audio_variations": [
        audio_variations[0],
        audio_variations[1],
        audio_variations[2]
      ],
      "visual_prompts": [
        visuals[0],
        visuals[1],
        visuals[2]
      ],
      "lyrics": [
        lyrics,
        lyrics,
        lyrics
      ],
      "seeds": [
        None,
        None,
        None
      ],
      "ids": [
        ids[0],
        ids[1],
        ids[2]
      ],
      "title": "Title Here",
      "is_public": False,
      "interpolate_for_remix": False
    },
    "meta": {
      "values": {
        "seeds.0": [
          "undefined"
        ],
        "seeds.1": [
          "undefined"
        ],
        "seeds.2": [
          "undefined"
        ]
      }
    }
  })

  response = requests.request("POST", url, headers=headers, data=payload)

  if response.status_code == 200:
      parsed_data = json.loads(response.text)

      json_data = parsed_data.get("result", {}).get("data", {}).get("json", {})
      predictions = json_data.get("predictions", [])

      for index, item in enumerate(predictions):
          audio_bytes = base64.b64decode(item.get("audio", "").split(",")[-1])

          filename = f"{item['key']}.mp3"

          with open(filename, "wb") as file:
              file.write(audio_bytes)
  else:
      print(f"Request failed with status code: {response.status_code}")
  url = "https://www.riffusion.com/api/trpc/inference.textToImageBatch"

  payload = json.dumps({
    "json": {
      "group_id": group_id,
      "prompts": [
        visuals[0],
        visuals[1],
        visuals[2]
      ],
      "ids": [
        ids[0],
        ids[1],
        ids[2]
      ]
    }
  })
  response = requests.request("POST", url, headers=headers, data=payload)

  if response.status_code == 200:
      parsed_data = json.loads(response.text)

      json_data = parsed_data.get("result", {}).get("data", {}).get("json", {})
      predictions = json_data.get("predictions", [])

      for index, item in enumerate(predictions):
          image_bytes = base64.b64decode(item.get("image", "").split(",")[-1])

          filename = f"{item['key']}.jpeg"

          with open(filename, "wb") as file:
              file.write(image_bytes)

  else:
      print(f"Request failed with status code: {response.status_code}")
  mp3_files = [file for file in os.listdir() if file.endswith('.mp3')]
  mp4_files = [file for file in os.listdir() if file.endswith('.mp4')]
  for mp4_filename in mp4_files:
      os.remove(mp4_filename)
      
  for mp3_filename in mp3_files:
        image_filename = mp3_filename.replace('.mp3', '.jpeg')
        mp4_filename = mp3_filename.replace('.mp3', '.mp4')

        if os.path.isfile(image_filename):
            audio = AudioFileClip(mp3_filename)
            image = ImageClip(image_filename, duration=audio.duration)
            video = image.set_audio(audio)
            video.write_videofile(mp4_filename, codec="libx264", audio_codec="aac", threads=4, preset="ultrafast", fps=24, verbose=False, logger=None)
            os.remove(mp3_filename)
            os.remove(image_filename)
            print(f"Saved video as {mp4_filename}")