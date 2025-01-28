# ✅ PROJECT-17

In this project, **Netflix, Inc.**, a prominent American **subscription streaming service** and **production company**, was founded on August 29, 1997. It offers an extensive library of **films** and **television series** acquired through **licensing agreements** and **in-house production**. **Netflix** publishes its **top 10 titles** weekly, along with the corresponding **viewing hours** for each title. These rankings are segmented into four categories: **English Films**, **Non-English Films**, **English TV**, and **Non-English TV**. This data is vital for **investors** seeking insights into **Netflix's content strategy**, including the **production** and **licensing** of engaging content, the **effectiveness** of investments in new **genres** or **geographies**, and **viewership trends** over time, all of which influence **subscriber numbers**.

To address these objectives, we **scrape data** from the **Netflix Top 10 website** on a weekly basis, assuming its continued availability. Subsequently, we enhance our analysis by extracting additional details from **IMDb**, such as **runtime** and **ratings**. However, during the week of May 22nd, 2022, our **data collection system** encountered an issue affecting the '**weekly_hours_viewed**' column. As this column is crucial for tracking **viewership metrics**, we must exclude this week from our estimations. This assignment is divided into two parts: **Part 1** involves analyzing the **web-scraped NFLX viewership data**, while **Part 2** entails reviewing a brief report on our **Streaming Video product**, which encompasses various services, including **NFLX**. The objective is to evaluate your proficiency in understanding and analyzing new **datasets** and effectively communicating your findings in a clear and concise manner.

Keywords: Data Analysis, Statistical Analysis, Data Science, Machine Learning, Bussiness Intelligence, Netflix, Excel, Python, Pandas, numpy.

# ✅ PROCESS

This analysis comprises two sections: **Part 1** examines the **Netflix Top 10** dataset, focusing on film frequency, **IMDb ratings**, viewership metrics, data estimation methods, and the impact of excluding specific data points. **Part 2** assesses a report on our **Streaming Video product**, evaluating its advantages and disadvantages for **Netflix** and anticipating potential client inquiries. This structure demonstrates expertise in data analysis, critical evaluation, and effective communication of dataset-derived insights.

# ✅ CONCLUSION

> **Question 1: Identify the film in the 'Films (English)' category with the highest number of appearances in the **Netflix Top 10** dataset. What is its average weekly hours viewed, excluding the outage week?**

**Sonic the Hedgehog** achieved the highest number of appearances in the **Netflix Top 10** dataset within the **"Films (English)"** category, with an impressive total of **8,550,000** weekly hours viewed. This result highlights the film's **sustained popularity** and **consistent audience engagement** over time. The **high viewing hours** suggest that the movie likely appealed to a **broad demographic**, leveraging its **family-friendly content** and **widespread brand recognition** to maintain its position in the rankings. This sustained performance underscores the importance of **recognizable franchises** in driving **consistent viewer retention** and **engagement** on streaming platforms like **Netflix**. Additionally, the data implies that the film's **release timing** and **availability** may have strategically aligned with **audience demand**, maximizing its **visibility** and **performance**. This case serves as a strong example of how **existing intellectual property (IP)** can be leveraged to achieve **significant success** in streaming markets.

> **Question 2: Which film in the 'Films (English)' category has the lowest **IMDb rating**? What is its average weekly hours viewed, excluding the outage week?** 

**Chickenhare and the Hamster of Darkness** holds the lowest **IMDb rating** within the **"Films (English)"** category, yet achieved an impressive **14,843,333** weekly hours viewed. This result highlights an intriguing case where **viewer engagement** does not directly correlate with **IMDb ratings**. The film's performance suggests that factors such as **genre appeal**, **family-friendly content**, or **availability during a strategic time period** (e.g., holidays or school breaks) may have contributed to its success despite low critical reception. Additionally, this case demonstrates how certain titles can resonate strongly with specific audiences, such as **children** or **families**, who may prioritize entertainment value over critical reviews. The high weekly viewing hours emphasize the importance of understanding **target audiences** and leveraging **accessible, light-hearted content** to drive significant engagement on streaming platforms like **Netflix**. This scenario also raises questions about the weight of **IMDb ratings** in predicting the success of films in the streaming market, particularly for **family-oriented** or **animated movies**.

> **Question 3: In the 'Films (Non-English)' category, which film has the longest tenure in the top 10? What assumptions and associated risks are involved in estimating its viewership?** 

**"Through my Window"** remained in the **Netflix Top 10** for an impressive **13 weeks**, showcasing its **long-lasting appeal** and **sustained audience engagement**. To estimate viewership, **personal account data** from **Netflix** was utilized. The calculation involved dividing **four weeks of viewing hours** by the **monthly average** of hours watched, resulting in an estimated **17,897** weekly views. This calculation also took into account the film's **116-minute runtime**, enabling a more accurate estimation of the number of viewers. 

However, there are inherent **risks** with this approach, including the potential deviation from the **global average** if the account used for estimation is not representative of the general audience. For example, variations in viewing habits, demographics, or regional trends could introduce bias into the estimate. Despite these limitations, the method ensures **reliability** by leveraging **real user data** to form the basis of the calculation. This case underscores the importance of understanding **viewer behavior trends**, especially for films that maintain high visibility over multiple weeks. It also highlights the value of **data-driven estimations** to derive insights from incomplete information, ensuring that titles with **extended audience retention** like **"Through my Window"** receive proper recognition in analysis.

