# Customerchurn
This project is about predicting the churn of the customers of a telecom company.
# Description of model and Insights

Data cleaning has been performed.

No null values were found. However, blank spaces were there which were replaced with zero in total purchase collumn.

EDA was performed and the features were selected based on it. Statistical test like chi2-sqaure test has also been used for the feature selection.

Various model performance has been shown in the ROC curve. Logistic regression has performed best. It gave the auc score for 74.6% at thareshold of 0.6.

There was class imbalance in the data so oversampling technique has been used to counter the class imbalance.

F1 score is matrix of concern since the dataset has class imbalance the accuracy won't be a good matrix here since ML algorithms have biasness towards the majority class.

Key factors like contract,seniorcitizen,tenure,totalcharges have significant effect on the churn of the customers. Customer having longer contract are less likely to churn since they are under contraint.

We can offer customers discounts, coupouns,special services to let them intact with the company and it can be monitored via the feedback taken from the customers every week or month. We can also provide them cheap internet plans and outgoing calls.
