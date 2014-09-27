from turtle import left,forward,right,width,speed,color

)       


left(180)
distances = [250 * 0.5, 250 * 0.3, 250 * 0.2]
for counter in range(0,6):
    if counter < 3:
        distance_index = counter
    else:
        distance_index = 5 - counter
    distance = distances[distance_index] / 57.5
    for degree in range(0,90):
        forward(distance)
        right(2)
    if counter != 2:
        left(180)
left(90)
