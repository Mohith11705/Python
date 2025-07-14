import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data Loaded Successfully!")
        return df
    except FileNotFoundError:
        print("File not found.")
        return None

def total_revenue(df):
    return df["Amount"].sum()

def revenue_by_customer(df):
    return df.groupby("Customer")["Amount"].sum()

def revenue_by_product(df):
    return df.groupby("Product")["Amount"].sum()

def daily_sales(df):
    return df.groupby("Date")["Amount"].sum()

def high_value_orders(df, threshold=1000):
    return df[df["Amount"] > threshold]

def export_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"✅ Exported to '{filename}'")

def main():
    df = load_data("sales.csv")
    if df is None:
        return

    print("\n💰 Total Revenue: ₹", total_revenue(df))

    print("\n🧍 Revenue by Customer:")
    print(revenue_by_customer(df))

    print("\n📦 Revenue by Product:")
    print(revenue_by_product(df))

    print("\n📅 Daily Sales:")
    print(daily_sales(df))

    high_orders = high_value_orders(df)
    print("\n🔍 High-Value Orders (> ₹1000):")
    print(high_orders)

    export_to_csv(high_orders, "high_value_orders.csv")
if __name__ == "__main__":
    main()