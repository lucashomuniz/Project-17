# ✅ PROJECT-17

In this project, **Netflix, Inc.**, a prominent American **subscription streaming service** and **production company**, was founded on August 29, 1997. It offers an extensive library of **films** and **television series** acquired through **licensing agreements** and **in-house production**. **Netflix** publishes its **top 10 titles** weekly, along with the corresponding **viewing hours** for each title. These rankings are segmented into four categories: **English Films**, **Non-English Films**, **English TV**, and **Non-English TV**. This data is vital for **investors** seeking insights into **Netflix's content strategy**, including the **production** and **licensing** of engaging content, the **effectiveness** of investments in new **genres** or **geographies**, and **viewership trends** over time, all of which influence **subscriber numbers**.

To address these objectives, we **scrape data** from the **Netflix Top 10 website** on a weekly basis, assuming its continued availability. Subsequently, we enhance our analysis by extracting additional details from **IMDb**, such as **runtime** and **ratings**. However, during the week of May 22nd, 2022, our **data collection system** encountered an issue affecting the '**weekly_hours_viewed**' column. As this column is crucial for tracking **viewership metrics**, we must exclude this week from our estimations. This assignment is divided into two parts: **Part 1** involves analyzing the **web-scraped NFLX viewership data**, while **Part 2** entails reviewing a brief report on our **Streaming Video product**, which encompasses various services, including **NFLX**. The objective is to evaluate your proficiency in understanding and analyzing new **datasets** and effectively communicating your findings in a clear and concise manner.

Keywords: Data Analysis, Statistical Analysis, Data Science, Machine Learning, Bussiness Intelligence, Netflix, Excel, Python, Pandas, numpy.

# ✅ PROCESS

This analysis comprises two sections. **Part 1** examines the **Netflix Top 10** dataset, focusing on film frequency, **IMDb ratings**, viewership metrics, data estimation methods, and the impact of excluding specific data points. **Part 2** assesses a report on our **Streaming Video product**, evaluating its advantages and disadvantages for **Netflix** and anticipating potential client inquiries. This structure demonstrates expertise in data analysis, critical evaluation, and effective communication of dataset-derived insights.

**Part 1**
1. Identify the film in the 'Films (English)' category with the highest number of appearances in the **Netflix Top 10** dataset. What is its average weekly hours viewed, excluding the outage week?
2. Which film in the 'Films (English)' category has the lowest **IMDb rating**? What is its average weekly hours viewed, excluding the outage week?
3. In the 'Films (Non-English)' category, which film has the longest tenure in the top 10? What assumptions and associated risks are involved in estimating its viewership?
4. What are the implications of excluding data from the week of May 22nd when calculating the aforementioned metrics?
5. As a Data Specialist, propose a method to estimate the 'weekly_hours_viewed' for May 22nd, given its absence from our estimates.

**Part 2**
6. Does the report's information present advantages or disadvantages for **Netflix**? Justify your evaluation.
7. List three potential client questions following their review of the report.

# ✅ CONCLUSION

**Part 1**

1. **Sonic the Hedgehog** achieved the highest number of appearances with **8,550,000** weekly hours viewed.

2. **Chickenhare and the Hamster of Darkness** holds the lowest **IMDb rating** with **14,843,333** weekly hours viewed.

3. **"Through my Window"** remained in the top 10 for **13 weeks**. To estimate viewership, personal account data from Netflix was utilized. By dividing four weeks of viewing hours by the monthly average, an estimate of **17,897** weekly views was derived, considering the film's **116-minute runtime**. Risks include potential deviation from the global average if the account is not representative. This method ensures reliability through the use of personal data.

4. Excluding data from **May 22nd** may lead to underestimation of title performance and biased trend analysis, affecting content recommendations. Specifically, excluding this week results in a **12.50%** increase in average weekly views from **7,481,250** to **8,550,000**, altering the ranking of top movies. Additionally, eight other films in the **"Films (English)"** category have zero **IMDb ratings**, which could skew average view metrics by **50%** if not addressed. The highest recurring movie is unaffected by the outage date.

5. **Data imputation** methods to address missing data include:
- **Mean/Median Imputation**: Replaces missing values with the column's mean or median.
- **Regression Models**: Predict missing values based on other variables.
- **K-Nearest Neighbors (KNN)**: Imputes based on similarity to neighboring data points.
- **Clustering-Based Imputation**: Uses cluster means for replacement.
- **Temporal Analysis**: Applies moving averages based on time-series patterns.

Each method impacts dataset integrity differently. A **supervised machine learning model** is recommended for imputation, involving model development, evaluation, validation, and optimization to ensure accurate and reliable estimates.

**Part 2**
6. The competitive landscape analysis of **Netflix (NFLX)** presents both strengths and challenges. Positively, NFLX excels in acquiring new subscribers and maintaining a high **subscription renewal rate**, indicating strong customer loyalty and content quality. There is minimal correlation between NFLX churn and competitor subscriber growth, suggesting effective retention. However, challenges include a declining percentage of NFLX subscribers engaging with additional services, indicating potential market saturation and heightened competition. Low churner migration to competitors underscores the need for enhanced value propositions to retain and attract subscribers. The decreasing influx of new subscribers further intensifies market competition, necessitating differentiation and innovative strategies. To sustain growth, NFLX must focus on **innovation**, **content differentiation**, and **customer engagement** to adapt to evolving market dynamics and consumer preferences.

<img width="1050" alt="Screenshot 2024-04-09 at 14 31 12" src="https://github.com/lucashomuniz/Project-17/assets/123151332/4bab2f8e-a742-438a-992c-1cbf1a005a7d">

7. **Client Inquiries:**
- How can **NFLX** enhance **customer engagement** and **retention** amidst declining multi-service subscriptions and increased competition?
- What strategies should **NFLX** implement to improve its **value proposition** to prevent churn and attract new subscribers in a competitive streaming market?
- In response to the decreasing share of new **streaming subscribers**, what measures should **NFLX** adopt to differentiate from competitors and increase its market appeal?
