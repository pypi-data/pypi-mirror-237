import requests


def check_endpoint(owner: str, endpoint: str, beta=False):
  """Checks to see if the endpoint is valid. Takes `owner`, `endpoint`, and `beta`. Returns Boolean. For example, `check_endpoint(owner = "openai", endpoint = "/chat/completions", beta = False) would return `True`"""
  # beta = True (Needed when Beta needed to be forced!)
  try:
    r = requests.get(
      f"https://{'beta.' if beta == True else ''}purgpt.xyz/models").text
  except :
    return False
  #print(f"/{owner}/{endpoint}".replace("//", "/"))
  if f"/{owner}/{endpoint}".replace("//", "/") in r:
    return True
  else:
    return False

def check_model(owner: str, endpoint: str, model: str, beta=False):
  """Checks to see if the endpoint is valid. Takes `owner`, `endpoint`, and `beta`. Returns Boolean. For example, `check_model(owner = "openai", model, endpoint = "/chat/completions", beta = False) would return `True`"""
  # beta = True (Needed when Beta needed to be forced!)
  try:
    r = requests.get(
      f"https://{'beta.' if beta == True else ''}purgpt.xyz/models").json()
  except :
    return False
  #print(f"/{owner}/{endpoint}".replace("//", "/"))
  for i in r:
    if i["id"] == model:
      if f"/{owner}/{endpoint}".replace("//", "/") in i["endpoints"]:
        return True

  return False

