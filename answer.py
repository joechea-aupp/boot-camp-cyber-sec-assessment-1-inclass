import os

# print(os.listdir())
directories = []
for item in os.listdir():
    if os.path.isdir(item):
        directories.append(item)

print(len(directories))
# print(len(os.listdir()))

# with open("135", "r") as file:
#     # print(file.readlines())
#     data = file.readlines()
#
#     numbers = []
#     for item in data:
#         numbers.append(int(item.strip()))
#
#     print(max(numbers))
#     print(sum(numbers))
#     avg = sum(numbers) / len(numbers)
#     print(round(avg, 2))