> **Question 4: What are the implications of excluding data from the week of May 22nd when calculating the aforementioned metrics?** 

Excluding data from **May 22nd** introduces the risk of **underestimating title performance** and generating **biased trend analyses**, which can negatively impact **content recommendations** and overall strategic decisions. Specifically, the absence of this data results in a **12.50%** increase in the average weekly views, rising from **7,481,250** to **8,550,000**, and consequently alters the **ranking of top movies**. This highlights the significance of even a single week of data in accurately reflecting a film's performance.

Moreover, eight other films within the **"Films (English)"** category have **zero IMDb ratings**, which, if not addressed, could skew average view metrics by up to **50%**. This further emphasizes the importance of addressing missing or incomplete data to ensure robust and unbiased analyses.Despite these data gaps, the **highest recurring movie** remains unaffected by the outage date, suggesting a level of **stability** in its performance metrics. However, this scenario underscores the critical need for **data imputation strategies** or **alternative analytical approaches** to address missing data. By properly handling data exclusions, analysts can maintain the integrity of **trend analyses** and provide more accurate insights into **viewer behavior** and **content performance**.

> **Question 5: As a Data Specialist, propose a method to estimate the 'weekly_hours_viewed' for May 22nd, given its absence from our estimates.** 

**Data imputation** methods to address missing data include several robust approaches that can help mitigate the effects of incomplete datasets:

**Mean/Median Imputation**: This method replaces missing values with the **mean** or **median** of the column. It is a simple and efficient technique but may not capture complex patterns in the data, potentially reducing variability.

**Regression Models**: This approach predicts missing values based on other **variables** in the dataset by using regression algorithms. It considers relationships between variables but requires sufficient data for training the model to ensure accuracy.

**K-Nearest Neighbors (KNN)**: KNN imputes missing values based on the similarity to **neighboring data points**. It is particularly useful when relationships between features are nonlinear but can be computationally intensive for large datasets.

**Clustering-Based Imputation**: This method groups data into **clusters** and replaces missing values with the **mean** or **centroid** of the respective cluster. It is effective for datasets with distinct groupings but relies heavily on the quality of clustering.

**Temporal Analysis**: Using **moving averages** or other time-series techniques, this method imputes missing values based on **patterns over time**. It is particularly useful for datasets with **sequential dependencies** but may struggle with abrupt changes or anomalies.

Each of these methods has **strengths** and **limitations**. The choice of imputation strategy depends on factors such as **dataset size**, **data structure**, and **analytical goals**. A comprehensive evaluation of potential impacts on the analysis is critical, ensuring that the selected method aligns with the **context** and **objectives** of the study.

> **Question 6: Does the report's information present advantages or disadvantages for **Netflix**? Justify your evaluation.** 

The competitive landscape analysis of **Netflix (NFLX)** highlights a combination of strengths and challenges in the streaming industry. One of the platform's key strengths lies in its ability to acquire new subscribers while maintaining a high **subscription renewal rate**, which reflects strong **customer loyalty** and the perceived quality of its content. Additionally, there appears to be minimal correlation between **NFLX churn** and the growth of competitors’ subscriber bases, suggesting that Netflix's **retention strategies** are effective in keeping its audience engaged and loyal.

However, Netflix faces several challenges. The **declining percentage** of its subscribers who also engage with additional streaming services suggests potential **market saturation** or heightened competition. Furthermore, while the low migration of churners to competitors indicates a lack of immediate alternatives for those leaving the platform, it also highlights the need for Netflix to improve its **value proposition** to retain existing users and attract new ones. Compounding these challenges is a **decrease in the influx of new subscribers**, which underscores the growing difficulty of standing out in an increasingly competitive market.

To address these challenges and sustain growth, Netflix must focus on **innovation**, **content differentiation**, and **customer engagement**. By introducing new features and technologies, creating unique and compelling content, and fostering stronger connections with its subscribers through personalized experiences and responsive support, Netflix can better adapt to **evolving market dynamics** and changing **consumer preferences**. This strategic focus will enable the company to navigate the competitive landscape effectively and maintain its position as a leader in the streaming industry.



<img width="1050" alt="Screenshot 2024-04-09 at 14 31 12" src="https://github.com/lucashomuniz/Project-17/assets/123151332/4bab2f8e-a742-438a-992c-1cbf1a005a7d">




> **Question 7: List three potential client questions following their review of the report.** 

**Enhancing Customer Engagement and Retention**: 
How can **Netflix (NFLX)** improve **customer engagement** and strengthen **retention strategies** to counteract the declining trend of multi-service subscriptions and the increasing competition in the streaming industry? Addressing this question would involve exploring innovative approaches, such as offering personalized recommendations, expanding interactive content, or introducing loyalty programs to deepen subscriber connections.

**Improving Value Proposition**:
What actionable strategies should **NFLX** adopt to enhance its **value proposition**, reduce churn, and attract new subscribers in a highly competitive market? This could include measures like investing in exclusive, high-quality content, offering more flexible subscription plans, or bundling services to provide greater perceived value.

**Differentiating from Competitors**:
In light of the declining share of new **streaming subscribers**, what steps should **NFLX** take to differentiate itself from competitors and expand its market appeal? Potential measures may involve leveraging unique technological innovations, creating culturally diverse content tailored to specific regions, or forming partnerships to increase reach and visibility.
