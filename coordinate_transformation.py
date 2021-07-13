import numpy as np
from scipy.optimize import minimize


def fun1(args):
    x_input, target_x = args[0], args[1]
    count = len(x_input)
    v = lambda x: (sum([(x[0] * x_input[i] + x[1] - target_x[i]) ** 2 for i in range(count)]) / count) ** 0.5
    return v


def fun2(args):
    y_input, target_y = args[0], args[1]
    count = len(y_input)
    v = lambda x: (sum([(x[0] * y_input[i] + x[1] - target_y[i]) ** 2 for i in range(count)]) / count) ** 0.5
    return v


def trans(file_path=r".\node_coord.csv"):
    rec_coord = dict()
    rec_gps = dict()
    with open(file_path, 'r') as f:
        f.readline()
        lines = f.readlines()
        for line in lines:
            lines = line.split(',')
            node_id = int(lines[0])
            rec_coord[node_id] = (float(lines[1]), float(lines[2]))
            if len(lines) == 5 and lines[3] != '' and lines[4] != '':
                rec_gps[node_id] = float(lines[3]), float(lines[4])
    if len(rec_gps) < 3:
        raise Exception("At least 3 coordinates of longitude and latitude are required")
    # if len(rec_gps) < 10:
    #     keys = [key for key in rec_gps.keys()]
    # else:
    keys = [key for key in rec_gps.keys()]
    x_input = [rec_coord[key][0] for key in keys]
    y_input = [rec_coord[key][1] for key in keys]
    target_x = [rec_gps[key][0] for key in keys]
    target_y = [rec_gps[key][1] for key in keys]
    args1 = [x_input, target_x]
    args2 = [y_input, target_y]
    x0 = np.array([1, 1])
    res1 = minimize(fun1(args1), x0, method='SLSQP')
    res2 = minimize(fun2(args2), x0, method='SLSQP')
    trans_rec = dict()
    trans_fun = lambda x, y: (res1.x[0] * x + res1.x[1], res2.x[0] * y + res2.x[1])
    for key in rec_coord.keys():
        if key in keys:
            trans_rec[key] = rec_gps[key]
        else:
            trans_rec[key] = trans_fun(rec_coord[key][0], rec_coord[key][1])
    with open(r'.\new_node_coord.csv', 'w+', newline='') as f:
        lines = []
        f.write('node_id,x,y,long,lat\n')
        for key in trans_rec.keys():
            line = str.format(
                "{0},{1},{2},{3},{4}\n".format(key, rec_coord[key][0], rec_coord[key][1], trans_rec[key][0],
                                               trans_rec[key][1]))
            lines.append(line)
        f.writelines(lines)
    print('OK')


if __name__ == '__main__':
    trans()
