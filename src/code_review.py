import math


class PathCalculator():

    def __init__(self):
        self.locations = {}
        self.max_distance = 0
        self.result_locations = None

    def process(self, line):
        string_list = line.split(':')
        if len(string_list) != 3:
            return None
        location1 = string_list[0]
        location2 = string_list[1]
        distance = int(string_list[2])
        if location1 not in self.locations:
            self.locations[location1] = [(distance, location2)]
        else:
            self.locations[location1].append((distance, location2))
            self.locations[location1].sort()
        if location2 not in self.locations:
            self.locations[location2] = [(distance, location1)]
        else:
            self.locations[location2].append((distance, location1))
            self.locations[location2].sort()
        for location in self.locations:
            if len(self.locations[location]) > 1 and self.max_distance < (self.locations[location][-1][0] + self.locations[location][-2][0]):
                self.max_distance = self.locations[location][-1][0] + self.locations[location][-2][0]
                self.result_locations = [self.locations[location][-1][1], location, self.locations[location][-2][1]]
        if self.result_locations:
            return ':'.join([str(self.max_distance)] + self.result_locations)
        else:
            return 'NONE'


def is_valid(text):
    if len(text) != 8:
        return 'INVALID'
    first = int(text[0]) if text[0].isdigit() else ord(text[0].capitalize()) - ord('A') + 10
    second = int(text[1]) if text[1].isdigit() else ord(text[1].capitalize()) - ord('A') + 10
    target = first * 16 + second
    count = 0
    for letter in text[2:]:
        if letter.isdigit():
            count = count * 16 + int(letter)
        else:
            count = count * 16 + ord(letter.capitalize()) - ord('A') + 10
    total = 0
    while count > 0:
        total += count % 10
        count //= 10
    if total == target:
        return 'VALID'
    else:
        return 'INVALID'


def find_multiples_3or5(upper):
    if upper < 3:
        return None
    elif upper < 5:
        return [3]

    def dfs(cur_num, maxnum, collector):
        if cur_num > maxnum:
            return
        if cur_num not in collector:
            collector.add(cur_num)
        dfs(cur_num * 3, maxnum, collector)
        dfs(cur_num * 5, maxnum, collector)

    result = set()
    dfs(1, upper, result)
    result.remove(1)
    return list(result)


class DistanceCalculator():

    def __init__(self):
        self.locations = {}
        self.radius = 3958.8

    def process(self, line):
        if line[0] == 'L':
            string_list = line.split(':')
            if string_list[1] not in self.locations:
                latitude = math.radians(float(string_list[2]))
                longitude = math.radians(float(string_list[3]))
                self.locations[string_list[1]] = (latitude, longitude)
            return string_list[1]
        elif line[0] == 'T':
            string_list = line.split(':')
            member_account = string_list[1]
            if string_list[2] in self.locations and string_list[3] in self.locations:
                location1 = self.locations[string_list[2]]
                location2 = self.locations[string_list[3]]
                longitude_difference = abs(location1[1] - location2[1])
                angle = math.acos(math.sin(location1[0]) * math.sin(location2[0])
                                  + math.cos(location1[0]) * math.cos(location2[0]) * math.cos(longitude_difference))
                distance = int(self.radius * angle)
                return ':'.join([member_account, string_list[2], string_list[3], str(distance)])
            else:
                return 'NONE'


test1 = PathCalculator()
print(test1.process('a:b:1'))
print(test1.process('c:b:2'))
print(test1.process('c:e:4'))
print(test1.process('d:c:6'))
print(test1.process('f:g:12'))

print(is_valid('1CC0FfEE'))

print(find_multiples_3or5(100))

test2 = DistanceCalculator()
print(test2.process('LOC:a:41.836944:-87.694722'))
print(test2.process('LOC:b:40.7127:-74.0059'))
print(test2.process('TRIP:ISAAC:a:b'))

