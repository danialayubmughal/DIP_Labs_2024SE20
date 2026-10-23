# Exercise 1: Variables and Data Types
width = 640
height = 480
image_name = "sample.png"
is_color = True

print(width, type(width))
print(height, type(height))
print(image_name, type(image_name))
print(is_color, type(is_color))

total_pixels = width * height
print("Total Pixels:", total_pixels)

# # Exercise 2: if, elif, else
# print("\nExercise 2")

# for intensity in [-1, 0, 127, 128, 255, 256]:
#     if intensity < 0 or intensity > 255:
#         print(intensity, "Invalid")
#     elif intensity >= 128:
#         print(intensity, "Bright pixel")
#     else:
#         print(intensity, "Dark pixel")

# # Exercise 3: Loops
# print("\nExercise 3")

# for pixel in [20, 130, 255]:
#     if pixel >= 128:
#         print(pixel, "Bright pixel")
#     else:
#         print(pixel, "Dark pixel")

# i = 0
# while i < 3:
#     print(i)
#     i += 1

# # Exercise 4: Function
# print("\nExercise 4")

# def is_bright(pixel, threshold=128):
#     return pixel >= threshold

# print(is_bright(127))
# print(is_bright(128))
# print(is_bright(200, 210))

# # Exercise 5: Lists and Tuples
# print("\nExercise 5")

# pixels = [0, 128, 255]
# print("First Item:", pixels[0])

# pixels[1] = 150
# pixels.append(64)

# print("List:", pixels)
# print("Length:", len(pixels))

# size = (640, 480)
# width, height = size
# print(width, height)

# # List can change, tuple cannot.

# # Exercise 6: Dictionary and Set
# print("\nExercise 6")

# image = {"width": 640, "height": 480}
# image["mode"] = "RGB"

# print(image["width"])
# print(image["mode"])

# labels = {"cat", "dog", "cat", "bird"}
# print("Unique labels:", len(labels))