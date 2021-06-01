def solution(m, musicinfos):
    melody_list = []
    songs = []
    for idx in range(len(m)-1):
        if m[idx+1] == '#':
            melody_list.append(m[idx:idx+2])
        elif m[idx] == '#':
            pass
        else:
            melody_list.append(m[idx])
    if m[len(m)-1] != '#':
        melody_list.append(m[len(m)-1])

    for tmp in musicinfos:
        start, end, song, melody = tmp.split(',')
        temp = []
        for idx in range(len(melody) - 1):
            if melody[idx + 1] == '#':
                temp.append(melody[idx:idx + 2])
            elif melody[idx] == '#':
                pass
            else:
                temp.append(melody[idx])
        if melody[len(melody) - 1] != '#':
            temp.append(melody[len(melody) - 1])
        melody = temp
        play_time = (int(end[:2]) - int(start[:2]))*60 + (int(end[3:]) - int(start[3:]))
        # print(play_time)
        if play_time < len(melody_list):
            continue
        idx = 0
        jdx = 0
        cnt = 0
        times = play_time
        # print(melody_list, melody)
        while play_time + cnt >= len(melody_list):
            # print(melody_list[idx], melody[jdx])
            if melody_list[idx] == melody[jdx]:
                idx = (idx + 1) % len(melody_list)
                cnt += 1
            else:
                idx = cnt = 0
            if cnt == len(melody_list):
                songs.append((song, times))
                break
            play_time -= 1
            jdx = (jdx + 1) % len(melody)
    if songs:
        songs.sort(key=lambda x: x[1], reverse=True)
        return songs[0][0]
    return "(None)"

if __name__ == "__main__":
    print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
    print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
    print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))