# ==========================================================
# Day 53 : Anomaly Detection
# Repository : Machine Learning Foundation
# Author : Saloni Tiwari
# ==========================================================

print("=" * 60)
print("      MACHINE LEARNING FOUNDATIONS - DAY 53")
print("=" * 60)

print("\nAnomaly Detection")
print("-" * 30)

print("""
Anomaly Detection is a Machine Learning
technique used to identify unusual,
rare, or abnormal observations in data.

These unusual observations are called:

✓ Anomalies
✓ Outliers
✓ Exceptions

Goal:

Detect data points that differ
significantly from normal behavior.
""")

# ----------------------------------------------------------
# What is an Anomaly?
# ----------------------------------------------------------

print("\nWhat is an Anomaly?")
print("-" * 30)

print("""
An anomaly is a data point that
does not follow the normal pattern
of the dataset.

Example:

Normal Transactions:

500
700
600
800

Anomalous Transaction:

50000

The value 50000 is suspicious.
""")

# ----------------------------------------------------------
# Example Dataset
# ----------------------------------------------------------

print("\nExample Dataset")
print("-" * 30)

transactions = [
    500,
    700,
    650,
    800,
    750,
    600,
    550,
    50000
]

print("Transactions =")
print(transactions)

# ----------------------------------------------------------
# Why Anomaly Detection?
# ----------------------------------------------------------

print("\nWhy Anomaly Detection?")
print("-" * 30)

print("""
Anomaly Detection helps identify:

✓ Fraud
✓ Cyber Attacks
✓ Equipment Failures
✓ Medical Abnormalities
✓ Data Errors

It is widely used in industry.
""")

# ----------------------------------------------------------
# Types of Anomalies
# ----------------------------------------------------------

print("\nTypes of Anomalies")
print("-" * 30)

print("""
1. Point Anomaly
2. Contextual Anomaly
3. Collective Anomaly
""")

# ----------------------------------------------------------
# Point Anomaly
# ----------------------------------------------------------

print("\n1. Point Anomaly")
print("-" * 30)

print("""
A single observation is abnormal.

Example:

Normal Temperatures:

30, 31, 29, 32

Anomaly:

80

The value 80 is unusual.
""")

# ----------------------------------------------------------
# Contextual Anomaly
# ----------------------------------------------------------

print("\n2. Contextual Anomaly")
print("-" * 30)

print("""
An observation may be normal
in one context but abnormal
in another.

Example:

Temperature:

35°C in Summer
→ Normal

35°C in Winter
→ Abnormal
""")

# ----------------------------------------------------------
# Collective Anomaly
# ----------------------------------------------------------

print("\n3. Collective Anomaly")
print("-" * 30)

print("""
A group of observations is abnormal.

Example:

Network Traffic Pattern

One request:
Normal

Thousands of requests
in a few seconds:
Abnormal
""")

# ----------------------------------------------------------
# Statistical Approach
# ----------------------------------------------------------

print("\nStatistical Approach")
print("-" * 30)

print("""
One simple approach is:

Calculate Mean

Calculate Standard Deviation

Detect observations that are
far away from the mean.
""")

# ----------------------------------------------------------
# Mean Calculation
# ----------------------------------------------------------

print("\nMean Calculation")
print("-" * 30)

values = [
    10,
    12,
    11,
    13,
    12
]

mean = sum(values) / len(values)

print("Values =", values)
print("Mean =", mean)

# ----------------------------------------------------------
# Distance From Mean
# ----------------------------------------------------------

print("\nDistance From Mean")
print("-" * 30)

test_value = 50

distance = abs(
    test_value - mean
)

print("Value =", test_value)
print("Distance From Mean =",
      distance)

print("""
Large distances may indicate
an anomaly.
""")

# ----------------------------------------------------------
# Z-Score Concept
# ----------------------------------------------------------

print("\nZ-Score")
print("-" * 30)

print("""
Z-Score measures how far a value
is from the mean.

Formula:

Z =
(Value - Mean)
---------------
Standard Deviation

Large Z-Scores often indicate
anomalies.
""")

# Example

z_score = 3.5

print("Example Z-Score =",
      z_score)

# ----------------------------------------------------------
# Visualization Example
# ----------------------------------------------------------

print("\nVisualization")
print("-" * 30)

print("""
Normal Data:

● ● ● ● ● ● ●

Anomaly:

                ▲

The isolated point may be
an anomaly.
""")

# ----------------------------------------------------------
# Fraud Detection
# ----------------------------------------------------------

print("\nFraud Detection")
print("-" * 30)

