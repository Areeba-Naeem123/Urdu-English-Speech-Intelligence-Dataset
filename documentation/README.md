# Urdu-English Speech Intelligence Dataset

**Tagline:** From Spoken Words to Structured Intelligence

## 1. Project Overview

This project demonstrates a speech data annotation workflow using Urdu audio recordings from Mozilla Common Voice.

The initial dataset contains 20 Urdu audio recordings with corresponding transcripts.

## 2. Dataset Information

| Field | Details |
|---|---|
| Source | Mozilla Common Voice |
| Language | Urdu |
| Number of recordings | 20 |
| Audio format | MP3 |
| Transcript status | Human verified |
| Annotation tool | Manual review and CSV annotation |

## 3. Annotation Tasks

### Transcription
- Preserve the spoken Urdu words.
- Correct transcription errors after listening to the recording.
- Do not translate the original speech.

### Speaker Identification
- Assign consistent pseudonymous speaker IDs.
- Use the same ID for recordings from the same contributor.
- Do not publish original contributor identifiers.

### Language Identification
- Identify the language spoken in each recording.
- Use `ur` for Urdu.

### Sentiment Annotation
- Classify the sentiment expressed by the text.
- Available labels: `positive`, `negative`, and `neutral`.
- Do not infer the speaker's psychological state.

### Named Entity Recognition (NER)
- Identify named entities such as people, locations, and organizations.
- Assign an appropriate entity type.
- Do not label ordinary pronouns as named entities.
- Leave sentences without named entities out of the NER file.

## 4. Quality Control

- Check transcripts against the audio.
- Check consistency of speaker IDs.
- Verify language labels.
- Review sentiment and entity labels.
- Check that annotation records match the audio filenames.

## 5. Project Structure

```text
Urdu-English-Speech-Intelligence/
├── audio/
├── transcripts/
├── annotations/
├── metadata/
├── documentation/
└── raw_dataset/
```

## 6. Important Notes

This is an initial Urdu-only sample. English and Urdu-English code-switching data are planned extensions, not yet included in this sample.

The original Common Voice dataset is credited as the source. Its applicable release-specific license and redistribution conditions must be followed.

## 7. Project Goal

To demonstrate practical skills in audio dataset preparation, transcript correction, speaker identification, language identification, sentiment analysis, and named entity annotation.