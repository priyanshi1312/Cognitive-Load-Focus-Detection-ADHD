# Cognitive-Load-Focus-Detection-ADHD
Task-based Cognitive Load and Focus Detection System for ADHD Support


System Architecture

User → Task Module → Data Collection → Focus Calculation → Result Dashboard

Methodology

1. User completes cognitive tasks (math/memory).
2. System records:
   Response time
   Accuracy
   Consistency
3. Focus score is calculated using weighted formula.
4. Cognitive load level is classified as:
   High
   Medium
   Low

 Focus Score Formula

Focus Score =
(Accuracy × 0.5) +
(1 / Average Response Time × 0.3) +
(Consistency × 0.2)


Frontend Interface

The project includes a simple HTML/CSS-based user interface.

Features:
- Start Assessment button
- Question display area
- User input field
- Focus score result display

This modular structure allows future integration with the Python backend.
