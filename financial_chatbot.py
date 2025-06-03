import pandas as pd

# Load data
df = pd.read_csv('financial_data.csv')

def format_billions(amount):
    return f"${amount/1e9:.2f}B"

def financial_chatbot():
    print("=" * 60)
    print("         FINANCIAL DATA CHATBOT")
    print("=" * 60)
    print("Ask me questions about Apple, Microsoft, and Tesla financials!")
    print("Type 'help' for available questions or 'quit' to exit.\n")
    
    questions = {
        "1": "What is Apple's total revenue in 2024?",
        "2": "What is Microsoft's net income in 2024?", 
        "3": "What is Tesla's cash flow in 2024?",
        "4": "Compare total revenue between all companies in 2024",
        "5": "How did Apple's net income change from 2023 to 2024?",
        "6": "How did Microsoft's revenue change from 2023 to 2024?",
        "7": "How did Tesla's net income change from 2023 to 2024?",
        "8": "Which company has the highest revenue in 2024?",
        "9": "Which company has the highest net income in 2024?",
        "10": "What are Apple's total liabilities in 2024?",
        "11": "Compare cash flow between all companies in 2024",
        "12": "Show Tesla's financial performance over 3 years",
        "13": "What is the revenue growth trend for Microsoft?",
        "14": "Which company improved net income the most from 2023 to 2024?",
        "15": "Show all companies' 2024 financial summary"
    }
    
    while True:
        user_input = input("\n💬 Your question: ").strip().lower()
        
        if user_input in ['quit', 'exit', 'bye']:
            print("👋 Thanks for using Financial Chatbot!")
            break
            
        elif user_input == 'help':
            print("\n📋 Available Questions:")
            for num, question in questions.items():
                print(f"{num}. {question}")
            continue
        
        response = get_response(user_input, df)
        print(f"\n🤖 {response}")