print("""
Banks use anomaly detection
to identify suspicious transactions.

Example:

Normal Purchase:
₹500

Suspicious Purchase:
₹5,00,000

The system raises an alert.
""")

# ----------------------------------------------------------
# Cybersecurity
# ----------------------------------------------------------

print("\nCybersecurity")
print("-" * 30)

print("""
Anomaly Detection helps identify:

✓ Unusual Login Activity
✓ Malware Behavior
✓ Network Attacks
✓ Data Breaches
""")

# ----------------------------------------------------------
# Medical Diagnosis
# ----------------------------------------------------------

print("\nMedical Diagnosis")
print("-" * 30)

print("""
Doctors use anomaly detection
to identify abnormal:

✓ Heart Rates
✓ Blood Pressure
✓ Test Results
✓ Medical Images
""")

# ----------------------------------------------------------
# Manufacturing
# ----------------------------------------------------------

print("\nManufacturing")
print("-" * 30)

print("""
Factories use anomaly detection
for predictive maintenance.

Example:

Machine Temperature suddenly
increases beyond normal limits.
""")

# ----------------------------------------------------------
# Popular Algorithms
# ----------------------------------------------------------

print("\nPopular Algorithms")
print("-" * 30)

algorithms = [
    "Z-Score Method",
    "Isolation Forest",
    "Local Outlier Factor",
    "One-Class SVM",
    "DBSCAN"
]

for algorithm in algorithms:
    print("✓", algorithm)

# ----------------------------------------------------------
# Advantages
# ----------------------------------------------------------

print("\nAdvantages")
print("-" * 30)

advantages = [
    "Detects Rare Events",
    "Improves Security",
    "Prevents Fraud",
    "Reduces Risks",
    "Supports Automation"
]

for item in advantages:
    print("✓", item)

# ----------------------------------------------------------
# Limitations
# ----------------------------------------------------------

print("\nLimitations")
print("-" * 30)

limitations = [
    "False Alarms",
    "Sensitive to Noise",
    "Difficult Threshold Selection",
    "May Miss Some Anomalies"
]

for item in limitations:
    print("✗", item)

# ----------------------------------------------------------
# Applications
# ----------------------------------------------------------

print("\nApplications")
print("-" * 30)

applications = [
    "Fraud Detection",
    "Cybersecurity",
    "Healthcare",
    "Manufacturing",
    "Finance",
    "Network Monitoring"
]

for app in applications:
    print("✓", app)

# ----------------------------------------------------------
# Workflow
# ----------------------------------------------------------

print("\nAnomaly Detection Workflow")
print("-" * 30)

steps = [
    "Collect Data",
    "Clean Data",
    "Analyze Normal Behavior",
    "Detect Outliers",
    "Generate Alerts",
    "Take Action"
]

for i, step in enumerate(
        steps,
        start=1):

    print(f"{i}. {step}")

# ----------------------------------------------------------
# Practical Example
# ----------------------------------------------------------

print("\nPractical Example")
print("-" * 30)

daily_sales = [
    100,
    110,
    105,
    98,
    102,
    500
]

print("Daily Sales =", daily_sales)

print("""
Sales = 500 appears unusual
compared to other values.

Possible Anomaly Detected.
""")

# ----------------------------------------------------------
# Mini Practice
# ----------------------------------------------------------

print("\nMini Practice")
print("-" * 30)

print("""
Question:

What is another name
for an anomaly?

Answer:

Outlier
""")

# ----------------------------------------------------------
# Mini Quiz
# ----------------------------------------------------------

print("\nMini Quiz")
print("-" * 30)

print("""
1. What is Anomaly Detection?

2. What is an Outlier?

3. Name one anomaly type.

4. Name one anomaly detection algorithm.

5. Give one real-world application.
""")

print("""
Answers:

1. Detecting unusual observations
2. Abnormal data point
3. Point Anomaly
4. Isolation Forest
5. Fraud Detection
""")

# ----------------------------------------------------------
# Summary
# ----------------------------------------------------------

print("\nDay 53 Summary")
print("-" * 30)

print("""
1. Anomaly Detection identifies
   unusual data points.

2. Anomalies are also called:

   ✓ Outliers
   ✓ Exceptions

3. Types:

   ✓ Point Anomaly
   ✓ Contextual Anomaly
   ✓ Collective Anomaly

4. Popular Methods:

   ✓ Z-Score
   ✓ Isolation Forest
   ✓ One-Class SVM

5. Applications include:

   ✓ Fraud Detection
   ✓ Cybersecurity
   ✓ Healthcare

6. It is an important area of
   Unsupervised Learning.
""")

print("\nDay 53 Completed Successfully!")
print("=" * 60)