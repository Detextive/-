import argparse

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().split()
        return list(map(float, data)) 

def main():
    
    parser = argparse.ArgumentParser(description='Проверка расположения точек относительно окружности.')

    
    parser.add_argument('circle_file', type=str, help='Путь к файлу с центром и радиусом окружности')
    parser.add_argument('points_file', type=str, help='Путь к файлу с точками')

    
    args = parser.parse_args()

    
    circle = read_file(args.circle_file)
    points = read_file(args.points_file)

   
    for index in range(0, len(points), 2):
        x, y = points[index], points[index + 1]
        
        distance = ((x - circle[0]) ** 2 + (y - circle[1]) ** 2) ** 0.5
        radius = circle[2]
        
        
        if distance == radius:
            print('0')  
        elif distance < radius:
            print('1')  
        else:
            print('2')  

if __name__ == '__main__':
    main()
