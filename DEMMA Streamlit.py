import streamlit as st
import pandas as pd
import openai

# -------------------------
# STREAMLIT UI
# -------------------------
st.set_page_config(page_title="Digital Media Marketing Agent")
st.title("📊 Digital Media Marketing Agent")

st.header("🔮 Conversion Prediction Model")
st.text("Random Forest Classifier trained to predict likelihood of user conversion")
st.text(classification_report(y_test, y_pred))

st.header("💰 Spend Optimization")
st.dataframe(summary[['channel', 'campaign', 'message', 'ROAS', 'optimized_spend']])
st.bar_chart(summary.set_index('channel')['optimized_spend'])

st.header("🧠 User Segmentation")
st.bar_chart(user_data['segment'].value_counts())

st.header("💬 Recommended Messaging by Segment")
st.dataframe(message_perf)

st.header("🧾 Example AI Insights")
st.markdown("""
- **Segment 2** responds best to **Emotional Appeal + Discount** on **LinkedIn Video** campaigns.
- **Segment 1** prefers **Free Trials** and clicks most on **Google Ads**.
- **User 102** has a **68% chance to convert** on **Facebook Campaign B**.
- **Segment 3** has high interest score but low conversion → needs better targeting.
- **Emotional Appeal** drives highest ROAS on video campaigns (avg 18.9).
- Recommend reallocating 30% more budget to **Campaign A on LinkedIn with video**.
- **Users aged 25–34** show 2x higher CTR on video.
- **Rural segments** underperform on LinkedIn but excel on Facebook.
- **Segment 0** users convert well on static campaigns but fall off with video.
- **Discount messages** perform better in suburban areas with ROAS > 2.0.
- **Campaign B** underperforms across all channels, recommend A/B test.
""")
