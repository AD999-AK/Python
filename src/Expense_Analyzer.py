def expense_analyzer(expenses):
    if not expenses:
        return{
            "total" : 0,
            "average" : 0,
            "highest" : 0,            
            "lowest" : 0
        }
    total = sum(expenses)
    average = total/len(expenses)
    return {
            "total": total,
            "average": average,
            "highest": max(expenses),
            "lowest" : min(expenses)
    }
    
if __name__ == "__main__":
    raw = input("Enter expenses separated by space: ")
    expenses = list(map(float, raw.split()))
    analysis = expense_analyzer(expenses)
    print("Total:", analysis["total"])
    print("Average:", analysis["average"])
    print("Highest:" , analysis["highest"] )
    print("Lowest:" , analysis["lowest"])