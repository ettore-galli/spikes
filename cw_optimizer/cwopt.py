# https://en.wikipedia.org/wiki/Cockcroft–Walton_generator


def calculate_final_voltage(vcc: float, n1, n2):
    v_out_1 = vcc * n1
    v_out_2 = v_out_1 * n2
    return v_out_2


def calculate_final_voltage_3s(vcc: float, n1, n2, n3):
    v_out_1 = vcc * n1
    v_out_2 = v_out_1 * n2
    v_out_3 = v_out_2 * n3
    return v_out_3


def optimize_stages(vcc, tot_stages):
    results = [
        (
            n1,
            tot_stages - n1,
            calculate_final_voltage(vcc, n1, tot_stages - n1),
            calculate_final_voltage_3s(vcc, n1, n1, n1),
        )
        for n1 in range(1, tot_stages + 1)
    ]
    for res in sorted(results):
        print(res)


if __name__ == "__main__":
    optimize_stages(9, 6)