class PurGPT:

  def __init__(self, token: str, dev=False):
    """Initializes the PurGPT class. Takes `token` and `dev`. If `dev` is True, the package will return the full body json from the request. If `dev` is False, the package will return just the important stuff or an error."""
    self.dev = dev
    self.token = token

  def test(self):
    """Test the API"""
    response = requests.post("https://purgpt.xyz/openai/chat/completions",
                             headers={
                                 "Content-Type": "application/json",
                                 "Authorization": f"Bearer {self.token}"
                             },
                             json={
                                 "messages": [{
                                     "role": "user",
                                     "content": "Tell me a joke about how this request returned a 200"
                                 }],
                                 "model":
                                 "gpt-3.5-turbo-16k"
                             })
    if self.dev == True:
      try:
        return response.json()
      except:
        return {"error": "An unknown error occurred." + response.text}
    try:
      respond = response.json()["choices"][0]["message"]["content"]
    except:
      try:
        respond = response.json()["error"]
      except:
        return response.text
    return respond

  def generate(self, prompt: str, model = "gpt-3.5-turbo-16k", provider="openai", beta=False):
    """
  LAZY WAY! Quick and easy way to generate individual text. Pass your prompt (str), model (OPTIONAL st, see the docs for all **completion** models), provider (OPTIONAL str, see the docs for all **completion** providers, defaults to gpt-3.5-turbo-16k), beta (bool, defaults to False). Returns a string with the AI's answer or the error message. 
    """
    if not check_model(owner=provider, endpoint="/chat/completions", model = model, beta = beta):
      return "Invalid endpoint/owner. Please check the full [list](https://purgpt.xyz/models) of availible models/endpoints!"
    # beta = True (Needed when Beta needed to be forced!)
    response = requests.post(
        f"https://{'beta.' if beta == True else ''}purgpt.xyz/{provider}/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        },
        json={
            "messages": [{
                "role": "user",
                "content": f"{prompt}"
            }],
            "model": "gpt-3.5-turbo-16k"
        })
    if self.dev == True:
      try:
        return response.json()
      except:
        return {"error": "An unknown error occurred." + response.text}
    try:
      respond = response.json()["choices"][0]["message"]["content"]
    except:
      try:
        respond = response.json()["error"]
      except:
        return response.text
    return respond

  def chat(self, messages: list, provider="openai", model = "gpt-3.5-turbo-16k", beta=False):
    """
  Pass your prompt (str), token (str), provider (OPTIONAL str, see the docs for all providers), model (OPTIONAL st, see the docs for all **completion** models), beta (bool, defaults to False). Returns a list, argument 0 being the AI's answer or the error message, and argument 1 being the big, ~~bulky~~ json text that was recieved from . 
    """

    if provider == None:
      provider = "openai"
    if not check_model(owner=provider, endpoint="/chat/completions",model=model):
      return "Invalid endpoint/owner. Please check the full [list](https://purgpt.xyz/models) of availible models/endpoints!"
    # beta = True (Needed when Beta needed to be forced!)
    response = requests.post(
        f"https://{'beta.' if beta == True else ''}purgpt.xyz/{provider}/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        },
        json={
            "messages": messages,
            "model": model
        })
    if self.dev == True:
      try:
        return response.json()
      except:
        return {"error": "An unknown error occurred." + response.text}
    response = response.json()
    try:
      respond = response["choices"][0]["message"]["content"]
    except:
      try:
        respond = response["error"]
      except:
        try:
          respond = response['cache'][0]['response']['data']['error']
        except:
          respond = "There was an unexpected error. Printed error in console!"
          # print(response)
    return respond

  def document_analysis(self, document_url: str, prompt: str, beta=False):
    """
    Takes a URL in `document_url`, and a prompt in `prompt`. Returns a string. Example: `document_analysis(document_url = "https://http.cat/200", prompt = "What status code is being returned?")`
    Analyzing images and documents is an essential tool for any modern day app. With this tool, you can: 
    - Enhance searching through a library of images by analyzing each image with our AI and giving them specific tags,
    - Summarize PDFs easily, and quickly
    - Identify text in images
    - And so much more!
"""
    response = requests.post(
        f"https://{'beta.' if beta == True else ''}purgpt.xyz/hugging-face/documents/scan",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        },
        json={
            "document": document_url,
            "prompt": prompt
        })
    if self.dev == True:
      try:
        return response.json()
      except:
        return {"error": "An unknown error occurred." + response.text}
    try:
      respond = response.json()["choices"][0]["result"]["answer"]
    except:
      try:
        # print(response)
        respond = response.json()["error"]
      except:
        return response.text
    return respond

  def moderations(self, prompt: str, beta=False):
    """Takes in a string for `prompt` and a boolean for `beta`. Returns a list. 

Moderations are a vital tool for any messaging or social media app. Using moderations, one can scan text and find out if it includes certain NSFW categories, such as:

Sexual
Hate
Harassment
Self-harm
Sexual/minors
Hate/threatening
Violence/graphic
Self-harm/intent
Self-harm/instructions
Harassment/threatening
Violence"""
    response = requests.post(
        f"https://{'beta.' if beta == True else ''}purgpt.xyz/openai/moderations",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        },
        json={
            "model": "text-moderation-stable",
            "prompt": prompt
        })
    if self.dev == True:
      try:
        return response.json()
      except:
        return {"error": "An unknown error occurred." + response.text}
    try:
      respond = response.json()["results"]
    except:
      try:
        # print(response)
        respond = response.json()["error"]
      except:
        return response.text
    return respond

  def image(self, prompt: str, provider="openai", beta=False):
    """
  LAZY WAY! Quick and easy way to generate images. Pass your prompt (str), provider (OPTIONAL str, see the docs for all **image** providers! Defaults to `openai`), beta (bool, defaults to `True`). 
    """
    if not check_endpoint(owner=provider, endpoint="/images/generations"):
      return "Invalid endpoint/owner. Please check the full [list](https://purgpt.xyz/models) of availible models/endpoints!"
    # beta = True (Needed when Beta needed to be forced!)
    response = requests.post(
        f"https://{'beta.' if beta == True else ''}purgpt.xyz/{provider}/images/generations",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        },
        json={"prompt": prompt})
    if self.dev == True:
      try:
        return response.json()
      except:
        return {"error": "An unknown error ocurred." + response.text}
    try:
      respond = response.json()["data"][0]["url"]
    except:
      try:
        respond = response.json()["error"]
      except:
        return "Our API returned an error:" + response.text
    return respond

  def transcribe(self, file_url, beta=False):
    """Transcribe an audio file from it's URL (`file_url`)"""
    # beta = True (Needed when Beta needed to be forced!)
    response = requests.post(
        f"https://{'beta.' if beta == True else ''}purgpt.xyz/openai/audio/transcriptions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        },
        json={
  "file": file_url,
  "model": "whisper-1",
  "response_format": "json"
})
    if self.dev == True:
      try:
        return response.json()
      except:
        return {"error": "An unknown error occurred." + response.text}
    try:
      respond = response.json()["text"]
    except:
      try:
        # print(response)
        respond = response.json()["error"]
      except:
        return response.text
    return respond

  def translate(self, file_url: str, beta=False):
    """Translate an audio file from it's URL (`file_url`)"""
    # beta = True (Needed when Beta needed to be forced!)
    response = requests.post(
        f"https://{'beta.' if beta == True else ''}purgpt.xyz/openai/audio/transcriptions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        },
        json={
  "file": file_url,
  "model": "whisper-1",
  "response_format": "json"
})
    if self.dev == True:
      try:
        return response.json()
      except:
        return {"error": "An unknown error occurred." + response.text}
    try:
      respond = response.json()["text"]
    except:
      try:
        # print(response)
        respond = response.json()["error"]
      except:
        return response.text
    return respond

  def custom(self, owner: str, endpoint: str, body: dict, subdomain: str = None):
    """Use a custom endpoint provided by PurGPT not listed here. An example would be `custom(owner = "openai", endpoint = "/chat/completions, body = `{"messages": [{"role": "user","content": "Say \"PurGPT is the best!\""}],"model":"gpt-3.5-turbo-16k"}, subdomain = "beta")`"""
    if not check_endpoint(owner=owner, endpoint=endpoint):
      return "Invalid endpoint/owner. Please check the full [list](https://purgpt.xyz/models) of availible models/endpoints!"
    # beta = True (Needed when Beta needed to be forced!)
    response = requests.post(
        f"https://{subdomain}.purgpt.xyz/{owner}{endpoint}".replace("..","."),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        },
        json=body)
    return response.json()
  def other(self, full_url: str, body: dict, headers: dict):
    """Use a third-party endpoint. Ex: `other(full_url = "https://myai.com/chat", body: {"message": "this is an example"}, headers={"Content-Type":"application/json","Authorization":f"Bearer {token}"})`"""
    response = requests.post(
      full_url,
      headers=headers,
      json=body)
    return response
