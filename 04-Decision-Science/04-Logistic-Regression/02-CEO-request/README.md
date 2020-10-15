⚠️ This is the final challenge of the week (you have until Friday evening to complete it).
**Before diving into it, take time to finish yesterday's challenge 02 on sellers analysis**.


Our preliminary analysis is good enough for the limited time we have. Let's recap our key findings:
- We have seen how `wait_time` was the most significant factor explaining low review scores, but reading comments of the bad reviews also showed that some of them were linked to the seller or to the product itself.
- `wait_time` is made of seller's `delay_to_carrier` + `carrier_delivery_time`. The latter being outside of Olist's direct control, improving it is not a quick-win recommendation we can make to Olist CEO without in-depth analysis of their operational practices.
- On the contrary, better selecting `sellers` can positive impact on `delay_to_carrier` and reduce the number of bad `review_score` on Olist.

💡 Let's investigate the economic impact of banning some sellers from Olist marketplace:

## Unit Economics

***Revenue***

- Olist takes a **10% cut** on the product price (excl. freight) of each order delivered.
- Olist charges **80 BRL by month** per seller.

***Cost***

- On the long term, bad customer experience has business implications: low repeat rate, immediate customer support cost, refund or non favorable word of mouth. We will assume that we have an estimate measure of the monetary cost for each bad review:

review_score|cost (BRL)
---|---
1 star|100
2 stars|50
3 stars|40
4 stars|0
5 stars|0

- In addition, Olist's **IT costs** (servers, etc...) increase with the amount of orders processed, albeit less and less rapidly (scale effects).
For the sake of simplificy, we will consider IT Costs to be _proportional to the square-root of the number of orders processed_
The IT department also told you that since birth of the marketplace, cumulated IT costs have amounted to 500,000 BRL.

## ✏️ Your turn!

👉 **Open the `ceo_request.ipynb` notebook and start from there.**

- We'll start from a blank Notebook
- Refrain from re-using from previous notebooks - they were made for investigation only
- All your re-usable logic is coded in `olist/*.py` scripts

You have until Friday afternoon to produce the following analysis:

> **Should Olist remove underperforming sellers from its marketplace?**

### (Optional): Feel free to extend your analysis to the following options:

- Should Olist remove the worst performing products / categories from its marketplace entirely?
- Should Olist remove only repetively underperforming sellers, after it has a honeymoon period of few months
- Should Olist restricts (seller, customer) pairs between certain states to avoid delays?
- Olist acquire new sellers, with some cost assumptions to be suggested?
- ...

### (Tomorrow evening) you will present your analysis to your favorite TAs & classmates!