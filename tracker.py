import os

# Datos detectados en el reporte de hoy
DEALS = [
    {"provider": "Nebula", "credits": "Variable", "link": "https://nebula.example.com/deals", "benefit": "Free credits for startups"},
    {"provider": "AWS", "credits": "$1000", "link": "https://aws.amazon.com/credits", "benefit": "Startup credits package"},
    {"provider": "Google Cloud", "credits": "$200", "link": "https://cloud.google.com/credits", "benefit": "Free tier credits"},
    {"provider": "Azure", "credits": "$500", "link": "https://azure.microsoft.com/credits", "benefit": "Cloud credits for devs"}
]

def main():
    print("--- Cloud Credits Tracker ---")
    next_steps = []
    
    for deal in DEALS:
        print(f"Provider: {deal['provider']} | Credits: {deal['credits']} | Link: {deal['link']}")
        next_steps.append(f"Apply to {deal['provider']}: {deal['link']} (Benefit: {deal['benefit']})")
    
    with open("next_steps.txt", "w") as f:
        f.write("\n".join(next_steps))
    
    print("\nSummary saved to next_steps.txt")

if __name__ == "__main__":
    main()