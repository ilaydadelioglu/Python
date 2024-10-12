class Solution:
    def ContainerLoading(self, capacity, weight):
        weight.sort()  # Ağırlıkları küçükten büyüğe sırala
        print("Sorted container weights:", weight)  # Sıralanmış ağırlıkları yazdır

        containers_loaded = 0
        i = 0
        while i < len(weight) and weight[i] <= capacity:
            containers_loaded += 1
            capacity -= weight[i]
            i += 1
        return containers_loaded

if __name__ == "__main__":
    capacity = int(input("Enter the capacity of the ship: "))  # Gemi kapasitesi girişi
    n = int(input("Enter the number of containers: "))  # Konteyner sayısı girişi
    weight = list(map(int, input("Enter the weights of containers: ").split()))  # Konteyner ağırlıkları girişi

    sol = Solution()
    num_of_containers = sol.ContainerLoading(capacity, weight)
    print("Number of containers loaded:", num_of_containers)
