# pip install gradio
import gradio as gr
from summarizer import summarize


# -----------------------------
# Sample text (replace with yours)
# -----------------------------
SAMPLES = {
    "🚀 Startup site": """
https://www.delhivery.com/
""",

    "📰 News article": """
https://www.thehindu.com/news/international/west-asia-conflict-iran-us-israel-war-strait-of-hormuz-live-updates-june-6-2026/article71068325.ece
""",

    "✍️ Personal blog": """
https://gkoberger.com/
"""
}


def load_sample(choice):
    return SAMPLES.get(choice, "")


def run_summary(text, personality):
    if not text.strip():
        return "⚠️ Paste some text or pick a sample first."

    prompt = f"""
    Personality: {personality}

    Summarize the following text in this style:

    {text}
    """

    return summarize(prompt)


# -----------------------------
# UI
# -----------------------------
theme = gr.themes.Soft(
    primary_hue="orange",
    secondary_hue="orange",
)

with gr.Blocks(theme=theme, title="AI Website Summarizer") as demo:

    gr.Markdown(
        """
        # 🔎 AI Website Summarizer
        """
    )

    with gr.Row():

        # ---------------- LEFT PANEL ----------------
        with gr.Column(scale=1):

            # gr.Markdown("### Pick a sample *website*")

            sample_choice = gr.Radio(
                choices=[
                    "🚀 Startup site",
                    "📰 News article",
                    "✍️ Personal blog",
                ],
                label="Pick a sample website",
                value=None,
            )

            article_box = gr.Textbox(
                label="...or paste any article text",
                placeholder="Paste a paragraph or article here and hit Summarize...",
                lines=10,
            )

            # gr.Markdown("### Personality (the system prompt)")

            personality = gr.Radio(
                choices=[
                    "😊 Friendly",
                    "😏 Snarky",
                    "🧒 Explain like I'm 5",
                    "💼 Professional",
                ],
                value="😏 Snarky",
                label="Personality (the system prompt)",
            )

            summarize_btn = gr.Button(
                "✨ Summarize",
                variant="primary",
                size="lg",
            )

        # ---------------- RIGHT PANEL ----------------
        with gr.Column(scale=1):

            output = gr.Markdown(
                value="*Paste some text or pick a sample first.*",
                label="Summary",
            )

    # -----------------------------
    # Events
    # -----------------------------
    sample_choice.change(
        fn=load_sample,
        inputs=sample_choice,
        outputs=article_box,
    )

    summarize_btn.click(
        fn=run_summary,
        inputs=[article_box, personality],
        outputs=output,
    )

demo.launch(share=True)