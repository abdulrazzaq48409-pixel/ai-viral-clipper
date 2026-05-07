def detect_viral_segments(result):

    viral_keywords = [

        # Emotion
        "cry", "pain", "sad", "emotional",
        "hurt", "family", "mother", "father",

        # Urdu / Roman Urdu
        "rona", "dukhi", "maa", "baap",

        # Controversy
        "fight", "jhagra", "viral",
        "exposed", "truth", "secret",

        # Money
        "crore", "lakh", "money",
        "paisa", "rich", "poor",

        # Relationships
        "shaadi", "breakup",
        "love", "divorce",

        # Engagement
        "why", "how", "shocking",
        "insane", "danger"
    ]

    viral_clips = []

    used_ranges = []

    segments = result["segments"]

    for segment in segments:

        text = segment["text"].lower()

        score = 0

        # Hook detection
        hook_phrases = [
            "i never",
            "truth is",
            "nobody knows",
            "secret",
            "exposed",
            "shocking",
            "listen",
            "believe me",
            "real story",
            "viral",
            "danger",
            "he said",
            "she said",
            "finally"
        ]

        for phrase in hook_phrases:

            if phrase in text:
                score += 3

        # Keyword scoring
        for keyword in viral_keywords:

            if keyword in text:
                score += 1

        # Engagement boosts
        if "?" in text:
            score += 1

        if "!" in text:
            score += 1

        # Minimum score
        if score >= 1:

            # Faster pacing
            start = max(0, segment["start"] - 1.5)

            end = segment["end"] + 3

            # Max 45 sec clips
            if (end - start) > 45:
                end = start + 45

            # Prevent duplicates
            duplicate = False

            for used_start, used_end in used_ranges:

                overlap = (
                    min(end, used_end)
                    - max(start, used_start)
                )

                if overlap > 15:
                    duplicate = True
                    break

            if duplicate:
                continue

            used_ranges.append((start, end))

            clip = {
                "start": start,
                "end": end,
                "text": segment["text"],
                "score": score
            }

            viral_clips.append(clip)

    # Sort strongest first
    viral_clips.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # Keep top clips
    viral_clips = viral_clips[:20]

    return viral_clips