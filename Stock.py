print("\n\n\t\tWelcome To The Stock Trading Expert System\n")
print("\tNote: Please answer the following questions honestly\n\n")

QUESTIONS = [
    "Is the stock market trending upward today?",
    "Is the company showing strong quarterly results?",
    "Is the stock undervalued based on your analysis?",
    "Are analysts recommending to BUY the stock?",
    "Do you plan to hold the stock for more than 6 months?",
    "Do you have spare cash you can invest without stress?",
    "Are there any upcoming positive announcements/events?",
    "Is the stock in a sector that is performing well?",
    "Has the stock price recently corrected (dropped a bit)?"
]

THRESHOLD = {
    'Buy': 60,
    'Hold': 30,
    'Sell': 0
}

def tradingExpertSystem(questions, threshold):
    score = 0

    for question in questions:
        print(question + " (Y/N)")
        ans = input("> ")
        if ans.lower() == 'y':
            print('On a scale of 1-10, how confident are you?')
            ip = input('> ')
            while not ip.isnumeric() or int(ip) < 1 or int(ip) > 10:
                print('Enter a valid number from 1 to 10!')
                ip = input('> ')
            score += int(ip)

    print("\n---------------------------------------------\n")

    if score >= threshold['Buy']:
        print("✅ Recommendation: BUY the Stock")
        print("Your analysis and confidence indicate a strong buy opportunity.")
    elif score >= threshold['Hold']:
        print("➖ Recommendation: HOLD the Stock")
        print("Market and stock indicators are neutral. Consider holding.")
    else:
        print("❌ Recommendation: SELL the Stock or AVOID Buying")
        print("Conditions are not favorable for investment at this time.")

    print("\nFinal Score:", score)

if __name__ == '__main__':
    tradingExpertSystem(QUESTIONS, THRESHOLD)
