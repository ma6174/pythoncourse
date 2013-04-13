def main():
    turtle.clearscreen()
    pen = turtle.Turtle()
    pen.speed('fastest')
    senegal_file = open('senegal.txt')
    senegal_flag = Flag(senegal_file)
    print(senegal_flag)
    senegal_flag.draw(pen)
    senegal_file.close()

    time.sleep(4)   # delay so you can see your flag
    turtle.clearscreen()
    panama_file = open('panama.txt')
    panama_flag = Flag(panama_file)
    print(panama_flag)
    panama_flag.draw(pen)
    panama_file.close()
    
