# 방금 그 곡
# 1차 66.7점 (4, 14, 15, 20 ~ 24, 29, 30 실패)
# 2차 90.0점 (20, 21, 30 실패)
# 3차 93.3점 (27, 28 실패) 
# 4차 성공 (정렬순서 조정)
# 문제 조건 중 조건이 일치하는 음악이 여러개일 때는 재생된 시간이 가장 긴 음악제목을 반환
# 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환


def solution(m, musicinfos):
    answer = []
    # m 변환 (#A -> a)
    mm = list(_ for _ in m)
    for l in range(len(mm)):
        if l < len(mm) and mm[l] == '#':
            mm[l-1] = mm[l-1].lower()
            mm.pop(l)
    m = ''.join(mm)

    # musicinfor 리스트 정리 4개씩
    music_info = []
    for i in musicinfos:
        music_info.append(i.split(','))

    for idx, info in enumerate(music_info):
        for i in range(len(info)):
            # 시간 숫자로 변환
            if i <= 1:
                a, b = info[i].split(':')
                info[i] = int(a) * 60 + int(b)
            # m 과 동일하게 변환(#A -> a)
            if i == 3:
                time = info[1] - info[0]
                new = list(_ for _ in info[i])
                for j in range(len(new)):
                    if j < len(new) and new[j] == '#':
                        new[j-1] = new[j-1].lower()
                        new.pop(j)
                
                # 음악 길이 조정
                time_x = time // len(new)
                time_y = time % len(new)
                if time >= len(new):
                    new  = ''.join(new * time_x + new[:time_y])
                else:
                    new = ''.join(new[:time])
                    
                if m in new:
                    answer.append([idx, time, info[2]])
    
    # answer 안에 저장된 값이 있을 경우
    # 재생된 시간이 가장 긴거 + 먼저 들어온 순서로 정렬 필요
    if answer:
        answer = sorted(answer, key= lambda x: (-x[1], x[0]))
        return answer[0][2]
    else:
        return '(None)'


# print(solution('ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB','13:00,13:05,WORLD,ABCDEF']))
# print(solution('CC#B', ['03:00','03:30','FOO','CC#B', '04:00','04:08','BAR','CC#BCC#BCC#B']))
# print(solution('ABC', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']))
# print(solution('CDEFGAC', ['12:00,12:06,HELLO,CDEFGA']))


'''
타인풀이

def ttt(ts, te):
    tmp = (int(te.split(":")[0]) - int(ts.split(":")[0])) * 60 + int(te.split(":")[1]) - int(ts.split(":")[1])
    return tmp


def con(s):
    while s.find("#") != -1:
        a = s.find("#")
        s = s[:a - 1] + s[a - 1].lower() + s[a + 1:]
    return s


def solution(m, musicinfos):
    m = con(m)
    ans = ''
    temp = 0
    for i in musicinfos:
        mu = i.split(',')[2]
        ss = i.split(',')[3]
        ti = ttt(i.split(',')[0], i.split(',')[1])
        ss = con(ss)
        tttt = ''
        ttmp = ti
        while ttmp > ss.__len__():
            tttt += ss
            ttmp -= ss.__len__()
        tttt += ss[:ti]
        if m in tttt and temp < ti:
            ans = mu
            temp = ti
    return ans if ans != '' else "(None)"

'''

'''
타인풀이 

class Music:
    def __init__(self, start_time, end_time, name, sound):
        self.start_time = start_time
        self.end_time = end_time
        self.name = name
        self.sound = sound

        self.set_music_time()
        self.set_full_sound()

    def set_music_time(self):
        start = self.start_time.split(":")
        end = self.end_time.split(":")

        hours = int(start[0]) - int(end[0])
        minutes = int(start[1]) - int(end[1])

        time = (hours * 60) + minutes

        if time < 0:
            self.run_time = -time
        else:
            self.run_time = time

    def set_full_sound(self):
        self.full_sound = str()

        if len(self.sound) >= self.run_time:
            self.full_sound = self.sound[:self.run_time]
        else:
            tmp = self.run_time / len(self.sound)
            self.full_sound += self.sound * int(tmp)

            tmp = self.run_time % len(self.sound)
            self.full_sound += self.sound[:int(tmp)]

    def contain_sound(self, m):
        if m in self.full_sound:
            return True

        return False

    def __str__(self):
        return """
        name: %s
        start_time: %s
        end_time: %s
        run_time: %s
        sound: %s
        full_sound: %s
        """ % (self.name, self.start_time, self.end_time, self.run_time, self.sound, self.full_sound)

    def __lt__(self, other):
        return self.run_time > other.run_time

def set_music(music_info):

    return Music(music_info.split(",")[0],
                 music_info.split(",")[1],
                 music_info.split(",")[2],
                 encode_sound(music_info.split(",")[3]))

def encode_sound(before_sound):
    encode = before_sound
    sound_encodes = ['C#', 'D#', 'F#', 'G#', 'A#']
    sound_decodes = ['c', 'd', 'f', 'g', 'a']

    for sound_encode, sound_decode in zip(sound_encodes, sound_decodes):
        if sound_encode in encode:
            encode = encode.replace(sound_encode, sound_decode)

    return encode

def solution(m, musicinfos):
    answer = "(None)"

    tmp_answer = []
    for musicinfo in musicinfos:
        tmp = set_music(musicinfo)
        if tmp.contain_sound(encode_sound(m)):
            tmp_answer.append(tmp)

    if len(tmp_answer) != 0:
        answer = sorted(tmp_answer)[0].name

    return answer
    '''