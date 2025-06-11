# content_generator.py
import os
import requests
import time


def generate_script_and_prompts(topic):
    prompt = f"""
    Write a 250-word engaging YouTube script about {topic}.
    Include: a hook, 3 health benefits, how to consume, and a call to action.
    Make it suitable for a 2-minute video.
    """
    script = call_groq_api(prompt)

    image_prompts = [
        f"{topic} beautifully illustrated in traditional Chinese scroll painting, ink wash style --v 7q",
        f"Health benefits of {topic} shown as serene infographic in ink wash style with chrysanthemums --v 7q",
        f"Person consuming {topic} in natural scene, Chinese watercolor style, scroll background --v 7q"
    ]
    return script.strip(), image_prompts


def call_groq_api(user_prompt, max_retries=3, delay=5):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set.")

    url = "https://api.groq.com/openai/v1/chat/completions" 
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [{"role": "user", "content": user_prompt}],
        "temperature": 0.7
    }

    for attempt in range(max_retries):
        try:
            print(f"📡 Attempt {attempt + 1} to call Groq API...")
            res = requests.post(url, headers=headers, json=data, timeout=30)
            print(f"📥 Response Status Code: {res.status_code}")
            print(f"📥 Response Body: {res.text}")

            if res.status_code == 200:
                return res.json()["choices"][0]["message"]["content"]
            else:
                print(f"❌ API Error: {res.status_code}, {res.text}")
                if res.status_code == 429:
                    print("⚠️ Rate limited. Retrying after delay...")
                    time.sleep(delay)
                else:
                    break
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Network error: {e}. Retrying...")
            time.sleep(delay)

    raise RuntimeError("Failed to get valid response from Groq API.")