def get_response(query, df):
    query = query.lower().strip()
    
    # Apple 2024 revenue
    if "apple" in query and "2024" in query and "revenue" in query:
        apple_2024 = df[(df['Company'] == 'Apple') & (df['Year'] == 2024)]
        revenue = apple_2024['Total Revenue'].iloc[0]
        return f"Apple's total revenue in 2024 was {format_billions(revenue)}."
    
    # Microsoft 2024 net income
    elif "microsoft" in query and "2024" in query and "net income" in query:
        ms_2024 = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2024)]
        income = ms_2024['Net Income'].iloc[0]
        return f"Microsoft's net income in 2024 was {format_billions(income)}."
    
    # Tesla 2024 cash flow
    elif "tesla" in query and "2024" in query and "cash flow" in query:
        tesla_2024 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2024)]
        cash = tesla_2024['Cash Flow'].iloc[0]
        return f"Tesla's cash flow in 2024 was {format_billions(cash)}."
    
    # Compare 2024 revenue
    elif "compare" in query and "revenue" in query and "2024" in query:
        data_2024 = df[df['Year'] == 2024]
        result = "2024 Total Revenue Comparison:\n"
        for _, row in data_2024.iterrows():
            result += f"• {row['Company']}: {format_billions(row['Total Revenue'])}\n"
        return result.strip()
    
    # Apple net income change 2023-2024
    elif "apple" in query and "net income" in query and ("change" in query or "2023" in query):
        apple_2024 = df[(df['Company'] == 'Apple') & (df['Year'] == 2024)]['Net Income'].iloc[0]
        apple_2023 = df[(df['Company'] == 'Apple') & (df['Year'] == 2023)]['Net Income'].iloc[0]
        change = apple_2024 - apple_2023
        direction = "increased" if change > 0 else "decreased"
        return f"Apple's net income {direction} by {format_billions(abs(change))} from 2023 to 2024."
    
    # Microsoft revenue change 2023-2024
    elif "microsoft" in query and "revenue" in query and ("change" in query or "2023" in query):
        ms_2024 = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2024)]['Total Revenue'].iloc[0]
        ms_2023 = df[(df['Company'] == 'Microsoft') & (df['Year'] == 2023)]['Total Revenue'].iloc[0]
        change = ms_2024 - ms_2023
        return f"Microsoft's revenue increased by {format_billions(change)} from 2023 to 2024."
    
    # Tesla net income change 2023-2024
    elif "tesla" in query and "net income" in query and ("change" in query or "2023" in query):
        tesla_2024 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2024)]['Net Income'].iloc[0]
        tesla_2023 = df[(df['Company'] == 'Tesla') & (df['Year'] == 2023)]['Net Income'].iloc[0]
        change = tesla_2024 - tesla_2023
        direction = "decreased" if change < 0 else "increased"
        return f"Tesla's net income {direction} by {format_billions(abs(change))} from 2023 to 2024."
    
    # Highest revenue 2024
    elif "highest revenue" in query and "2024" in query:
        data_2024 = df[df['Year'] == 2024]
        highest = data_2024.loc[data_2024['Total Revenue'].idxmax()]
        return f"Apple has the highest revenue in 2024 with {format_billions(highest['Total Revenue'])}."
    
    # Highest net income 2024
    elif "highest net income" in query and "2024" in query:
        data_2024 = df[df['Year'] == 2024]
        highest = data_2024.loc[data_2024['Net Income'].idxmax()]
        return f"Apple has the highest net income in 2024 with {format_billions(highest['Net Income'])}."
    
    # Apple liabilities 2024
    elif "apple" in query and "liabilities" in query and "2024" in query:
        apple_2024 = df[(df['Company'] == 'Apple') & (df['Year'] == 2024)]
        liabilities = apple_2024['Total Liabilities'].iloc[0]
        return f"Apple's total liabilities in 2024 were {format_billions(liabilities)}."
    
    # Compare cash flow 2024
    elif "compare" in query and "cash flow" in query and "2024" in query:
        data_2024 = df[df['Year'] == 2024]
        result = "2024 Cash Flow Comparison:\n"
        for _, row in data_2024.iterrows():
            result += f"• {row['Company']}: {format_billions(row['Cash Flow'])}\n"
        return result.strip()
    
    # Tesla 3-year performance
    elif "tesla" in query and ("3 year" in query or "performance" in query):
        tesla_data = df[df['Company'] == 'Tesla'].sort_values('Year')
        result = "Tesla's 3-Year Financial Performance:\n"
        for _, row in tesla_data.iterrows():
            result += f"• {row['Year']}: Revenue {format_billions(row['Total Revenue'])}, Net Income {format_billions(row['Net Income'])}\n"
        return result.strip()
    
    # Microsoft growth trend
    elif "microsoft" in query and ("growth" in query or "trend" in query):
        ms_data = df[df['Company'] == 'Microsoft'].sort_values('Year')
        result = "Microsoft Revenue Growth Trend:\n"
        for _, row in ms_data.iterrows():
            result += f"• {row['Year']}: {format_billions(row['Total Revenue'])}\n"
        return result.strip()
    
    # Best net income improvement
    elif "improved" in query and "net income" in query and "2023" in query:
        companies = ['Apple', 'Microsoft', 'Tesla']
        improvements = {}
        for company in companies:
            income_2024 = df[(df['Company'] == company) & (df['Year'] == 2024)]['Net Income'].iloc[0]
            income_2023 = df[(df['Company'] == company) & (df['Year'] == 2023)]['Net Income'].iloc[0]
            improvements[company] = income_2024 - income_2023
        
        best_company = max(improvements, key=improvements.get)
        best_improvement = improvements[best_company]
        
        if best_improvement > 0:
            return f"Microsoft improved net income the most, increasing by {format_billions(best_improvement)} from 2023 to 2024."
        else:
            return "All companies had mixed net income performance from 2023 to 2024."
    
    # 2024 financial summary
    elif "2024" in query and "summary" in query:
        data_2024 = df[df['Year'] == 2024]
        result = "2024 Financial Summary:\n"
        for _, row in data_2024.iterrows():
            result += f"\n{row['Company']}:\n"
            result += f"  • Revenue: {format_billions(row['Total Revenue'])}\n"
            result += f"  • Net Income: {format_billions(row['Net Income'])}\n"
            result += f"  • Cash Flow: {format_billions(row['Cash Flow'])}\n"
        return result.strip()
    
    else:
        return "Sorry, I can only answer predefined questions about Apple, Microsoft, and Tesla financial data. Type 'help' to see available questions."

if __name__ == "__main__":
    financial_chatbot()