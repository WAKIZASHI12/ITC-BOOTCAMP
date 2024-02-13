ram_size_gb = 6
storage_size_gb = 512
storage_type = "SSD"
laptop_price = 900
laptop_condition = "новый"

if 4 <= ram_size_gb <= 8 and laptop_price <= 1000 and laptop_condition == "новый":
    if (storage_type == "SSD" and storage_size_gb >= 256) or (storage_type == "HDD" and storage_size_gb >= 1000):
        print("Выберите этот ноутбук")
    else:
        print("Не удовлетворяет требованиям по размеру жесткого диска.")
else:
    print("Не удовлетворяет общим требованиям.")

