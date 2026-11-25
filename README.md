# Urdu-English Speech Intelligence Dataset

**From Spoken Words to Structured Intelligence**

A speech annotation portfolio project demonstrating Urdu speech transcription, speaker identification, language identification, sentiment analysis, and named entity recognition (NER).

## Project Overview

This project explores how spoken language can be converted into structured, machine-readable data through speech transcription and NLP annotation.

The initial dataset sample contains **20 Urdu audio recordings** sourced from Mozilla Common Voice Scripted Speech 27.0.

The current work focuses on Urdu. English and Urdu-English code-switched recordings are planned extensions.

## Dataset Information

| Attribute | Details |
|---|---|
| Source | Mozilla Common Voice Scripted Speech |
| Release | 27.0 (2026-09-11) |
| Language | Urdu |
| Sample size | 20 recordings |
| Audio format | MP3 |
| Transcription | Human verified |
| Speaker identification | Completed |
| Language identification | Completed |
| Sentiment annotation | Preliminary |
| Named entity recognition | Preliminary |

## Annotation Tasks

### 1. Speech Transcription
Transcribed Urdu speech and manually reviewed the text against the corresponding audio.

### 2. Speaker Identification
Assigned anonymized speaker IDs to recordings from the same contributor.

### 3. Language Identification
Annotated the language of each recording. All 20 current samples are Urdu.

### 4. Sentiment Analysis
Added preliminary text-based sentiment labels:
- Positive
- Negative
- Neutral

### 5. Named Entity Recognition
Annotated selected named entities and assigned entity categories.

## Dataset Quality Checks

A Python validation script checks:
- Audio file availability
- Transcript and annotation record counts
- Matching audio IDs across annotation files
- Unknown recording IDs

Audio-transcript matching was also manually reviewed.

## Repository Structure

```text
Urdu-English-Speech-Intelligence-Dataset/
│
├── README.md
├── .gitignore
├── check_dataset.py
│
├── metadata/
│   └── dataset_info.csv
│
├── transcripts/
│   └── urdu_transcripts.csv
│
├── annotations/
│   ├── speaker_annotations.csv
│   ├── language_annotations.csv
│   ├── sentiment_annotations.csv
│   └── ner_annotations.csv
│
└── documentation/
    └── README.md
```

## Tools and Technologies

- Python
- CSV
- Mozilla Common Voice
- Text annotation
- Speech data quality validation

## Data Access and Licensing

The original audio recordings are sourced from Mozilla Common Voice Scripted Speech 27.0.

Original Common Voice audio files are not included in this repository. Please obtain the dataset through its official distribution platform and follow the applicable dataset terms.

This repository focuses on the project's annotation files, metadata, documentation, and validation code.

## My Contribution

- Selected and organized a 20-recording Urdu sample.
- Human-verified the transcripts against the audio.
- Created anonymized speaker annotations.
- Prepared language identification annotations.
- Added preliminary sentiment and NER annotations.
- Developed a Python script for basic dataset validation.
- Organized the project into a documented dataset structure.

## Project Status

**Current status:** Initial Urdu sample completed.

**Future extensions:** English speech, Urdu-English code-switching, expanded annotation, and ASR evaluation.

---

*Created as a data annotation and speech intelligence portfolio project.*
