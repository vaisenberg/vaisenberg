import re
import json

text = "On my trip to Paris, I spent $500 on accommodation, €150 on food, and £100 on activities. I traveled from 12th June 2024 to 18th June 2024."

# Regex patterns
date_pattern = r"(\d{1,2}[a-z]{2}\s[A-Za-z]+\s\d{4})"
location_pattern = r"trip to\s([A-Za-z\s]+)"
cost_pattern = r"([$\€\£\¥])(\d+(?:\.\d{1,2})?)\s(on\s([a-zA-Z\s]+))?"  # Added context capture
rating_pattern = r"(\d(\.\d)?)\s?stars?"

# Find all matches
dates = re.findall(date_pattern, text)
locations = re.findall(location_pattern, text)
costs = re.findall(cost_pattern, text)

# Categorize costs into hotel, food, activities
categorized_costs = {
    "hotel": [],
    "food": [],
    "activities": []
}

# Match context and assign costs to appropriate category
for cost in costs:
    amount = cost[1]
    currency = cost[0]
    context = cost[3]
    
    if context:
        if "accommodation" in context or "hotel" in context:
            categorized_costs["hotel"].append({"currency": currency, "amount": amount})
        elif "food" in context:
            categorized_costs["food"].append({"currency": currency, "amount": amount})
        elif "activities" in context:
            categorized_costs["activities"].append({"currency": currency, "amount": amount})

# Create a dictionary to store the data
data = {
    "dates": dates,
    "locations": locations,
    "costs": categorized_costs
}

# Dump the data into JSON
json_data = json.dumps(data, indent=4)
print(json_data)
