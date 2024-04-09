<img width="1050" alt="Screenshot 2024-04-09 at 14 31 12" src="https://github.com/lucashomuniz/Project-17/assets/123151332/308094f4-0892-4d7c-8d60-4941d0dbfa45"># ✅ PROJECT-17

Netflix, Inc., an American subscription streaming service and production company, commenced its operations on August 29, 1997. It boasts an extensive library of films and television series acquired through licensing agreements and in-house production.

Weekly, Netflix releases its top 10 titles, accompanied by the corresponding hours users spent watching each title. These rankings are categorized into four segments: English Films, Non-English Films, English TV, and Non-English TV. This data holds significance for investors seeking insights into Netflix's content strategy, including the production and licensing of engaging content, the effectiveness of investments in new genres or geographies, and the trends in viewership over time, all of which influence subscriber numbers.

To address these inquiries, we scrape data from the Netflix top 10 website weekly, assuming its continued publication. Subsequently, we extract additional details from IMDb, such as running time and ratings, to enhance our analysis. However, during the week of May 22nd, 2022, our data collection system experienced an issue specifically affecting the 'weekly_hours_viewed' column. As this column is pivotal for tracking viewership metrics, we must exclude this week from our estimations.

This assignment comprises two parts: Part 1 involves analyzing web-scraped NFLX viewership data, while Part 2 entails reviewing a brief report on our Streaming Video product, encompassing various services, including NFLX. The objective is to assess your proficiency in comprehending and analyzing new datasets and articulating your findings succinctly and clearly.

Keywords: Data Analysis, Statistical Analysis, Data Science, Machine Learning, Bussiness Intelligence, Netflix, Excel, Python, Pandas, numpy.

# ✅ PROCESS

Part 1

1. Which film in the 'Films (English)' category holds the record for the most appearances in our dataset (NFLX Top 10 tab of the Sheet)? What is its average weekly hours viewed, excluding the week of the outage?
2. Among the films in the 'Films (English)' category, which one has the lowest IMDb rating? What is its average weekly hours viewed, excluding the week of the outage?
3. In the 'Films (Non-English)' category, which film has maintained the highest number of weeks in the top 10? To approximate the number of viewers for this film, what assumptions would you rely on, and what potential risks are associated?
4. What are the consequences of disregarding the data from the week of May 22nd when computing the metrics from the previous questions?
5. Although we cannot incorporate the 'weekly_hours_viewed' data for the week of May 22nd into our estimates, there might be a need to fill in this missing information for other analyses. As a Data Specialist, what approach would you suggest for estimating the 'weekly_hours_viewed' for this absent week?

Part 2

6. Based on your interpretation, is the information conveyed in this report advantageous or disadvantageous for NFLX as a company? Provide reasons for your assessment.
7. Identify three inquiries that our clients may raise after reviewing the report.
8. Please specify your level of proficiency in any coding skills you possess. If you do not have any coding skills, please state "NA".

# ✅ CONCLUSION

Part 1

1. Sonic the Hedgehog, 8.550.000

<img width="1210" alt="Screenshot 2024-04-09 at 14 25 12" src="https://github.com/lucashomuniz/Project-17/assets/123151332/a79e96cb-0b5e-41e9-92a9-486394509bcb">

2. Chickenhare and the Hamster of Darkness, 14.843.333

<img width="1210" alt="Screenshot 2024-04-09 at 14 25 51" src="https://github.com/lucashomuniz/Project-17/assets/123151332/15a296e5-2df4-4759-90fe-fdfbaad7873c">

3. The movie "Through my Window" remained in the top 10 for 13 weeks. To estimate the number of viewers, my approach would be to request my personal account data from Netflix. Based on my daily watched hours, I would calculate how many people watched the movie by dividing the viewing hours of 4 weeks by my monthly average hours on the platform. The risks are that perhaps I am not a "regular" Netflix user, so my monthly watched hours may be lower than the global average. However, this would be the most faithful approach, as I would be using "reliable data." Important to say that, the film's “runtime” has 116 min, so by dividing the weekly average of watched hours by the runtime, it is estimated the movie was watched 17.897 times per week.

<img width="1210" alt="Screenshot 2024-04-09 at 14 25 51" src="https://github.com/lucashomuniz/Project-17/assets/123151332/33b24ca9-a171-457e-8e00-b38e6ab9b526">

