def statement_message(option, balance_amount, value, data):
    if option == 1:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {data:^33} |"}
{"+" + "-" * 35 + "+"}
{f"| {"Deposit amount":^22}|" + f"{f"R${value:.2f}":<11}|"}
{"+" + "-" * 35 + "+"}
{f"| {"Balance amount":^22}|" + f"{f"R${balance_amount:.2f}":<11}|"}
{"+" + "-" * 35 + "+"}
"""

    elif option == 2:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {data:^35} |"}
{"+" + "-" * 35 + "+"}
{f"| {"withdrawal amount":^22}|" + f"{f"R${value:.2f}":<11}|"}
{"+" + "-" * 35 + "+"}
{f"| {"Balance amount":^22}|" + f"{f"R${balance_amount:.2f}":<11}|"}
{"+" + "-" * 35 + "+"}
"""
    
