# # Voter Assistance Chatbot

## 📌 Overview

The Voter Assistance Chatbot is an AI-powered solution designed to answer common voter queries related to voter enrolment, electoral roll corrections, required documents, and polling day procedures.

During Special Intensive Revision (SIR) and election periods, Booth Level Officers (BLOs) receive thousands of repeated questions from first-time voters, college students, shifted tenants, and senior citizens. Although the Election Commission of India (ECI) provides official handbooks and guidelines, finding specific information can be time-consuming. Helplines may also become overloaded during peak periods.

This project aims to simplify access to voter information through a user-friendly chatbot that provides clear, concise, and easy-to-understand answers based on official election guidelines.

## 🎯 Problem Statement

Voters often face difficulties understanding enrolment procedures, correction forms, document requirements, and polling booth details. Existing resources can be lengthy, and support channels may be difficult to reach during peak election periods.

The proposed chatbot helps users access relevant voter information quickly, reducing repetitive queries and supporting BLOs in assisting citizens more efficiently.

## 🎯 Objectives

- Help first-time voters understand the voter registration process.
- Explain the purpose and usage of Form 6 and Form 8.
- Provide guidance on documents required for voter-related applications.
- Answer common questions about electoral roll revision.
- Help voters understand polling day procedures and how to find official polling information.
- Reduce repetitive enquiries handled by Booth Level Officers.
- Make voter information more accessible to students, tenants, and senior citizens.

## ✨ Key Features

- **Voter Enrolment Assistance:** Guidance on new voter registration.
- **Electoral Roll Corrections:** Information about correcting voter details.
- **Document Guidance:** Explanations of supporting documents required for relevant applications.
- **Polling Day Assistance:** Answers to frequently asked questions about voting procedures.
- **First-Time Voter Support:** Simple explanations designed for new voters.
- **24/7 Query Support:** Access to common voter information without waiting for office hours.
- **Official Information:** Responses grounded in verified Election Commission of India resources.

## 🛠️ Technology Stack

The technology stack will be updated according to the implementation.

- **Frontend:** To be decided
- **Backend:** To be decided
- **AI / NLP:** To be decided
- **Knowledge Base:** Official ECI guidelines, handbooks, and voter FAQs
- **Data Sources:** Election Commission of India and applicable official election resources

## 🔄 How It Works

1. The voter enters a question in the chatbot.
2. The system identifies the query category, such as enrolment, corrections, documents, or polling day.
3. It retrieves relevant information from verified election guidelines.
4. The chatbot provides a concise and understandable answer.
5. For complex cases or information that requires confirmation, users are directed to official ECI services or the appropriate election official.

## 👥 Target Users

- First-time voters
- College students
- Tenants and people who have changed residence
- Senior citizens
- Citizens seeking voter registration or correction guidance
- Booth Level Officers handling repeated voter enquiries

## 🌟 Expected Impact

- Faster access to voter-related information
- Reduced repetitive enquiries for BLOs
- Improved awareness of voter enrolment and correction procedures
- Better accessibility of election information
- A more convenient experience for first-time voters

## 🔐 Accuracy and Reliability

The chatbot should prioritize official and up-to-date election information. It should clearly distinguish general guidance from individual application decisions and direct users to official ECI channels when verification is necessary.

It will not replace the authority of election officials or guarantee enrolment, correction, or polling eligibility.

## 🚀 Future Enhancements

- Support for Tamil, English, and other regional languages
- Voice-based questions and answers
- Retrieval-Augmented Generation (RAG) for searching official election documents
- Frequently asked questions dashboard for BLOs
- Mobile-friendly interface
- Links to official voter services and application tracking
- Evaluation of answer accuracy using verified voter FAQs

## 📚 References

- [Election Commission of India](https://www.eci.gov.in/)
- [Voters' Services Portal](https://voters.eci.gov.in/)

## 📄 License

This project is intended for educational and informational purposes. Official election procedures and requirements should always be verified through the relevant Election Commission resources.




## Problem
<3–5 sentences: who struggles with what today, and what your product changes.>

## Who it is for
<One or two real user types, for example "compliance officer at a gold-loan NBFC in Coimbatore".>

## Signature feature
<One sentence: the feature only your product has.>

## Hardest problem (my interview story)
<In your own words, from your project card.>

## Dataset
| Source | Link | Documents | Pages | Licence / terms |
|---|---|---|---|---|
| <name> | <url> | <n> | <n> | <licence> |

## 10 real questions
See [docs/QUESTIONS.md](docs/QUESTIONS.md).

## Run it
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
cp .env.example .env                                 # Windows: copy .env.example .env
uvicorn app.main:app --reload
curl localhost:8000/health
```

## Live link
<Added in Week 2>
