import helpers
import llm
from prompts import youtube_prompts

selected_model = "gpt-3.5-turbo"
yt_url = "https://youtu.be/vN_6jfIoYE4?si=XqCX4R6eKGVvODP4"
video_transcript = helpers.get_video_transcript(yt_url)

prompt = youtube_prompts.youtube_to_points_summary.format(transcript=video_transcript)
response = llm.llm_generate_text_with_save(prompt, "OpenAI", selected_model)
print(response)