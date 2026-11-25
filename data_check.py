
import csv
from pathlib import Path

ROOT = Path(__file__).parent
AUDIO = ROOT / "audio"
TRANSCRIPTS = ROOT / "transcripts" / "urdu_transcripts.csv"
ANNOTATIONS = ROOT / "annotations"

def read_csv(filename):
    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))

errors = []

transcripts = read_csv(TRANSCRIPTS)
audio_ids = {row["audio_id"] for row in transcripts}

print("Transcript records:", len(transcripts))

# Check audio files
for audio_id in audio_ids:
    if not (AUDIO / f"{audio_id}.mp3").exists():
        errors.append(f"Missing audio: {audio_id}.mp3")

# Check annotation files
for filename in [
    "speaker_annotations.csv",
    "language_annotations.csv",
    "sentiment_annotations.csv",
]:
    rows = read_csv(ANNOTATIONS / filename)
    annotated_ids = {row["audio_id"] for row in rows}

    print(f"{filename}: {len(rows)} records")

    missing = audio_ids - annotated_ids
    extra = annotated_ids - audio_ids

    if missing:
        errors.append(f"{filename}: missing {len(missing)} recordings")
    if extra:
        errors.append(f"{filename}: contains unknown recordings")

ner_rows = read_csv(ANNOTATIONS / "ner_annotations.csv")
print("NER records:", len(ner_rows))

ner_ids = {row["audio_id"] for row in ner_rows}
unknown_ner_ids = ner_ids - audio_ids

if unknown_ner_ids:
    print("Unknown NER audio IDs:", unknown_ner_ids)
    errors.append("ner_annotations.csv: contains unknown recordings")
print("\nErrors found:", len(errors))

for error in errors:
    print("-", error)

if not errors and len(transcripts) == 20:
    print("Basic dataset validation passed!")
else:
    print("Please review the errors above.")
