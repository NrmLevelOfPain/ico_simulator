import json

# ICO Simulation Parameters
class ICOSimulator:
    def __init__(self, total_supply, token_price, funding_goal):
        self.total_supply = total_supply
        self.token_price = token_price
        self.funding_goal = funding_goal
        self.tokens_sold = 0
        self.funds_raised = 0
        self.participants = {}

    def contribute(self, participant, contribution_amount):
        tokens_to_allocate = contribution_amount / self.token_price
        if self.tokens_sold + tokens_to_allocate > self.total_supply:
            tokens_to_allocate = self.total_supply - self.tokens_sold

        if tokens_to_allocate > 0:
            self.tokens_sold += tokens_to_allocate
            self.funds_raised += tokens_to_allocate * self.token_price
            self.participants[participant] = self.participants.get(participant, 0) + tokens_to_allocate
        else:
            print(f"No more tokens available for {participant}!")

    def get_progress(self):
        return {
            "total_supply": self.total_supply,
            "tokens_sold": self.tokens_sold,
            "tokens_remaining": self.total_supply - self.tokens_sold,
            "funds_raised": self.funds_raised,
            "funding_goal": self.funding_goal,
            "participants": self.participants,
        }

    def save_progress(self, filename="ico_progress.json"):
        with open(filename, "w") as f:
            json.dump(self.get_progress(), f, indent=4)
        print(f"ICO progress saved to {filename}")

# Example Usage
if __name__ == "__main__":
    ico = ICOSimulator(total_supply=1000000, token_price=0.01, funding_goal=10000)

    # Simulated contributions
    ico.contribute("Alice", 100)
    ico.contribute("Bob", 5000)
    ico.contribute("Charlie", 20000)
    ico.contribute("Alice", 3000)

    # Output progress
    progress = ico.get_progress()
    print(json.dumps(progress, indent=4))

    # Save to file
    ico.save_progress()
