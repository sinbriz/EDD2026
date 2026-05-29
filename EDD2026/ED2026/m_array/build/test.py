import m_array

# Crear array con índices 1..10
arr = m_array.IntArray(10, 1)

# Asignar valores
for i in range(1, 11):
    arr[i] = i * 10

# Mostrar valores
print(f"Longitud: {len(arr)}")
print("Elementos:")
for i in range(1, 11):
    print(f"arr[{i}] = {arr[i]}")

# Mostrar representación completa
print("\nArray completo:")
print(arr)