"""Lesson 1: collect a user-defined goal and a small experiment.

This is a fixed planning exercise, not an AI conversation yet.
Run with: python3 main.py
"""


def ask(question):
    """Keep asking until the user enters an answer or chooses to quit."""
    while True:
        answer = input(question + "\n> ").strip()
        if answer.lower() == "q":
            raise SystemExit("Session ended. Nothing was saved by this program.")
        if answer:
            return answer
        print("Enter a short answer, or q to stop.\n")


def run_session():
    print("Life Companion — first Python prototype")
    print("A fixed planning exercise for adult testers; no AI is connected.")
    print("Use a fictional example. Avoid names and sensitive details.")
    print("Answers are not saved or sent by this program.")
    print("They remain visible in your terminal. Type q to stop.\n")

    plan = {}
    plan["goal"] = ask("What would you like to work toward?")
    plan["meaning"] = ask("Why does this matter to you personally?")
    plan["context"] = ask(
        "What resources or limits should a realistic plan respect?"
    )
    plan["assumption"] = ask(
        "What is one assumption about this path that you need to check?"
    )
    plan["experiment"] = ask(
        "What small action could help you learn whether this path fits you?"
    )
    plan["review"] = ask(
        "When will you review it, and what would make you change direction?"
    )

    print("\nYour draft plan — your words, for you to revise:")
    labels = {
        "goal": "Goal",
        "meaning": "Why it matters",
        "context": "Resources and limits",
        "assumption": "Assumption to check",
        "experiment": "Small experiment",
        "review": "Review point",
    }
    for key, label in labels.items():
        print(f"{label}: {plan[key]}")
    print("\nThis exercise has not evaluated the plan or checked any facts.")


if __name__ == "__main__":
    try:
        run_session()
    except (EOFError, KeyboardInterrupt):
        print("\nSession stopped.")
