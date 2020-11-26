# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            if object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            if object_type == "dt":
                time_step = float(line.split()[1].lower())
            else:
                pass

    return objects, time_step


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    star.R = float(line.split()[1].lower())
    star.color = line.split()[2].lower()
    star.m = float(line.split()[3].lower())
    star.x = float(line.split()[4].lower())
    star.y = float(line.split()[5].lower())
    star.Vx = float(line.split()[6].lower())
    star.Vy = float(line.split()[7].lower())
    

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet.R = float(line.split()[1].lower())
    planet.color = line.split()[2].lower()
    planet.m = float(line.split()[3].lower())
    planet.x = float(line.split()[4].lower())
    planet.y = float(line.split()[5].lower())
    planet.Vx = float(line.split()[6].lower())
    planet.Vy = float(line.split()[7].lower())


def write_space_objects_data_to_file(output_filename, space_objects,
                                     time_step):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    **time_step** — шаг времени для данной системы
    """
    
    with open(output_filename, 'w') as out_file:
        print(space_objects[0].type, space_objects[0].R, 
              space_objects[0].color, space_objects[0].m, 
              space_objects[0].x, space_objects[0].y,
              space_objects[0].Vx, space_objects[0].Vy, 
              end = '\n', file = out_file)
        print(end = '\n', file = out_file)
        
        print("# dt", end = '\n', file = out_file)
        print("dt", time_step, end = '\n', file = out_file)
        print(end = '\n', file = out_file)

        for i in range(len(space_objects) - 1):
                print(space_objects[i + 1].type, space_objects[i + 1].R, 
                      space_objects[i + 1].color, space_objects[i + 1].m, 
                      space_objects[i + 1].x, space_objects[i + 1].y,
                      space_objects[i + 1].Vx, space_objects[i + 1].Vy, 
                      end = '\n', file = out_file)
                print(end = '\n', file = out_file)


if __name__ == "__main__":
    print("This module is not for direct call!")
