import matplotlib.pyplot as plt


def read_file(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


def process_data(data: list) -> dict:
    sales_dict = {}
    for line in data:
        date, sales = line.strip().split(",")
        sales_dict[date] = int(sales)
    return sales_dict


def print_sales_data(sales_data: dict, product_name: str) -> None:
    print(f"Продажи {product_name}:")
    print(f"{'Дата':<10} {'Продажи':>10}")
    print("-" * 21)
    for date, sales in sorted(sales_data.items()):
        print(f"{date:<10} {sales:>10}")
    print()


def filter_data(data: dict, threshold: int) -> dict:
    return {date: sales for date, sales in data.items() if sales > threshold}


def aggregate_data(data: dict) -> int:
    return sum(data.values())


def visualize_data(aggregated_data: dict) -> None:
    products = list(aggregated_data.keys())
    sales = list(aggregated_data.values())

    plt.figure(figsize=(10, 5))
    plt.bar(products, sales, color=["blue", "orange", "green"])

    plt.xlabel("Продукты")
    plt.ylabel("Суммарные продажи")
    plt.title("Суммарные продажи по продуктам")
    plt.show()


def main(file_paths: list, threshold: int) -> None:
    all_data = {}

    for file_path in file_paths:
        data = read_file(file_path)
        sales_data = process_data(data)
        filtered_sales_data = filter_data(sales_data, threshold)
        total_sales = aggregate_data(filtered_sales_data)
        product_name = file_path.split(".")[
            0
        ].capitalize()  # Получаем название продукта из имени файла
        all_data[product_name] = total_sales

        print(f"Продукт: {product_name}")
        print(f"Все продажи:")
        print_sales_data(sales_data, product_name)
        print(f"Продажи больше {threshold=}:")
        print_sales_data(filtered_sales_data, product_name)
        print(f"Суммарные продажи: {total_sales}")
        print("-" * 40)

    visualize_data(all_data)


# Список файлов с данными
file_paths = ["apple.txt", "banana.txt", "pear.txt"]

# Порог для фильтрации
threshold = 200

main(file_paths, threshold)
