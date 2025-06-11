import os
import json
from datetime import datetime
import random
from groq import Groq


class ContentGenerator:
    def __init__(self):
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        if not self.groq_api_key:
            raise EnvironmentError("GROQ_API_KEY environment variable not set.")
        self.groq_client = Groq(api_key=self.groq_api_key)
        self.topics = self.load_health_topics()

    def load_health_topics(self):
        try:
            with open('assets/health_topics.json', 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Could not load topics from JSON: {e}")
            return [
                "spinach", "kale", "broccoli", "carrots", "blueberries",
                "avocado", "sweet_potato", "quinoa", "salmon", "almonds",
                "walnuts", "chia_seeds", "flax_seeds", "green_tea", "turmeric"
            ]

    def get_todays_topic(self):
        day_of_year = datetime.now().timetuple().tm_yday
        return self.topics[day_of_year % len(self.topics)]

    def generate_script(self, topic=None):
        if not topic:
            topic = self.get_todays_topic()

        prompt = f"""Write a compelling 250-word health video script about {topic}.

Structure:
- Hook (first 15 seconds) - surprising fact or question
- 3 specific health benefits with brief explanations
- Simple way to incorporate into daily diet
- Strong call to action for engagement

Style: Conversational, enthusiastic, fact-based
Target: Health-conscious audience
Length: Exactly 2-3 minutes when spoken

Make it engaging and monetizable for YouTube."""

        try:
            response = self.groq_client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=400
            )
            script = response.choices[0].message.content
            return script.strip(), topic

        except Exception as e:
            print(f"⚠️ Groq API error: {e}. Using fallback script.")
            return self.get_fallback_script(topic), topic

    def get_fallback_script(self, topic):
        return f"""Did you know that {topic} is one of nature's most powerful superfoods?

Today, I'm sharing three incredible health benefits that will make you want to add {topic} to your daily routine immediately.

First, {topic} is packed with essential vitamins and minerals that boost your immune system naturally. Just a small serving provides significant nutrition your body craves.

Second, studies show {topic} contains powerful antioxidants that fight inflammation and protect your cells from damage, potentially slowing the aging process.

Third, {topic} supports heart health by helping regulate cholesterol levels and improving blood circulation throughout your body.

The best part? You can easily add {topic} to smoothies, salads, or eat it as a healthy snack. Try incorporating it into your meals for just one week and notice the difference in your energy levels.

What's your favorite way to enjoy {topic}? Share your tips in the comments below, and don't forget to subscribe for more daily health secrets that actually work!"""

    def create_image_prompts(self, script, topic):
        base_style = "scroll painting of chrysanthemums in background, ink wash style --v 7q, traditional Chinese art, watercolor, serene, elegant"

        return [
            f"Fresh {topic} beautifully arranged, {base_style}, minimalist composition",
            f"Health benefits of {topic} illustrated as artistic infographic, {base_style}, clean design",
            f"{topic} in natural setting with soft lighting, {base_style}, peaceful atmosphere",
            f"Person enjoying {topic} in healthy lifestyle context, {base_style}, wellness theme"
        ]

    def generate_youtube_metadata(self, topic):
        titles = [
            f"5 Amazing {topic.title()} Benefits That Will Shock You!",
            f"Eat {topic.title()} Daily and See What Happens to Your Body",
            f"Why {topic.title()} is Nature's Most Powerful Superfood",
            f"The {topic.title()} Secret That Doctors Don't Want You to Know",
            f"What Happens When You Eat {topic.title()} Every Day for 30 Days"
        ]
        title = random.choice(titles)

        description = f"""🌿 Discover the incredible health benefits of {topic}!

In this video, you'll learn why {topic} should be part of your daily nutrition routine.

⏰ TIMESTAMPS:
00:00 - Introduction
00:30 - Health Benefit #1  
01:00 - Health Benefit #2
01:30 - Health Benefit #3
02:00 - How to Add to Your Diet
02:30 - Conclusion & Call to Action

🔔 SUBSCRIBE for daily health tips that actually work!
👍 LIKE if you found this helpful!
💬 COMMENT your favorite way to enjoy {topic}!

🏷️ RELATED VIDEOS:
- Top 10 Superfoods for Better Health
- Daily Nutrition Tips for Busy People  
- Natural Ways to Boost Your Energy

#health #nutrition #{topic} #superfood #wellness #healthyeating #naturalmedicine #healthtips #diet #healthylifestyle

⚠️ Disclaimer: This content is for educational purposes only and should not replace professional medical advice."""

        tags = [
            "health", "nutrition", f"{topic}", "superfood", "wellness",
            "healthy eating", "natural health", "diet tips", "healthy lifestyle",
            "natural medicine", "health benefits", "daily nutrition",
            "immune system", "antioxidants", "vitamins", "minerals"
        ]

        return title, description, tags
