def meal_time(military_time):
  hour, minutes = military_time.split(":")
  hour = int(hour)
  if hour < 8 and hour >= 7:
    return "Breakfast"
  elif hour < 13 and hour >= 12:
    return "Lunch"
  elif hour < 19 and hour >= 18:
    return "Dinner"
  else:
    return("Nothing right now.")
print("11:02 =>", meal_time("11:02"))
print("03:32 =>", meal_time("03:32"))
print("15:00 =>", meal_time("15:00"))
print("19:00 =>", meal_time("19:00"))
print("18:30 =>", meal_time("18:30"))
print("8:45 =>", meal_time("8:45"))

def get_filename_extension(file):
 filename, fileExtenstion = file.split(".")
 return fileExtenstion
print("hello.json => ", get_filename_extension("hello.json"))
print("hello.csv => ", get_filename_extension("hello.csv"))

def is_image_file(filename):
  file, extension = filename.split(".")
  if extension == "jpg" or extension == "png" or extension == "jpeg" or extension == "gif" or extension == "tiff":
    return True
  else:
    return False
    
print("hello.jpg => ", is_image_file("hello.jpg"))
print("hello.jpeg => ", is_image_file("hello.jpeg"))
print("hello.png => ", is_image_file("hello.png"))
print("hello.gif => ", is_image_file("hello.gif"))
print("hello.tiff => ", is_image_file("hello.tiff"))
print("hello.json => ", is_image_file("hello.json"))