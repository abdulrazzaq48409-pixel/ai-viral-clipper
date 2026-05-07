import random

def generate_title(text):

    hooks = [
        "He Finally Revealed...",
        "This Changed Everything...",
        "Nobody Expected This...",
        "The Truth Comes Out...",
        "This Went Viral For A Reason...",
        "What He Said Shocked Everyone...",
        "This Moment Is Insane...",
        "The Most Emotional Moment...",
        "This Got Everyone Talking...",
        "Unexpected Confession..."
    ]

    hook = random.choice(hooks)

    short_text = text[:60]

    title = f"{hook} | {short_text}"

    return title