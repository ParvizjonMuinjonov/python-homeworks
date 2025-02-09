kilometer_input = int(input("Kilometrni kiriting: "))

meter_convert = kilometer_input * 1000
centimeter_convert = kilometer_input * 100000

print(f"Siz kiritgan {kilometer_input} kilometr masofa metrlarda {meter_convert} metr bo'ladi.")
print(f"Siz kiritgan {kilometer_input} kilometr masofa santimetrlarda {centimeter_convert} santimetr bo'ladi.")