import turtle as t
t.bgcolor('black')
planet_name = ['sun','mercury','venus','earth','mars','jupiter','saturn','uranus','neptune']
planet_color = ['yellow','#E2E2E2','#8b7d82','blue','red','orange','#dad2be','#B4DADD','#7197E1']
planet_radius = [0,110,160,210,260,310,360,410,460,510]
planet_size = [5,0.5,0.9,1,0.7,2,1.8,1.5,1.5]
planet_speed = [0,40,35,30,25,20,15,10,5]
planet = [t.Turtle() for i in range (9)]
  
def planet_config(planet,color,size,radius):
    planet.speed(0)
    planet.pencolor('white')
    planet.shape('circle')
    planet.color(color)
    planet.shapesize(size,size)
    planet.penup()
    planet.fd(radius)
    planet.lt(90)

planet_config(planet[0],planet_color[0],planet_size[0],0)
for p in range (1,9):
    planet_config(planet[p],planet_color[p],planet_size[p],p*50+60)

while(True):
    for i in range (1,9):
        planet[i].pendown()
        planet[i].circle(planet_radius[i],planet_speed[i])
    
