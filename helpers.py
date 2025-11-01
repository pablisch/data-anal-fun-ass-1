def is_significant(p_value, alpha=0.05):
    if p_value < alpha:
        print(f"✅ The difference is significant\nThe p-value: {p_value} is {alpha - p_value} less than the alpha: {alpha}\nThe null hypothesis is rejected")
        return True
    elif p_value > alpha:
        print(f"❌ The difference is not significant\nThe p-value: {p_value} is {p_value - alpha} more than the alpha: {alpha}\nThe null hypothesis is NOT rejected")
        return False
    else:
        print(f"❓The p-value: {p_value} is equal to the alpha: {alpha}\nI am not sure what this means in terms of rejecting the null hypothesis")
        return False