4. Ignoring zero data when calculating metrics may underestimate the importance of titles on the Netflix platform and distort understanding of their true performance. Additionally, it can cause bias in the analysis of viewing trends and influence content recommendations. Failure to understand this data also results in the loss of valuable information about user behavior and title popularity. It is critical to explore alternative approaches, such as data imputation. The movie with the highest recurrence has the outage date. Including the date gives 7,481,250 weekly views, excluding it gives 8,550,000, a 12.50% average difference. This affects the order of other top movies, with the date interruption impacting about 7.6% of the data, 2% within the specified category. Despite its small percentage, its implications on the dataset are notable. In the second question, during the analysis it was seen that it is not only the film "Chickenhare and the Hamster of Darkness" that has the lowest rating on IMDB, there are 8 other films in the "Films (English)" category that also have ratings equal to zero. Therefore, if the answer to this question were "Operation Mincemeat", then it would have a negative impact in relation to the average weekly views, with a difference of 50% in the "weekly_hours_viewed" variable. In the third question remains unaffected by the corrupted date, as the movie spending the most weeks in the top 10 lacks the outage date.

![figure_with_outage](https://github.com/lucashomuniz/Project-17/assets/123151332/58ae1207-28d4-4556-a58b-aa535b10787c)

![figure_without_outage](https://github.com/lucashomuniz/Project-17/assets/123151332/7d85feaa-4eae-4e3e-b199-4ea1ecd00e5b)

5. Several data imputation methodologies are available for replacing corrupted data. Mean or median imputation involves replacing zero values with the mean or median of non-zero values in the "weekly_hours_viewed" column. Regression models predict "weekly_hours_viewed" based on other variables, trained on known data to predict zero values. K-Nearest Neighbors (KNN) imputes missing values based on similarity to nearest neighbors. Clustering-based imputation groups data into clusters and replaces missing values with the cluster mean. Temporal analysis-based imputation uses temporal patterns, like moving averages, for missing values. Each method has pros and cons, influencing dataset size, structure, and bias. Analyzing the
choice is crucial as it impacts analysis results. The chosen method depends on data characteristics, context, and objectives, requiring evaluation of potential effects on final results and validation of imputation outcomes. In my opinion, I would proceed with developing a machine learning model (supervised learning), I would develop the model, evaluate it, then validate and optimize it. Based on these steps, particularly the validation stage, we would have a good solution for the imputation process.

Part 2

6. Based on the insights presented, the competitive landscape of NFLX reveals a mix of favorable and challenging aspects. On the positive side, historically, NFLX has succeeded in attracting a significant number of new streaming subscribers, demonstrating its strong appeal to a broad audience. Additionally, the company exhibits a healthy subscription renewal rate, reflecting the loyalty of its customer base and the perceived quality of its content and service. The analysis also suggests a limited correlation between NFLX churn and the addition of subscribers to competing services, indicating a level of customer retention. However, there are challenges to be addressed. The declining percentage of NFLX subscribers also subscribing to other services may indicate market saturation or increased competition. Moreover, historically low levels of churners transitioning to competing services highlight the need for NFLX to enhance its offerings and value propositions to retain and regain subscribers. The decreasing share of new streaming subscribers over time suggests heightened competition in the market, posing a challenge for NFLX to differentiate itself and attract new customers. In summary, while NFLX has demonstrated strengths in customer acquisition and retention, it faces challenges in a competitive and evolving streaming landscape. To sustain its growth and competitive position, the company needs to focus on innovation, content differentiation, and customer engagement strategies, adapting to market changes and consumer preferences.

<img width="1050" alt="Screenshot 2024-04-09 at 14 31 12" src="https://github.com/lucashomuniz/Project-17/assets/123151332/4bab2f8e-a742-438a-992c-1cbf1a005a7d">

7. How can NFLX adapt its customer engagement and retention strategies in response to the decelerating trend in the share of subscribers who are also subscribed to additional services, considering the potential market saturation and increased competition in the streaming industry?

What actions should NFLX take to address the challenges indicated by the historically low levels of NFLX churners joining competing services, and how can the company improve its value proposition to retain existing subscribers and attract new ones in a competitive streaming market environment?

In light of the declining share of new streaming subscribers captured by NFLX over time, what measures should the company implement to differentiate itself from competitors and enhance its appeal to potential customers, considering the intensifying competition in the streaming industry?
