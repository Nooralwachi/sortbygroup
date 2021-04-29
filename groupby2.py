from collections import defaultdict
def groupby(filename):
    lines =defaultdict(list)
    result=[]
    try:
        with open(filename, 'r') as file:
            for line in file:
                line= line.strip()
                group = line.split()[1]
                lines[group].append(line)
    except IOError:
        print(f'Cannot open file: {filename}')
        return None
    sorted_lines = sorted(lines.items(), key= lambda x:x[0])
    with open('groupby.txt', 'w') as file:
        for group, line in sorted_lines:
            result.extend(line)
        lines = '\n'.join(result)
        file.write(lines)
    # or 
    # with open('groupby.txt', 'w') as file:
    #     for group, line in sorted_lines:
                # for item in line:
                #     file.write(item + '\n')

def groupby2(filename):
    lines =[]
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.split())
    sorted_lines = sorted(lines, key= lambda x:x[1])
    with open('groupby2.txt', 'w') as file:
        file.writelines([' '.join(line) + '\n' for line in sorted_lines])


groupby('file_test.txt')
groupby2('file_test.txt')